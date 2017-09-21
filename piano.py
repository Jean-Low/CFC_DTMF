import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt


fs = 44100
tempo = 120
currentChannel = 0;
channels = []
track = [] # [note,label]

noteDic = {'c':261.626,'c#':277.183,'d':293.665, 'd#':311.127, 'e':329.628, 'f':349.228 , 'f#':369.994, 'g':391.995, 'g#':415,305, 'a':440,'a#':466.164, 'b':493.883}


def playSound(sound):
    print("playing audio")
    sd.play(sound, fs)
    sd.wait()

def generateWave(fs,duration): 
    
    sound = [0] * duration * fs
    for i in range(0,len(sound)):
        sound[i] = np.sin(2*math.pi  * key[0] * (i/fs))
    return sound

def createNotes(note,octave,duration):
    label = note
    note = noteDic[note]
    tick = 1 / (tempo / 60)
    time = duration * tick
    print(note, ' dura ', time, ' segundos')
        
    octaveDif = 4 - octave
    
    if(octaveDif == 0):
        return([generateWave(note,time),label])
    
    if(octaveDif > 0):
        for i in range(octaveDif):
            note *= 2
    elif(octaveDif < 0):
        for i in range(octaveDif):
            note /= 2
    
def playTrack():
    
    


while(True):
    print('Digite um numero :')
    key = int(input())
    beep = generateWave(key,3)
    playSound(beep)
    plt.plot(np.arange(1000),beep[:1000])
    plt.show()
    plt.plot(np.arange(1000),fft(beep[:1000]))
    plt.show()
