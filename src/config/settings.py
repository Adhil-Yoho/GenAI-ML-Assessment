import os
from pathlib import Path
from dotenv import load_dotenv

# project_root points at the top folder of the project
project_root = Path(__file__).resolve().parents[2]
load_dotenv(project_root / ".env")

API_URL = os.getenv("API_URL", "https://api.exchangerate-api.com/v4/latest")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))

data_raw = project_root / "data" / "raw"
PROCESSED_DATA_DIR = project_root / "data" / "processed"
CHARTS_DIR = project_root / "outputs" / "charts"
REPORTS_DIR = project_root / "outputs" / "reports"