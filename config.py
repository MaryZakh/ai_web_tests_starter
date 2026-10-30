import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("SAUCE_USER", "standard_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))
