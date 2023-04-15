import time 
import random
import os


def initGame():
    print('--- BIENVENIDO A MEMORIA ---')
    

    time.sleep(2)


def mapa(matriz):
    print("--- MEMORIA ---")
    print()
    print("---------------------------------------")
    print("|         |         |         |         |")
    print("|    {}    |    {}    |    {}    |    {}    |".format(matriz[0], matriz[1], matriz[2], matriz[3]))
    print("|         |         |         |         |")
    print("---------------------------------------")
    print("|         |         |         |         |")
    print("|    {}    |    {}    |    {}    |    {}    |".format(matriz[4], matriz[5], matriz[6], matriz[7]))
    print("|         |         |         |         |")
    print("---------------------------------------")
    print("|         |         |         |         |")
    print("|    {}    |    {}    |    {}    |    {}    |".format(matriz[8], matriz[9], matriz[10], matriz[11]))
    print("|         |         |         |         |")
    print("---------------------------------------")


def mapaOculto():
    print("--- MEMORIA ---")
    print()
    print("---------------------------------------")
    print("|         |         |         |         |")
    print("|    ?    |    ?    |    ?    |    ?    |")
    print("|         |         |         |         |")
    print("---------------------------------------")
    print("|         |         |         |         |")
    print("|    ?    |    ?    |    ?    |    ?    |")
    print("|         |         |         |         |")
    print("---------------------------------------")
    print("|         |         |         |         |")
    print("|    ?    |    ?    |    ?    |    ?    |")
    print("|         |         |         |         |")
    print("---------------------------------------")

def playerMov(matriz):

    posiciones = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    posicion = None

    while True: 
        if posicion not in posiciones:
            posicion = input("\nINGRESE UNA POSICION EN EL TABLERO(1-12): ")
        else:
            posicion = int(posicion)
            
            print("Hay un {} en la posicion seleccionada".format(matriz[posicion]))
            return matriz[posicion], posiciones

def iaMov(matriz):
    posicion = random.randint(0,11)
            
    print("Hay un {} en la posicion seleccionada por la IA".format(matriz[posicion]))
    return matriz[posicion]
    

def mostrarPuntos(iaPoints, playerPoints):
    print("--- TABLA DE PUNTOS ---")
    print("-- PLAYER POINTS: {} --".format(playerPoints))
    print("-- IA POINTS: {} --".format(iaPoints))

    time.sleep(3)

    if playerPoints > iaPoints:
        print("=== El ganador es El PLAYER ===")
    else:
        print("=== La ganodora es La IA ===")

    time.sleep(6)

def searchPoint(numA, numB):

    if numA == numB:
        return True
    else:
        return False

game = True
playerPoints = 0
iaPoints = 0

while game:
    os.system("cls")
    matriz = [" "] * 12

    for i in range(12):
        matriz[i] = random.randint(0,5)

    initGame()

    os.system("cls")
    mapaOculto()
    mapa(matriz)


    time.sleep(2)
    turno = "Player"

    partida = True

    while partida:
        if playerPoints == 3 or iaPoints == 3:

            print("EL JUEGO HA TERMINADO")

            time.sleep(3)
            
            mostrarPuntos(iaPoints, playerPoints)
            partida = False
        elif turno == "Player":
            numA = playerMov(matriz)
            numB = playerMov(matriz)
            turno = "IA"

            if searchPoint(numA, numB):
                print ("--- HAS GANADO UN PUNTO ---")
                playerPoints = playerPoints + 1
                print("Tienes: {}\n\n".format(playerPoints))
                
        elif turno == "IA":
            posiciones = playerMov
            
            print(" ES TURNO DE LA IA...") 
            numA = iaMov(matriz)
            print(" ES TURNO DE LA IA...") 
            numB = iaMov(matriz)
            
            time.sleep(2)
            turno = "Player"
            if searchPoint(numA, numB):
                print ("--- LA IA HA GANADO UN PUNTO ---")
                iaPoints = iaPoints + 1
                print("La IA tiene: {}".format(iaPoints))
                