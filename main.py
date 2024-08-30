from openal import *
from audio import Audio
import sys
import threading

def printMenu():
    with open("menu.txt", "r") as file:
        menu = file.read()
        print(menu)

def start():
    print("¡El juego ha comenzado!")

def play_audio_in_thread(audio_obj):
    audio_obj.play()

def main():
    # Start OpenAL 
    device = alc.alcOpenDevice(None)
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)

    printMenu()

    menuSonido = Audio("menuSound", (0, 0, 0))
    
    # Hilo para la reproducción de audio simultanea
    audioThread = threading.Thread(target=play_audio_in_thread, args=(menuSonido,))
    audioThread.start()

    userInput = input().strip().lower()

    if userInput == '1':
        print("Saliendo del programa...")
        menuSonido.stop()
        audioThread.join()
        alc.alcDestroyContext(context)
        alc.alcCloseDevice(device)
        sys.exit()
    elif userInput == '0':
        menuSonido.stop()
        audioThread.join()  # Esperar a que el hilo termine
        start()

    # Cerrar OpenAL
    oalQuit()
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)

main()
