from VARclass import *

def main():
    # Definition of 'var' as an 'VAR' specifying the video path, the YOLO model, the user32 dll (for screen properties) and the class to detect
    var = VAR('assets/prueba_resize.mp4', 'yolov8x.pt', ctypes.windll.user32, 32)
    
    # While loop to read the video frame by frame
    while var.video.isOpened():
        # Boolean variable 'success' to know if the video is being read correctly and the 'frame' variable to store the current frame
        success, frame = var.video.read()
        # If the video is being read correctly, the 'success' variable will be True
        if success:
            # 'results' variable to store the results of the YOLO model of the current frame
            results = var.modelType(frame)
            
            # This loop is used to only get the first detected object and prevents an error when the model does not detect any object
            for track in results[0]:
                # 'xywh' variable to store the coordinates of the bounding box of the first detected object and its dimensions
                xywh = track.boxes.xywh
                # 'x' and 'y' variables to store the coordinates of the center of the bounding box of the first detected object
                x, y = xywh[0][:2]
                # Store the center coordinates in 'track_history' to use them to plot the ball square
                var.track_history.append((x.item(), y.item()))
            
            # Validate that the 'track_history' is not empty
            if var.track_history:
                # Define the dimensions of the zoomed rectangle providing the frame
                var.zoomRectangle(frame)

                # If the space bar is pressed, the zoom is activated or deactivated
                if keyboard.is_pressed('space'):
                    # If the zoom is activated, it is deactivated and vice versa
                    if not var.zoomBool:
                        var.zoomBool = True
                    else:
                        var.zoomBool = False
                    # Wait 200 ms to avoid multiple activations or deactivations of the zoom
                    time.sleep(0.2)
                # Show the frame in the window
                var.showWindow(frame)
            else:
                # If the 'track_history' is empty, print a message
                print("Track history is empty")
            # Read the key pressed by the user
            key = cv2.waitKey(1)
            # Process the input key
            var.controls(key)
        else:
            break
    # Release the video and destroy all windows
    var.video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()