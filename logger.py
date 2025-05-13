import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate a log file with timestamp
log_file = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Custom Logger Function
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
