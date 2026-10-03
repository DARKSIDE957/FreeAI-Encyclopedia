# 05. AI Image Generation & Vision Models

> **Last Updated**: October 3, 2026  
> **Coverage**: Text-to-image synthesis, vector generation, upscaling, local ComfyUI/Forge setups, and free web quotas.

---

## Master Image Generation Quota Matrix

| Tool / Platform | Type | Free Quota / Allowance | Generation Speed | Paid Tier | Is Paid Worth It? | Best Free Alternative |
|---|---|---|---|---|---|---|
| **Ideogram** | Web App | 10 slow prompts/day (~40 images daily) | Fast on free tier | Basic: $8/mo<br>Plus: $20/mo | **5/10** (Text rendering is top-tier, but 40 free daily images is plenty) | **FLUX.1-schnell**, **Bing Designer** |
| **Leonardo.ai** | Web App | 150 tokens replenished every 24 hours (~15-30 images/day) | Moderate | Apprentice: $12/mo<br>Artisan: $24/mo | **5/10** (Great model ecosystem, but daily free allowance handles casual needs) | **Civitai Generator**, **Playground** |
| **Recraft.ai** | Web App | Daily free credits (~30-50 vector SVGs or raster images) | Blazing fast | Pro: $20/mo | **6/10** (Best vector SVG generator on Earth. Free is great for icons) | **Inkscape + Local SDXL** |
| **Krea.ai** | Web App | Generous daily credits for real-time canvas & upscaling | Real-time / Instant | Basic: $10/mo<br>Pro: $35/mo | **6/10** (Real-time generation is magical, free tier is enough to play) | **ComfyUI Realtime** |
| **Bing Image Creator (Designer)** | Web App (DALL-E 3) | 15 Fast Boosts / day + unlimited slower generations | Fast with boost; slow without | Bundled in Copilot Pro ($20/mo) | **3/10** (Do not pay. The free 15 daily boosts reset every midnight) | **Ideogram Free**, **FLUX Web Demos** |
| **Civitai On-Site Generator** | Web App | Free Buzz points granted daily on login (~50-100 Buzz) | Model dependent | Supporter: $5-$10/mo | **4/10** (Free buzz is enough for daily experiments) | **Local ComfyUI / Forge** |
| **Playground.com** | Web App | ~50 free images / day with canvas editing tools | Moderate | Pro: $15/mo | **5/10** (Solid graphic design suite) | **Leonardo.ai Free** |
| **ComfyUI** | Local Open Source | **100% Unlimited Forever** (Runs locally on your GPU) | Depends on GPU (2s - 20s) | None ($0 open-source) | **N/A** (Completely free) | **Forge WebUI** |
| **Stable Diffusion WebUI Forge** | Local Open Source | **100% Unlimited Forever** (Optimized for low VRAM) | Optimized CUDA/DirectML | None ($0 open-source) | **N/A** (Completely free) | **ComfyUI** |
| **Fooocus** | Local Open Source | **100% Unlimited Forever** (Midjourney UI replica locally) | Automated SDXL pipeline | None ($0 open-source) | **N/A** (Completely free) | **Midjourney ($10-$60/mo)** |

---

## Detailed Tool Breakdowns

### 1. Ideogram (King of Text and Typography)
* **Website**: [ideogram.ai](https://ideogram.ai)
* **What It Excels At**: Rendering legible, beautiful text, logos, t-shirt designs, posters, and typography inside generated images.
* **Free Quota**:
  * 10 prompt submissions per day under the slow priority queue (yielding 4 images per prompt = 40 images/day).
  * Access to Ideogram 2.0 model with full text rendering.
  * Reset Cycle: Daily at 00:00 UTC.
* **Paid Tier**: $8/mo (Basic) or $20/mo (Plus).
* **Is Paying Worth It?**: **5 / 10**  
  * *Verdict*: Unless you are generating commercial merchandise in bulk, 40 images per day on the free tier is more than enough for logos, thumbnails, and concept art.

---

### 2. Recraft.ai (King of Vector SVGs and Brand Graphics)
* **Website**: [recraft.ai](https://www.recraft.ai)
* **What It Excels At**: Generating clean, scalable vector graphics (`.svg`), 3D icons, clean UI illustrations, and brand assets.
* **Free Quota**:
  * Generous daily credit allowance.
  * Vector export (.svg) is available on the free tier without watermarks.
* **Paid Tier**: $20/month for Pro.
* **Is Paying Worth It?**: **6 / 10**  
  * *Verdict*: Graphic designers and UI designers love Recraft. Free tier is generous enough for web design projects and icon creation.

---

### 3. Microsoft Designer / Bing Image Creator (DALL-E 3)
* **Website**: [designer.microsoft.com/image-creator](https://designer.microsoft.com/image-creator)
* **What It Excels At**: Photorealism, natural language prompt adherence, complex multi-character scenes.
* **Free Quota**:
  * 15 "Boosts" (fast generation credits) every day.
  * Once boosts are depleted, generations continue at a lower priority queue for free (never completely cuts you off).
* **Reset Cycle**: Daily at 00:00 UTC.
* **Cost**: $0.00.

---

### 4. Local Image Generation: The Zero-Dollar Professional Studio

If you possess a modern NVIDIA GPU (RTX 2060 6GB or higher), you never need to pay for Midjourney or DALL-E 3 again.

#### Recommended Local Tools:
1. **ComfyUI** ([github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)):
   * Node-based modular interface.
   * Native support for **FLUX.1-schnell** (Apache 2.0 open-source, 4-step generation) and **FLUX.1-dev** (via GGUF / NF4 quantization).
   * Generates images rivaling Midjourney v6 in photorealism, skin textures, and lighting in 4 to 10 seconds.
2. **Stable Diffusion WebUI Forge** ([github.com/lllyasviel/stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)):
   * Slashes VRAM requirements by 50-75% compared to legacy AUTOMATIC1111.
   * Runs FLUX.1 and SDXL models easily on 6GB-8GB VRAM cards.
3. **Fooocus** ([github.com/lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)):
   * Designed specifically to mimic Midjourney's effortless UX: type a prompt, choose a style preset, click Generate.
   * Auto-refines prompts behind the scenes without complex parameter tweaking.

---

## The Big Comparison: Midjourney ($10-$60/mo) vs Free Options

* **Midjourney Price**: $10/mo (Basic: 200 min/mo), $30/mo (Standard: 15h fast + unlimited relaxed), $60/mo (Pro: 30h fast + stealth mode).
* **Is Midjourney Worth Paying For in 2026?**: **4 / 10**  
  * *Why?*: Midjourney no longer holds a monopoly on aesthetic quality.
  * **FLUX.1** (Open Source / Free) matches or exceeds Midjourney in prompt adherence, anatomy, and photorealism.
  * **Ideogram 2.0** (Free 40 images/day) completely crushes Midjourney in text and typography generation.
  * **Recraft.ai** (Free daily tier) generates true SVG vectors that Midjourney cannot produce.
  * *Final Verdict*: Unless you demand Midjourney's signature painterly artistic style and have zero interest in running local tools or free web alternatives, paying $30-$60/month is unnecessary.
