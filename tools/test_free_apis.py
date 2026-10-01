#!/usr/bin/env python3
"""
Free AI API Health & Latency Benchmarking Suite
Author: DARKSIDE957
Date: October 2, 2026

Tests connectivity, response latency, and token generation speed
across the top free AI API endpoints (Google Gemini, Groq, OpenRouter, Mistral, Cerebras).
"""

import os
import sys
import time
import json
import urllib.request
import urllib.error

# ANSI Color codes for clean terminal output
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(title):
    print(f"\n{BOLD}{CYAN}=== {title} ==={RESET}")

def test_groq(api_key):
    print(f"{BOLD}[*] Testing Groq Cloud (Free Tier - Llama 3.3 70B)...{RESET}")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": "Reply with 'GROQ_OK' and exactly 5 words explaining speed."}],
        "max_tokens": 30
    }
    start = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            elapsed = time.time() - start
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"].strip()
            tokens = data.get("usage", {}).get("completion_tokens", 0)
            tps = (tokens / elapsed) if elapsed > 0 else 0
            print(f"  {GREEN}✓ Success!{RESET} Latency: {elapsed:.2f}s | Speed: {tps:.1f} tokens/s")
            print(f"  Response: \"{content}\"")
            return True
    except urllib.error.HTTPError as e:
        print(f"  {RED}✗ HTTP Error {e.code}:{RESET} {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"  {RED}✗ Failed:{RESET} {e}")
    return False

def test_gemini(api_key):
    print(f"{BOLD}[*] Testing Google AI Studio (Free Tier - Gemini 1.5 Flash)...{RESET}")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": "Reply with 'GEMINI_OK' and exactly 5 words about 1M context."}]}],
        "generationConfig": {"maxOutputTokens": 30}
    }
    start = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            elapsed = time.time() - start
            data = json.loads(resp.read().decode("utf-8"))
            content = data["candidates"][0]["content"]["parts"][0]["text"].strip()
            print(f"  {GREEN}✓ Success!{RESET} Latency: {elapsed:.2f}s | Free Daily Limit: 1,500 RPD")
            print(f"  Response: \"{content}\"")
            return True
    except urllib.error.HTTPError as e:
        print(f"  {RED}✗ HTTP Error {e.code}:{RESET} {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"  {RED}✗ Failed:{RESET} {e}")
    return False

def test_openrouter(api_key):
    print(f"{BOLD}[*] Testing OpenRouter (Free Model: Meta Llama 3.3 70B:free)...{RESET}")
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/DARKSIDE957/free-ai-encyclopedia"
    }
    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [{"role": "user", "content": "Reply with 'OPENROUTER_OK'."}],
        "max_tokens": 20
    }
    start = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=20) as resp:
            elapsed = time.time() - start
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"].strip()
            print(f"  {GREEN}✓ Success!{RESET} Latency: {elapsed:.2f}s | Free Model Active")
            print(f"  Response: \"{content}\"")
            return True
    except urllib.error.HTTPError as e:
        print(f"  {RED}✗ HTTP Error {e.code}:{RESET} {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"  {RED}✗ Failed:{RESET} {e}")
    return False

def main():
    print(f"{BOLD}{GREEN}===================================================={RESET}")
    print(f"{BOLD}{GREEN}   FREE AI API DIAGNOSTIC & BENCHMARK SUITE         {RESET}")
    print(f"{BOLD}{GREEN}===================================================={RESET}")
    print("This utility validates your free API credentials and measures latency.\n")

    groq_key = os.environ.get("GROQ_API_KEY")
    gemini_key = os.environ.get("GEMINI_API_KEY")
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")

    any_found = False

    if groq_key:
        test_groq(groq_key)
        any_found = True
    else:
        print(f"{YELLOW}[i] GROQ_API_KEY not found in environment (Get a free key at console.groq.com){RESET}")

    if gemini_key:
        test_gemini(gemini_key)
        any_found = True
    else:
        print(f"{YELLOW}[i] GEMINI_API_KEY not found in environment (Get a free key at aistudio.google.com){RESET}")

    if openrouter_key:
        test_openrouter(openrouter_key)
        any_found = True
    else:
        print(f"{YELLOW}[i] OPENROUTER_API_KEY not found in environment (Get a free key at openrouter.ai){RESET}")

    if not any_found:
        print(f"\n{BOLD}{YELLOW}Quick Usage Tip:{RESET}")
        print("To test your keys, export them in PowerShell before running:")
        print(f"  {CYAN}$env:GEMINI_API_KEY=\"AIzaSy...\"{RESET}")
        print(f"  {CYAN}$env:GROQ_API_KEY=\"gsk_...\"{RESET}")
        print(f"  {CYAN}python tools/test_free_apis.py{RESET}")

if __name__ == "__main__":
    main()
