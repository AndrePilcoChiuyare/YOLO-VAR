from ultralytics import YOLO as yl
import cv2

# Load a pretrained YOLO model (recommended for training)
model = yl('yolov8n-seg.pt')

# Perform object detection on an image using the model
#results = model(, stream=True)

results = model.predict('https://www.youtube.com/watch?v=dmckTJuZzSM', imgsz = 640, stream = True, show = True)

