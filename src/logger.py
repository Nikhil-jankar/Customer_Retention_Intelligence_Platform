import logging
from pathlib import Path

from src.config import LOG_DIR

# Log file path
LOG_FILE = LOG_DIR / "project.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Logger object
logger = logging.getLogger("CustomerRetention")