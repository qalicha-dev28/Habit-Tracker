from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Get database URL from environment variable or fallback to SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///habits.db")

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal is what we'll use in CRUD functions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that our models will inherit from
Base = declarative_base()
