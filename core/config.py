import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "Student Portal API"
    PROJECT_VERSION: str = "0.115.7"

    POSTGRES_USER = os.getenv("PGUSER")
    POSTGRES_PASSWORD = os.getenv("PGPASSWORD")
    POSTGRES_SERVER = os.getenv("PGHOST")
    POSTGRES_DB = os.getenv("PGDATABASE")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

settings = Settings()


