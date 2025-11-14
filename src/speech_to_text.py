from __future__ import annotations

from typing import Optional

import torch
from transformers import pipeline


_ASR_PIPELINE = None


def _get_device() -> int:
    if torch.backends.mps.is_available():
        return 0  # treat MPS as "0" for pipeline(device=0)
    if torch.cuda.is_available():
        return 0
    return -1  # CPU


def get_asr_pipeline():
    global _ASR_PIPELINE
    if _ASR_PIPELINE is None:
        _ASR_PIPELINE = pipeline(
            task="automatic-speech-recognition",
            model="openai/whisper-small",
            device=_get_device(),
        )
    return _ASR_PIPELINE


def transcribe(path: str) -> str:
    """
    Transcribe a WAV file into text.

    Parameters
    ----------
    path : str
        Path to an audio file (ideally 16kHz mono WAV).

    Returns
    -------
    str
        Transcribed text (lowercased).
    """
    asr = get_asr_pipeline()
    result = asr(path)
    text = result.get("text", "").strip()
    return text
