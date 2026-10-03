# 03. Free AI Cloud API Providers & Paid APIs' Free Credits

> **Last Updated**: October 3, 2026  
> **Coverage**: Developer APIs, REST endpoints, OpenAI-compatible SDK gateways, token limits, rate limits, starter credits, and zero-cost cloud compute.

---

## 🎁 Commercial & Paid API Providers: Free Starter Credits & Free Quotas

Many developers want to know: *"Which commercial paid AI APIs give free starter credits or tokens, how much do they offer, and what can you use without paying?"* Here is the verified, up-to-date reality across all major commercial API providers:

### Master Paid API Free Credits & Allowances Table

| Provider | Free Starter Credit / Tokens | Ongoing Free Quota? | Credit Card Required? | Expiration Window | What Happens When Depleted? | Best Zero-Dollar Strategy |
|---|---|---|---|---|---|---|
| [**Google AI Studio (Gemini)**](https://aistudio.google.com) | **Permanent Free Tier** + $300 Google Cloud credit (Vertex AI) | **Yes**: 1,500 RPD (Flash), 50 RPD (Pro) | **No** (Google account only) | Never expires for AI Studio; 90 days for GCP $300 | Requests return HTTP 429 until 00:00 UTC daily reset | Use `gemini-1.5-flash` as primary backend for Cline/Continue; 1,500 calls/day covers full-time coding. |
| [**DeepSeek API**](https://platform.deepseek.com) | **5,000,000 Free Tokens** (10 RMB / ~$1.40 USD) upon phone verification | No ongoing free tier (API is pay-per-token) | **No** (Phone SMS verification) | 30 days from registration | API calls halt until deposit (Min deposit: ~$2) | Claim the 5M tokens for local testing. Post-free rate is ultralow ($0.14/1M input for V3). |
| [**Together AI**](https://api.together.xyz) | **$5.00 Free Starter Credit** (~2.5M - 5M tokens) | No ongoing free tier | **No** (Email + phone verification) | 90 days (3 months) | API calls halt until card added | Use starter credit to test open weights (Llama 3.3 70B, DeepSeek-V3, FLUX.1) via standard OpenAI SDK format. |
| [**Groq Cloud API**](https://console.groq.com) | **Permanent Free Tier** (14,400 Requests/Day on 70B & 8B) | **Yes**: 14,400 RPD forever | **No** | Never expires | Soft throttle if hitting 30 RPM; resets next minute/day | Best zero-cost high-speed API in existence. Plug into Continue.dev for 300+ tokens/sec coding. |
| [**Mistral AI API**](https://console.mistral.ai) | **Experimentation Tier** (1 RPS, 500,000 TPM) | **Yes** (Soft limits for prototyping) | **No** (Phone verification) | Never expires | Rate-limited to 1 request/sec | Excellent for Codestral coding completions and structured JSON function calling. |
| [**Cohere API**](https://dashboard.cohere.com) | **1,000 Free Calls Every Month** (Trial API Key) | **Yes**: 1,000 calls / month | **No** | Refreshes on 1st of every month | Calls pause until next month's 1st | Perfect for production-grade semantic search and reranking (`cohere.rerank`). |
| [**Cerebras Cloud**](https://cloud.cerebras.ai) | **1,000,000 Free Tokens / Day** | **Yes**: 1M tokens / day | **No** | Daily at 00:00 UTC | Pauses until midnight UTC reset | Fastest inference engine available (>1,500 t/s on 8B; 450 t/s on 70B). |
| [**SambaNova Cloud**](https://cloud.sambanova.ai) | **~100,000+ Free Tokens / Day** (Llama 3.1 405B & Qwen 2.5 72B) | **Yes**: Daily developer allowance | **No** | Daily at 00:00 UTC | Throttles until daily reset | One of the only providers offering free developer API access to massive 405B parameter models. |
| [**GitHub Models**](https://github.com/marketplace/models) | **150 Free Requests / Day per Model** (GPT-4o, Claude 3.5 Sonnet) | **Yes**: 150 RPD per model | **No** (GitHub PAT token) | Daily at 00:00 UTC | Returns rate limit until midnight UTC | Run flagship proprietary models (GPT-4o, Claude 3.5 Sonnet) for $0 without OpenAI or Anthropic credit cards. |
| [**OpenAI API**](https://platform.openai.com) | **$0.00** (Discontinued automatic free signup credits) | **No** (Requires prepaid deposit, min $5) | **Yes** (Credit card required) | N/A | Cannot generate API keys without payment | **Do not pay upfront for hobby testing.** Use GitHub Models or OpenRouter free models to test GPT-4o for $0. |
| [**Anthropic Claude API**](https://console.anthropic.com) | **$5.00 Trial Credit** (In select regions via phone verification) | **No** (Prepaid deposit required once exhausted) | **Yes** (For sustained usage) | Varies (Typically 14–30 days) | API calls return credit error | Query Claude 3.5 Sonnet for free via GitHub Models (150 calls/day) or use Claude web artifacts. |
| [**Cloudflare Workers AI**](https://developers.cloudflare.com/workers-ai/) | **10,000 Free Neurons / Day** (~200k - 500k input tokens) | **Yes**: 10,000 Neurons daily | **No** (Free Cloudflare account) | Daily at 00:00 UTC | Halts until midnight UTC | Host serverless AI edge workers for translation, embeddings, and Whisper transcription for $0. |
| [**Replicate**](https://replicate.com) | **Trial Predictions Allowance** (~20-50 initial runs) | **No** (Pay-per-second GPU compute) | Card required after initial trial | Varies | Halts with billing prompt | Use local ComfyUI or Hugging Face Spaces instead for free unlimited image/video inference. |
| [**OpenRouter**](https://openrouter.ai) | **20+ Free Models** (All `:free` tagged models) | **Yes**: 20 RPM / 200 RPD soft cap | **No** | Rolling 24 hours | Rejects free requests until rolling window clears | Configure OpenRouter as an automatic fallback provider in Continue.dev or Aider. |

---

## Technical Deep-Dives: Free Starter Credits & APIs

### 1. Google AI Studio (Gemini API)
* **Console URL**: [aistudio.google.com](https://aistudio.google.com)
* **API Style**: Native Google GenAI SDK & OpenAI-Compatible REST endpoint (`https://generativelanguage.googleapis.com/v1beta/openai/`).
* **Free Tier Quotas**:
  * **Gemini 1.5 Flash**: 15 Requests Per Minute (RPM), 1,000,000 Tokens Per Minute (TPM), 1,500 Requests Per Day (RPD).
  * **Gemini 1.5 Pro**: 2 RPM, 32,000 TPM, 50 RPD.
  * **Gemini 2.0 Flash Exp**: 10 RPM, 1,000,000 TPM, 1,500 RPD.
  * **Context Window**: 1,048,576 tokens on Flash; up to 2,097,152 tokens on Pro.
* **Paid Tier & Credits**:
  * Free tier does not require a credit card.
  * New Google Cloud accounts receive **$300 in free trial credits** valid for 90 days across Vertex AI.
* **Privacy Note**: Google logs and human-reviews free-tier prompt data for model improvement. For proprietary or sensitive code, use local offline models or upgrade to Google Cloud Pay-As-You-Go.

---

### 2. DeepSeek API
* **Console URL**: [platform.deepseek.com](https://platform.deepseek.com)
* **API Style**: 100% Drop-in OpenAI Compatible (`https://api.deepseek.com/v1`).
* **Free Starter Allowance**:
  * Grants **5,000,000 Free Tokens** (10 RMB balance) upon registration and phone number verification.
  * Tokens expire 30 days after registration.
* **Pay-As-You-Go Pricing (Post-Free)**:
  * **DeepSeek-V3**: $0.14 per 1M input tokens (cached tokens: $0.014/1M), $0.28 per 1M output tokens.
  * **DeepSeek-R1**: $0.55 per 1M input tokens, $2.19 per 1M output tokens.
* **Assessment**: Extremely developer-friendly. The 5M free tokens give ample headroom for experimentation, and the pay-as-you-go pricing is roughly 10x cheaper than OpenAI or Anthropic.

---

### 3. Groq Cloud API
* **Console URL**: [console.groq.com](https://console.groq.com)
* **Hardware Architecture**: LPU™ (Language Processing Units) delivering 280 to 450 tokens/second.
* **API Style**: 100% Drop-in replacement for OpenAI SDK (`base_url="https://api.groq.com/openai/v1"`).
* **Free Quotas (Permanent)**:
  * **Llama 3.3 70B Versatile**: 30 RPM, 6,000 TPM, 14,400 RPD.
  * **Llama 3.1 8B Instant**: 30 RPM, 30,000 TPM, 14,400 RPD.
  * **Whisper Large v3**: 20 RPM, 2,000 audio seconds per minute, 7,200 audio seconds per hour.
* **Assessment**: 14,400 requests every single day means you can fire one request every 6 seconds for 24 hours continuously without paying anything.

---

### 4. Together AI
* **Console URL**: [api.together.xyz](https://api.together.xyz)
* **Free Starter Allowance**:
  * **$5.00 Free Credit** automatically granted upon phone and email verification.
  * Credits remain valid for 90 days (3 months).
* **Available Models**: Over 100 open models including Llama 3.3 70B, DeepSeek-V3, Qwen 2.5 Coder, and FLUX.1 image generation.
* **Assessment**: $5.00 translates to roughly 2.5 to 5 million input tokens on 70B models, providing an ideal sandbox for testing open-weights deployments.

---

### 5. Mistral AI API (La Plateforme)
* **Console URL**: [console.mistral.ai](https://console.mistral.ai)
* **Free Experimentation Tier**:
  * Rate limited to 1 Request Per Second (RPS) and 500,000 tokens/minute.
  * Grants access to `codestral-2501`, `mistral-small-latest`, and `mistral-large-latest`.
* **Requirements**: Phone verification; no credit card required for the experimentation tier.
* **Assessment**: Great for code completion via Codestral and native JSON Schema output mode.

---

### 6. Cohere API
* **Console URL**: [dashboard.cohere.com](https://dashboard.cohere.com)
* **Free Trial Key Allowance**:
  * **1,000 API calls per month free forever**.
  * 100 calls per minute rate limit.
  * Resets on the 1st of every month.
* **Best Use Case**: Production-grade embeddings (`embed-english-v3.0`) and semantic reranking (`rerank-v3.5`), which significantly improve RAG pipeline accuracy.

---

### 7. GitHub Models (Azure AI Gateway)
* **Portal URL**: [github.com/marketplace/models](https://github.com/marketplace/models)
* **Free Tier Quotas**:
  * **150 Requests Per Day per model family** (15 RPM).
  * Accessible using your standard GitHub Personal Access Token (PAT).
* **Available Models**: GPT-4o, GPT-4o mini, Claude 3.5 Sonnet, Claude 3.5 Haiku, Llama 3.3 70B, Cohere Command R+.
* **Assessment**: The cleanest zero-dollar method to prototype commercial models (GPT-4o and Claude 3.5) without entering billing information into OpenAI or Anthropic consoles.

---

## Strategy: The Multi-Key Fallback Failover Architecture

Never let scripts or applications fail due to rate limits. Configure an automatic priority fallback chain:

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

By chaining these free cloud providers, applications gain access to **over 17,000 free API calls every single day** with zero infrastructure costs.
