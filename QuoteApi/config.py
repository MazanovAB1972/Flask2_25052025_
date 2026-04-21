from pathlib import Path
BASE_DIR = Path(__file__).parent

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
        path_to_db = BASE_DIR / "quotes.db"  # <- тут путь к БД
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{path_to_db}"
        SQLALCHEMY_ECHO = False
