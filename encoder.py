import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt


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

def generateWave(putin,duration): 
    
    NumKeyboard = [[1336,941],[1209,697],[1336,697], [1477,697],[1209,770],[1336,770],[1477,770],[1209,852],[1336,852],[1477,852]]
    key = NumKeyboard[putin]
    print(key)
    sound = [0] * duration * fs
    for i in range(0,len(sound)):
        sound[i] = np.sin(2*math.pi  * key[0] * (i/fs)) + np.sin(2*math.pi  * key[1] * (i/fs))
    return sound


beep = generateWave(1,1)
playSound(beep)
beep = generateWave(2,1)
playSound(beep)
beep = generateWave(3,1)
playSound(beep)
beep = generateWave(4,1)
playSound(beep)
plt.plot(np.arange(1000),beep[:1000])
plt.show()
