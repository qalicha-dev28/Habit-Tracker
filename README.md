# Habit Tracker (CLI with SQLAlchemy)

This project is a command-line application for tracking habits. It uses **Python 3**, **SQLAlchemy ORM**, and **Alembic** for database migrations.

The application allows you to:

- Create and manage categories for habits  
- Add, view, update, and delete habits  
- Record daily completions with optional notes  
- Track streaks and progress  

---

## Project Structure

Habit-Tracker/
│
├── alembic/ # Alembic migration files
│ ├── versions/ # Migration scripts
│ └── env.py # Alembic environment setup
│
├── lib/
│ ├── init.py # Marks lib as a Python package
│ ├── database.py # Database configuration
│ ├── init_db.py # Initializes database and runs migrations
│ ├── models.py # SQLAlchemy models
│ ├── crud.py # CRUD operations
│ ├── seed.py # Seed script for inserting sample data
│ └── cli.py # CLI entry point
│
├── test.py # Basic script to test models and database
├── .gitignore # Git ignore file
└── README.md # Project documentation


---

## Requirements

- Python 3.8 or later  
- SQLAlchemy  
- Alembic  

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/qalicha-dev28/Habit-Tracker.git
   cd Habit-Tracker

    Create and activate a virtual environment

    Linux / Mac:

python -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

Install dependencies

    pip install sqlalchemy alembic

Database Setup and Migrations

    Initialize the database

python -m lib.init_db

This will create the database tables according to your models.

Apply migrations

If you make changes to your models, generate a migration with:

alembic revision --autogenerate -m "describe changes"

Then apply the migration:

    alembic upgrade head

Seeding the Database

To insert initial sample data:

python -m lib.seed

Expected output:

Seed data inserted successfully!

This will create one category (Health), one habit (Morning Run), and one completion record.
Testing the Application

Run the included test script to verify database functionality:

python test.py

It will display the current categories, habits, and completions in the database.
Running the CLI

To start the Habit Tracker CLI:

python -m lib.cli

From here, you can add habits, mark completions, and view progress.
(The available commands depend on your implementation in cli.py.)
Author

Name: Najma Boru
GitHub: qalicha-dev28
License

This project is licensed under the MIT License.
