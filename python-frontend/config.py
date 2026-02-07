from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings for the Python CLI frontend.
    """
    backend_api_url: str = "http://0.0.0.0:8000"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache
def get_settings():
    """
    Returns a cached instance of the settings.
    """
    return Settings()
