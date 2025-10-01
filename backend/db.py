import sqlite3
from datetime import date

DB_NAME = "activity.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            platform TEXT,
            metric TEXT,
            value INTEGER,
            snapshot_date DATE
        )
    ''')
    conn.commit()
    conn.close()

def insert_stat(username, platform, metric, value):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    today = date.today().isoformat()
    c.execute('''
        INSERT INTO user_activity (username, platform, metric, value, snapshot_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, platform, metric, value, today))
    conn.commit()
    conn.close()

def get_stats(username, platform):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT metric, value, snapshot_date 
        FROM user_activity
        WHERE username = ? AND platform = ?
        ORDER BY snapshot_date
    ''', (username, platform))
    rows = c.fetchall()
    conn.close()
    return rows
