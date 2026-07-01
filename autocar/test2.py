import pyaudio
import numpy as p  # 요청하신 대로 numpy를 p로 임포트합니다.


class Tone:
    def __init__(self, volume= 0.5, rate=48000, channels=1):
        self.volume = volume
        self.rate = rate
        self.channels = channels
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=self.channels, rate=self.rate, output=True)
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.stop()
    
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
    def play()


import pyaudio
import wave
CHUNK = 1024
RATE = 48000

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
w=wave.open("./out.wav","wb")
w.setnchannels(1)
w.setsampwidth(p.get_sample_size(pyaudio.paInt16))
w.setframerate(RATE)
TIME = 5
data = []

for _ in range(0, int(RATE / CHUNK * TIME)):
    d = stream.read(CHUNK)
    data.append(d)

w.writeframes(b''.join(data))

w.close()
stream.stop_stream()
stream.close()
p.terminate()

import time
from pip import SoundMeter

sm = SoundMeter()

def onSoundMeter(rms, inData):
    if(rms>600):
        print(rms)

sm.setCallback(onSoundMeter)

input("input something")

sm.stop()

from pop import AudioRecord, AudioPlay
import time

with AudioRecord("output.wav") as ar:
    record.run()
    print("Recording...")

    for _ in range(5):
        time.sleep(1)

    record.stop()
    print("Recording stopped.")

with AudioPlay("output.wav") as ap:
    play.run()
    print("Playing...")
    for _ in range(12):
        time.sleep(1)
    
    play.stop()
    print("Playing stopped.")




from gtts import gTTS
import subprocess

text = "And the saddeest thing. under the sun above."
filename = "en_tts.mp3"

tts = gTTS(text)
tts.save(filename)
with subprocess.Popen(['play', filename]) as p:
    p.wait()
    

