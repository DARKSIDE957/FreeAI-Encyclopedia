#!/usr/bin/env python3
"""
AI Subscription vs. Free Stack Cost & Savings Calculator
Author: DARKSIDE957
Date: October 2, 2026

Calculates real-world financial savings by comparing paid AI subscriptions
against the zero-dollar free tiers and open-source models documented in this repo.
"""

import sys

SUBSCRIPTION_CATALOG = {
    "1": {"name": "ChatGPT Plus (OpenAI)", "cost": 20.0, "free_alt": "DeepSeek-V3 / R1 + Mistral Le Chat"},
    "2": {"name": "Claude Pro (Anthropic)", "cost": 20.0, "free_alt": "Google AI Studio (Gemini 1.5 Pro) + Claude Free"},
    "3": {"name": "Cursor Pro (Anysphere)", "cost": 20.0, "free_alt": "Cline / Continue.dev + Free Gemini Flash API"},
    "4": {"name": "GitHub Copilot (Microsoft)", "cost": 10.0, "free_alt": "Supermaven Free + Amazon Q Developer Free"},
    "5": {"name": "Midjourney Standard (Image)", "cost": 30.0, "free_alt": "Local FLUX.1-schnell + Ideogram 2.0 Free"},
    "6": {"name": "Perplexity Pro (Search)", "cost": 20.0, "free_alt": "Perplexity Free (5 Pro/4h) + Genspark Free"},
    "7": {"name": "ElevenLabs Creator (Voice)", "cost": 22.0, "free_alt": "Kokoro-82M (Local/CPU) + Fish Audio Free"},
    "8": {"name": "Suno / Udio Pro (Music)", "cost": 10.0, "free_alt": "Suno Free (50 daily credits = 10 songs/day)"},
    "9": {"name": "Runway Gen-3 Standard (Video)", "cost": 15.0, "free_alt": "Kling AI (66 daily credits = 6 videos/day)"},
}

PRESETS = {
    "developer": ["1", "3", "4", "6"],  # ChatGPT, Cursor, Copilot, Perplexity
    "creator": ["1", "5", "7", "8", "9"],  # ChatGPT, Midjourney, ElevenLabs, Suno, Runway
    "power_user": ["1", "2", "3", "5", "6", "7"],  # Everything heavy
}

def print_banner():
    print("=" * 68)
    print("       FREE AI ENCYCLOPEDIA - SUBSCRIPTION SAVINGS CALCULATOR       ")
    print("=" * 68)

def run_calculator():
    print_banner()
    print("\nSelect your usage profile or customize:")
    print("  [1] Software Developer Bundle  (ChatGPT + Cursor + Copilot + Perplexity)")
    print("  [2] Content Creator Bundle     (ChatGPT + Midjourney + ElevenLabs + Suno + Runway)")
    print("  [3] Maximum AI Power User      (All Flagship Subscriptions)")
    print("  [4] Custom Selection           (Pick individual services)")
    
    choice = input("\nEnter choice [1-4] (default: 1): ").strip() or "1"
    
    selected_keys = []
    if choice == "1":
        selected_keys = PRESETS["developer"]
    elif choice == "2":
        selected_keys = PRESETS["creator"]
    elif choice == "3":
        selected_keys = PRESETS["power_user"]
    elif choice == "4":
        print("\nSelect the subscriptions you currently pay for (or plan to):")
        for key, item in SUBSCRIPTION_CATALOG.items():
            print(f"  [{key}] {item['name']:<30} (${item['cost']:.2f}/mo)")
        raw = input("\nEnter numbers separated by spaces (e.g. 1 3 5): ").strip()
        selected_keys = [k for k in raw.split() if k in SUBSCRIPTION_CATALOG]
    else:
        selected_keys = PRESETS["developer"]

    monthly_total = sum(SUBSCRIPTION_CATALOG[k]["cost"] for k in selected_keys)
    yearly_total = monthly_total * 12.0

    print("\n" + "-" * 68)
    print(f"{'SERVICE':<28} | {'PAID COST':<10} | {'100% FREE EQUIVALENT'}")
    print("-" * 68)
    for k in selected_keys:
        item = SUBSCRIPTION_CATALOG[k]
        print(f"{item['name']:<28} | ${item['cost']:>6.2f}/mo | {item['free_alt']}")
    
    print("-" * 68)
    print(f"Total Monthly Cost Currently:    ${monthly_total:>8.2f} / month")
    print(f"Total Annual Cost Currently:     ${yearly_total:>8.2f} / year")
    print("=" * 68)
    print(f">>> YOUR ANNUAL SAVINGS WITH FREE STACK: ${yearly_total:>8.2f} / YEAR <<<")
    print("=" * 68)
    print("\nRecommended Next Step:")
    print("Read 'docs/09-paid-vs-free-verdict-matrix.md' to switch to your zero-cost stack today!")

if __name__ == "__main__":
    run_calculator()
