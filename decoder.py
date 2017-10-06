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
    print(iterations)

    while True:
        print('updating')
        plt.clf()
        plt.ylim([-0.4,0.4])
        plt.plot(timeLenght,audio)
        plt.pause(0.0001)
        audioSplit =  recordSound(1 / iterations)
        audio = np.concatenate([audio[(len(audio) // iterations ):] , audioSplit])

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

def FourierAoVivaco(duration):
    notgood = '''
    duration = 1
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    plt.xlabel('Time')
    plt.ylabel('sin(x)')
    def animate(i):
        ax1.clear()
        audio = sd.rec(int(1*fs), fs, channels=1)
        fftAudio = np.abs(fft(audio))
        t = np.arange(2000)   
        ax1.plot(t,fftAudio[:2000])
        plt.axis([0,2000,0,25000])
        print(Identify(fftAudio))
        
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()'''

    audio = recordSound(duration)
    Lenght = np.arange(3000)
    plt.ion()

    while True:
        plt.clf()
        #plt.ylim([-0.4,0.4])
        fftAudio = np.abs(fft(audio))
        plt.axis([0,2000/2,0,25000])
        plt.plot(Lenght,fftAudio[:3000])
        plt.pause(0.0001)
        print(Identify(fftAudio))
        audio =  recordSound(duration)


def Identify(fftAudio):
    HFList = []
    peek = 0
    #plt.plot(np.arange(2000),fftAudio[:2000])
    #plt.show()
    for v in fftAudio[:2000]:
        if v > peek:
            peek = v
    threshold = peek * 0.4
    for i in range(600,2000):
        if(fftAudio[i]) >= threshold:
            HFList.append(i)
    
    print(HFList)
    High = []
    Low = []
    for v in HFList:
        if v > 1100:
            High.append(v)
        else:
            Low.append(v)
    keyPad = [[1,2,3,"A","Deu ruin"],[4,5,6,"B","Deu ruin"],[7,8,9,"C","Deu ruin"],["*",0,"#","D","Deu ruin"],["Deu ruin","Deu ruin","Deu ruin","Deu ruin","Deu ruin em dobro"]]
    HighGroup = [1209,1336,1477,1633]
    LowGroup = [697,770,852,941]
    H = 4
    L = 4
    for i in range(4):
        if (len(High) > 0 and HighGroup[i] == High[0]):
            H = i
        if(len(Low) > 0 and LowGroup[i] == Low[0]):
            L = i

    print(H,L)
    return keyPad[L][H]
    
    
def recordBeep(duration):
    while True:
        print('Iremos gravar o audio com o beep.\nAperte enter para continuar...')
        input()
        audio=recordSound(duration)
        while True:
            print('Escolha:\n1-Salvar\n2-Reproduzir\n3-Mostrar grafico\n4-Gravar novamente\n5-Carregar save\n6-Identificar sinal')
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
            elif(choice == 6):
                print('Otima escolha!\nVocê deseja...\n1-Identificar o sinal por save\n2-Identificar em tempo real')
                choice = (int(input()))
                if(choice == 1):
                    print(Identify(np.abs(fft(audio))))
                    break
                elif(choice == 2):
                    print("quantas iterações por segundo:")
                    wither = int(input())
                    FourierAoVivaco(1 / wither)
                    break
                else:
                    print("Opção inválida")
                    break    
            else:
                print('opção invalida')


plt.grid()
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
