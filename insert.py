import sqlite3
from datetime import datetime

def insert_detection(obj_type, confidence, lat, lon):
    conn = sqlite3.connect("detections.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO detections (object_type, confidence, timestamp, latitude, longitude)
    VALUES (?, ?, ?, ?, ?)
    """, (obj_type, confidence, datetime.now(), lat, lon))

    conn.commit()
    conn.close()
