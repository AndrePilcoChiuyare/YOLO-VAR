from ultralytics import YOLO
import cv2
import numpy as np
import keyboard
import time
import ctypes

class VAR:
    def __init__(self, videoPath, YOLOmodel, user32, classes):
        self.track_history = []
        self.zoomSize = 150
        self.YOLOmodel = YOLO(YOLOmodel)
        self.zoomBool = False
        self.classes = classes
        self.windowProperties(user32, videoPath)

    def windowProperties(self, user32, videoPath):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.fontScale = 0.5
        self.color = (255, 0, 255)
        self.thickness = 2
        self.screen_width, self.screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.video = cv2.VideoCapture(videoPath)
        cv2.namedWindow('VAR', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('VAR', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        self.max_side_length = min(self.screen_width, self.screen_height) - 1
    
    def modelType(self, frame, track):
        if track == True:
            return self.YOLOmodel.track(frame, classes=self.classes)
        return self.YOLOmodel(frame, classes=self.classes)
    
    def controls(self, key):
        if key == ord('q'):
            self.video.release()
            cv2.destroyAllWindows()
        if key == ord('p'):
            cv2.waitKey(-1)
        if (key == ord('a')):
            cur_frame_number = self.video.get(cv2.CAP_PROP_POS_FRAMES)
            prev_frame = cur_frame_number
            if (cur_frame_number > 1):
                prev_frame -= 20
            self.video.set(cv2.CAP_PROP_POS_FRAMES, prev_frame)
        if (key == ord('d')):
            cur_frame_number = self.video.get(cv2.CAP_PROP_POS_FRAMES)
            prev_frame = cur_frame_number
            if (cur_frame_number > 1):
                prev_frame += 10
            self.video.set(cv2.CAP_PROP_POS_FRAMES, prev_frame)

        if key == ord('w') and self.zoomSize > 50:
            self.zoomSize -= 10
            
        if key == ord('s') and self.zoomSize < 200:
            self.zoomSize += 10
    
    def showWindow(self, frame):
        if self.zoomBool:
            zoomed_content = frame[self.top_left[1]:self.bottom_right[1], self.top_left[0]:self.bottom_right[0]]
            if zoomed_content.shape[0] > 0 and zoomed_content.shape[1] > 0:
                cv2.imshow('VAR', zoomed_content)
            else:
                print("Invalid dimensions for zoomed content.")
        else:
            cv2.imshow('VAR', frame)
    
    def zoomRectangle(self, frame):
        x, y = self.track_history[-1]
        self.side_length = min(self.zoomSize, self.max_side_length)
        self.top_left = (int(x - self.side_length / 2), int(y - self.side_length / 2))
        self.bottom_right = (int(x + self.side_length / 2), int(y + self.side_length / 2))
        cv2.rectangle(frame, self.top_left, self.bottom_right, self.color, self.thickness)
        print(self.track_history[-1])
    

