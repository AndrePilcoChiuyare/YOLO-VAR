from ultralytics import YOLO as yl
import random
import numpy as np
import cv2

# Cargar un modelo YOLO preentrenado (recomendado para entrenamiento)
model = yl("yolov8n.pt", "v8")

# Cargar el video
# video_path = "./assets/test.mp4"
# cap = cv2.ideoCapture(video_path)

# Obtener las propiedades del video
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))

class_list = model.names

# Generar colores aleatorios para cada clase
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# Abrimos la camara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Empezamos a obtener cada frame de la camara
    ret, frame = cap.read()

    # Verificamos que se haya abierto correctamente la camara
    if not ret:
        break

    # Realizar prediccion de detección de objetos en el frame
    results = model.predict([frame], imgsz=640, conf=0.45, save=False)

    # Obtenemos la lista de los valores de cada objeto detectado
    boxes = results[0].boxes
    
    # Si detecta objetos entra al `if`
    if len(boxes) != 0:
        for i in range(len(boxes)):
            print(i)
            
            # Obtenemos los valores de cada objeto
            box = boxes[i]  
            clsID = box.cls.numpy()[0] # Leemos la clasificacion (clase)
            conf = box.conf.numpy()[0] # Leemos la prediccion del objeto (%)
            bb = box.xyxy.numpy()[0]   # Leemos las posiciones de la caja

            # Dibujamos la caja del objeto con el color correspodiente del objeto
            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )

            # Mostrar la clase y el porcentaje de prediccion
            font = cv2.FONT_HERSHEY_COMPLEX # Fuente de la clase
            
            # Dibujamos el texto de la clase del objeto
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

    # Mostrar el video en pantalla
    cv2.imshow("Video Detection", frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) == ord("q"):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
