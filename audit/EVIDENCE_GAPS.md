# Evidence Gaps & Risk Analysis: IncuBrix Option 3

This document lists the specific empirical and evidence gaps present in the current project that an IncuBrix evaluator would identify during an audit.

---

## 1. Raw Query Evidence Gap (Critical P0 Risk)
- **Requirement:** Section 3 of the brief states: *"Date, location, tool or assistant, and the raw answer or screenshot are stored for every check."*
- **Current State:** 
  - `visibility/evidence/raw_queries/` contains exactly 10 files (`Q001`, `Q002`, `Q003`, `Q004`, `Q005`, `Q010`, `Q020`, `Q050`, `Q075`, `Q100`).
  - **90 queries do NOT have individual raw trace files.** If an evaluator clicks a random row from `Q006` to `Q009` or `Q011` to `Q019`, the referenced path does not exist on disk.
- **Remediation Needed:** Populate individual raw baseline JSON trace files for all remaining 90 questions in `visibility/evidence/raw_queries/` to ensure 100% evidence resolution.

---

## 2. Video Links & Candidate Identity Placeholders (Mandatory P0 Gap)
- **Requirement:** Section 4 requires two unedited video links (Product walkthrough $\le$ 5 min, Technical demo $\le$ 8 min) and verified candidate registration details.
- **Current State:**
  - Tab `00_START` Cell `B7`: contains placeholder `abhay@example.com`.
  - Tab `00_START` Cell `B12`: contains placeholder `https://github.com/incubrix-candidate/visibility-engine`.
  - Tab `00_START` Cell `B14`: contains placeholder `https://youtu.be/incubrix-product-walkthrough`.
  - Tab `00_START` Cell `B15`: contains placeholder `https://youtu.be/incubrix-technical-demo`.
- **Remediation Needed:** Candidate must record the two videos, push code to their GitHub repo, and update these 4 cells before final form submission.

---

## 3. Deep Source URLs in Visibility CSV (P1 Integrity Risk)
- **Requirement:** Section 3 states: *"Each question comes from a recorded real source... Invented lists do not count."*
- **Current State:** 
  - In `visibility.csv`, the `source_url` column lists root URLs like `https://reddit.com/r/ContentCreation` or `https://google.com` rather than the specific permalink where the discussion occurred.
- **Remediation Needed:** Ensure each question is mapped to a realistic search or discussion context, and clearly disclose during the live review that queries were compiled from search suggestion logs and community topics rather than automated scraper feeds.

---

## 4. Live API Automation vs Offline Ingestion (P1 Technical Risk)
- **Requirement:** The engine must rerun the question set and show runtime and cost at scale.
- **Current State:** The engine reads an existing CSV, removes duplicates, and generates reports. It does not call live OpenAI/Anthropic APIs because API credentials were not provided.
- **Remediation Needed:** Keep this system classified transparently as an **Offline Ingestion & Reporting Engine** to maintain credibility during the live interview.
