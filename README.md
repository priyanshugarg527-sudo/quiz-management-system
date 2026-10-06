# Quiz Management System

A console-based quiz application in Python with an SQLite database. Admins manage questions and other admins, and players take a randomised quiz and appear on a leaderboard.

Built during the **Summer Training Program 2025 (Python for Data Science)** at IIT Kanpur, E&ICT Academy.

## Features
- **Play quiz:** choose how many questions to answer; questions are picked at random, with score and percentage tracking
- **Leaderboard:** shows correct answers, wrong answers and percentage for every player
- **Admin login** with these options:
  - Add, delete (one or all) and view questions
  - Load questions in bulk from a CSV file
  - Create a new admin, remove an admin, change password
  - Clear the leaderboard

## Tech stack
Python, SQLite (`sqlite3`)

## Project files
| File | Purpose |
|---|---|
| `setup_db.py` | One-time setup: creates the database, loads questions, creates the first admin |
| `main.py` | Main menu (Login, Play Quiz, Leaderboard, Exit) |
| `admin.py` | Admin authentication and admin management |
| `quizmgmt.py` | Question management (add, delete, view, load from CSV) |
| `quiz.py` | Quiz play and scoring |
| `leaderboard.py` | Leaderboard display |
| `quiz.csv` | 100 sample questions |

## How to run
```bash
python setup_db.py   # first time only: creates qm.db, loads 100 questions, asks for an admin username and password
python main.py
```

Run both commands from inside this folder. Python 3 is enough; no extra packages are needed.

## Possible improvements
- Store hashed passwords instead of plain text
- Use parameterized queries everywhere
- Add input validation for menu choices
- Build a GUI or web version
