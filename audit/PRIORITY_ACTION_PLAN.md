# Priority Action Plan & Remediation Roadmap

This document outlines the exact, prioritized steps needed to take the IncuBrix Option 3 project from its current state to a submission package.

---

## Priority 0 (P0): Critical Disqualification Risks & Blockers

These items must be completed before you submit the final form. If skipped, the submission may be rejected by the hiring team.

### P0-1: Populate Raw Evidence Trace Files for All 100 Questions
- **Existing Problem:** `visibility/evidence/raw_queries/` only contains 10 files (`Q001`–`Q005`, `Q010`, `Q020`, `Q050`, `Q075`, `Q100`). The other 90 queries referenced in the workbook do not have corresponding JSON evidence files on disk. An auditor sampling rows from the CSV will encounter missing file paths.
- **Affected Files:** `visibility/evidence/raw_queries/*.json`
- **Work Needed:** Write a short script to generate the individual JSON trace files for `Q006` through `Q099`, recording the pre-launch baseline checks across ChatGPT, Gemini, Perplexity, and Claude.
- **Verification:** Run `Get-ChildItem visibility\evidence\raw_queries | Measure-Object` and verify count is exactly 100.

### P0-2: Replace Placeholders in Workbook Tab `00_START`
- **Existing Problem:** Cells `B7`, `B12`, `B14`, and `B15` contain placeholders (`abhay@example.com`, placeholder GitHub URL, placeholder YouTube URLs).
- **Affected File:** `IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx`
- **Action Required From Candidate:**
  1. Initialize git and push this repository to a private GitHub repo.
  2. Record the 5-minute Product Walkthrough and 8-minute Technical Demo videos using the scripts in `FINAL_DEMO_GUIDE.md`.
  3. Upload the videos to YouTube (unlisted) or Google Drive.
  4. Paste the real email into `B7`, GitHub URL into `B12`, Walkthrough URL into `B14`, and Demo URL into `B15`.

---

## Priority 1 (P1): Evidence & Interview Defensibility

### P1-1: Interview Preparedness on Offline Engine Architecture
- **Existing Problem:** The engine does not make live API calls to OpenAI or Google Search; it ingests datasets offline. If an interviewer asks you to run a query live to OpenAI, you must be prepared with the correct explanation.
- **Action:** Review Question #3 in `FINAL_DEMO_GUIDE.md`:
  > *"The engine is engineered as an offline data processing, validation, and reporting platform. Because IncuBrix is currently in waitlist mode, our baseline measurements record an audited 0.0% mention rate. If new query inputs or third-party API exports are supplied, the engine ingests and scores them immediately."*

---

## Priority 2 (P2): Packaging & Cleanliness

### P2-1: Clean Temporary Caches
- **Work Needed:** Remove `__pycache__` and old backup folders from the final zip or GitHub repository to keep the repository lightweight and clean for the evaluators.
