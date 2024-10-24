from flask import Flask, Response, render_template, request
import cv2
import mediapipe as mp
import pyautogui
import numpy as np

app = Flask(__name__)

# Inicializar los módulos de MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

def count_fingers(hand_landmarks):
    fingers = []
    for i in range(5):
        tip_y = hand_landmarks.landmark[mp_hands.HandLandmark(4 * i + 4)].y
        fold_y = hand_landmarks.landmark[mp_hands.HandLandmark(4 * i + 1)].y
        fingers.append(1 if tip_y < fold_y else 0)
    return sum(fingers)

def generar_video():
    cap = cv2.VideoCapture(0)  # Captura desde la cámara por defecto
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignorando el video vacío.")
            continue
            
        image_color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_color)

        # Dibujar los resultados y contar los dedos
        if results.multi_hand_landmarks:
            for hand_landmarks, hand_label in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                num_fingers = count_fingers(hand_landmarks)
                hand_type = hand_label.classification[0].label
                hand_label_text = 'Consonante' if hand_type == 'Left' else 'Vocal'
                
                # Definir letras según la mano
                vocales = [None, 'a', 'e', 'i', 'o', 'u']
                consonantes = [None, 'b', 'c', 'd', 'y', 'g']
                letras = consonantes if hand_label_text == 'Consonante' else vocales

                # Mostrar la letra en la imagen
                cv2.putText(image, f'{hand_label_text}: {letras[num_fingers]}', (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                
                # Escribir la letra usando PyAutoGUI
                if letras[num_fingers]:
                    pyautogui.write(letras[num_fingers])
        
        
        # Codificar el fotograma en JPEG
        _, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        
        # Devuelve el fotograma en un formato adecuado para MJPEG
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/video_feed')
def video_feed():
    return Response(generar_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Gestus')
def Gestus():
    return render_template('gestus.html')

# @app.route('/funcion/<param1>/<param2>')
# def funcion(param1, param2):
#     resultado = f'{param1} {param2}'
#     return render_template('home.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)