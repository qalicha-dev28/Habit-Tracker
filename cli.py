#!/usr/bin/env python3
# cli.py - Habit Tracker CLI with input validation

from lib.database import SessionLocal
from lib.models import Category, Habit, Completion
from datetime import date

db = SessionLocal()

def safe_int_input(prompt):
    """Prompt the user for an integer until they enter a valid one."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    while True:
        print("\n--- Habit Tracker CLI ---")
        print("1. Add Category")
        print("2. Add Habit")
        print("3. Add Completion")
        print("4. List Categories")
        print("5. List Habits")
        print("6. List Completions")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Category name: ").strip()
            if name:
                cat = Category(name=name)
                db.add(cat)
                db.commit()
                print(f"✅ Category '{name}' added.")
            else:
                print("❌ Category name cannot be empty.")

        elif choice == "2":
            categories = db.query(Category).all()
            if not categories:
                print("❌ No categories found. Add a category first.")
                continue
            print("\nCategories:")
            for c in categories:
                print(f"{c.id}: {c.name}")
            cat_id = safe_int_input("Category ID for this habit: ")
            if not db.query(Category).filter_by(id=cat_id).first():
                print("❌ Invalid Category ID.")
                continue
            habit_name = input("Habit name: ").strip()
            if habit_name:
                habit = Habit(name=habit_name, category_id=cat_id)
                db.add(habit)
                db.commit()
                print(f"✅ Habit '{habit_name}' added.")
            else:
                print("❌ Habit name cannot be empty.")

        elif choice == "3":
            habits = db.query(Habit).all()
            if not habits:
                print("❌ No habits found. Add a habit first.")
                continue
            print("\nHabits:")
            for h in habits:
                print(f"{h.id}: {h.name}")
            habit_id = safe_int_input("Habit ID to complete: ")
            if not db.query(Habit).filter_by(id=habit_id).first():
                print("❌ Invalid Habit ID.")
                continue
            comp = Completion(habit_id=habit_id, date=date.today())
            db.add(comp)
            db.commit()
            print("✅ Completion added!")

        elif choice == "4":
            print("\n--- Categories ---")
            for c in db.query(Category).all():
                print(f"{c.id}: {c.name}")

        elif choice == "5":
            print("\n--- Habits ---")
            for h in db.query(Habit).all():
                print(f"{h.id}: {h.name} (Category ID: {h.category_id})")

        elif choice == "6":
            print("\n--- Completions ---")
            for comp in db.query(Completion).all():
                print(f"{comp.id}: Habit ID {comp.habit_id} on {comp.date}")

        elif choice == "0":
            print("Exiting CLI. Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
