from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App configuration
    root_path: str = Field(default="../", alias="ROOT_PATH")
    data_path: str = Field(default="../data", alias="DATA_PATH")


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Create a default settings instance
settings = get_settings()
