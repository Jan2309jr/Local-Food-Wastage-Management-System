import os
import sqlite3
from contextlib import contextmanager

# Always resolve path relative to repo root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
DB_PATH = os.path.join(BASE_DIR, "data", "database", "food.db")

def get_connection():
    """Return a SQLite connection to food.db"""
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    return con

@contextmanager
def db_cursor():
    """Context manager for a DB cursor with auto commit/close."""
    con = get_connection()
    cur = con.cursor()
    try:
        yield cur
        con.commit()
    finally:
        cur.close()
        con.close()
