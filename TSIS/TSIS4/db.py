import psycopg2
from config import DB_CONFIG


def connect():
    return psycopg2.connect(
        host=DB_CONFIG[0],
        port=DB_CONFIG[1],
        user=DB_CONFIG[3],
        dbname=DB_CONFIG[2],
        password=DB_CONFIG[4]
    )


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions(
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER,
        level_reached INTEGER,
        played_at TIMESTAMP DEFAULT NOW()
    )
    """)

    conn.commit()
    conn.close()


def get_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    row = cur.fetchone()

    if row:
        pid = row[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    conn.close()
    return pid


def save_result(username, score, level):
    pid = get_player(username)

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES(%s,%s,%s)
    """, (pid, score, level))

    conn.commit()
    conn.close()


def get_best(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT MAX(score)
        FROM game_sessions gs
        JOIN players p ON p.id = gs.player_id
        WHERE p.username=%s
    """, (username,))

    res = cur.fetchone()[0]
    conn.close()

    return res if res else 0


def get_top():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, gs.score
        FROM game_sessions gs
        JOIN players p ON p.id = gs.player_id
        ORDER BY gs.score DESC
        LIMIT 10
    """)

    rows = cur.fetchall()
    conn.close()

    return rows