from ultralytics import YOLO
import cv2
import numpy as np
import keyboard
import time
import ctypes

class VAR:
    def __init__(self, videoPath, YOLOmodel, user32, classes):
        # Initialize the 'track_history' to store the coordinates of the center of the bounding box of the first detected object
        self.track_history = []
        # Initialize the 'zoomSize' to store the size of the zoomed rectangle
        self.zoomSize = 150
        # Initialize the 'YOLOmodel' to store the YOLO model
        self.YOLOmodel = YOLO(YOLOmodel)
        # Initialize the 'zoomBool' to store the state of the zoom
        self.zoomBool = False
        # Initialize the 'classes' to store the classes to detect
        self.classes = classes
        # Set the windows properties providing the user32 dll and the video path
        self.windowProperties(user32, videoPath)

    def windowProperties(self, user32, videoPath):
        # Set the font properties
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.fontScale = 0.5
        self.color = (255, 0, 255)
        self.thickness = 2
        # Set the screen properties
        self.screen_width, self.screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # Set the video properties
        self.video = cv2.VideoCapture(videoPath)
        cv2.namedWindow('VAR', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('VAR', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Set the maximum side length of the zoomed rectangle
        self.max_side_length = min(self.screen_width, self.screen_height) - 1
    
    def modelType(self, frame):
        # Return the results of the YOLO model
        return self.YOLOmodel.track(frame, classes=self.classes)
    
    def controls(self, key):
        # If the 'q' key is pressed, release the video and destroy all windows
        if key == ord('q'):
            self.video.release()
            cv2.destroyAllWindows()
        # If the 'p' key is pressed, pause the video
        if key == ord('p'):
            cv2.waitKey(-1)
        # If the 'a' key is pressed, go back 20 frames
        if (key == ord('a')):
            # Get the current frame number
            cur_frame_number = self.video.get(cv2.CAP_PROP_POS_FRAMES)
            # Set the previous frame number
            prev_frame = cur_frame_number
            # Go back 20 frames
            prev_frame -= 20
            # Set the video to the previous frame
            self.video.set(cv2.CAP_PROP_POS_FRAMES, prev_frame)
        # If the 'd' key is pressed, go forward 10 frames
        if (key == ord('d')):
            # Get the current frame number
            cur_frame_number = self.video.get(cv2.CAP_PROP_POS_FRAMES)
            # Set the next frame number
            next_frame = cur_frame_number
            # Go forward 10 frames
            next_frame += 10
            # Set the video to the next frame
            self.video.set(cv2.CAP_PROP_POS_FRAMES, next_frame)
        # If the 'w' key is pressed, decrease the zoom size
        if key == ord('w') and self.zoomSize > 50:
            # Decrease the zoom square size (more zoom)
            self.zoomSize -= 10
        # If the 's' key is pressed, increase the zoom size    
        if key == ord('s') and self.zoomSize < 200:
            # Increase the zoom square size (less zoom)
            self.zoomSize += 10
    
    def showWindow(self, frame):
        # If the zoom is activated, show the zoomed content
        if self.zoomBool:
            # Get the zoomed content
            zoomed_content = frame[self.top_left[1]:self.bottom_right[1], self.top_left[0]:self.bottom_right[0]]
            # Validate that the zoomed content has valid dimensions
            if zoomed_content.shape[0] > 0 and zoomed_content.shape[1] > 0:
                # Show the zoomed content
                cv2.imshow('VAR', zoomed_content)
            else:
                # If the zoomed content has invalid dimensions, print a message
                print("Invalid dimensions for zoomed content.")
        # If the zoom is deactivated, show the frame
        else:
            # Show the frame
            cv2.imshow('VAR', frame)
    
    def zoomRectangle(self, frame):
        # Get the coordinates of the center of the last position of the ball in 'track_history'
        x, y = self.track_history[-1]
        # Get the minimum value between the zoom size and the maximum side length of the zoomed rectangle
        self.side_length = min(self.zoomSize, self.max_side_length)
        # Set the coordinates of the top left and bottom right corners of the zoomed rectangle
        self.top_left = (int(x - self.side_length / 2), int(y - self.side_length / 2))
        self.bottom_right = (int(x + self.side_length / 2), int(y + self.side_length / 2))
        # Draw the zoomed rectangle
        cv2.rectangle(frame, self.top_left, self.bottom_right, self.color, self.thickness)
        # Print the center of the zoomed rectangle
        print(self.track_history[-1])
    

