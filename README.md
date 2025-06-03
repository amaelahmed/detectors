🎯 Pose + YOLO Video Analyzer

A Python tool that uses YOLOv8 and MediaPipe Pose to detect objects and human pose landmarks in a video.

🧠 What It Does

Accepts a video file as input.

Detects people and objects using YOLOv8.

Draws full body pose landmarks using MediaPipe.

Saves a new video with detections.

Shows a live preview while processing.

📦 Requirements

Python 3.10+

Virtual environment (recommended)

OpenCV

MediaPipe

Ultralytics (YOLOv8)

🛠️ Setup Instructions

1. Clone the repo

git clone https://github.com/amaelahmed/detectors.git
cd detectors

2. Set up a virtual environment

apt update
apt install python3.10 python3.10-venv -y
python3.10 -m venv ~/venv310
source ~/venv310/bin/activate


3. Install the dependencies

pip install --upgrade pip
pip install opencv-python mediapipe torch torchvision torchaudio ultralytics

1. Create a folder to store the video:
mkdir -p /root/Videos
Make sure the path is correct by checking with:
ls "/media/sf_Desktop/"


🎞️ Usage

1. Move your video into the project folder

For example, move a file from Desktop to this project:

cp "/media/sf_Desktop/your-video.mp4" ./input.mp4

📌 Rename it to input.mp4 or modify the filename in the script.

✅ STEP 5: Run the script
Make sure you're in the virtual environment:


source ~/venv310/bin/activate
Then run the script:

python ~/pose_yolo.py
The video will play live and create an output.mp4 with detected poses and objects.

📁 File Structure

.
├── pose_yolo_video.py     # Main script
├── yolov8n.pt             # YOLOv8 model file
├── input.mp4              # Input video (add manually)
├── output.mp4             # Processed output
├── requirements.txt       # Dependencies
└── README.md              # Instructions

💡 Notes

Press ESC to stop the video preview early.

If you want to use a different model (like yolov8s.pt), just replace the file name in the code.

🙌 Credits

Ultralytics YOLO

MediaPipe

OpenCV

👤 Built by

Amal Ahammed

