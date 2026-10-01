# 10. Master Token Quotas, Rate Limits & Reset Windows Reference

> **Last Updated**: October 2, 2026  
> **Purpose**: The definitive technical reference for context windows, rate limits (RPM/TPM/RPD), reset mechanisms, and quotas across all free AI tiers.

---

## 1. Cloud API Rate Limits & Quota Master Table

| Provider | Model Identifier | Max Context Window | Requests / Min (RPM) | Tokens / Min (TPM) | Requests / Day (RPD) | Reset Interval | Paid Upgrade Price |
|---|---|---|---|---|---|---|---|
| **Google AI Studio** | `gemini-1.5-flash` | 1,048,576 tokens | 15 RPM | 1,000,000 TPM | 1,500 RPD | 00:00 UTC (Daily) | $0.075 / 1M input<br>$0.30 / 1M output |
| **Google AI Studio** | `gemini-1.5-pro` | 2,097,152 tokens | 2 RPM | 32,000 TPM | 50 RPD | 00:00 UTC (Daily) | $1.25 / 1M input<br>$5.00 / 1M output |
| **Google AI Studio** | `gemini-2.0-flash-exp` | 1,048,576 tokens | 10 RPM | 1,000,000 TPM | 1,500 RPD | 00:00 UTC (Daily) | Experimental ($0) |
| **Groq Cloud** | `llama-3.3-70b-versatile` | 131,072 tokens | 30 RPM | 6,000 TPM | 14,400 RPD | 00:00 UTC (Daily) | $0.59 / 1M input<br>$0.79 / 1M output |
| **Groq Cloud** | `llama-3.1-8b-instant` | 8,192 tokens | 30 RPM | 30,000 TPM | 14,400 RPD | 00:00 UTC (Daily) | $0.05 / 1M input<br>$0.08 / 1M output |
| **Groq Cloud** | `whisper-large-v3` | ~25MB audio file | 20 RPM | 2,000 sec/min | 7,200 sec/hour | Hourly rolling | $0.111 / hour audio |
| **Cerebras Cloud** | `llama3.1-8b` | 8,192 tokens | 30 RPM | 60,000 TPM | 1,000,000 TPD | 00:00 UTC (Daily) | $0.10 / 1M input |
| **Cerebras Cloud** | `llama3.3-70b` | 8,192 tokens | 30 RPM | 60,000 TPM | 1,000,000 TPD | 00:00 UTC (Daily) | $0.60 / 1M input |
| **SambaNova Cloud** | `Meta-Llama-3.3-70B-Instruct` | 64,000 tokens | 30 RPM | 40,000 TPM | ~100k+ TPD | 00:00 UTC (Daily) | Pay-as-you-go |
| **SambaNova Cloud** | `Meta-Llama-3.1-405B-Instruct`| 8,192 tokens | 20 RPM | 20,000 TPM | ~50k+ TPD | 00:00 UTC (Daily) | Pay-as-you-go |
| **OpenRouter** | `*:free` models | Up to 128,000 | 20 RPM | Varies | 200 RPD (Soft) | Rolling 24 Hours | From $5 prepay |
| **Mistral AI API** | `codestral-2501` | 32,768 tokens | 1 RPS (~60 RPM) | 500,000 TPM | Unlimited (Exp. tier)| Hourly soft | Pay-as-you-go |
| **Mistral AI API** | `mistral-large-latest` | 128,000 tokens | 1 RPS (~60 RPM) | 500,000 TPM | Unlimited (Exp. tier)| Hourly soft | $2.00 / 1M input |
| **Cloudflare Workers** | `@cf/meta/llama-3.1-8b-instruct`| 8,192 tokens | Edge concurrency | 10k Neurons/day | ~200k-500k TPD | 00:00 UTC (Daily) | $5/mo Workers Paid |
| **GitHub Models** | `gpt-4o` / `claude-3-5-sonnet` | Up to 128,000 | 15 RPM | Low concurrency | 150 RPD | 00:00 UTC (Daily) | Azure AI Foundry |
| **Cohere API** | `command-r` / `command-r-plus` | 128,000 tokens | 100 RPM | Trial limits | 1,000 Calls/month | 1st of month | Pay-as-you-go |

---

## 2. Web Chat Interface Quotas & Reset Timers

| Platform | Model | Free Turn / Message Allowance | Reset Interval Mechanism | Fallback Behavior on Depletion |
|---|---|---|---|---|
| **ChatGPT (Free)** | GPT-4o | ~10 to 16 messages / 3 hours (Dynamic based on load) | **Strict 3-hour rolling timer** from the first prompt sent | Automatically downgrades to unlimited GPT-4o mini |
| **ChatGPT (Free)** | DALL-E 3 | 2 image generations per day | **24 hours** from first generation | Prompts return "limit reached" until reset timer |
| **Claude.ai (Free)** | Claude 3.5 Sonnet | ~10 to 30 messages / 5 hours (Dynamic based on token volume) | **Strict 5-hour rolling timer** displayed in the UI | Completely blocks new messages until the timer expires |
| **Google Gemini (Free)**| Gemini 1.5 Flash | Virtually unlimited (Soft anti-spam limit) | Rolling hourly | Throttles to slower generation |
| **DeepSeek (Free)** | DeepSeek-V3 & R1 | ~50-100 messages / hour | Rolling hourly | Displays "server busy", retry after 1 minute |
| **Microsoft Copilot** | GPT-4o | 30 turns per topic / conversation | Reset when clicking "New Topic" button | Requires starting new topic thread |
| **Microsoft Designer** | DALL-E 3 | 15 Fast Boosts / day | Daily at 00:00 UTC | Generates in "Standard" slow queue (never cuts off) |
| **Perplexity AI** | Standard / Pro | Unlimited Quick Search; 5 Pro Searches / 4 hours | **4-hour rolling timer** | Pro search switch toggles to standard search |
| **Ideogram** | Ideogram 2.0 | 10 slow prompt submissions / day (40 images) | Daily at 00:00 UTC | Generation disabled until reset |
| **Leonardo.ai** | Multi-model | 150 generation tokens / day | **24 hours rolling** | Prompts locked until tokens replenish |
| **Suno AI** | Audio / Music | 50 credits / day (= 10 generated songs) | Daily at 00:00 UTC | Song creation locked until next day |
| **Kling AI** | Video (T2V/I2V) | 66 credits / day (= 6 video generations) | Daily at 00:00 UTC | Generation disabled until daily claim |

---

## 3. Developer IDE & Extension Quotas

| Tool | Autocomplete Limit | Chat & Command Limit | Reset Interval | Bypass / Extension Hack |
|---|---|---|---|---|
| **Cursor (Hobby)** | 2,000 completions / month | 50 one-off slow requests to premium models | Monthly on signup date | Switch to Continue.dev or Cline with free Gemini key |
| **Windsurf (Free)** | **Unlimited** inline completions | ~100 Cascade/Chat credits | Monthly on signup date | Use Codeium chat models when Cascade is exhausted |
| **GitHub Copilot (Free)**| 2,000 completions / month | 50 chat messages / month | Monthly on 1st | Verified GitHub Student Developer Pack (100% Free Pro) |
| **Supermaven (Free)** | **Unlimited** inline completions | None (Chat is Pro only) | Permanent | Pair with Cline or Continue.dev for chat |
| **Continue.dev** | **Unlimited** (BYOK / Ollama) | **Unlimited** (BYOK / Ollama) | Never | Open-source — zero artificial limits |
| **Cline / Roo Code** | **Unlimited** (BYOK / Ollama) | **Unlimited** (BYOK / Ollama) | Never | Open-source — plug in free Google AI Studio key |

---

## 4. Reset Cycle Strategies: How to Never Run Out of Tokens

1. **The Timezone Arbitrage (00:00 UTC vs Rolling)**:
   * Services with **fixed 00:00 UTC resets** (Google AI Studio, Groq Cloud, Cerebras, SambaNova, Bing Designer) refresh all your daily quotas simultaneously at:
     * `04:00 GST` (Gulf Standard Time)
     * `01:00 BST` (British Summer Time)
     * `20:00 EDT` (US Eastern Time)
     * `17:00 PDT` (US Pacific Time)
   * Time your batch scripts or large token ingestions right before 00:00 UTC so you get a double-quota window within minutes.

2. **Handling 429 (Too Many Requests) Errors**:
   * Implement an **exponential backoff with jitter** in your API clients:
     ```python
     import time, random

     def api_call_with_retry(fn, max_retries=5):
         for attempt in range(max_retries):
             try:
                 return fn()
             except Exception as e:
                 if "429" in str(e) and attempt < max_retries - 1:
                     sleep_time = (2 ** attempt) + random.uniform(0.1, 1.0)
                     time.sleep(sleep_time)
                 else:
                     raise e
     ```

3. **Context Window Compression**:
   * If you are nearing token limits on models with smaller context windows (e.g., 8k on Groq 8B):
     * Strip whitespace and code comments before submitting.
     * Use a system prompt instructing the model to reply concisely in raw JSON or bullet points.
     * Route long-context requests (>32k) strictly to **Google AI Studio (Gemini 1.5 Flash)** which boasts a 1,000,000-token capacity for free.
