from openal import *
from audio import Audio
from line import Line
from sys import stdin

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
        print("¡El juego ha comenzado!")
        start()
    print("Gracias por jugar! :)")

def start():
    sounds = [Audio("menuSound", (0, 0, 0))]
    intro = Line(0, sounds)
    intro.playSounds()
    print(intro)
    userInput = int(stdin.readline())
    intro.stopSounds()
    if userInput:
        print(1)
    else:
        print(0)
    print(-1)

def main():
    # Start OpenAL 
    device = alc.alcOpenDevice(None)
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)

    menu()

    # Close OpenAL
    oalQuit()
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)

main()