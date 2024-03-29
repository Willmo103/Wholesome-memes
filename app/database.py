# database ORM setup instructions at https://fastapi.tiangolo.com/tutorial/sql-databases/
# used the sample code here to set up my database connection.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ as env


# import for pydantic settings model for .env file
from app.config import settings


# using an f-string to call all of my env variables from settings instance
SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{env.get("DATABASE_USERNAME")}:{env.get("DATABASE_PASSWORD")}@'
    f'{env.get("DATABASE_HOSTNAME")}:{env.get("DATABASE_PORT")}/{env.get("DATABASE_NAME")}'
)

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# call this function as a dependency when preforming database operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
