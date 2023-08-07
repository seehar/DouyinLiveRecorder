from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).parent
    LOGGER_FILENAME: Path = PROJECT_DIR / "log" / "log.log"
    LOGGER_ERROR_FILENAME: Path = PROJECT_DIR / "log" / "error.log"


settings: Settings = Settings()
