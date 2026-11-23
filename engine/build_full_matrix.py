import os
import sys
import csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.unified_analyzer import UnifiedProgressAnalyzer

def build_full_coverage_matrix():
    u = UnifiedProgressAnalyzer()
    questions = u.load_all_questions()
    obs = u.scan_stored_observations()

    obs_by_q_p = {}
    for o in obs:
        qid = o.get("question_id")
        p = o.get("provider_name")
        if qid:
            if qid not in obs_by_q_p:
                obs_by_q_p[qid] = set()
            obs_by_q_p[qid].add(p)

    output_path = "FULL_QUESTION_PROVIDER_DAY_MATRIX.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Question_ID", "Market", "Question_Text",
            "Google_Search_Status", "Gemini_Status", "ChatGPT_Web_Status", "Claude_Web_Status", "Perplexity_Web_Status",
            "Day1_Status", "Day2_Status", "Assistant_Coverage_Tier"
        ])
        for q in questions:
            qid = q["question_id"]
            mkt = q["market"]
            qtext = q["question"]
            provs = obs_by_q_p.get(qid, set())
            
            g_search = "VERIFIED (SERP)" if ("Google Search" in provs or "Google Search Web" in provs) else "NOT MEASURED"
            gemini = "VERIFIED (API Grounded)" if "Google Gemini" in provs else "PENDING (Rate Limited)"
            chatgpt = "VERIFIED (Manual)" if "ChatGPT Web" in provs else "PENDING MANUAL"
            claude = "VERIFIED (Manual)" if "Claude Web" in provs else "PENDING MANUAL"
            perp = "VERIFIED (Manual)" if "Perplexity Web" in provs else "PENDING MANUAL"

            asst_count = len([p for p in provs if p in ["Google Gemini", "ChatGPT Web", "Claude Web", "Perplexity Web"]])
            if asst_count == 4:
                tier = "FULL 4-ASSISTANT COMPLETE"
            elif asst_count > 0:
                tier = f"PARTIAL ({asst_count}/4 ASSISTANTS)"
            else:
                tier = "0/4 ASSISTANTS (SEARCH ONLY)"

            day1 = "MEASURED" if len(provs) > 0 else "NOT MEASURED"
            day2 = "PENDING (Scheduled Nov 23)"

            writer.writerow([qid, mkt, qtext, g_search, gemini, chatgpt, claude, perp, day1, day2, tier])

    print(f"Matrix built successfully: {output_path}")

if __name__ == "__main__":
    build_full_coverage_matrix()
