# AI-Based Intelligent Road Monitoring System

##  Project Overview
This project is an AI-based road monitoring system that detects objects on roads such as vehicles, pedestrians, animals, and obstacles using a deep learning object detection model.  
The system logs GPS coordinates **only when an object is detected**, ensuring optimized and meaningful data storage.

---

##  Objectives
- Detect road objects using AI (YOLO-based detection)
- Log latitude & longitude conditionally
- Avoid duplicate and unnecessary database entries
- Visualize detected locations on Google Maps

---

## Technologies Used
- Python
- YOLOv8 (Object Detection)
- OpenCV
- SQLite Database
- Geocoder (GPS)
- Google My Maps (Visualization)

---

##  System Architecture
1. Video Input
2. Object Detection Model
3. Conditional GPS Fetching
4. Database Logging
5. CSV Export
6. Google Maps Visualization

---

##  Database Schema
| Field Name | Description |
|----------|-------------|
| id | Auto-increment ID |
| object_type | Detected object category |
| confidence | Detection confidence |
| timestamp | Detection time |
| latitude | GPS latitude |
| longitude | GPS longitude |

## Demo video Link
https://youtube.com/shorts/VXbhGZKUESQ?si=QYrP_HOtpZR1LlFB
