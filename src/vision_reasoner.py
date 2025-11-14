# src/vision_reasoner.py
from __future__ import annotations

from typing import Dict

from PIL import Image
import torch
from transformers import pipeline


_CAPTION_PIPELINE = None
_LLM_PIPELINE = None


def _get_device() -> int:
    if torch.backends.mps.is_available():
        return 0
    if torch.cuda.is_available():
        return 0
    return -1


def get_caption_pipeline():
    global _CAPTION_PIPELINE
    if _CAPTION_PIPELINE is None:
        _CAPTION_PIPELINE = pipeline(
            task="image-to-text",
            model="Salesforce/blip-image-captioning-base",
            device=_get_device(),
        )
    return _CAPTION_PIPELINE


def get_llm_pipeline():
    """
    Small text-generation model for demo.
    You can swap in any instruction-tuned model.
    """
    global _LLM_PIPELINE
    if _LLM_PIPELINE is None:
        _LLM_PIPELINE = pipeline(
            task="text-generation",
            model="gpt2",
            device=_get_device(),
        )
    return _LLM_PIPELINE


def caption_image(image_path: str) -> str:
    """
    Generate a short caption for an image.
    """
    captioner = get_caption_pipeline()
    image = Image.open(image_path).convert("RGB")
    out = captioner(image, max_new_tokens=30)
    if isinstance(out, list) and len(out) > 0:
        return out[0].get("generated_text", "").strip()
    return ""


def reason_about_scene(transcript: str, caption: str) -> str:
    """
    Combine speech transcript + image caption and ask an LLM
    to reason about the scene.
    """
    llm = get_llm_pipeline()

    prompt = (
        "You are a helpful assistant that answers user questions about an image.\n\n"
        f"User spoke: {transcript}\n"
        f"Image description: {caption}\n\n"
        "Based on BOTH the spoken question and the image description, "
        "give a short, clear answer for the user:\n"
    )

    out = llm(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        num_return_sequences=1,
    )
    if isinstance(out, list) and len(out) > 0:
        text = out[0].get("generated_text", "")
        answer = text[len(prompt) :].strip()
        return answer
    return ""
