# Step-by-Step Guide: How to Obtain & Configure Provider API Keys Safely

This guide explains how to obtain official API credentials for the five search and AI providers without exposing secrets or incurring unexpected costs.

---

## 1. Environment File Setup

In the root directory of the project, create a file named `.env` by copying `.env.example`:

```powershell
Copy-Item .env.example .env
```

Open `.env` in any text editor. Only paste keys into `.env` (which is excluded from Git commits via `.gitignore`).

---

## 2. Obtaining Keys for Each Provider

### A. Google Gemini API (Recommended for Immediate Free Testing)
- **Portal:** [Google AI Studio](https://aistudio.google.com/)
- **Cost:** Free tier available (up to 15 requests/minute at zero cost).
- **Steps:**
  1. Sign in with any Google account at `https://aistudio.google.com/`.
  2. Click **Get API key** $\rightarrow$ **Create API key in new project**.
  3. Copy the key and set in `.env`:
     ```env
     GEMINI_API_KEY=AIzaSy...
     GEMINI_MODEL=gemini-2.0-flash
     ```

### B. OpenAI API (ChatGPT)
- **Portal:** [OpenAI Developer Platform](https://platform.openai.com/api-keys)
- **Cost:** Pay-as-you-go (~$0.0005 per query with `gpt-4o-mini`).
- **Steps:**
  1. Sign in at `https://platform.openai.com/`.
  2. Navigate to **API Keys** $\rightarrow$ **Create new secret key**.
  3. Set in `.env`:
     ```env
     OPENAI_API_KEY=sk-proj-...
     OPENAI_MODEL=gpt-4o-mini
     ```

### C. Perplexity AI API (Sonar with Live Search)
- **Portal:** [Perplexity AI API Settings](https://www.perplexity.ai/settings/api)
- **Cost:** Pay-as-you-go (~$0.001 per query).
- **Steps:**
  1. Sign in at `https://www.perplexity.ai/`.
  2. Navigate to **Settings** $\rightarrow$ **API** $\rightarrow$ **Generate API Key**.
  3. Set in `.env`:
     ```env
     PERPLEXITY_API_KEY=pplx-...
     PERPLEXITY_MODEL=sonar
     ```

### D. Anthropic Claude API
- **Portal:** [Anthropic Console](https://console.anthropic.com/settings/keys)
- **Cost:** Pay-as-you-go (~$0.0008 per query with Haiku).
- **Steps:**
  1. Sign in at `https://console.anthropic.com/`.
  2. Click **API Keys** $\rightarrow$ **Create Key**.
  3. Set in `.env`:
     ```env
     ANTHROPIC_API_KEY=sk-ant-...
     ANTHROPIC_MODEL=claude-3-5-haiku-latest
     ```

### E. Google Search / SerpAPI
- **Portal:** [SerpAPI](https://serpapi.com/)
- **Cost:** Free tier includes 100 free searches/month.
- **Steps:**
  1. Register at `https://serpapi.com/`.
  2. Copy your private API key from your dashboard.
  3. Set in `.env`:
     ```env
     SERPAPI_API_KEY=...
     ```

---

## 3. Verifying Configuration Safely

After setting any key in `.env`, run the health check CLI:

```powershell
python -m engine.providers.provider_status
```

Then execute a single-question live test:

```powershell
python engine/run_live_test.py --provider gemini --market US
```

The system will execute one live call, extract citations and competitor mentions, and save the raw JSON response to `visibility/evidence/live_runs/`.
