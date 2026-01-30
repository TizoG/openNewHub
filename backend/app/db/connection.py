from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
url_base = os.getenv("DATABASE_URL")
print(f"La URL detectada es: {url_base}")

engine = create_engine(url_base)
sesion = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def db_get():
    db = sesion()
    try:
        yield db
    finally:
        db.close()
