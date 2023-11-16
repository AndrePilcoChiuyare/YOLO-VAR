from VARclass import *

def main():
    
    var = VAR('assets/prueba_resize.mp4', 'yolov8x.pt', ctypes.windll.user32, 32)

    while var.video.isOpened():
        success, frame = var.video.read()
        if success:
            results = var.modelType(frame, True)

            for track in results[0]:
                xywh = track.boxes.xywh
                x, y = xywh[0][:2]
                var.track_history.append((x.item(), y.item()))
            
            if var.track_history:
                var.zoomRectangle(frame)

                if keyboard.is_pressed('space'):
                    if not var.zoomBool:
                        var.zoomBool = True
                    else:
                        var.zoomBool = False
                    time.sleep(0.2)
                
                var.showWindow(frame)
            else:
                print("Track history is empty")
            
            key = cv2.waitKey(1)
            var.controls(key)
        else:
            break
    
    var.video.release()
    cv2.destroyAllWindows()

    

if __name__ == "__main__":
    main()