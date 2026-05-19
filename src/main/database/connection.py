from pathlib import Path
import sqlite3

DB_FILENAME = "wattio.db"


def get_db_path() -> Path:
    return Path(__file__).resolve().parents[3] / DB_FILENAME


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                director TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                genre TEXT NOT NULL
            )
            """
        )
        conn.commit()
