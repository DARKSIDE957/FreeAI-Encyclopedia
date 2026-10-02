# 06. Audio, Voice, Music & Transcription AI

> **Last Updated**: October 2, 2026  
> **Coverage**: Text-to-Speech (TTS), voice cloning, Speech-to-Text (STT) transcription, AI music generation, and sound design.

---

## Master Audio AI Quotas & Comparison Matrix

| Tool | Category | Free Quota / Limits | Speed / Latency | Paid Upgrade | Is Paid Worth It? | Best Free Alternative |
|---|---|---|---|---|---|---|
| **ElevenLabs** | Voice / TTS | 10,000 characters / month (~10-15 minutes of speech); requires attribution | High quality cloud streaming | Starter: $5/mo<br>Creator: $22/mo<br>Pro: $99/mo | **5/10** (Only worth it for massive commercial narration or custom voice clones) | **Kokoro-82M (Local/Free)**, **Fish Audio** |
| **Kokoro TTS** | Voice / TTS (Open Source) | **100% Unlimited Forever** (Runs on local CPU or GPU, 82M params) | Realtime on CPU, 50x realtime on GPU | None ($0 open-source Apache 2.0) | **N/A** (Completely free) | **Native / Self-hosted** |
| **Fish Audio** | Voice / Voice Cloning | Free daily points (~50 generations daily); 1-minute voice clone for free | Fast cloud inference | Pro: $19.90/mo | **6/10** (Great voice cloning, free tier is generous) | **F5-TTS (Local)**, **Kokoro** |
| **Groq Whisper API** | Transcription / STT | **20 RPM \| 2,000 audio seconds/min \| 7,200 audio seconds/hr 100% FREE** | ~200x realtime (Transcribes a 1-hour podcast in 15 seconds) | Paid tier available | **2/10** (The free tier is so absurdly generous that paying is unnecessary) | **faster-whisper (Local)** |
| **OpenAI Whisper** | Transcription / STT | **100% Unlimited Forever** (Local `faster-whisper` or `whisper.cpp`) | Depends on local GPU/CPU | None ($0 open-source) | **N/A** (Completely free) | **Groq Whisper API** |
| **Suno AI** | Music Generation | 50 free credits daily (= 10 songs / 5 generation prompts per day) | Cloud generation (~30s) | Pro: $10/mo (2,500 credits)<br>Premier: $30/mo | **7/10** (10 free daily songs is very generous and plenty for making music) | **Udio Free Tier** |
| **Udio** | Music Generation | Daily & monthly free credit allotment (~10 credits/day) | Cloud generation (~40s) | Standard: $10/mo<br>Pro: $30/mo | **7/10** (Exceptional musicality and vocals; free tier lets you test ideas) | **Suno Free Tier** |
| **F5-TTS** | Voice Cloning | **100% Unlimited Forever** (Zero-shot voice cloning with 5s audio reference) | Local GPU inference | None ($0 open-source) | **N/A** (Completely free) | **Fish Audio** |

---

## Deep Dive: Voice & TTS Breakdown

### 1. ElevenLabs (The Commercial Voice Standard)
* **Website**: [elevenlabs.io](https://elevenlabs.io)
* **Free Tier Details**:
  * 10,000 characters per month (~1,500 words / ~10 minutes of synthesized speech).
  * Access to standard voice library and Multilingual v2 model.
  * *Condition*: Requires attribution ("created with ElevenLabs") on public media; non-commercial license on free tier.
  * Reset Cycle: Monthly on account signup date.
* **Paid Plans**:
  * Starter: $5/month (30,000 characters, instant voice cloning, commercial license).
  * Creator: $22/month (100,000 characters, higher quality audio).
* **Is Paying Worth It?**: **5 / 10**  
  * *Verdict*: If you need a commercial license for YouTube video narration or need exact voice clones of yourself, the $5-$22/month plan is a reasonable business expense. But for personal projects, games, audiobooks, or developer apps, **Kokoro-82M** matches the quality for $0.00.

---

### 2. Kokoro TTS (The Open-Source Miracle)
* **Model**: [huggingface.co/hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) — [GitHub](https://github.com/hexgrad/kokoro)
* **What It Is**: An ultra-compact 82-million parameter text-to-speech model released under Apache 2.0 license.
* **Why It Changes Everything**:
  * Sounds astonishingly natural with nuanced emotional cadence and American/British/Japanese/Mandarin accents.
  * Runs **in real-time even on a basic CPU** without needing an expensive GPU.
  * 100% Free, infinite characters, zero rate limits, zero internet connection required.
* **How to Run**:
  ```bash
  pip install kokoro soundfile
  ```

---

## Deep Dive: Speech-to-Text & Transcription

### 1. Groq Cloud Whisper (The Free Cloud Miracle)
* **Endpoint**: OpenAI compatible (`https://api.groq.com/openai/v1/audio/transcriptions`)
* **Cost**: **$0.00 (100% Free Tier)**
* **Quotas**:
  * 20 Requests per minute.
  * 2,000 audio seconds per minute (~33 minutes of audio processed in 60 seconds).
  * 7,200 audio seconds per hour.
* **Performance**: Groq's custom LPU hardware transcribes a 30-minute meeting in under 10 seconds with Whisper Large v3 accuracy.

### 2. Local Whisper via `faster-whisper`
* **Repository**: [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)
* **Why Use It**: 4x faster than OpenAI's default Whisper codebase and consumes 50% less VRAM using CTranslate2.
* **Cost**: Free forever, offline, infinite hours of audio.

---

## Deep Dive: AI Music Generation

### 1. Suno AI vs Udio (Free Tier Comparison)
* **Suno AI** ([suno.com](https://suno.com)):
  * **Free Tier**: 50 credits refreshed **daily**. Each generation makes 2 song variations (consumes 10 credits). That gives you **10 free songs every day (300 songs per month)**.
  * *Terms*: Free songs are for personal and non-commercial creative use (commercial distribution requires a Pro plan).
* **Udio** ([udio.com](https://udio.com)):
  * **Free Tier**: Grants regular free daily credits to create musical fragments and 2-minute full tracks.
  * Stronger in jazz, soul, complex melodies, and intricate production; Suno is stronger in radio pop and punchy lyrics.

### Is Paying for Suno / Udio Worth It?
* **Verdict**: **7 / 10** (Only required if you need commercial distribution licenses).
* For creating tracks, testing musical ideas, and everyday song creation, the **50 free daily credits on Suno (10 free songs daily) are very generous and plenty**.
