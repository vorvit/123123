from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

HOST = os.environ.get('DB_HOST', 'postgres')
USER = os.environ.get('POSTGRES_USER', 'postgres')
PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
DB = os.environ.get('POSTGRES_DB', 'postgres')

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
