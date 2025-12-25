import sqlite3

conn = sqlite3.connect("detections.db")
cursor = conn.cursor()

print("\nLast 10 detections:\n")

for row in cursor.execute(
    "SELECT * FROM detections ORDER BY object_id DESC LIMIT 100"
):
    print(row)

conn.close()
