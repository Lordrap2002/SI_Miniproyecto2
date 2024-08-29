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
    
    # Crear un hilo para la reproducción de audio
    audio_thread = threading.Thread(target=play_audio_in_thread, args=(menuSonido,))
    audio_thread.start()

    userInput = input().strip().lower()

    if userInput == '2':
        print("Saliendo del programa...")
        menuSonido.stop()
        audio_thread.join()  # Esperar a que el hilo termine
        alc.alcDestroyContext(context)
        alc.alcCloseDevice(device)
        sys.exit()
    else:
        menuSonido.stop()
        audio_thread.join()  # Esperar a que el hilo termine
        start()

    # Cerrar OpenAL al final
    oalQuit()
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)

if __name__ == "__main__":
    main()
