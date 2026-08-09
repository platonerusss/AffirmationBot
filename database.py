import sqlite3

from config import DATABASE_FILE


def get_connection():
    return sqlite3.connect(DATABASE_FILE)


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            enabled INTEGER NOT NULL DEFAULT 0,
            time TEXT NOT NULL DEFAULT '09:00',
            last_sent_date TEXT
        )
    """)

    try:
        cursor.execute("""
            ALTER TABLE users
            ADD COLUMN mode TEXT NOT NULL DEFAULT 'female'
        """)
    except sqlite3.OperationalError:
        pass

    connection.commit()
    connection.close()


def ensure_user_exists(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id)
        VALUES (?)
    """, (user_id,))

    connection.commit()
    connection.close()


def get_user_settings(user_id):
    ensure_user_exists(user_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT enabled, time, mode
        FROM users
        WHERE user_id = ?
    """, (user_id,))

    row = cursor.fetchone()
    connection.close()

    return {
        "enabled": bool(row[0]),
        "time": row[1],
        "mode": row[2]
    }


def set_user_enabled(user_id, enabled):
    ensure_user_exists(user_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET enabled = ?
        WHERE user_id = ?
    """, (int(enabled), user_id))

    connection.commit()
    connection.close()


def set_user_time(user_id, new_time):
    ensure_user_exists(user_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET time = ?
        WHERE user_id = ?
    """, (new_time, user_id))

    connection.commit()
    connection.close()


def set_user_mode(user_id, mode):
    ensure_user_exists(user_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET mode = ?
        WHERE user_id = ?
    """, (mode, user_id))

    connection.commit()
    connection.close()


def set_user_last_sent_date(user_id, date):
    ensure_user_exists(user_id)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET last_sent_date = ?
        WHERE user_id = ?
    """, (date, user_id))

    connection.commit()
    connection.close()


def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, enabled, time, last_sent_date, mode
        FROM users
    """)

    rows = cursor.fetchall()
    connection.close()
    return rows