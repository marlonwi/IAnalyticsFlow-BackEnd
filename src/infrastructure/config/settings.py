from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "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"
    db_host: str = "localhost"
    db_name: str = "challenge_db"
    db_user: str = "postgres"
    db_password: str = "bnte141769"
    db_port: int = 5432

    class Config:
        env_file = ".env"

settings = Settings()
