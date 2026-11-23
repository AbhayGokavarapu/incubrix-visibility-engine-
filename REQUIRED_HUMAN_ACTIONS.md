# IncuBrix Option 3 — Required Candidate Human Actions

This document details the **exact physical and manual actions** remaining for you to finalize and submit your assessment before the official deadline (**Monday, 23 November 2026, 11:59 PM IST**).

---

## 1. Verify Personal Details in Submission Workbook

Open [`IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx) in Excel and check sheet `00_START`:
- **Cell B5**: Candidate ID (Check your email from IncuBrix, e.g. `GROWTH-ENG-XXXX`).
- **Cell B6**: Full Name (`Abhay`).
- **Cell B7**: Registered Email address.
- **Cell B8**: College and degree (`Amrita Vishwa Vidyapeetham, B.Tech CSE`).

---

## 2. Push Codebase to Private GitHub Repository

1. Open PowerShell in the project directory:
   ```bash
   git init
   git add .
   git commit -m "feat: complete IncuBrix AEO/SEO/GEO Visibility Engine with Day 1 & Day 2 evidence"
   ```
2. Create a **private repository** on GitHub (e.g. `https://github.com/your-username/incubrix-visibility-engine`).
3. Push your main branch:
   ```bash
   git branch -M main
   git remote add origin https://github.com/your-username/incubrix-visibility-engine.git
   git push -u origin main
   ```
4. Paste your exact repository URL into cell **`B12`** of tab `00_START`.

---

## 3. Record Demonstration Videos

The assessment requires two short videos:
1. **Product Walkthrough ($\le$ 5 minutes)**:
   - Walk through the problem, the IncuBrix website gap analysis, the 20 technical fixes, and the 10 cornerstone pages.
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

## 4. Final Google Form Submission

1. Open the [IncuBrix Final Submission Form](https://forms.gle/UCQam7YeCKzdt2hb8).
2. Attach:
   - `IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx`
   - Your private GitHub repository link
   - Both unlisted video links
3. Submit before **Monday, 23 November 2026, 11:59 PM IST**.
