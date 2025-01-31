from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/myapi"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()