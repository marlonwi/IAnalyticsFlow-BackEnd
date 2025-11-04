from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "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"
    db_host: str = "localhost"
    db_name: str = "challenge_db"
    db_user: str = "postgres"
    db_password: str = "123456"
    db_port: int = 5432

    class Config:
        env_file = ".env"

settings = Settings()
