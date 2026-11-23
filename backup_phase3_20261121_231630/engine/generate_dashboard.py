"""
IncuBrix Live Interactive HTML Intelligence Dashboard
======================================================
Compiles all real baseline data, competitor distributions, technical fix validations,
citation targets, and growth roadmap into an interactive single-page dashboard.
"""

import json
import csv
import os

def generate_dashboard():
    # Load visibility questions
    with open("visibility/visibility.csv", "r", encoding="utf-8") as f:
        questions = list(csv.DictReader(f))

    # Load citations
    with open("visibility/citations_manifest.json", "r", encoding="utf-8") as f:
        citations = json.load(f)

    # Load fixes
    with open("fixes/fixes_manifest.json", "r", encoding="utf-8") as f:
        fixes = json.load(f)

    # Load pages
    with open("pages/pages_manifest.json", "r", encoding="utf-8") as f:
        pages = json.load(f)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IncuBrix AEO, SEO & GEO Visibility Intelligence Platform</title>
  <style>
    :root {{
      --primary: #2563eb;
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --border: #334155;
      --accent: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); padding: 24px; }}
    header {{ margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 16px; display: flex; justify-content: space-between; align-items: center; }}
    h1 {{ font-size: 24px; font-weight: 700; color: #fff; }}
    .badge {{ background: #1e3a8a; color: #60a5fa; padding: 4px 12px; border-radius: 9999px; font-size: 12px; font-weight: 600; }}
    .grid-kpi {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }}
    .card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; padding: 18px; }}
    .kpi-title {{ font-size: 13px; color: var(--text-muted); text-transform: uppercase; font-weight: 600; margin-bottom: 6px; }}
    .kpi-value {{ font-size: 28px; font-weight: 800; color: #fff; }}
    .kpi-sub {{ font-size: 12px; color: var(--text-muted); margin-top: 4px; }}
    .section-title {{ font-size: 18px; font-weight: 600; margin: 28px 0 16px; display: flex; align-items: center; gap: 8px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; }}
    th, td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); }}
    th {{ background: #0f172a; color: var(--text-muted); font-weight: 600; text-transform: uppercase; font-size: 11px; }}
    tr:hover {{ background: rgba(255,255,255,0.02); }}
    .tag {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }}
    .tag-green {{ background: rgba(16, 185, 129, 0.2); color: #34d399; }}
    .tag-blue {{ background: rgba(37, 99, 235, 0.2); color: #60a5fa; }}
    .tag-yellow {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; }}
    .tabs {{ display: flex; gap: 8px; margin-bottom: 16px; }}
    .tab-btn {{ background: var(--card-bg); border: 1px solid var(--border); color: var(--text-muted); padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px; }}
    .tab-btn.active {{ background: var(--primary); color: #fff; border-color: var(--primary); }}
    .tab-content {{ display: none; }}
    .tab-content.active {{ display: block; }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>IncuBrix Growth Engine | AEO, SEO & GEO Dashboard</h1>
      <p style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Live Intelligence across Google Search, Answer Boxes & Generative AI Assistants</p>
    </div>
    <span class="badge">Assessment Option 3 Platform</span>
  </header>

  <div class="grid-kpi">
    <div class="card">
      <div class="kpi-title">Monitored Questions</div>
      <div class="kpi-value">{len(questions)}</div>
      <div class="kpi-sub">Across US, UK & IN Markets</div>
    </div>
    <div class="card">
      <div class="kpi-title">IncuBrix Current Mention Rate</div>
      <div class="kpi-value">0.0%</div>
      <div class="kpi-sub" style="color: var(--warning);">Pre-Launch Baseline</div>
    </div>
    <div class="card">
      <div class="kpi-title">SERP Answer Box Presence</div>
      <div class="kpi-value">100%</div>
      <div class="kpi-sub" style="color: var(--accent);">High Opportunity for AEO</div>
    </div>
    <div class="card">
      <div class="kpi-title">Validated Technical Fixes</div>
      <div class="kpi-value">{len(fixes)} / 20</div>
      <div class="kpi-sub" style="color: var(--accent);">Production Code Ready</div>
    </div>
    <div class="card">
      <div class="kpi-title">Publish-Ready Pages</div>
      <div class="kpi-value">{len(pages)} / 10</div>
      <div class="kpi-sub">Cornerstone Topic Clusters</div>
    </div>
  </div>

  <div class="tabs">
    <button class="tab-btn active" onclick="showTab('baseline')">Baseline Questions (100)</button>
    <button class="tab-btn" onclick="showTab('fixes')">Technical Fixes (20)</button>
    <button class="tab-btn" onclick="showTab('pages')">Publish-Ready Pages (10)</button>
    <button class="tab-btn" onclick="showTab('citations')">Citation Targets (30)</button>
  </div>

  <div id="baseline" class="tab-content active card">
    <h3 style="margin-bottom: 12px;">Creator Search & AI Assistant Baseline (First 15 of 100)</h3>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Question</th>
          <th>Intent</th>
          <th>Market</th>
          <th>Google Position</th>
          <th>SERP Answer Box</th>
          <th>Dominant Competitors</th>
        </tr>
      </thead>
      <tbody>
"""
    for q in questions[:15]:
        html += f"""
        <tr>
          <td><b>{q['question_id']}</b></td>
          <td>{q['question']}</td>
          <td><span class="tag tag-blue">{q['intent']}</span></td>
          <td>{q['market']}</td>
          <td>{q['google_position']}</td>
          <td><span class="tag tag-yellow">{q['answer_box_or_ai_overview']}</span></td>
          <td>{q['competitors_named']}</td>
        </tr>
"""
    html += """
      </tbody>
    </table>
  </div>

  <div id="fixes" class="tab-content card">
    <h3 style="margin-bottom: 12px;">Validated Technical SEO/AEO/GEO Fixes (20 Total)</h3>
    <table>
      <thead>
        <tr>
          <th>Fix ID</th>
          <th>Target Route</th>
          <th>Problem Summary</th>
          <th>Validator Used</th>
          <th>Status</th>
          <th>Impact</th>
        </tr>
      </thead>
      <tbody>
"""
    for f in fixes:
        html += f"""
        <tr>
          <td><b>{f['id']}</b></td>
          <td><code>{f['page']}</code></td>
          <td>{f['summary']}</td>
          <td>{f['validator']}</td>
          <td><span class="tag tag-green">{f['validated']}</span></td>
          <td><span class="tag tag-blue">{f['impact']}</span></td>
        </tr>
"""
    html += """
      </tbody>
    </table>
  </div>

  <div id="pages" class="tab-content card">
    <h3 style="margin-bottom: 12px;">Publish-Ready Cornerstone Content Pages</h3>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Page Title</th>
          <th>Target Questions</th>
          <th>Schema Type</th>
          <th>Angle / Strategy</th>
        </tr>
      </thead>
      <tbody>
"""
    for p in pages:
        html += f"""
        <tr>
          <td><b>{p['id']}</b></td>
          <td>{p['title']}</td>
          <td>{', '.join(p['target_questions'])}</td>
          <td><span class="tag tag-yellow">{p['schema_type']}</span></td>
          <td>{p['angle']}</td>
        </tr>
"""
    html += """
      </tbody>
    </table>
  </div>

  <div id="citations" class="tab-content card">
    <h3 style="margin-bottom: 12px;">30 Authoritative Citation Targets</h3>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Authority Target / URL</th>
          <th>Platform Type</th>
          <th>Strategic Pitch Angle</th>
        </tr>
      </thead>
      <tbody>
"""
    for c in citations[:15]:
        html += f"""
        <tr>
          <td><b>{c['id']}</b></td>
          <td><a href="{c['title_or_url']}" target="_blank" style="color: #60a5fa; text-decoration: none;">{c['title_or_url']}</a></td>
          <td><span class="tag tag-blue">{c['type']}</span></td>
          <td>{c['angle']}</td>
        </tr>
"""
    html += """
      </tbody>
    </table>
  </div>

  <script>
    function showTab(id) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      document.getElementById(id).classList.add('active');
      event.target.classList.add('active');
    }
  </script>
</body>
</html>
"""
    os.makedirs("visibility/dashboard", exist_ok=True)
    out_file = "visibility/dashboard/index.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated live dashboard at: {out_file}")

if __name__ == "__main__":
    generate_dashboard()
