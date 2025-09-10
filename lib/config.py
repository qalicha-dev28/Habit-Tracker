# lib/config.py
# Loads environment variables from .env and provides DATABASE_URL

from dotenv import load_dotenv
import os

# load .env into environment variables
load_dotenv()

# default to sqlite file in project root
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///habit_tracker.db")
