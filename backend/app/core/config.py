import os
from dotenv import load_dotenv
from pydantic import BaseSettings, AnyUrl

load_dotenv()

class Settings(BaseSettings):
    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
    DATABASE_URL: AnyUrl = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost:5432/afiyor")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_this_before_prod")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
