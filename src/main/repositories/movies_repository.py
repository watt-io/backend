from typing import Any, Dict, List, Optional

from src.main.database import get_connection


def create_movie_repo(data: Dict[str, Any]) -> Dict[str, Any]:
    query = (
        "INSERT INTO movies (title, director, release_year, genre) "
        "VALUES (?, ?, ?, ?)"
    )
    with get_connection() as conn:
        cursor = conn.execute(
            query,
            (
                data["title"],
                data["director"],
                data["release_year"],
                data["genre"],
            ),
        )
        conn.commit()
        movie_id = cursor.lastrowid
        row = conn.execute(
            "SELECT id, title, director, release_year, genre FROM movies WHERE id = ?",
            (movie_id,),
        ).fetchone()

    return dict(row) if row else {}


def list_movies_repo() -> List[Dict[str, Any]]:
    query = "SELECT id, title, director, release_year, genre FROM movies ORDER BY id"
    with get_connection() as conn:
        rows = conn.execute(query).fetchall()

    return [dict(row) for row in rows]


def get_movie_by_id_repo(movie_id: int) -> Optional[Dict[str, Any]]:
    query = "SELECT id, title, director, release_year, genre FROM movies WHERE id = ?"
    with get_connection() as conn:
        row = conn.execute(query, (movie_id,)).fetchone()

    return dict(row) if row else None
