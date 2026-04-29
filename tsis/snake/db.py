# db.py — PostgreSQL integration via psycopg2

import psycopg2
import psycopg2.extras
from config import DB_CONFIG

# Connection 

def get_connection():
    """Return a new psycopg2 connection, or None on failure."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        print(f"[DB] Connection failed: {e}")
        return None


# Schema initialisation 

def init_db():
    """Create tables if they do not exist yet."""
    conn = get_connection()
    if conn is None:
        return False
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS players (
                        id       SERIAL PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL
                    );
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS game_sessions (
                        id            SERIAL PRIMARY KEY,
                        player_id     INTEGER REFERENCES players(id),
                        score         INTEGER   NOT NULL,
                        level_reached INTEGER   NOT NULL,
                        played_at     TIMESTAMP DEFAULT NOW()
                    );
                """)
        return True
    except Exception as e:
        print(f"[DB] init_db error: {e}")
        return False
    finally:
        conn.close()


# ─── Player helpers ───────

def get_or_create_player(username: str) -> int | None:
    """Return player id, creating the row if necessary."""
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO players (username) VALUES (%s) "
                    "ON CONFLICT (username) DO NOTHING;",
                    (username,)
                )
                cur.execute(
                    "SELECT id FROM players WHERE username = %s;",
                    (username,)
                )
                row = cur.fetchone()
                return row[0] if row else None
    except Exception as e:
        print(f"[DB] get_or_create_player error: {e}")
        return None
    finally:
        conn.close()


# Session helpers

def save_game_session(username: str, score: int, level_reached: int) -> bool:
    """Persist a finished game session."""
    player_id = get_or_create_player(username)
    if player_id is None:
        return False
    conn = get_connection()
    if conn is None:
        return False
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO game_sessions (player_id, score, level_reached) "
                    "VALUES (%s, %s, %s);",
                    (player_id, score, level_reached)
                )
        return True
    except Exception as e:
        print(f"[DB] save_game_session error: {e}")
        return False
    finally:
        conn.close()


def get_personal_best(username: str) -> int:
    """Return the player's all-time best score, or 0 if none."""
    conn = get_connection()
    if conn is None:
        return 0
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COALESCE(MAX(gs.score), 0)
                FROM game_sessions gs
                JOIN players p ON p.id = gs.player_id
                WHERE p.username = %s;
            """, (username,))
            row = cur.fetchone()
            return row[0] if row else 0
    except Exception as e:
        print(f"[DB] get_personal_best error: {e}")
        return 0
    finally:
        conn.close()


def get_leaderboard(limit: int = 10) -> list[dict]:
    """Return the top `limit` all-time scores."""
    conn = get_connection()
    if conn is None:
        return []
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                SELECT
                    p.username,
                    gs.score,
                    gs.level_reached,
                    gs.played_at
                FROM game_sessions gs
                JOIN players p ON p.id = gs.player_id
                ORDER BY gs.score DESC, gs.played_at ASC
                LIMIT %s;
            """, (limit,))
            return [dict(row) for row in cur.fetchall()]
    except Exception as e:
        print(f"[DB] get_leaderboard error: {e}")
        return []
    finally:
        conn.close()