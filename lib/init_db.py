# lib/init_db.py
from lib.models import Base
from lib.database import engine

# Create all tables in the existing habits.db
Base.metadata.create_all(bind=engine)

print("✅ Database tables created successfully!")

