# lib/seed.py
from lib.database import SessionLocal
from lib.models import Category, Habit, Completion
from datetime import date

def seed_data():
    session = SessionLocal()

    # Clear old data first (so running twice won’t duplicate)
    session.query(Completion).delete()
    session.query(Habit).delete()
    session.query(Category).delete()

    # Create a category
    health = Category(name="Health")

    # Create a habit under this category
    habit = Habit(
        name="Morning Run",
        description="Run 3km every morning",
        category=health
    )

    # Create a completion record for today
    completion = Completion(
        date=date.today(),
        notes="Felt good, sunny weather!",
        habit=habit
    )

    # Add everything and commit
    session.add_all([health, habit, completion])
    session.commit()
    session.close()

    print("✅ Seed data inserted successfully!")

if __name__ == "__main__":
    seed_data()
