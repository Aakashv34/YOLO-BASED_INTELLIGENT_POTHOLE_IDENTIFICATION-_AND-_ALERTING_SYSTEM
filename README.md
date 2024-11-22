Potholes pose a significant threat to road safety, contributing to vehicle damage and accidents. Timely detection and repair are crucial for maintaining road quality and
ensuring driver safety. This project presents a real-time pothole detection system utilizing the YOLO (You Only Look Once) object detection model. The system
processes road images uploaded by users to accurately identify and locate potholes, leveraging computer vision techniques for efficient detection. By using YOLO's fast
and accurate object recognition capabilities, this system offers a low-cost, scalable
solution for monitoring road conditions. The proposed solution detects single or
multiple potholes in an image and provides critical feedback, such as warnings for
drivers to take caution, based on the extent of the road damage. Additionally, the
detected images are saved for future reference and analysis, enabling authorities to
plan maintenance activities efficiently. Experimental results demonstrate the
effectiveness of the YOLO-based detection system in various road conditions, achieving high accuracy and real-time performance. This project contributes to
Intelligent Transportation Systems (ITS) by providing a tool that enhances road safety
and facilitates proactive road maintenance.

The Files must arrange like this:
Pothole_Detection_Web/
│
├── app.py                  # Flask backend file (main Python app)
├── uploads/                # Folder where uploaded images are stored
├── static/                 # Folder for static files (results, images, CSS, JS)
│   ├── results/            # Folder where processed (detection) images are saved
│   └── styles/             # Optional folder for custom stylesheets (if needed)
├── templates/              # Folder for HTML files
│   ├── index.html          # HTML file for the home page (upload form)
│   └── result.html         # HTML file for the result page (show detected image)
└── runs/                   # YOLO will save the inference result in this folder (created by YOLO automatically)
    └── detect/             # YOLO’s subdirectory for saving detections
