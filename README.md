#  VoiceVisionReasoner: Speech-Driven Visual Reasoning with Safety Checks

**Kriti Behl — Voice → Vision → Answer**

VoiceVisionReasoner is a research prototype that chains together:

1. **Automatic Speech Recognition (ASR)** — transcribes a spoken query.  
2. **Image Captioning** — summarizes the visual scene.  
3. **LLM Reasoning** — answers a *spoken question about an image* using both audio + visual context.  
4. **Lightweight Safety & Quality Checks** — rule-based toxicity flags and answer sanity signals.

This repo is designed as a **multimodal evaluation playground** for:
- speech → understanding  
- image → context  
- language → reasoning  
- safety → simple on-device filters

and complements my **FairEval** framework for human-aligned LLM evaluation.

---

## High-Level Architecture

```text
[User Speech]  ──▶  ASR (Whisper) ──▶ transcript
[Input Image] ──▶  Image Captioner ──▶ scene description

[transcript + caption] ──▶ Text LLM ──▶ answer
                               │
                               └─▶ eval_metrics (toxicity, sanity heuristics)
