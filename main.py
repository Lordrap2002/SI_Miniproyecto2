from openal import *
from audio import Audio
from line import Line
from sys import stdin

def playLine(lineNumber):
    line = Line(lineNumber)
    line.playSounds()
    print(line)
    if len(line.paths):
        userInput = stdin.readline().strip().upper()
        while not userInput in line.options:
            print("Esa no es una opcion.")
            userInput = stdin.readline().strip().upper()
        line.stopSounds()
        playLine(line.paths[line.options.index(userInput)])
    else:
        print("El juego ha llegado a su fin, presiona Enter para salir.")
        userInput = stdin.readline()
        line.stopSounds()

def printMenu():
    with open("menu.txt", "r") as file:
        menu = file.read()
        print(menu)

def menu():
    userInput = 0
    while userInput != 1:
        menuSonido = Audio("MainTheme", (0, 0, 0), 0.3)
        menuSonido.play()
        printMenu()
        userInput = int(stdin.readline())
        opciones = [0, 1]
        while not userInput in opciones:
            print("Esa no es una opcion.")
            userInput = int(stdin.readline())
        menuSonido.stop()
        if userInput == 1:
            print("Saliendo del programa...")
        elif userInput == 0:
            print("¡El juego ha comenzado!")
            playLine(1)
    print("Gracias por jugar! :)")

def main():
    # Start OpenAL 
    device = alc.alcOpenDevice(None)
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)
    oalGetListener().set_position((0, 0, 0))
    # (forward_x, forward_y, forward_z, up_x, up_y, up_z)
    oalGetListener().set_orientation((0, 0, -1, 0, 1, 0))

    menu()

    # Close OpenAL
    oalQuit()
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)

main()