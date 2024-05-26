from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    pgadmin_default_email: str
    pgadmin_default_password: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"

settings = Settings()