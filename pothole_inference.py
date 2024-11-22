from ultralytics import YOLO

# Load the trained model (best.pt or last.pt)
model = YOLO('runs/detect/train3/weights/last.pt')

# Perform inference on new images in the folder (you can replace 'path_to_test_images' with your actual path)
results = model.predict(source='D:/Pothole_Test_Images1', save=True)

# Display the results
for result in results:
    result.show()
