import shutil
import os
import datetime

def make_backup():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = f"backup_{ts}"
    os.makedirs(dest, exist_ok=True)
    
    items = [
        "engine", "fixes", "pages", "visibility", "launch_kit",
        "README.md", "IncuBrix_2027_Growth_Engineer_Option_3_AEO_SEO_GEO_Submission_Workbook.xlsx",
        "generate_citations.py", "generate_fixes.py", "generate_pages.py",
        "generate_visibility.py", "populate_workbook.py"
    ]
    
    for item in items:
        if os.path.exists(item):
            target = os.path.join(dest, item)
            if os.path.isdir(item):
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)
    print(f"SUCCESS: Backup saved to {dest}")

if __name__ == "__main__":
    make_backup()
