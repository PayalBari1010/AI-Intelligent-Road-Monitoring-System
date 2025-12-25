import sqlite3
import csv
import os

DB_PATH = "detections.db"
CSV_PATH = "detections.csv"

# Check DB exists
if not os.path.exists(DB_PATH):
    print("ERROR: detections.db not found")
    exit()

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT object_type, latitude, longitude FROM detections")
rows = cursor.fetchall()

print(f"Total rows fetched from DB: {len(rows)}")

if len(rows) == 0:
    print("No data found in database. CSV not created.")
else:
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["object_type", "latitude", "longitude"])
        writer.writerows(rows)

    print(f"CSV file created successfully: {CSV_PATH}")

conn.close()
