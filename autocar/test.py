# 1. 장치연결
# 2. opencv 이미지 데이터 얻기(gstrmer)
# 3. 데이터처리
# 4. 보여주기 모니터 -imshow 웹 -api이미지 보내기 / 파일 저장

import time
from pop import Pilot
from pop import Util
import cv2 
Car = Pilot.AutoCar()


Car._steering


cap = cv2.VideoCapture(cam, cv2.CAP_GSTREAMER)
haar_face = '/user/local/share/opencv4/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_face)


import cv2 
from pop import Util
Util.enable_imshow()

m = Util.gstrmer(width=640, height=480, fps=30)
cap = cv2.VideoCapture(m, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Camera not founded")
try:
    for _ in range(3000):
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1, minSize=(100,100))
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame, "FACE", {x,y -10}, cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
        cv2.imshow("soda", img)
except KeyboardInterrupt:
    pass
finally:
    cap.release()

import pyaudio
import wave
p = pyaudio.PyAudio()
with wave.open("/usr/share/sounds/alsa/Side_Left.wav","rb") as w:
    data = w.readframes(w.getnframes())
    stream = p.open
    with p.open(format=p.get_format_from_width(2), channels=1, rate=48000, output=True)
    stream.write(data)
    stream.stop_stream()
    stream.close

import pyaudio
import wave
p = pyaudio.PyAudio()
data = None
with wave.open("/usr/share/sounds/alsa/Side_Left.wav","rb") as w:
    data = w.readframes(w.getnframes())
def play_cb(in_data, frame_count, time_info, status):
    data = w.readframes(frame_count)
    return(data, pyaudio.paContinue)
p= pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(w.getsampwidth()),
                channels=w.getnchannels(),
                rate=w.getframerate(),
                output=True,
                stream_callback=play_cb)
stream.start_stream()

while stream.is_active():
    print("재생 중..")
    time.sleep(0.1)

stream.stop_stream()
stream.close()
p.terminate()
w.close()


