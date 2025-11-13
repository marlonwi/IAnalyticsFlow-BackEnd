from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "" #Adicionar a key posteriormente
    db_host: str = "localhost"
    db_name: str = "challenge_db"
    db_user: str = "postgres"
    db_password: str = "123456" #Adicionar a senha posteriormente
    db_port: int = 5432

    class Config:
        env_file = ".env"

settings = Settings()
