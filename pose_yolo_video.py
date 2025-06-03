import cv2
import mediapipe as mp
from ultralytics import YOLO
import os
from tkinter import Tk, filedialog

# Attribution
print("🔧 Built by Amal Ahammed\n")

# File picker dialog
Tk().withdraw()
input_video = filedialog.askopenfilename(title="Select Input Video")
if not input_video:
    print("❌ No video selected. Exiting.")
    exit()

output_video = "output.mp4"
USE_MEDIAPIPE = True
USE_YOLO = True

# MediaPipe setup
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) if USE_MEDIAPIPE else None

# YOLO model
yolo_model = YOLO("yolov8n.pt") if USE_YOLO else None

# Open video
cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    print(f"❌ Failed to open video file: {input_video}")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"📹 Loaded video: {input_video} ({frame_width}x{frame_height} @ {fps} FPS, {total_frames} frames)")

out = cv2.VideoWriter(output_video,
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      fps,
                      (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if yolo_model:
        yolo_results = yolo_model(frame, verbose=False)
        frame = yolo_results[0].plot()

    if pose:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb)
        if result.pose_landmarks:
            mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Pose + YOLO", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
if pose:
    pose.close()

print(f"✅ Saved output to: {output_video}")

