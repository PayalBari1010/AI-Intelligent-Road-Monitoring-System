from ultralytics import YOLO
import cv2

from gps import get_gps_location
from insert import insert_detection
from db import init_db

import time

LOG_COOLDOWN_SECONDS = 5  # log same object type once every 5 seconds
last_logged_time = {}    # dictionary to track last log time

init_db()

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("road_video.mp4")

ROAD_OBJECT_MAP = {
    "car": "vehicle",
    "bus": "vehicle",
    "truck": "vehicle",
    "motorcycle": "vehicle",
    "bicycle": "vehicle",
    "person": "pedestrian",
    "dog": "animal",
    "cow": "animal"
}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.4)

    detections_in_frame = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            confidence = float(box.conf[0])

            if label in ROAD_OBJECT_MAP:
                detections_in_frame.append((label, confidence, box))

            if detections_in_frame:
                current_time = time.time()
                lat, lon = get_gps_location()

                if lat is None or lon is None:
                    print("GPS not available, skipping DB insert")
                continue


    for label, confidence, box in detections_in_frame:
        object_type = ROAD_OBJECT_MAP[label]

        last_time = last_logged_time.get(object_type, 0)

        if current_time - last_time >= LOG_COOLDOWN_SECONDS:
            insert_detection(object_type, confidence, lat, lon)
            last_logged_time[object_type] = current_time

            print(f"Logged {object_type} at {lat}, {lon}")
        else:
            print(f"Skipped duplicate {object_type}")

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{object_type} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            print(f"Detected {object_type} | Conf: {confidence:.2f} | Lat: {lat}, Lon: {lon}")

    cv2.imshow("Intelligent Road Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
