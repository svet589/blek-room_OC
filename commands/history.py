import sqlite3
from blek import HISTORY_DB

def show_history():
    conn = sqlite3.connect(HISTORY_DB)
    c = conn.cursor()
    c.execute("SELECT command, timestamp FROM history ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    for cmd, ts in rows:
        print(f"{ts} -> {cmd}")
    conn.close()
