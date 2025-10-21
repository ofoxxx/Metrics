import os
from dotenv import load_dotenv

load_dotenv()

OWNER = os.environ.get("OWNER", "")
REPO = os.environ.get("REPO", "")
REPO_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

# Log REPO_URL
print(f"Inspecting: {REPO_URL}")

TOKEN = os.environ.get("TOKEN", "")
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
