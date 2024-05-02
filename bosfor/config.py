from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

env_file_path = Path(__file__).resolve().parent.parent / '.env'

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASS: str
    SECRET_KEY: str
    DEBUG: bool

    model_config = SettingsConfigDict(env_file=env_file_path)

settings = Settings()
