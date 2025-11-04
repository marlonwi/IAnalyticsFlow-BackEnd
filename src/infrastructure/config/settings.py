from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "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" #Adicionar a key posteriormente
    db_host: str = "localhost"
    db_name: str = "challenge_db"
    db_user: str = "postgres"
    db_password: str = "123456" #Adicionar a senha posteriormente
    db_port: int = 5432

    class Config:
        env_file = ".env"

settings = Settings()
