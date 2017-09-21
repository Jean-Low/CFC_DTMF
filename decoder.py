import sounddevice as sd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pickle
import os
from scipy.fftpack import fft

fs = 44100
globalDuration = 1

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
        plt.ylim([-0.4,0.4])
        plt.plot(timeLenght,audio)
        plt.pause(0.0001)
        audioSplit =  recordSound(1 / iterations)
        audio = np.concatenate([audio[(len(audio) / iterations ):] , audioSplit])




def gabsContribuition(duration):
    duration = 1

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    plt.xlabel('Time')
    plt.ylabel('sin(x)')
    def animate(i):
        audio = sd.rec(int(1*fs), fs, channels=1)
        y = audio[:,0]
        t = np.linspace(0,1,fs*duration)    
        ax1.clear()
        ax1.plot(t[0:1000],y[0:1000])
        
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def recordBeep(duration):
    while True:
        print('Iremos gravar o audio com o beep.\nAperte enter para continuar...')
        input()
        audio=recordSound(duration)
        while True:
            print('Escolha:\n1-Salvar\n2-Reproduzir\n3-Mostrar grafico\n4-Gravar novamente\n5-Carregar save')
            choice = int(input())
            if(choice == 1):
                print('Digite o nome do arquivo (Sem extensão):')
                name = input()
                pickle.dump(audio,open('Saves/' + name + '.p','wb'))
                print('gravado\n')
            elif(choice == 2):
                playSound(audio)
            elif(choice == 3):
                print('Aplicar transformada de fourier ? (Y ou N)')
                ft = input()
                if(ft == 'y'):
                    fftAudio = np.abs(fft(audio))
                    plt.plot(np.arange(2000),fftAudio[:2000])
                    plt.show()
                elif(ft == 'n'):
                    print('mostrar um zoom do grafico ? (Y ou N)')
                    zoom = input()
                    plt.plot(np.arange(len(audio) if zoom == 'n' else 1000),audio if zoom == 'n' else audio[40000:41000])
                    plt.show()
                else:
                    print('opção invalida')
            elif(choice == 4):
                print('Quanto tempo você quer gravar?')
                duration = (int(input()))
                break
            elif(choice == 5):
                print('Os seguintes saves foram encontrados:')
                for i in sorted(os.listdir('Saves')):
                    print(' - ' + i)
                print('qual o nome do arquivo que deseja carregar (sem extensão):')
                name = input()
                audio = pickle.load(open('Saves/' + name + '.p','rb'))
                print('carregado')
            else:
                print('opção invalida')


print('Bem vindo ao impressionivel DTMF-pro-ultra-master\nRelease 1\n')
print('Temos 2 funcionalidades:\n1 - O incrivel Real-Time-Sound-Ploting Deluxe Edition\nou\n2 - O imprescindivel Beep-Recording-VX Professional\nfaça a sua escolha:')
choice = int(input())
if(choice == 1):
    print('Otima escolha!\nDiga-nos quantas interações por segundo você deseja (padrão: 5):')
    continuosRec(int(input()))
elif(choice ==2):
    print('Otima escolha!\nDiga-nos quanto tempo deseja gravar, em segundos (padrão: 1):')
    recordBeep(int(input()))
else:
    print('Desculpe-me, sua opção não foi reconhecida pelo nosso gnomo...\nTente novamente')
