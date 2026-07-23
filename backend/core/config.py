from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Read the database URL and secret key from the .env file
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

# Create an instance of the settings we can use elsewhere
settings = Settings()