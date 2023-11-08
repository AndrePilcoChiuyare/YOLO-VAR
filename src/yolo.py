# https://docs.ultralytics.com/quickstart/#conda-docker-image
# https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode
# https://docs.ultralytics.com/usage/cfg/#predict
# args: https://docs.ultralytics.com/modes/predict/#inference-sources
# https://www.youtube.com/watch?v=fu2tfOV9vbY&t=529s
# https://pytorch.org/get-started/locally/

from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n-seg.pt')

# Perform object detection on an image using the model
#results = model('https://www.youtube.com/shorts/kn-B13Ch9dw', stream=True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #results = model.predict(frame, imgsz = 640, retina_masks = False)
    
    
    #predict without segmentation
    results = model.predict('https://www.youtube.com/watch?v=dmckTJuZzSM', imgsz = 640, show = True)

    #annotations = results[0].plot()

    #cv2.imshow('Detection and segmentation', annotations)

    #if cv2.waitKey(1) == 27:
    #    break

#cap.release()
#cv2.destroyAllWindows()

