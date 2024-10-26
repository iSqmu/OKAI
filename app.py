import pickle
import cv2
import mediapipe as mp
import numpy as np
from flask import Flask, Response, render_template, request
import pyautogui
# import pyttsx3

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)

labels_dict = {0: 'A', 1: 'E', 2: 'I', 3: 'O', 4: 'U', 5: 'B', 6: 'C', 7: 'D', 8: 'F', 9: 'L'}
options = {
    'byn': False,
    'dcolors': False,
    'voice': True
}

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 150)  
# engine.setProperty('volume', 1.0) 




def gen_frame():

    while cap.isOpened():
        data_aux = []
        x_ = []
        y_ = []
        ret, frame = cap.read()
        # letra = ''
        
        if not ret:
            print('Ignorando el video vacío.')
            continue
        
        H, W, _ = frame.shape
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if options['byn']:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
            
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    
                    x_.append(x)
                    y_.append(y)
                
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
            
            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            
            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10
            
            prediction = model.predict([np.asarray(data_aux)])
            
            predicted_character = labels_dict[int(prediction[0])]
            

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)

            pyautogui.write(predicted_character)
                
        
        suc, encode = cv2.imencode('.jpg', frame)
        frame = encode.tobytes()
        
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Gestus')
def Gestus():
    option_byn = request.args.get('byn')
    option_dcolors = request.args.get('dcolors')

    if option_byn == 'active': 
        options['byn'] = True
    else:
        options['byn'] = False
    if option_dcolors == 'active':
        print('dcolors')
    
    return render_template('gestus.html')

@app.route('/video')
def video():
    return Response(gen_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)