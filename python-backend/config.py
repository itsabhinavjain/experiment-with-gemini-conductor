from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    """
    Application settings managed via environment variables.
    """
    # Anthropic API Key for Claude Agent SDK
    anthropic_api_key: Optional[str] = None
    
    # App General Settings
    app_name: str = "Claude Agent SDK Backend"
    debug: bool = True
    port: int = 8000
    host: str = "0.0.0.0"

    # Pydantic Settings Configuration
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache
def get_settings():
    """
    Returns a cached instance of the settings to avoid redundant file reads.
    """
    return Settings()
