import sqlite3

def init_db():
    conn = sqlite3.connect("detections.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections (
        object_id INTEGER PRIMARY KEY AUTOINCREMENT,
        object_type TEXT,
        confidence REAL,
        timestamp TEXT,
        latitude REAL,
        longitude REAL
    )
    """)

    conn.commit()
    conn.close()
