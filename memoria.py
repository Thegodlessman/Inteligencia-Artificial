import pygame
import sys
import math
import time
import random

pygame.init()
pygame.font.init()

altura_boton = 30
medida_cuadro = 100
segundos_mostrar_pieza = 2

# Definimos los colores para las tarjetas
COLORES = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class Cuadro:
    def __init__(self, color):
        self.mostrar = True
        self.descubierto = False
        self.color = color

cuadros = []
for color in COLORES:
    cuadros.append(Cuadro(color))
    cuadros.append(Cuadro(color))

random.shuffle(cuadros)

color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_gris = (206, 206, 206)
color_azul = (30, 136, 229)

anchura_pantalla = 2 * medida_cuadro * math.ceil(math.sqrt(len(cuadros)))
altura_pantalla = 2 * medida_cuadro * math.ceil(len(cuadros) / math.ceil(math.sqrt(len(cuadros))))
anchura_boton = anchura_pantalla

tamanio_fuente = 20
fuente = pygame.font.SysFont("Arial", tamanio_fuente)
xFuente = int((anchura_boton / 2) - (tamanio_fuente / 2))
yFuente = int(altura_pantalla - altura_boton)

boton = pygame.Rect(0, altura_pantalla - altura_boton, anchura_boton, altura_pantalla)
ultimos_segundos = None
puede_jugar = True
juego_iniciado = False
x1 = None
y1 = None
x2 = None
y2 = None

def ocultar_todos_los_cuadros():
    for cuadro in cuadros:
        cuadro.mostrar = False
        cuadro.descubierto = False

def comprobar_si_gana():
    if gana():
        reiniciar_juego()

def gana():
    for cuadro in cuadros:
        if not cuadro.descubierto:
            return False
    return True

def reiniciar_juego():
    global juego_iniciado
    juego_iniciado = False

def iniciar_juego():
    ocultar_todos_los_cuadros()
    global juego_iniciado
    juego_iniciado = True

def seleccionar_tarjeta_ia():
    tarjetas_no_descubiertas = [(x, y) for y in range(int(altura_pantalla / medida_cuadro)) for x in range(int(anchura_pantalla / medida_cuadro)) if not cuadros[y * int(anchura_pantalla / medida_cuadro) + x].descubierto]
    if len(tarjetas_no_descubiertas) >= 2:
        random.shuffle(tarjetas_no_descubiertas)
        return tarjetas_no_descubiertas[:2]
    return []

pantalla_juego = pygame.display.set_mode((anchura_pantalla, altura_pantalla))
pygame.display.set_caption('MEMORIA')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:
            xAbsoluto, yAbsoluto = event.pos
            if boton.collidepoint(event.pos):
                if not juego_iniciado:
                    iniciar_juego()
            else:
                if not juego_iniciado:
                    continue
                x = math.floor(xAbsoluto / medida_cuadro)
                y = math.floor(yAbsoluto / medida_cuadro)
                indice = y * int(anchura_pantalla / medida_cuadro) + x
                if indice < len(cuadros):
                    cuadro = cuadros[indice]
                    if cuadro.mostrar or cuadro.descubierto:
                        continue
                    if x1 is None and y1 is None:
                        x1 = x
                        y1 = y
                        cuadros[indice].mostrar = True
                    else:
                        x2 = x
                        y2 = y
                        cuadros[indice].mostrar = True
                        if cuadros[y1 * int(anchura_pantalla / medida_cuadro) + x1].color == cuadro.color:
                            cuadros[y1 * int(anchura_pantalla / medida_cuadro) + x1].descubierto = True
                            cuadros[indice].descubierto = True
                            x1 = None
                            y1 = None
                            x2 = None
                            y2 = None
                        else:
                            ultimos_segundos = int(time.time())
                            puede_jugar = False
                    comprobar_si_gana()

    ahora = int(time.time())
    if ultimos_segundos is not None and ahora - ultimos_segundos >= segundos_mostrar_pieza:
        cuadros[y1 * int(anchura_pantalla / medida_cuadro) + x1].mostrar = False
        cuadros[y2 * int(anchura_pantalla / medida_cuadro) + x2].mostrar = False
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        ultimos_segundos = None
        puede_jugar = True

    pantalla_juego.fill(color_blanco)
    x = 0
    y = 0
    for cuadro in cuadros:
        if cuadro.descubierto or cuadro.mostrar:
            pygame.draw.rect(pantalla_juego, cuadro.color, pygame.Rect(x, y, medida_cuadro, medida_cuadro))
        else:
            pygame.draw.rect(pantalla_juego, color_negro, pygame.Rect(x, y, medida_cuadro, medida_cuadro))
        x += medida_cuadro
        if x >= anchura_pantalla:
            x = 0
            y += medida_cuadro

    if juego_iniciado:
        pygame.draw.rect(pantalla_juego, color_blanco, boton)
        pantalla_juego.blit(fuente.render("Iniciar juego", True, color_gris), (xFuente, yFuente))
    else:
        pygame.draw.rect(pantalla_juego, color_azul, boton)
        pantalla_juego.blit(fuente.render("Iniciar juego", True, color_blanco), (xFuente, yFuente))

    pygame.display.update()
