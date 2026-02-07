from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    PROJECT_NAME: str = "Sustainable IT Asset Management Platform"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 8
    ALGORITHM: str = "HS256"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "itam"
    POSTGRES_SERVER: str = "db"
    POSTGRES_PORT: int = 5432

    FRONTEND_ORIGIN: str = "http://localhost:5173"
    MODEL_PATH: str = "models/waste_risk_rf.pkl"
    MODEL_VERSION: str = "rf-v1"
    AUTO_CREATE_TABLES: bool = True

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:  # type: ignore
    return Settings()
