# Free AI Encyclopedia Companion Tools

This folder contains command-line utilities to test and benchmark free AI APIs and calculate financial savings.

---

## 1. Free API Health & Latency Benchmarker (`test_free_apis.py`)

A zero-dependency Python script that tests connectivity, latency, and tokens-per-second across popular free API providers.

### How to Run:
```bash
# Optional: Set your free API keys in PowerShell
$env:GEMINI_API_KEY="AIzaSy..."
$env:GROQ_API_KEY="gsk_..."
$env:OPENROUTER_API_KEY="sk-or-..."

# Run the test
python tools/test_free_apis.py
```

---

## 2. Subscription vs. Free Savings Calculator (`token_cost_calculator.py`)

Calculates how much money you save annually by replacing paid subscriptions (ChatGPT Plus, Claude Pro, Cursor Pro, Midjourney, etc.) with 1:1 free alternatives.

### How to Run:
```bash
python tools/token_cost_calculator.py
```
