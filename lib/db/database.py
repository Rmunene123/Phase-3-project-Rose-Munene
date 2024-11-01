# lib/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection string (update this with your actual database URL)
DATABASE_URL = "sqlite:///./test.db"  # Example using SQLite

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

def get_db():
    """Create a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
