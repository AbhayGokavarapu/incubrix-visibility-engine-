"""
IncuBrix Environment Loader
===========================
Safely reads .env without printing secrets or requiring external packages.
"""

import os

def load_dotenv(env_path: str = ".env") -> bool:
    if not os.path.exists(env_path):
        return False
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and not os.environ.get(key):
                        os.environ[key] = val
        return True
    except Exception:
        return False

# Automatically invoke when imported
load_dotenv()
