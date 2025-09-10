# lib/models.py
# SQLAlchemy ORM models: Category, Habit, Completion

from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.database import Base  # <-- import Base instead of creating new one


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Category(TimestampMixin, Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    habits = relationship("Habit", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Category id={self.id} name={self.name!r}>"


class Habit(TimestampMixin, Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(500))
    streak = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="habits")
    completions = relationship("Completion", back_populates="habit", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Habit id={self.id} name={self.name!r}>"


class Completion(TimestampMixin, Base):
    __tablename__ = "completions"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    notes = Column(String(500))
    habit_id = Column(Integer, ForeignKey("habits.id"))
    habit = relationship("Habit", back_populates="completions")

    def __repr__(self):
        return f"<Completion id={self.id} date={self.date}>"
