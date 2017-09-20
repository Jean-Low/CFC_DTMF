import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt
import time

fs = 44100

def recordSound(duration):
    print("recording for the next " , duration , " seconds")
    audio = sd.rec(int(duration*fs), fs, channels=4)
    sd.wait()
    return audio[:,0]

def playSound(sound):
    print("playing audio")
    sd.play(sound, fs)
    sd.wait()

audio = recordSound(1)
timeLenght = np.arange(len(audio))
print(len(audio))
plt.ion()

while True:
    print('updating')
    plt.clf()
    plt.plot(timeLenght,audio)
    plt.pause(0.0001)
    audioSplit =  recordSound(0.05)
    audio = np.concatenate([audio[2205:] , audioSplit])
