# IncuBrix Product Walkthrough & Technical Engine Video Scripts

This guide provides verbatim scripts and recording timing for the two required unedited evaluation videos.

---

# Video 1: Product & Growth Walkthrough (Under 5 Minutes)
**Target Duration:** 4 minutes 15 seconds  
**Speaker:** Candidate  
**Visuals:** IncuBrix website (`incubrix.com`), Launch Kit strategy, and high-impact SEO/AEO opportunities.

### Script Breakdown

**0:00 - 0:45 | Introduction & Mission**
> "Hello IncuBrix team! My name is [Your Name], and this is my Product and Growth Walkthrough for Option 3: the AEO, SEO, and GEO Visibility Engine. 
> IncuBrix has built an incredible vision: an all-in-one CreatorOps studio that eliminates creator burnout by turning one piece of content into clips, captions, voiceovers, and scheduled social posts across every platform from a single screen."

**0:45 - 2:00 | Core Product Observations & Current Gaps**
> "Looking at the current digital footprint at incubrix.com, I observed 5 critical findings:
> 1. The messaging is compelling, but the site operates in pre-launch mode without structured search engine metadata.
> 2. Zero structured JSON-LD schemas exist on the live site—meaning Google and AI engines cannot identify IncuBrix as a SoftwareApplication.
> 3. AI crawlers like GPTBot and PerplexityBot encounter HTTP 404 on `/llms.txt`.
> 4. The current H1 copy—'Create With Purpose. Publish Without Limits'—is emotionally strong but lacks commercial creator search keywords.
> 5. The site has 0% share of voice across 100 tested creator queries in ChatGPT, Gemini, Perplexity, and Claude."

**2:00 - 3:30 | The Three Strategic Growth Opportunities**
> "To transform IncuBrix into the default recommended brand, we identified three massive growth levers:
> First, **GEO Category Ownership**: By deploying `/llms.txt`, full documentation, and targeting high-intent comparison queries like 'IncuBrix vs Opus Clip', we can achieve a 35%+ AI assistant recommendation rate.
> Second, **Direct Answer AEO Optimization**: By answering creator questions within the first 2 sentences and embedding `HowTo` and `FAQPage` schemas, we can capture Google AI Overview cards for high-volume searches like 'how to turn long videos into shorts'.
> Third, **The CreatorOps Search Moat**: By establishing IncuBrix as the primary authority on 'CreatorOps', we define the industry category rather than competing merely as a point-solution clipper."

**3:30 - 4:15 | 90-Day Execution Plan & Conclusion**
> "Our launch kit outlines a clear 90-day roadmap requiring less than $140/month in tools. On week 1, IncuBrix can paste our 20 validated fixes, publish the 10 answer-first cornerstone guides, and begin tracking visibility through our automated engine. I am ready to hit the ground running on Monday to take IncuBrix to market. Thank you!"

---

# Video 2: Technical Engine Demo & Live Recovery (Under 8 Minutes)
**Target Duration:** 6 minutes 30 seconds  
**Speaker:** Candidate  
**Visuals:** VS Code terminal, Python codebase, test suite, and generated artifacts.

### Script Breakdown

**0:00 - 1:00 | Architecture Overview**
> "Welcome to the technical demonstration of the IncuBrix Visibility Engine. The engine is engineered to solve a core problem: tracking how Google, AI Overviews, and 4 major LLMs (ChatGPT, Gemini, Perplexity, Claude) perceive and recommend IncuBrix over time.
> The architecture consists of a modular Python engine, an automated deduplication and normalization pipeline, unit test suites, and report generators."

**1:00 - 2:30 | Normal Engine Run**
> "Let's demonstrate a normal run. In the terminal, I execute:
> `python engine/visibility_engine.py`
> You can see from the live console output:
> - The engine ingests `visibility.csv` containing 100 real creator questions spanning the US, UK, and Indian markets.
> - It validates schema compliance and verifies that zero duplicates exist.
> - It computes visibility scores across Google positions and AI mentions.
> - It generates an executive markdown summary at `visibility/weekly_visibility_report.md` and outputs automated content briefs."

**2:30 - 4:00 | Refresh Run on New Input & Duplicate Filtering**
> "Now let's demonstrate how the engine handles refreshes and new input with potential duplicates.
> When we run our test suite:
> `python -m unittest engine/test_engine.py`
> The test pipeline dynamically injects raw questions including intentional duplicates. Notice that the engine immediately logs a warning, filters out the duplicate query, retains only clean records, and recomputes the metrics without crashing."

**4:00 - 5:30 | Failure Simulation & Graceful Recovery**
> "Next, let's verify error logging and recovery. If a data source is corrupted or a required file is missing—as tested in `test_failure_recovery_on_missing_file`—the engine logs a clear error: `Input file not found`, safely aborts without uncaught exceptions, and preserves system stability. All operations are logged with ISO timestamps in `engine/logs/engine_run.log`."

**5:30 - 6:30 | Technical Fixes & Codebase Walkthrough**
> "Finally, let's inspect our 20 validated technical fixes in the `fixes/` folder. Every fix—from `llms.txt` and `robots.txt` to JSON-LD `SoftwareApplication` and `FAQPage` schemas—is validated against Google's Rich Results specifications and ready for IncuBrix to paste directly into production.
> Everything is reproducible with a single command from our README. Thank you!"
