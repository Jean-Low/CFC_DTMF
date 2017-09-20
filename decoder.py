import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt
import time

fs = 44100

def recordSound(duration):
    print("recording for the next " , duration , " seconds")
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    return audio[:,0]

def playSound(sound):
    print("playing audio")
    sd.play(sound, fs)
    sd.wait()


def continuosRec(iterations):
    audio = recordSound(1)
    timeLenght = np.arange(len(audio))
    print(len(audio))
    plt.ion()

    while True:
        print('updating')
        plt.clf()
        plt.plot(timeLenght,audio)
        plt.pause(0.0001)
        audioSplit =  recordSound(1 / iterations)
        audio = np.concatenate([audio[(fs / iterations ):] , audioSplit])

def recordBeep(duration):
    while True:
        print('Iremos gravar o audio com o beep.\nAperte enter para continuar...')
        input()
        audio=recordSound(duration)
        while True:
            print('Escolha:\n1-gravar\n2-reproduzir\n3-mostrar grafico\n4-tentar novamente')
            choice = int(input())
            if(choice == 1):
                #TODO-gravar com pickle
                print('gravado')
                break
            elif(choice == 2):
                playSound(audio)
            elif(choice == 3):
                plt.plot(np.arange(len(audio)),audio)
                plt.show()
            elif(choice == 4):
                break
            else:
                print('opção invalida')


print('Bem vindo ao inpressionivel DTMF-pro-ultra-master\nRelease 1\n')
print('Temos 2 funcionalidades:\n o incrivel Real-Time-Sound-Ploting Deluxe Edition\n ou o \nimprescindivel Beep-Recording-VX Professional\nfaça a sua escolha:')
choice = int(input())
if(choice == 1):
    print('Otima escolha!\nDiga-nos quantas interações por segundo você deseja (padrão: 5):')
    continuosRec(int(input()))
elif(choice ==2):
    print('Otima escolha!\nDiga-nos quanto tempo deseja gravar, em segundos (padrão: 1):')
    recordBeep(int(input()))
else:
    print('Desculpe-me, sua opção não foi reconhecida pelo nosso gnomo...\nTente novamente')
