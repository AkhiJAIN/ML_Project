import logging
import os
from datetime import datetime

# Creating file name → example: 03_04_2026_14_32_10.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs folder inside your project
logs_path = os.path.join(os.getcwd(), "logs")

# Create folder if not exists
os.makedirs(logs_path, exist_ok=True)

# Full path of log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
