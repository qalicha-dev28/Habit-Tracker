# lib/crud.py
# Simple CRUD helpers — accept a session to keep them testable

from datetime import date
from .models import Category, Habit, Completion

def create_category(session, name):
    existing = session.query(Category).filter_by(name=name).first()
    if existing:
        return existing
    cat = Category(name=name)
    session.add(cat)
    session.flush()
    return cat

def list_categories(session):
    return session.query(Category).order_by(Category.name).all()

def create_habit(session, name, description=None, category_id=None):
    habit = Habit(name=name, description=description, category_id=category_id)
    session.add(habit)
    session.flush()
    return habit

def list_habits(session):
    return session.query(Habit).order_by(Habit.name).all()

def add_completion(session, habit_id, completion_date: date):
    existing = session.query(Completion).filter_by(habit_id=habit_id, date=completion_date).first()
    if existing:
        return existing
    comp = Completion(habit_id=habit_id, date=completion_date)
    session.add(comp)
    # update simple streak logic
    last = session.query(Completion).filter(Completion.habit_id==habit_id).order_by(Completion.date.desc()).first()
    habit = session.get(Habit, habit_id)
    if not habit:
        raise ValueError("Habit not found")
    if last:
        if (completion_date - last.date).days == 1:
            habit.streak = (habit.streak or 0) + 1
        else:
            habit.streak = 1
    else:
        habit.streak = 1
    return comp

def list_completions(session, habit_id=None):
    q = session.query(Completion).order_by(Completion.date.desc())
    if habit_id:
        q = q.filter_by(habit_id=habit_id)
    return q.all()

def delete_habit(session, habit_id):
    h = session.get(Habit, habit_id)
    if not h:
        return False
    session.delete(h)
    return True
