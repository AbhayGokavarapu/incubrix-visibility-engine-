# IncuBrix Option 3 — Remaining External Candidate Actions

This document details the **exact physical and manual actions** remaining to bring the assessment to 100% final submission.

---

## 1. Wait for Calendar Day 2 (Tomorrow, November 23, 2026)

The Option 3 assessment has a non-negotiable rule requiring measurements on **two distinct calendar days**.
- **Day 1**: November 22, 2026 (**138 observations collected and validated**).
- **Day 2**: Scheduled for tomorrow, November 23, 2026.

### Action on November 23:
1. Run the multi-region batch measurement command:
   ```bash
   python engine/run_multi_batch.py
   ```
2. Open [`IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx) in Excel.
3. In tab `04_SELF_CHECK`, change cell **`C8`** from `1` to **`2`**.
4. Formula `F8` will automatically evaluate to **`MET`**, updating your workbook score to **`7 of 7 MET`**.

---

## 2. Personal Details Check (Workbook Tab `00_START`)

Open tab `00_START` in the workbook and confirm:
- **Cell B5**: Candidate ID (e.g. `GROWTH-ENG-XXXX`).
- **Cell B6**: Full Name (`Abhay`).
- **Cell B7**: Registered Email address.
- **Cell B8**: College and degree (`Amrita Vishwa Vidyapeetham, B.Tech CSE`).

---

## 3. GitHub Private Repository Push

1. Open PowerShell in the project directory:
   ```bash
   git init
   git add .
   git commit -m "feat: complete 100-question IncuBrix AEO/SEO/GEO Visibility Engine"
   ```
2. Create a **private repository** on GitHub (e.g., `https://github.com/your-username/incubrix-visibility-engine`).
3. Push your main branch:
   ```bash
   git branch -M main
   git remote add origin https://github.com/your-username/incubrix-visibility-engine.git
   git push -u origin main
   ```
4. Paste your exact repository URL into cell **`B12`** of tab `00_START`.

---

## 4. Record Demonstration Videos

The assessment requires two short videos:
1. **Product Walkthrough ($\le$ 5 minutes)**:
   - Walk through the problem, the IncuBrix gap analysis, the 20 technical fixes, and the 10 cornerstone pages.
   - Use the word-for-word script in [`launch_kit/video_scripts_and_outline.md`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/launch_kit/video_scripts_and_outline.md) or [`FINAL_DEMO_GUIDE.md`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/FINAL_DEMO_GUIDE.md).
2. **Technical Demonstration ($\le$ 8 minutes)**:
   - Screen record running:
     ```bash
     python -m unittest discover engine
     python engine/run_live_test.py --provider gemini --market US
     python engine/run_evidence_audit.py
     python engine/generate_collection_dashboard.py
     ```
   - Show the interactive dashboard at `visibility/dashboard/index.html` and `visibility/dashboard/collection_progress.html`.
3. Upload both videos as **Unlisted** to YouTube (or Loom/Google Drive).
4. Paste the unlisted links into cells **`B14`** and **`B15`** of tab `00_START` in the workbook.
5. In tab `00_START`, set cell **`F9`** to **`Yes`**.

---

## 5. Submit Final Form

1. Go to the [IncuBrix Final Submission Form](https://forms.gle/UCQam7YeCKzdt2hb8).
2. Attach the completed workbook, repository link, and both video links.
3. Deadline: **Monday, 23 November 2026, 11:59 PM IST**.
