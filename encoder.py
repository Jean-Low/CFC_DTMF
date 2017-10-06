import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft


fs = 44100

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
	
def DB(energy):
    convert = []
    for i in energy:
        db = 10*math.log10(energy[i]/20000)
        convert.append(db)
    return convert

plt.title('Transmitido')	
plt.xlabel('Frequencia (Hz)', fontsize=18)
plt.ylabel('Decibel(dB)', fontsize=18)

while(True):
	print('Digite um numero :')
	key = int(input())
	beep = generateWave(key,1)
	playSound(beep)
	plt.plot(np.arange(1000),beep[:1000])
	plt.show()
	plt.plot(np.arange(2300),DB(np.abs(fft(beep)))[:2300])
	plt.title('Transmitido', fontsize=18)
	plt.xlabel('Frequencia (Hz)', fontsize=16)
	plt.ylabel('Decibel(dB)', fontsize=16)
	plt.show()

