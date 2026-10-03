# 03. Free AI Cloud API Providers & Endpoints

> **Last Updated**: October 3, 2026  
> **Coverage**: Developer APIs, REST endpoints, OpenAI-compatible SDK gateways, token limits, rate limits, and zero-cost cloud compute.

---

## Master Free API Quotas & Rate Limits Table

| Provider | Notable Free Models | Context Window | Rate Limits (RPM / TPM / RPD) | Daily Reset Cycle | Paid Upgrade Cost | Free Tier Credit Card Req? |
|---|---|---|---|---|---|---|
| **Google AI Studio** | Gemini 1.5 Flash<br>Gemini 1.5 Pro<br>Gemini 2.0 Flash Exp | Flash: 1,048,576 tokens<br>Pro: 2,097,152 tokens | **Flash**: 15 RPM \| 1,000,000 TPM \| 1,500 RPD<br>**Pro**: 2 RPM \| 32,000 TPM \| 50 RPD | 00:00 UTC (Daily) | Pay-as-you-go ($0.075/1M input) | **No** (Google account only) |
| **Groq Cloud** | Llama 3.3 70B Versatile<br>Llama 3.1 8B Instant<br>Whisper Large v3 | 131,072 tokens (Llama 3.3)<br>8,192 tokens (others) | **70B**: 30 RPM \| 6,000 TPM \| 14,400 RPD<br>**8B**: 30 RPM \| 30,000 TPM \| 14,400 RPD<br>**Whisper**: 20 RPM \| 2,000 Audio Sec/min | 00:00 UTC (Daily) | On-demand / Enterprise ($0.59/1M input 70B) | **No** |
| **OpenRouter** | 20+ models with `:free` suffix (Llama 3.3, Qwen 2.5, Gemini 2.0 Flash, DeepSeek-R1) | Up to 128k tokens | **Free Tier**: 20 Requests / Min<br>200 Requests / Day (Soft cap) | Rolling 24 hours | Pre-paid credits (From $5 deposit) | **No** |
| **Cerebras Cloud** | Llama 3.1 8B<br>Llama 3.3 70B | 8,192 tokens | **Free Tier**: 30 RPM \| 60,000 TPM<br>1,000,000 tokens / day free limit | 00:00 UTC (Daily) | Pro: $50/mo or Pay-as-you-go ($0.60/1M 70B) | **No** |
| **SambaNova Cloud** | Llama 3.3 70B<br>Llama 3.1 405B<br>Qwen 2.5 72B | 8k - 64k tokens | 30 RPM \| 40,000 TPM \| Generous daily volume (~100k+ tokens) | 00:00 UTC (Daily) | Pay-as-you-go | **No** |
| **Mistral AI API** | Codestral 2501<br>Mistral Small<br>Mistral Large | 32k - 128k tokens | **Experimentation Tier**: 1 RPS (Requests per second) \| 500,000 tokens / min | Soft monthly reset | Pay-as-you-go | **No** (Phone verification) |
| **Cloudflare Workers AI** | Llama 3.1 8B, Gemma 2, Whisper, FLUX-schnell | 4k - 32k tokens | **10,000 Neurons / Day** (Equivalent to ~200k-500k input tokens daily) | 00:00 UTC (Daily) | Paid Workers plan ($5/mo for 10M Neurons) | **No** (Free Cloudflare account) |
| **GitHub Models** | GPT-4o, Claude 3.5 Sonnet, Llama 3.3, Command R+ | 8k - 128k tokens | **Free Tier**: 15 RPM \| 150 RPD per model family (Personal GitHub PAT) | 00:00 UTC (Daily) | Direct Azure AI Foundry billing | **No** (GitHub account) |
| **Together AI** | Llama 3.3, DeepSeek, FLUX | Up to 128k tokens | $5.00 one-time starter credit upon sign-up (~2.5M tokens on 70B) | Expires after 3 months | Pay-as-you-go | **No** (Phone verification) |
| **Cohere API** | Command R, Command R+, Embed, Rerank | 128k tokens | **Trial Key**: 1000 calls / month \| 100 calls / minute | Monthly on the 1st | Pay-as-you-go | **No** |

---

## Deep Dive: Provider Specifications & Integration

### 1. Google AI Studio (The Uncontested King of Free Cloud APIs)
* **Console URL**: [aistudio.google.com](https://aistudio.google.com)
* **SDK Compatibility**: Native Google GenAI SDK & OpenAI-Compatible REST endpoint (`https://generativelanguage.googleapis.com/v1beta/openai/`).
* **Free Tier Details**:
  * **Gemini 1.5 Flash**: 15 Requests Per Minute (RPM), 1,000,000 Tokens Per Minute (TPM), 1,500 Requests Per Day (RPD).
  * **Gemini 1.5 Pro**: 2 RPM, 32,000 TPM, 50 RPD.
  * **Context Window**: 1,048,576 tokens on Flash; up to 2,097,152 tokens on Pro.
  * **System Prompts & Structured Outputs**: Fully supported via JSON Schema mode.
* **Catch / Privacy Note**: On Google's Free tier, prompt data may be logged and reviewed by human reviewers to train models. If handling proprietary or HIPAA/GDPR data, upgrade to Pay-As-You-Go (where data logging is strictly disabled).
* **Is Paying Worth It?**: **8 / 10**  
  * *Verdict*: Gemini's pay-as-you-go pricing is among the cheapest in existence ($0.075 per 1M input tokens on Flash). However, for personal projects, automation scripts, and hobby development, the free 1,500 requests/day will rarely be exhausted.

---

### 2. Groq Cloud (The Speed Champion)
* **Console URL**: [console.groq.com](https://console.groq.com)
* **Hardware Architecture**: LPU™ (Language Processing Units) — generates text at 280 to 450 tokens per second.
* **SDK Compatibility**: 100% Drop-in replacement for OpenAI SDK (`base_url="https://api.groq.com/openai/v1"`).
* **Free Tier Details**:
  * **Llama 3.3 70B Versatile**: 30 RPM, 6,000 TPM, 14,400 RPD.
  * **Llama 3.1 8B Instant**: 30 RPM, 30,000 TPM, 14,400 RPD.
  * **Whisper Large v3**: 20 RPM, 2,000 audio seconds per minute, 7,200 audio seconds per hour.
* **Is Paying Worth It?**: **4 / 10**  
  * *Verdict*: The free tier provides 14,400 requests every single day. That is one request every 6 seconds for 24 hours straight without paying a penny. Unless you are running production SaaS with high concurrency, you never need to pay Groq.

---

### 3. OpenRouter Free Models
* **Console URL**: [openrouter.ai](https://openrouter.ai)
* **What It Offers**: A unified API proxy granting access to dozens of models. Free users can query any model with the `:free` suffix without adding credits.
* **Current Free Models**:
  * `meta-llama/llama-3.3-70b-instruct:free`
  * `google/gemini-2.0-flash-exp:free`
  * `deepseek/deepseek-r1:free`
  * `qwen/qwen-2.5-72b-instruct:free`
* **Free Tier Limits**: 20 requests per minute, soft cap of 200 requests per day across free models.
* **Best Use Case**: Perfect as a universal fallback provider in your application config.

---

### 4. Cerebras & SambaNova Cloud (Specialized Compute)
* **Cerebras** ([cloud.cerebras.ai](https://cloud.cerebras.ai)):
  * Operates Wafer-Scale Engines (giant single chips). Delivers over 1,500 tokens/sec for Llama 3.1 8B and 450 tokens/sec for 70B.
  * Free allowance: 1 Million tokens generated per day, 30 RPM.
* **SambaNova** ([cloud.sambanova.ai](https://cloud.sambanova.ai)):
  * Operates Reconfigurable Dataflow Units (RDUs).
  * Notable perk: Runs massive models like **Llama 3.1 405B** and **Qwen 2.5 72B** with generous free developer access.

---

### 5. Cloudflare Workers AI
* **Console URL**: [dash.cloudflare.com](https://dash.cloudflare.com)
* **What It Offers**: Serverless edge AI compute running directly across Cloudflare's global data centers.
* **Free Tier Details**:
  * Every Cloudflare account gets **10,000 Neurons per day free forever**.
  * Supported models: Llama 3.1 8B, Gemma 2, Mistral 7B, Whisper audio transcription, FLUX-schnell image generation.
  * Zero cold-start latency, invocable via REST API or Cloudflare Worker TypeScript/JavaScript code.

---

### 6. GitHub Models (Azure AI Gateway)
* **Portal URL**: [github.com/marketplace/models](https://github.com/marketplace/models)
* **What It Offers**: Prototype flagship proprietary models (GPT-4o, Claude 3.5 Sonnet, AI21 Jamba, Cohere Command R+) directly inside your development workflow using your existing GitHub Personal Access Token (PAT).
* **Free Tier Limits**:
  * Low-throughput tier: 15 Requests per minute, 150 Requests per day.
  * Intended for testing, playground experimentation, and CI/CD evaluations.

---

## Strategy: The Multi-Key Fallback Failover Architecture

Never let your scripts or apps fail due to rate limits. Configure an automatic priority fallback chain:

```
[User Request] 
      │
      ▼
1. Primary: Google AI Studio (Gemini 1.5 Flash) ──> [Success: 1,500 RPD free]
      │ (If Rate Limited 429)
      ▼
2. Speed Fallback: Groq Cloud (Llama 3.3 70B) ────> [Success: 14,400 RPD free]
      │ (If Rate Limited 429)
      ▼
3. Reasoning Fallback: Cerebras / SambaNova ──────> [Success: 1M tokens/day free]
      │ (If Rate Limited 429)
      ▼
4. Universal Fallback: OpenRouter (:free models) ─> [Success: 200 RPD free]
      │ (If Offline / No Internet)
      ▼
5. Local Fallback: Localhost Ollama (Offline) ────> [Infinite local tokens]
```

By chaining these 4 free cloud providers, your applications gain access to **over 17,000 free API calls every single day** with zero infrastructure costs.
