import secrets
from typing import Any, Dict, List, Optional, Union
import os 
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_HOST: AnyHttpUrl
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:8050/docs"]
    SERVER_NAME: str = 'proj serv name'
    SERVER_HOST: AnyHttpUrl = None
    PROJECT_NAME: str = 'Conference service API'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_USER: str = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB: str = 'postgres'
    SQLALCHEMY_DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:5432/{POSTGRES_DB}"
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    FIRST_SUPERUSER: str = 'admin'
    FIRST_SUPERUSER_PASSWORD: str = 'super_pass'

    class Config:
        case_sensitive = True


settings = Settings()
