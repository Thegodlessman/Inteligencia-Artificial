import time 
import random
import os

def initGame():
    print('--- BIENVENIDO ---')
    time.sleep(1)
    while True:
        token = input('SELECCIONE SU TOKEN: X / O\n')
        token = token.upper()

        if token == "X":
            player = "X"
            ia = "O"
            break
        elif token == "O":
            player = "O"
            ia = "X"
            break
        else:
            print("INGRESE UN TOKEN VALIDO, INTENTELO DE NUEVO")

    return player, ia


def mapa(matriz):
    print("--- TICTACTOE---")
    print()
    print("          |          |          ")
    print("1  {}      |2  {}      |3   {}     ".format(matriz[0], matriz[1], matriz[2]))
    print("          |          |          ")
    print("------------------------------")
    print("          |          |          ")
    print("4  {}      |5  {}      |6   {}     ".format(matriz[3], matriz[4], matriz[5]))
    print("          |          |          ")
    print("------------------------------")
    print("          |          |          ")
    print("7  {}      |8  {}      |9   {}     ".format(matriz[6], matriz[7], matriz[8]))
    print("          |          |          ")


def checkFullMap(matriz):
    for i in matriz:
        if i == " ":
            return False
    else:
        return True
        
def checkCasilla(matriz, casilla):
    return matriz[casilla] == " "

def searchWinner(matriz, player):

    if matriz[0] == matriz[1] == matriz[2] == player or \
        matriz[3] == matriz[4] == matriz[5] == player or \
        matriz[6] == matriz[7] == matriz[8] == player or \
        matriz[0] == matriz[3] == matriz[6] == player or \
        matriz[1] == matriz[4] == matriz[7] == player or \
        matriz[2] == matriz[5] == matriz[8] == player or \
        matriz[0] == matriz[4] == matriz[8] == player or \
        matriz[2] == matriz[4] == matriz[6] == player:
        return True
    else:
        return False
        
def playerMov(matriz):

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None

    while True: 
        if posicion not in posiciones:
            posicion = input(" INGRESE UNA POSICION EN EL TABLERO(1-9): ")
        else:
            posicion = int(posicion)
            if not checkCasilla(matriz, posicion-1):
                print("Esta posicion esta ocupada")
            else:
                return posicion-1
            
def iaMov(matriz, player):
    for i in range(9):
        copia = list(matriz)
        if checkCasilla(copia, i):
            copia[i] = player
            if searchWinner(matriz, player):
                return i
            
    while True:
        casilla = random.randint(0,8)

        if not checkCasilla(matriz, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla
        
game = True

while game:
    os.system("cls")
    matriz = [" "] * 9

    player, ia = initGame() 

    os.system("cls")
    mapa(matriz)

    if player == 'X':
        turno = "Player"
    else:
        turno = "IA"

    partida = True

    while partida:

        if checkFullMap(matriz):
            print("--- EMPATE ---")
            partida = False
        
        elif turno == "Player":
            casilla = playerMov(matriz)
            matriz[casilla] = player
            turno = "IA"

            os.system("cls")
            mapa(matriz)
            if searchWinner(matriz, player):
                print ("--- HAS GANADO ---")
                partida = False

        elif turno == "IA":
            print(" ES TURNO DE LA IA...") 
            time.sleep(2)
            casilla = iaMov(matriz, player)
            matriz[casilla] = ia
            turno = "Player"

            os.system("cls")
            mapa(matriz)
            if searchWinner(matriz, ia):
                print ("--- HAS PERDIDO ---")
                partida = False

    time.sleep(5)
                