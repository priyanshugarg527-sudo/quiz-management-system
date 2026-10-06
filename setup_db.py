"""
One-time setup for the Quiz Management System.

Creates qm.db with the required tables, loads the questions from quiz.csv
and creates the first admin account.

Run this once before main.py:
    python setup_db.py
"""
import csv
import getpass
import os
import sqlite3

DB_NAME = "qm.db"
CSV_NAME = "quiz.csv"


def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS login (
        username TEXT,
        password TEXT,
        status   TEXT,
        role     TEXT,
        PRIMARY KEY (password)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS questions (
        qno         INTEGER,
        question    TEXT,
        a           TEXT,
        b           TEXT,
        c           TEXT,
        d           TEXT,
        correct     TEXT,
        hint        TEXT,
        explanation TEXT,
        PRIMARY KEY (qno AUTOINCREMENT)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
        name       TEXT,
        score      INTEGER,
        question   INTEGER,
        percentage REAL,
        PRIMARY KEY (name)
    )""")
    conn.commit()


def load_questions(conn, csv_name=CSV_NAME):
    cur = conn.cursor()
    with open(csv_name, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = [
            (r["Question"], r["Option1"], r["Option2"], r["Option3"],
             r["Option4"], r["CorrectAnswer"], r["hint"], r["explanation"])
            for r in reader
        ]
    cur.executemany(
        "INSERT INTO questions (question, a, b, c, d, correct, hint, explanation) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        rows,
    )
    conn.commit()
    return len(rows)


def create_admin(conn, username, password):
    conn.execute(
        "INSERT INTO login (username, password, status, role) VALUES (?, ?, 'active', 'admin')",
        (username, password),
    )
    conn.commit()


def main():
    if os.path.exists(DB_NAME):
        print(f"{DB_NAME} already exists. Delete it first if you want a fresh setup.")
        return

    conn = sqlite3.connect(DB_NAME)
    create_tables(conn)
    count = load_questions(conn)
    print(f"Loaded {count} questions from {CSV_NAME}")

    print("\nCreate the first admin account")
    username = input("Admin username: ").strip()
    password = getpass.getpass("Admin password: ")
    confirm = getpass.getpass("Re-enter password: ")
    if not username or not password or password != confirm:
        conn.close()
        os.remove(DB_NAME)
        print("Username was empty or passwords did not match. Setup cancelled, run it again.")
        return

    create_admin(conn, username, password)
    conn.close()
    print("\nSetup complete. Now run: python main.py")


if __name__ == "__main__":
    main()
