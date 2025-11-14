# app.py
from __future__ import annotations

import tempfile
from pathlib import Path

import streamlit as st

from src.pipeline import run_voice_vision_pipeline


st.set_page_config(page_title="VoiceVisionReasoner", layout="wide")
st.title("🎙️🖼️ VoiceVisionReasoner")
st.caption("Speech → Vision → Answer + simple safety checks (demo prototype)")


left, right = st.columns(2)

with left:
    st.subheader("1. Upload Inputs")

    audio_file = st.file_uploader(
        "Upload a speech file (WAV recommended)",
        type=["wav", "flac", "mp3", "m4a"],
    )

    image_file = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"],
    )

    run_btn = st.button("Run Voice → Vision Reasoning")

with right:
    st.subheader("2. Outputs")


def _save_temp(uploaded, suffix: str) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    tmp.write(uploaded.read())
    tmp.flush()
    return tmp.name


if run_btn:
    if not audio_file or not image_file:
        st.error("Please upload both an audio file and an image.")
    else:
        with st.spinner("Running pipeline... (first run will download models)"):
            audio_path = _save_temp(audio_file, suffix=Path(audio_file.name).suffix)
            image_path = _save_temp(image_file, suffix=Path(image_file.name).suffix)

            result = run_voice_vision_pipeline(audio_path, image_path)

        st.markdown("### 🔊 Transcript")
        st.write(result.transcript or "_(empty transcript)_")

        st.markdown("### 🖼️ Image Caption")
        st.write(result.caption or "_(empty caption)_")

        st.markdown("### 💬 Model Answer")
        st.write(result.answer or "_(no answer)_")

        st.markdown("### 🛡️ Safety & Quality Signals")
        st.json(result.safety)
else:
    st.info("Upload a speech file and an image on the left, then click **Run Voice → Vision Reasoning**.")
