from flask import Flask, request, render_template, jsonify, redirect, url_for, flash
from ultralytics import YOLO
import os
import glob
import shutil

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key_here'  # Set a strong secret key

# Load the trained YOLO model
model = YOLO('runs/detect/train3/weights/last.pt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        flash("No file uploaded.")
        return redirect(url_for('home'))

    file = request.files['image']
    if file.filename == '':
        flash("No file selected.")
        return redirect(url_for('home'))

    # Save the uploaded image temporarily
    image_path = os.path.join('uploads', file.filename)
    file.save(image_path)

    # Perform detection and save the annotated image in the 'runs' folder
    results = model.predict(source=image_path, save=True)

    # Get the latest YOLO output directory
    latest_folder = max(glob.glob('runs/detect/predict*'), key=os.path.getctime)
    detected_image_path = os.path.join(latest_folder, file.filename)

    # Define the path where the image will be stored in the static folder
    result_image_path = os.path.join('static/results', file.filename)

    # Move the detected image with annotations to the static results folder
    shutil.copy(detected_image_path, result_image_path)

    # Count the number of detected potholes
    detected_potholes = len(results[0].boxes)
    if detected_potholes == 0:
        message = "No potholes detected. Drive safely."
    elif detected_potholes == 1:
        message = "1 pothole detected! Drive carefully."
    else:
        message = f"{detected_potholes} potholes detected! The road is damaged. Drive slowly."

    # Send JSON response with the image URL and message
    return jsonify({
        'image_url': url_for('static', filename='results/' + file.filename),
        'message': message
    })

if __name__ == '__main__':
    app.run(debug=True)
