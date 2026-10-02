# 04. Local & Offline AI: The Infinite-Token Guide

> **Last Updated**: October 2, 2026  
> **Coverage**: Local inference engines, open weights, hardware requirements, quantization formats, and offline private AI.

---

## Why Local AI?

* **Cost**: $0.00 forever. Zero subscriptions, zero token metered billing.
* **Privacy**: 100% data sovereign. No logs, no telemetry, no corporate human review.
* **Uncensored / Unfiltered**: Ability to run models without arbitrary safety guardrails.
* **Offline Resilience**: Works without internet access.

---

## Top Local Inference Runtimes

| Runtime | Platform | Interface | Best For | OpenAI API Compatible? |
|---|---|---|---|---|
| **Ollama** | Win / Mac / Linux | CLI + Background Service | Developer automation, IDE integration, CLI agents | **Yes** |
| **LM Studio** | Win / Mac / Linux | Polished Desktop GUI | Interactive chat, testing Hugging Face GGUFs, visual hardware monitor | **Yes** |
| **Jan.ai** | Win / Mac / Linux | Native Electron GUI | Privacy-first local ChatGPT alternative, clean UI | **Yes** |
| **llama.cpp** | Win / Mac / Linux | Pure C/C++ CLI | Maximum raw inference speed, low overhead, CPU inference | **Yes** |
| **vLLM** | Linux / WSL2 | High-throughput Engine | Serving high-concurrency production workloads with PagedAttention | **Yes** |
| **Text-Generation-WebUI** | Win / Linux | Gradio Browser UI | Deep experimentation, LoRA loading, exotic sampling techniques | **Yes** |

---

## Hardware Tier & Model Matching Guide

To run local LLMs smoothly, VRAM (Video RAM on your GPU) is king. When a model fits entirely in VRAM, inference runs at 30-100+ tokens/second. When it overflows into system RAM (CPU offloading), speed drops to 2-10 tokens/second.

### Tier 1: Entry Level (4GB - 6GB VRAM or 8GB - 16GB System RAM)
* **Target Models**:
  * **Qwen 2.5 3B Instruct** (GGUF Q4_K_M ~2.0 GB VRAM) — Punches dramatically above its weight in multilingual and code logic.
  * **Meta Llama 3.2 3B** (GGUF Q4_K_M ~2.2 GB VRAM) — Snappy, great for lightweight summarization and drafting.
  * **Phi-3.5 Mini 3.8B** (GGUF Q4_K_M ~2.6 GB VRAM) — Remarkable reasoning for its compact size.
* **Speed**: 40–80 tokens/sec on modern entry GPUs (RTX 3050 / GTX 1660 / AMD 6600).

### Tier 2: The Sweet Spot (8GB - 12GB VRAM or 16GB - 32GB System RAM)
* **Target Models**:
  * **Meta Llama 3.1 8B Instruct** (GGUF Q4_K_M ~4.9 GB VRAM, Q8_0 ~8.5 GB VRAM).
  * **Qwen 2.5 7B / 14B Coder** (14B Q4_K_M ~9.0 GB VRAM) — Outperforms original GPT-3.5 in coding benchmarks.
  * **DeepSeek-R1-Distill-Qwen-8B** (GGUF Q4_K_M ~5.2 GB VRAM) — Brings DeepSeek's chain-of-thought reasoning to budget hardware.
  * **Mistral NeMo 12B Instruct** (GGUF Q4_K_M ~7.5 GB VRAM) — 128k context window support.
* **Hardware Example**: RTX 3060 12GB (the best budget AI GPU on the market), RTX 4060 Ti 16GB, or Apple M1/M2/M3 with 16GB unified memory.

### Tier 3: Enthusiast & Prosumer (16GB - 24GB VRAM or 32GB - 64GB System RAM)
* **Target Models**:
  * **Qwen 2.5 32B Instruct** (GGUF Q4_K_M ~19.5 GB VRAM) — Rivals early GPT-4 benchmarks in nuance and structure.
  * **DeepSeek-R1-Distill-Qwen-32B** (GGUF Q4_K_M ~20.0 GB VRAM) — High-end local reasoning model.
  * **Meta Llama 3.3 70B Instruct** (GGUF IQ2_XS / IQ3_S ~22-26 GB VRAM) — State-of-the-art open model fitting in 24GB VRAM with extreme quantization.
* **Hardware Example**: RTX 3090 24GB (used ~$650-$750), RTX 4090 24GB, or Apple Silicon with 36GB-64GB unified memory.

### Tier 4: Workstation / Dual-GPU (32GB - 48GB+ VRAM or 128GB System RAM)
* **Target Models**:
  * **Meta Llama 3.3 70B Instruct** (GGUF Q4_K_M / Q5_K_M ~40-48 GB VRAM) — Uncompromised flagship precision.
  * **Qwen 2.5 72B Instruct** (GGUF Q4_K_M ~43 GB VRAM).
* **Hardware Example**: Dual RTX 3090 (48GB combined VRAM), Mac Studio M2/M3 Ultra (64GB-192GB unified RAM).

---

## Quantization Demystified: Which Format to Choose?

When downloading models from Hugging Face or Ollama:

| Quantization Type | Size Reduction | Quality Retention | Recommendation |
|---|---|---|---|
| **FP16 / BF16** | 0% (Full baseline) | 100% | Only for training or enterprise datacenter servers. |
| **Q8_0** | ~50% | 99.8% | Use only if you have abundant VRAM to spare. |
| **Q5_K_M** | ~65% | 98.5% | Near-lossless sweet spot if VRAM allows. |
| **Q4_K_M** | **~72%** | **96.5%** | **The Gold Standard for 95% of users.** Optimal balance of speed, memory, and intelligence. |
| **IQ3_M / Q3_K_M** | ~78% | 90.0% | Acceptable when attempting to squeeze a 70B model into a 24GB card. |
| **Q2_K / IQ2_XXS** | ~85% | 75.0% | Noticeable degradation in vocabulary and edge cases. Avoid unless strictly necessary. |

---

## Instant Local Setup with Ollama

1. **Install Ollama** on Windows/macOS/Linux:
   Download from [ollama.com](https://ollama.com).
2. **Pull and Run State-of-the-Art Models**:
   ```bash
   # Balanced daily assistant (8B)
   ollama run llama3.1:8b

   # Coding specialist (14B)
   ollama run qwen2.5-coder:14b

   # Reasoning engine
   ollama run deepseek-r1:8b
   ```
3. **Connect Your IDE or Chat Apps**:
   Ollama automatically exposes an OpenAI-compatible REST server at `http://localhost:11434/v1`.
   * **API Base URL**: `http://localhost:11434/v1`
   * **API Key**: `ollama` (any dummy string works)

---

## Is Upgrading PC Hardware Worth It for Local AI?

* **Buying an RTX 3060 12GB (~$250 used)**: **10 / 10 Value**.  
  * Grants 12GB of fast VRAM, allowing you to run 8B models unquantized or 14B models at Q4 at blazing speeds locally forever.
* **Buying an RTX 4090 24GB (~$1,600 - $2,000)**: **6 / 10 Value**.  
  * Incredible performance, but from a purely financial perspective, $1,800 pays for over 2.5 Billion tokens on cloud APIs like Google Gemini Flash or Groq. Buy it only if offline privacy, zero latency, and local image/video generation (FLUX, ComfyUI) are your primary daily priorities.
