from openal import *
from audio import Audio
from sys import stdin
import threading

def printMenu():
    with open("menu.txt", "r") as file:
        menu = file.read()
        print(menu)

def menu():
    menuSonido = Audio("menuSound", (10, 0, 0))
    menuSonido.play()
    printMenu()
    userInput = int(stdin.readline())
    menuSonido.stop()
    if userInput == 1:
        print("Saliendo del programa...")
    elif userInput == 0:
        start()

def start():
    print("¡El juego ha comenzado!")

def main():
    # Start OpenAL 
    device = alc.alcOpenDevice(None)
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)

    menu()

    # Cerrar OpenAL
    oalQuit()
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)

main()

    # Hilo para la reproducción de audio simultanea
    #audioThread = threading.Thread(target=play_audio_in_thread, args=(menuSonido,))
    #audioThread = threading.Thread(target=menuSonido.play())
    #audioThread.start()
    #audioThread.join()