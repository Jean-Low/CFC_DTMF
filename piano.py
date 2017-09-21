import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt
import os
import pickle
import time


fs = 44100
tempo = 240
currentChannel = 0;
channels = []
track = [] # [note,label]

noteDic = {'c':261.626,'c#':277.183,'d':293.665, 'd#':311.127, 'e':329.628, 'f':349.228 , 'f#':369.994, 'g':391.995, 'g#':415.305, 'a':440.000,'a#':466.164, 'b':493.883}


def playSound(sound,looping = False):
    print("playing audio")
    sd.play(sound, fs,loop = looping)
    sd.wait()

def playSoundNoWait(sound,looping = False):
    print("playing audio")
    sd.play(sound, fs,loop = looping)

def generateWave(freq,duration): 
    
    print(int(duration * fs))
    sound = [0] * int(duration * fs)
    for i in range(0,len(sound)):
        sound[i] = np.sin(2*math.pi  * freq * (i/fs))
    lastZeroIndex = 0;
    for i in range(len(sound)):
        if (sound[-i-1] < 0.01 and sound[-i-1] > -0.01):
            lastZeroIndex = len(sound) - i - 1
            break
    print(len(sound[:lastZeroIndex]))
    return sound[:lastZeroIndex]

def createNote(note,octave,duration):
    label = note
    note = noteDic[note]
    tick = 1 / (tempo / 60)
    time = duration * tick
        
    octaveDif = octave - 4
    
    if(octaveDif == 0):
        print('creating note : ', note)
        return([generateWave(note,time),label])
    
    if(octaveDif > 0):
        for i in range(octaveDif):
            note *= 2
    elif(octaveDif < 0):
        for i in range(- octaveDif):
            note /= 2
    print('creating note : ', note)
    return([generateWave(note,time),label])


def playTrack():
    for i in track:
        print('playing : ' , i[1])
        playSound(i[0])
    print('done')

def addNote(note):
    track.append(note)

def deleteLastNote():
    track.pop()

def freePlay():
    print('freePlaying')
    note = createNote('d',4,0.5)
    playSoundNoWait(note[0],True)
        



while True:
    print('1 - add nota\n2 - tocar\n3 - delete\n4 - save\n5 - load\n6 - free play')
    choice = int(input())
    if(choice == 1):
        print('digite uma nota :')
        noteInput = input()
        print('em qual oitavo :')
        octave = int(input())
        print('em qual duração :')
        time = float(input())
        note = createNote(noteInput,octave,time)
        addNote(note)
    elif(choice == 2):
        playTrack()
    elif(choice == 3):
        deleteLastNote()
    elif(choice == 4):
        print('Digite o nome do arquivo (Sem extensão):')
        name = input()
        pickle.dump(track,open('Musics/' + name + '.p','wb'))
        print('gravado\n')
    elif(choice == 5):
        print('As seguintes musicas foram encontrados:')
        for i in sorted(os.listdir('Musics')):
            print(' - ' + i)
        print('qual o nome do arquivo que deseja carregar (sem extensão):')
        name = input()
        track = pickle.load(open('Musics/' + name + '.p','rb'))
        print('carregado')
    elif(choice == 6):
        freePlay()
