#config/config_page.py
import os
from dotenv import load_dotenv


env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")