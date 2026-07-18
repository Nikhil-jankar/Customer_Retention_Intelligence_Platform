from pathlib import Path

# Root directory of the project
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Artifact directory
ARTIFACT_DIR = ROOT_DIR / "artifacts"

# Log directory
LOG_DIR = ROOT_DIR / "logs"

# Create required directories automatically
for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    ARTIFACT_DIR,
    LOG_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)