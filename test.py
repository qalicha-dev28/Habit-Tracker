# test.py
from lib.database import SessionLocal
from lib.models import Category, Habit, Completion

# Create a database session
session = SessionLocal()

print("\n--- Categories ---")
for c in session.query(Category).all():
    print(c)

print("\n--- Habits ---")
for h in session.query(Habit).all():
    print(h)

print("\n--- Completions ---")
for comp in session.query(Completion).all():
    print(comp)

session.close()
