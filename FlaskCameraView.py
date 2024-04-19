from flask import Flask, Response
import cv2
import re
import os

app = Flask(__name__)

def gen_frames():  
    while True:
        success, frame = cap.read()  # read the camera frame
        
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            
@app.route('/')
def index():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    ipv4 = "192.168.12.136"
    app.run(host=ipv4, port=5000)
