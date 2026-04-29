import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carga archivo .env
load_dotenv()

# Rescatamos las variables que definimos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = "5432"
DB_NAME = "login_db"


DB_HOST = "127.0.0.1"

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
