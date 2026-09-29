from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: SecretStr
    postgres_host: str = "127.0.0.1"
    postgres_port: int = 5432

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def database_url(self) -> str:
        password = self.postgres_password.get_secret_value()

        return (
            f"postgresql+psycopg://"
            f"{self.postgres_user}:{password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )


settings = Settings()
