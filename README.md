# VoiceVisionReasoner

## Multimodal Reasoning and Intent-Preserving Safety for Voice and Vision

VoiceVisionReasoner is a research prototype that processes speech + visual context together. It produces grounded responses, avoids punitive refusals, and respects user intent.

This project explores multimodal failures of current assistants and proposes a simple approach:
- Whisper ASR (speech → text)
- Vision captioning (image → description)
- Joint reasoning (text + vision → answer)
- Intent-preserving safety checks

---

## 1. Motivation

Most AI assistants treat modalities as independent:

- Speech → transcription → answer
- Image → caption → answer

This siloed pipeline often produces:
- generic replies
- moralizing responses
- refusals framed as safety
- advice that ignores emotional context
- hallucinations unrelated to user environment

Most failures are not user attacks. They arise because the system fails to interpret human signals.

VoiceVisionReasoner attempts to reduce these failures by combining:
- Speech transcription
- Visual description
- Joint reasoning
- Safety and tone checks

---

## 2. System Overview

### 2.1 Processing Pipeline
Audio (wav) → Whisper ASR → Transcript
Image (jpg/png) → Caption Model → Caption
Transcript + Caption → LLM → Reasoned Answer
↓
Tone / Safety Analysis

### 2.2 Components

#### Speech (ASR)
Whisper generates transcription from spoken audio.

#### Vision (Captioning)
A captioning model describes the visible environment.

#### Reasoning
A language model produces answers grounded in transcript + caption.

#### Safety
Lightweight checks detect:
- toxic tone
- hallucinations
- punitive refusals
- moralizing language

The system repairs intent only when needed.

---

## 3. Core Idea

Typical LLMs treat:
- emotion as danger
- uncertainty as hallucination
- user vulnerability as policy violation

VoiceVisionReasoner takes a different stance:

Safety = collaboration, not punishment.
Use context → propose constructive actions → preserve user intent.

---

## 4. Quick Start

### 4.1 Installation

git clone https://github.com/kritibehl/VoiceVisionReasoner.git

cd VoiceVisionReasoner
pip install -r requirements.txt


### 4.2 Example Run

python app.py --audio_path examples/query.wav --image_path examples/desk.png


The program outputs:
- speech transcript
- image caption
- joint reasoning answer
- safety/tone indicators

---

## 5. Example Interaction

User (spoken):
“Why does my workspace make me feel stressed?”

Image:
A cluttered desk with cables, notebooks, and unopened mail.

System output:
Clutter increases decision fatigue.
Keep items you use daily within reach.
Move infrequent objects into a drawer or box.
Take a 5-minute break afterward.

The answer is grounded, actionable, and non-judgmental.

---

## 6. Relationship to Prior Work

### FairEval-Suite
Human-aligned evaluation for LLM responses.
Assesses clarity, relevance, tone, hallucination risk.
https://github.com/kritibehl/FairEval-Suite

### JailBreakDefense
Intent-preserving prompt repair.
Converts adversarial or distressed prompts into constructive goals.
https://github.com/kritibehl/JailBreakDefense

### VoiceVisionReasoner
Extends these principles to multimodal contexts.

---

## 7. Design Principles

1. Transparency  
Show intermediate steps.

2. User Respect  
Avoid moralizing or punitive refusal.

3. Visual Grounding  
Anchor reasoning in observed context.

4. Actionable Assistance  
Offer specific steps, not disclaimers.

---

## 8. Limitations

- Latency not optimized
- Captioning errors can propagate
- Safety layer minimal
- No personalization or memory
- Not clinical or crisis tooling
- Prototype, not production

---

## 9. Future Work

- Real-time multimodal reasoning
- Accessibility for low-vision users
- Emotion-aware speech analysis
- Caption confidence scoring
- Integration with FairEval metrics

---

## 10. License

MIT License. Research contributions are welcome.

---

## 11. Author

Kriti Behl  
GitHub: https://github.com/kritibehl  
Medium: https://medium.com/@kriti0608  
Zenodo: (FairEval DOI linked in main repository)


