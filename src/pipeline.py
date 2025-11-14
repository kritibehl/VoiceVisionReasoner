# src/pipeline.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .speech_to_text import transcribe
from .vision_reasoner import caption_image, reason_about_scene
from .eval_metrics import simple_toxicity_check, safety_report_to_dict


@dataclass
class PipelineResult:
    transcript: str
    caption: str
    answer: str
    safety: Dict


def run_voice_vision_pipeline(audio_path: str, image_path: str) -> PipelineResult:
    """
    End-to-end pipeline:
      audio → transcript
      image → caption
      transcript + caption → answer
      answer → safety flags
    """
    transcript = transcribe(audio_path)
    caption = caption_image(image_path)
    answer = reason_about_scene(transcript, caption)
    safety = safety_report_to_dict(simple_toxicity_check(answer))

    return PipelineResult(
        transcript=transcript,
        caption=caption,
        answer=answer,
        safety=safety,
    )
