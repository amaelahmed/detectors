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

# Update package list
sudo apt update

# Install prerequisite package for adding PPAs
sudo apt install software-properties-common -y

# Add the deadsnakes PPA repository for newer Python versions
sudo add-apt-repository ppa:deadsnakes/ppa

# Update package list again after adding the new repository
sudo apt update

# Install Python 3.10 and related packages
sudo apt install python3.10 python3.10-venv python3.10-dev -y

# (Optional) Add the deadsnakes PPA manually if needed
sudo sh -c 'echo "deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu focal main" > /etc/apt/sources.list.d/deadsnakes-ppa.list'

# Add the PPA signing key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A755776

# Update package list after adding manual repository and key
sudo apt update

# Create a Python 3.10 virtual environment
python3.10 -m venv ~/venv310

# Activate the virtual environment
source ~/venv310/bin/activate

# Upgrade pip inside the virtual environment
pip install --upgrade pip

# Install required Python packages inside the virtual environment
pip install opencv-python mediapipe ultralytics

# Make sure the virtual environment is activated before running your script
source ~/venv310/bin/activate

# Run your Python script
python pose_yolo_video.py


💡 Notes

Press ESC to stop the video preview early.

If you want to use a different model (like yolov8s.pt), just replace the file name in the code.

🙌 Credits

Ultralytics YOLO

MediaPipe

OpenCV

👤 Built by

Amal Ahammed

