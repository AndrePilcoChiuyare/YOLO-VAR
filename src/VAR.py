from ultralytics import YOLO
import cv2
import numpy as np
import keyboard
import time

# Create a video capture object
cap = cv2.VideoCapture('assets/prueba_resize.mp4')

# Initialize the YOLO model
model = YOLO('yolov8x.pt')

# Set up the font and color for drawing track information
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
color = (255, 0, 255)
thickness = 2

track_history = []

# Get the screen resolution
screen_width, screen_height = 1920, 1080  # Set your screen resolution

# Calculate the center position for the main window
main_window_width, main_window_height = 800, 600  # Set the size of the main window
main_window_x = int((screen_width - main_window_width) / 2)
main_window_y = int((screen_height - main_window_height) / 2)

# Create a window for the main display
cv2.namedWindow('YOLOv8 Inference', cv2.WINDOW_NORMAL)
cv2.moveWindow('YOLOv8 Inference', main_window_x, main_window_y)
cv2.resizeWindow('YOLOv8 Inference', main_window_width, main_window_height)

# Create a window for the second display
cv2.namedWindow('Zoomed View', cv2.WINDOW_NORMAL)
cv2.moveWindow('Zoomed View', main_window_x, main_window_y)
cv2.resizeWindow('Zoomed View', main_window_width, main_window_height)

# Flag to track if the second window is open
second_window_open = False

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model.track(frame, classes=32)

        for track in results[0]:
            xywh = track.boxes.xywh
            x, y = xywh[0][:2]
            track_history.append((x.item(), y.item()))

        if track_history:
            x, y = track_history[-1]

            # Change circle to rectangle
            max_side_length = min(main_window_width, main_window_height) - 1
            side_length = min(150, max_side_length)
            top_left = (int(x - side_length / 2), int(y - side_length / 2))
            bottom_right = (int(x + side_length / 2), int(y + side_length / 2))

            cv2.rectangle(frame, top_left, bottom_right, color, thickness)
            print(track_history[-1])

            # Check if the spacebar is pressed to toggle between windows
            if keyboard.is_pressed('space'):
                if not second_window_open:
                    # If the second window is closed, open it
                    cv2.namedWindow('Zoomed View', cv2.WINDOW_NORMAL)
                    cv2.moveWindow('Zoomed View', main_window_x, main_window_y)
                    cv2.resizeWindow('Zoomed View', main_window_width, main_window_height)
                    second_window_open = True
                else:
                    # If the second window is open, close it
                    cv2.destroyWindow('Zoomed View')
                    second_window_open = False
                # Wait for a short time to avoid registering multiple presses
                time.sleep(0.2)

            # Display the zoomed content in the second window if it's open
            if second_window_open:
                zoomed_content = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
                if zoomed_content.shape[0] > 0 and zoomed_content.shape[1] > 0:  # Check if dimensions are valid
                    cv2.imshow('Zoomed View', zoomed_content)
                else:
                    print("Invalid dimensions for zoomed content.")

        else:
            print("Track history is empty")

        cv2.imshow('YOLOv8 Inference', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        if key == ord('p'):
            cv2.waitKey(-1)
        if (key == ord('a')):
            cur_frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
            print('* At frame #' + str(cur_frame_number))

            prev_frame = cur_frame_number
            if (cur_frame_number > 1):
                prev_frame -= 20

            print('* Rewind to frame #' + str(prev_frame))
            cap.set(cv2.CAP_PROP_POS_FRAMES, prev_frame)
        if (key == ord('d')):
            cur_frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
            print('* At frame #' + str(cur_frame_number))

            prev_frame = cur_frame_number
            if (cur_frame_number > 1):
                prev_frame += 10

            print('* Rewind to frame #' + str(prev_frame))
            cap.set(cv2.CAP_PROP_POS_FRAMES, prev_frame)


    else:
        break

cap.release()
cv2.destroyAllWindows()
