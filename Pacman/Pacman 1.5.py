# Pacman 1.5 JC

# cada "puntito" da 10 puntos
# las "megapastillas" dan 40 puntos

import pygame
import time
import sys
import random

pygame.init()
pygame.display.set_caption("Pac-Man 1.5")

cuadros = 29  # tamaño de cada cuadro,  con esta variable se puede graduar el tamaño del juego en sí
size = (19*cuadros, 24*cuadros)
window = pygame.display.set_mode(size)

clock = pygame.time.Clock()

font_size_2 = cuadros*0.857142857*0.5
font_size_2 = round(font_size_2)

texto_fuente_1 = pygame.font.SysFont("snapitc", cuadros)
texto_fuente_2 = pygame.font.SysFont("comicsansms", font_size_2)
texto_fuente_3 = pygame.font.SysFont("arialblack", cuadros)

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 150)
orange = (255, 69, 0)
lightskyblue = (135, 206, 250)
pink = (255, 150, 255)

ritmo = 25  # variable para ajustar la velocidad del juego

window.fill(darkblue)

S_fondo = "siren_11.wav"
pygame.mixer.music.load(S_fondo)
S_iniciar = pygame.mixer.Sound("starting.mp3")
S_die = pygame.mixer.Sound("dies.mp3")
S_eat = pygame.mixer.Sound("eat-ghost.mp3")
S_waka_1 = pygame.mixer.Sound("waka_1.wav")
S_waka_2 = pygame.mixer.Sound("waka_2.wav")


def mostrar_puntaje_y_vida(score, lifes):
    letrero1_1 = texto_fuente_1.render("ScORE ", True, white)
    window.blit(letrero1_1, [cuadros*1.5, cuadros*21])

    letrero1_2 = texto_fuente_3.render(str(score), True, yellow)
    window.blit(letrero1_2, [cuadros*6, cuadros*20.9])

    letrero_2 = texto_fuente_1.render("LiVES ", True, white)
    window.blit(letrero_2, [cuadros*11, cuadros*21])

    if lifes > 0:
        pygame.draw.rect(window, yellow, [
                         cuadros*15.3, cuadros*21.1, cuadros, cuadros], border_radius=30)
        if lifes > 1:
            pygame.draw.rect(
                window, yellow, [cuadros*16.5, cuadros*21.1, cuadros, cuadros], border_radius=30)


# mapa #19x22


def draw_mapa():

    pygame.draw.rect(window, black, [cuadros, cuadros, cuadros*8, cuadros])
    pygame.draw.rect(window, black, [cuadros*10, cuadros, cuadros*8, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*2, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*4, cuadros*2, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*8, cuadros*2, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*10, cuadros*2, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*2, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*17, cuadros*2, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*3, cuadros*17, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*4, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*4, cuadros*4, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*4, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*12, cuadros*4, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*4, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*17, cuadros*4, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*5, cuadros*4, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*5, cuadros*3, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*10, cuadros*5, cuadros*3, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*14, cuadros*5, cuadros*4, cuadros])

    pygame.draw.rect(window, black, [cuadros*4, cuadros*6, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*8, cuadros*6, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*10, cuadros*6, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*6, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros*4, cuadros*7, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*7, cuadros*7, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*7, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros*4, cuadros*8, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*8, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*9, cuadros*8, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*12, cuadros*8, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*8, cuadros, cuadros])

    pygame.draw.rect(window, black, [0, cuadros*9, cuadros*7, cuadros])
    pygame.draw.rect(window, black, [cuadros*8, cuadros*9, cuadros*3, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*12, cuadros*9, cuadros*7, cuadros])

    pygame.draw.rect(window, black, [cuadros*4, cuadros*10, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*10, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*12, cuadros*10, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*10, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros*4, cuadros*11, cuadros, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*6, cuadros*11, cuadros*7, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*11, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros*4, cuadros*12, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*12, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*12, cuadros*12, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*12, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*13, cuadros*8, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*10, cuadros*13, cuadros*8, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*14, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*4, cuadros*14, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*8, cuadros*14, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*10, cuadros*14, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*14, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*17, cuadros*14, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*15, cuadros*2, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*4, cuadros*15, cuadros*11, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*16, cuadros*15, cuadros*2, cuadros])

    pygame.draw.rect(window, black, [cuadros*2, cuadros*16, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*4, cuadros*16, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*6, cuadros*16, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*12, cuadros*16, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*14, cuadros*16, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*16, cuadros*16, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*17, cuadros*4, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*6, cuadros*17, cuadros*3, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*10, cuadros*17, cuadros*3, cuadros])
    pygame.draw.rect(
        window, black, [cuadros*14, cuadros*17, cuadros*4, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*18, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*8, cuadros*18, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*10, cuadros*18, cuadros, cuadros])
    pygame.draw.rect(window, black, [cuadros*17, cuadros*18, cuadros, cuadros])

    pygame.draw.rect(window, black, [cuadros, cuadros*19, cuadros*17, cuadros])

    pygame.draw.rect(
        window, white, [cuadros*9, cuadros*8, cuadros, cuadros*0.2])

# para cuando choque con bordes del mapa


def limites_mapa(x, y, dx, dy, dxg, dyg, t):

    global desplazar_X, desplazar_Y
    desplazamiento_X = dx
    desplazamiento_Y = dy

    if t == 0:
        global desplazar_X_P, desplazar_Y_P
        desplazar_X = desplazar_X_P
        desplazar_Y = desplazar_Y_P

    else:

        desplazar_X = dxg
        desplazar_Y = dyg

    c = cuadros

    # separo cada columna de izquierda a derecha según el "X" y le permito movimientos dependiendo de dónde esté
    # si el objeto no está en las casillas designadas (!=) entonces no se permite el movimiento en X, de lo contrario sí se permite
    # si el objeto está o no está en ciertas casillas, su movimiento de izquierda a derecha se permite o se prohibe

    if (x == c):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        if (y != c*9):  # solo en ésta casilla se puede ir a izquierda y derecha, en el resto sólo derecha
            if desplazamiento_X < 0:
                desplazar_X = False

    if (x == c*2):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        if (y == c*15):  # casilla en que no se puede ir a la derecha
            if desplazamiento_X > 0:
                desplazar_X = False

    if (x == c*3):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*4):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        if (y == c*5) or (y == c*17):  # casillas en que no se puede ir a la derecha
            if desplazamiento_X > 0:
                desplazar_X = False
        if (y == c*15):  # casilla en que no se puede ir a la izquierda
            if desplazamiento_X < 0:
                desplazar_X = False

    if (x == c*5):
        if (y != c) and (y != c*3) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*6):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*7) and (y != c*9) and (y != c*11) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        # casillas en que no se puede ir a la izquierda
        if (y == c*5) or (y == c*7) or (y == c*11) or (y == c*17):
            if desplazamiento_X < 0:
                desplazar_X = False
        if (y == c*9):
            if desplazamiento_X > 0:
                desplazar_X = False

    if (x == c*7):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*7) and (y != c*11) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*8):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*7) and (y != c*11) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        # casillas que no se puede ir a la derecha
        if (y == c) or (y == c*5) or (y == c*13) or (y == c*17):
            if desplazamiento_X > 0:
                desplazar_X = False

    # columna de la mitad:
    if (x == c*9):
        if (y != c*3) and (y != c*7) and (y != c*11) and (y != c*15) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*10):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*7) and (y != c*11) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        # casillas que no se puede ir a la izquierda
        if (y == c) or (y == c*5) or (y == c*13) or (y == c*17):
            if desplazamiento_X < 0:
                desplazar_X = False

    if (x == c*11):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*7) and (y != c*11) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*12):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*7) and (y != c*9) and (y != c*11) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        # casillas en que no se puede ir a la derecha
        if (y == c*5) or (y == c*7) or (y == c*11) or (y == c*17):
            if desplazamiento_X > 0:
                desplazar_X = False
        if (y == c*9):  # casilla en que no se puede ir a la izquierda
            if desplazamiento_X < 0:
                desplazar_X = False

    if (x == c*13):
        if (y != c) and (y != c*3) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*14):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        if (y == c*5) or (y == c*17):  # casillas en que no se puede ir a la izquierda
            if desplazamiento_X < 0:
                desplazar_X = False
        if (y == c*15):  # casilla en que no se puede ir a la derecha
            if desplazamiento_X > 0:
                desplazar_X = False

    if (x == c*15):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True

    if (x == c*16):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        if (y == c*15):  # casilla en que no se puede ir a la izquierda
            if desplazamiento_X < 0:
                desplazar_X = False

    if (x == c*17):
        if (y != c) and (y != c*3) and (y != c*5) and (y != c*9) and (y != c*13) and (y != c*15) and (y != c*17) and (y != c*19):
            desplazar_X = False
        else:
            desplazar_X = True
        if (y != c*9):  # solo en ésta casilla se puede ir a izquierda y derecha, en el resto sólo izquierda
            if desplazamiento_X > 0:
                desplazar_X = False

    # ahora separo cada fila de arriba a abajo según el "Y" y le permito movimientos dependiendo de dónde esté

    if (y == c):
        if (x != c) and (x != c*4) and (x != c*8) and (x != c*10) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:  # casillas en que no se puede bajar
            desplazar_Y = True
            if desplazamiento_Y < 0:
                desplazar_Y = False

    if (y == c*2):
        if (x != c) and (x != c*4) and (x != c*8) and (x != c*10) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*3):
        if (x != c) and (x != c*4) and (x != c*6) and (x != c*8) and (x != c*10) and (x != c*12) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if (x == c*6) or (x == c*12):  # casillas en que no se puede subir
            if desplazamiento_Y < 0:
                desplazar_Y = False
        if (x == c*8) or (x == c*10):  # casillas en que no se puede bajar
            if desplazamiento_Y > 0:
                desplazar_Y = False

    if (y == c*4):
        if (x != c) and (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*5):
        if (x != c) and (x != c*4) and (x != c*6) and (x != c*8) and (x != c*10) and (x != c*12) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if (x == c*8) or (x == c*10):  # casillas en que no se puede subir
            if desplazamiento_Y < 0:
                desplazar_Y = False
        if (x == c) or (x == c*6) or (x == c*12) or (x == c*17):  # casillas en que no se puede bajar
            if desplazamiento_Y > 0:
                desplazar_Y = False

    if (y == c*6):
        if (x != c*4) and (x != c*8) and (x != c*10) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*7):
        if (x != c*4) and (x != c*6) and (x != c*8) and (x != c*10) and (x != c*12) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if (x == c*6) or (x == c*12):  # casillas en que no se puede subir
            if desplazamiento_Y < 0:
                desplazar_Y = False
        if (x == c*8) or (x == c*10):  # casillas en que no se puede bajar
            if desplazamiento_Y > 0:
                desplazar_Y = False

    if (y == c*8):
        if (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*9):
        if (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*10):
        if (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*11):
        if (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*12):
        if (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*13):
        if (x != c) and (x != c*4) and (x != c*6) and (x != c*8) and (x != c*10) and (x != c*12) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if (x == c) or (x == c*8) or (x == c*10) or (x == c*17):  # casillas en que no se puede subir
            if desplazamiento_Y < 0:
                desplazar_Y = False
        if (x == c*6) or (x == c*12):  # casillas en que no se puede bajar
            if desplazamiento_Y > 0:
                desplazar_Y = False

    if (y == c*14):
        if (x != c) and (x != c*4) and (x != c*8) and (x != c*10) and (x != c*14) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*15):
        if (x != c) and (x != c*2) and (x != c*4) and (x != c*6) and (x != c*8) and (x != c*10) and (x != c*12) and (x != c*14) and (x != c*16) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if (x == c*2) or (x == c*6) or (x == c*12) or (x == c*16):  # casillas en que no se puede subir
            if desplazamiento_Y < 0:
                desplazar_Y = False
        if (x == c) or (x == c*8) or (x == c*10) or (x == c*17):  # casillas en que no se puede bajar
            if desplazamiento_Y > 0:
                desplazar_Y = False

    if (y == c*16):
        if (x != c*2) and (x != c*4) and (x != c*6) and (x != c*12) and (x != c*14) and (x != c*16):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*17):
        if (x != c) and (x != c*2) and (x != c*4) and (x != c*6) and (x != c*8) and (x != c*10) and (x != c*12) and (x != c*14) and (x != c*16) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if (x == c) or (x == c*8) or (x == c*10) or (x == c*17):  # casillas en que no se puede subir
            if desplazamiento_Y < 0:
                desplazar_Y = False
        # casillas en que no se puede bajar
        if (x == c*2) or (x == c*4) or (x == c*6) or (x == c*12) or (x == c*14) or (x == c*16):
            if desplazamiento_Y > 0:
                desplazar_Y = False

    if (y == c*18):
        if (x != c) and (x != c*8) and (x != c*10) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True

    if (y == c*19):
        if (x != c) and (x != c*8) and (x != c*10) and (x != c*17):
            desplazar_Y = False
        else:
            desplazar_Y = True
        if desplazamiento_Y > 0:
            desplazar_Y = False

    if t == 0:
        desplazar_X_P = desplazar_X
        desplazar_Y_P = desplazar_Y

    else:
        element[5] = desplazar_X
        element[6] = desplazar_Y
        element[3] = desplazamiento_X
        element[4] = desplazamiento_Y

# puntitos


puntaje = 0

e = 0  # con esta variable y la de "existe" se sabrá si el puntito existe o ya fue agarrado
puntitos = list()  # aquí se guardan las coordenadas de cada punto

tipoMP = False  # esta variable se usará para indicar los puntitos que son megapastillas

# creamos y añadimos cada punto y sus coordenadas:

for i in range(0, 15, 1):
    xp = cuadros*1.5+(cuadros*0.5*i)
    yp = cuadros*1.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 15, 1):
    xp = cuadros*7*1.5+(cuadros*0.5*i)
    yp = cuadros*1.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 8, 1):
    xp = cuadros*1.5
    yp = cuadros*2+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 32, 1):
    xp = cuadros*4.5
    yp = cuadros*2+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 32, 1):
    xp = cuadros*14.5
    yp = cuadros*2+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 8, 1):
    xp = cuadros*17.5
    yp = cuadros*2+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*8.5
    yp = cuadros*2+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*10.5
    yp = cuadros*2+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 5, 1):
    xp = cuadros*2+(cuadros*0.5*i)
    yp = cuadros*3.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 5, 1):
    xp = cuadros*15+(cuadros*0.5*i)
    yp = cuadros*3.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 7, 1):
    xp = cuadros*5+(cuadros*0.5*i)
    yp = cuadros*3.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*9+(cuadros*0.5*i)
    yp = cuadros*3.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 7, 1):
    xp = cuadros*11+(cuadros*0.5*i)
    yp = cuadros*3.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 5, 1):
    xp = cuadros*2+(cuadros*0.5*i)
    yp = cuadros*5.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 5, 1):
    xp = cuadros*6.5+(cuadros*0.5*i)
    yp = cuadros*5.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*6.5
    yp = cuadros*4+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*12.5
    yp = cuadros*4+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 5, 1):
    xp = cuadros*10.5+(cuadros*0.5*i)
    yp = cuadros*5.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 5, 1):
    xp = cuadros*15+(cuadros*0.5*i)
    yp = cuadros*5.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 6, 1):
    xp = cuadros*1.5+(cuadros*0.5*i)
    yp = cuadros*13.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 8, 1):
    xp = cuadros*5+(cuadros*0.5*i)
    yp = cuadros*13.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 8, 1):
    xp = cuadros*10.5+(cuadros*0.5*i)
    yp = cuadros*13.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 6, 1):
    xp = cuadros*15+(cuadros*0.5*i)
    yp = cuadros*13.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*1.5
    yp = cuadros*14+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*17.5
    yp = cuadros*14+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 2, 1):
    xp = cuadros*2+(cuadros*0.5*i)
    yp = cuadros*15.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 2, 1):
    xp = cuadros*16.5+(cuadros*0.5*i)
    yp = cuadros*15.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*2.5
    yp = cuadros*16+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*16.5
    yp = cuadros*16+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 6, 1):
    xp = cuadros*1.5+(cuadros*0.5*i)
    yp = cuadros*17.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 6, 1):
    xp = cuadros*15+(cuadros*0.5*i)
    yp = cuadros*17.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 19, 1):
    xp = cuadros*5+(cuadros*0.5*i)
    yp = cuadros*15.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*8.5
    yp = cuadros*14+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*10.5
    yp = cuadros*14+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*6.5
    yp = cuadros*16+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*12.5
    yp = cuadros*16+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*7+(cuadros*0.5*i)
    yp = cuadros*17.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 4, 1):
    xp = cuadros*10.5+(cuadros*0.5*i)
    yp = cuadros*17.5

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*1.5
    yp = cuadros*18+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*8.5
    yp = cuadros*18+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*10.5
    yp = cuadros*18+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 3, 1):
    xp = cuadros*17.5
    yp = cuadros*18+(cuadros*0.5*i)

    puntitos.append([xp, yp, e, tipoMP])

for i in range(0, 33, 1):
    xp = cuadros*1.5+(cuadros*0.5*i)
    yp = cuadros*19.5

    puntitos.append([xp, yp, e, tipoMP])

# ahora creamos las megapastillas

tipoMP = True
for i in range(0, 2, 1):
    xp = cuadros*(1.5+16*i)
    yp = cuadros*2.5

    puntitos.append([xp, yp, e, tipoMP])

    xp = cuadros*(1.5+16*i)
    yp = cuadros*15.5

    puntitos.append([xp, yp, e, tipoMP])

# esta funcion se llamara para redibujar los puntos existentes

agarrados = 0


def dibujar_puntos():
    global puntaje, Mega_Pastilla_agarrada, agarrados

    # verificamos si los puntos aún existen (es decir, si el jugador aún no los ha agarrado) y se dibujan

    for element in puntitos:
        coordenada_X = element[0]
        coordenada_Y = element[1]
        tipo_MegaP = element[3]

        if (Player_X + cuadros*0.5 == coordenada_X) and (Player_Y + cuadros*0.5 == coordenada_Y):
            element[2] += 1

        if element[2] == 0:
            if tipo_MegaP == True:  # si es una megapastilla:
                pygame.draw.circle(
                    window, white, [coordenada_X, coordenada_Y], cuadros*0.142857142)
            else:  # sino:
                pygame.draw.circle(
                    window, white, [coordenada_X, coordenada_Y], cuadros*0.085714285)
        elif element[2] == 1:  # con esto se sumaran puntos una sola vez por cada punto agarrado
            element[2] += 1
            agarrados += 1

            if tipo_MegaP == True:
                puntaje += 40
                Mega_Pastilla_agarrada = True
                if agarrados % 2 != 0:
                    S_waka_1.play()
                elif agarrados % 2 == 0:
                    S_waka_2.play()
            else:
                puntaje += 10
                if agarrados % 2 != 0 and agarrados > 1:
                    S_waka_1.play()
                elif agarrados % 2 == 0:
                    S_waka_2.play()

    if agarrados == 319:
        wins()


# player (sus coordenadas y características)
Player_X = cuadros*9
Player_Y = cuadros*15
pygame.draw.rect(
    window, yellow, [Player_X, Player_Y, cuadros, cuadros], border_radius=30)
desplazamiento_X_Player = 0
desplazamiento_Y_Player = 0

# creo los fantasmas con sus caracteristicas (coordenadas y color)

ghosts = list()

# rosa naranja azul rojo
# 4    3       2    1

xg = cuadros*9
yg = cuadros*7
gcolor = red
gdesplazamiento_X = 0
gdesplazamiento_Y = 0

desplazar_X_G = True
desplazar_Y_G = True

comible = False  # variable para saber si el fantasma es comible, cuando pacman  come una megapastilla

ghosts.append([xg, yg, gcolor, gdesplazamiento_X,
              gdesplazamiento_Y, desplazar_X_G, desplazar_Y_G, comible])

for i in range(0, 3, 1):
    xg = cuadros*(8+i)
    yg = cuadros*9
    if i == 0:
        gcolor = lightskyblue
    elif i == 1:
        gcolor = orange
    else:
        gcolor = pink
    ghosts.append([xg, yg, gcolor, gdesplazamiento_X,
                  gdesplazamiento_Y, desplazar_X_G, desplazar_Y_G, comible])

for element in ghosts:
    pygame.draw.rect(window, element[2], [
                     element[0], element[1], cuadros, cuadros])

desplazamiento_X_Ghost = 0
desplazamiento_Y_Ghost = 0

# salida de los fantasmas

m1 = 0
m2 = 0
m3 = 0
m4 = 0


def salida_fantasmas(g1, g2, g3, g4):
    a = 1
    global m1, m2, m3, m4, salidaG1, salidaG2, salidaG3, salidaG4
    for element in ghosts:
        if a == 4 and g4 == True:
            if m4 < 8:
                element[0] += recorrido*-1
                m4 += 1
            elif m4 > 7 and m4 < 24:
                element[1] += recorrido*-1
                m4 += 1
            else:
                salidaG4 = False
        elif salidaG4 == False:
            m4 = 0
        if a == 3 and g3 == True:
            if m3 < 16:
                element[1] += recorrido*-1
                m3 += 1
            else:
                salidaG3 = False
        elif salidaG3 == False:
            m3 = 0
        if a == 2 and g2 == True:
            if m2 < 8:
                element[0] += recorrido
                m2 += 1
            elif m2 > 7 and m2 < 24:
                element[1] += recorrido*-1
                m2 += 1
            else:
                salidaG2 = False
        elif salidaG2 == False:
            m2 = 0
        if a == 1 and g1 == True:
            if m1 < 16:
                element[1] += recorrido*-1
                m1 += 1
            else:
                salidaG1 = False
        elif salidaG1 == False:
            m1 = 0

        a += 1


# movimiento de los fantasmas


def movimiento_fantasmas():

    d = 0  # con esto veremos si hacemos cambio de dirección
    # 0 = Horizontal y 1 = Vertical

    global f, firstX_G

    if (f == 1 and salidaG1 == False) or (f == 2 and salidaG2 == False) or (f == 3 and salidaG3 == False) or (f == 4 and salidaG4 == False):
        # si estamos en un cruce donde se puede ir tanto horizontalmente como verticalmente
        if element[3] != 0:
            firstX_G = False
        if element[4] != 0:
            firstX_G = True
        if element[5] == True and element[6] == True:
            d = random.randrange(0, 2, 1)  # sacamos un 1 o un 0

            if d == 0:  # el movimiento será horizontal
                if element[3] != 0:
                    pass
                else:
                    firstX_G = True
                    element[4] = 0
                    element[3] = random.randrange(-1, 2, 2)*recorrido
            else:  # el movimiento será vertical
                if element[4] != 0:
                    pass
                else:
                    firstX_G = False
                    element[3] = 0
                    element[4] = random.randrange(-1, 2, 2)*recorrido

    f += 1


# cuando pacman agarre una megapastilla

r = 999  # contador para definir la duración de este estado
duracion_MP = 200  # duracion del estado
combo = 1


def colision_player_fantasma():
    global r, Mega_Pastilla_agarrada, combo, S_fondo

    re = recorrido
    X = Player_X
    Y = Player_Y

    if Mega_Pastilla_agarrada == True:
        for el in ghosts:
            el[7] = True
        r = 0
        pygame.mixer.music.load("megap.wav")
        pygame.mixer.music.play(999)

        Mega_Pastilla_agarrada = False

    j = 1
    for el in ghosts:  # si la ubicacion de pacman es igual o cercana por 1-3 "recorridos" a la de un fantasma, se lo come
        for i in range(-3, 4, 1):
            if ((X == el[0]) and (Y == el[1]+re*i)) or ((Y == el[1]) and (X == el[0]+re*i)):
                if r < duracion_MP and el[7] == True:
                    comerse_un_ghost(combo, el[0], el[1])
                    if j == 1:
                        el[0] = cuadros*9
                        el[1] = cuadros*9
                        el[7] = False
                    elif j == 2:
                        el[0] = cuadros*8
                        el[1] = cuadros*9
                        el[7] = False
                    elif j == 3:
                        el[0] = cuadros*9
                        el[1] = cuadros*9
                        el[7] = False
                    elif j == 4:
                        el[0] = cuadros*10
                        el[1] = cuadros*9
                        el[7] = False

                    combo = combo*2
                else:
                    comerse_al_jugador()
        j += 1
    r += 1

    if r == duracion_MP:
        combo = 1
        for el in ghosts:
            el[7] = False

        pygame.mixer.music.load(S_fondo)
        pygame.mixer.music.play(999)


# cuando pacman se come un fantasma


def comerse_un_ghost(c, x, y):

    global puntaje

    puntos_dados = c*200

    puntaje += puntos_dados

    window.fill(darkblue)
    draw_mapa()
    dibujar_puntos()
    redibujar_ghosts()

    pygame.draw.rect(window, black, [x, y, cuadros, cuadros])

    letrero3 = texto_fuente_2.render(str(puntos_dados), True, lightskyblue)
    window.blit(letrero3, [x+cuadros*0.125, y+cuadros*0.15])

    mostrar_puntaje_y_vida(puntaje, vidas)

    S_eat.play()

    pygame.display.update()

    for i in range(0, 1, 1):
        clock.tick(2)
    clock.tick(ritmo)

# se comen al jugador


def comerse_al_jugador():
    global vidas

    pygame.mixer.music.stop()
    for i in range(0, 1, 1):
        clock.tick(1)

    S_die.play()
    window.fill(darkblue)
    draw_mapa()
    dibujar_puntos()
    mostrar_puntaje_y_vida(puntaje, vidas)

    for i in range(0, 4, 1):
        pygame.draw.circle(window, yellow, [
                           Player_X+cuadros*0.5, Player_Y+cuadros*0.5], cuadros*0.5-cuadros*0.1*i)
        pygame.display.update()
        pygame.draw.rect(window, black, [Player_X, Player_Y, cuadros, cuadros])
        clock.tick(4)

    pygame.display.update()

    for i in range(0, 3, 1):
        if i == 2 and vidas != 0:
            window.fill(black)
            pygame.display.update()
        clock.tick(1.5)
    vidas -= 1
    if vidas < 0:
        game_over()
    else:
        restart()

# redibujar los ghosts


def redibujar_ghosts():

    for element in ghosts:
        if element[7] == False:
            pygame.draw.rect(window, element[2], [
                             element[0], element[1], cuadros, cuadros])

        else:  # cuando pacman se come la megapastilla y los fantasmas están vulnerables, con esto miramos si los titilos son blancos o azules
            if (r > 150 and r < 155.6) or (r > 161.2 and r < 166.8) or (r > 172.4 and r < 178) or (r > 183.6 and r < 189.2) or (r > 194.8 and r < 200):  # titilos blancos
                pygame.draw.rect(
                    window, red, [element[0], element[1], cuadros, cuadros])
                pygame.draw.circle(window, white, [
                    element[0]+cuadros*0.5, element[1]+cuadros*0.5], cuadros/2)
            else:  # titilos azules
                pygame.draw.rect(
                    window, white, [element[0], element[1], cuadros, cuadros])
                pygame.draw.circle(window, blue, [
                    element[0]+cuadros*0.5, element[1]+cuadros*0.5], cuadros/2)

# para iniciar la partida


def start():

    window.fill(darkblue)

    pygame.mixer.Sound.play(S_iniciar)
    draw_mapa()
    dibujar_puntos()
    mostrar_puntaje_y_vida(puntaje, vidas)
    pygame.draw.rect(window, yellow, [
                     Player_X, Player_Y, cuadros, cuadros], border_radius=30)

    letrero_4 = texto_fuente_1.render("READY!", True, yellow)
    window.blit(letrero_4, [cuadros*7.1, cuadros*10.8])

    for i in range(0, 4, 1):
        pygame.display.update()
        if i == 1:
            redibujar_ghosts()
        clock.tick(0.89)

# funcion para cuando nos coman y se reinicie la partida (si aún tenemos vidas)


def restart():
    global combo, Player_X, Player_Y, desplazamiento_X_Player, desplazamiento_Y_Player, salidaG2, salidaG3, salidaG4, m1, m2, m3, m4

    Player_X = cuadros*9
    Player_Y = cuadros*15
    desplazamiento_X_Player = 0
    desplazamiento_Y_Player = 0

    z = 1  # un contador para saber cuál fantasma estamos revisando
    for element in ghosts:
        element[7] = False
        if z == 4:
            element[0] = cuadros*10
            element[1] = cuadros*9
        elif z == 3:
            element[0] = cuadros*9
            element[1] = cuadros*9
        elif z == 2:
            element[0] = cuadros*8
            element[1] = cuadros*9
        elif z == 1:
            element[0] = cuadros*9
            element[1] = cuadros*7

        z += 1
    salidaG2 = True
    salidaG3 = True
    salidaG4 = True

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0

    combo = 1

    window.fill(darkblue)
    draw_mapa()
    dibujar_puntos()
    mostrar_puntaje_y_vida(puntaje, vidas)
    pygame.draw.rect(window, yellow, [
                     Player_X, Player_Y, cuadros, cuadros], border_radius=30)
    redibujar_ghosts()
    letrero_4 = texto_fuente_1.render("READY!", True, yellow)
    window.blit(letrero_4, [cuadros*7.1, cuadros*10.8])
    pygame.display.update()

    for i in range(0, 2, 1):
        clock.tick(1)

    pygame.mixer.music.load(S_fondo)
    pygame.mixer.music.play(999)

# game over


def game_over():
    letrero_3 = texto_fuente_3.render("GAME OVER", True, red)
    window.blit(letrero_3, [cuadros*6.17, cuadros*10.75])
    pygame.display.update()
    while True:
        for i in range(0, 6, 1):
            clock.tick(1)
        sys.exit()


def wins():
    global agarrados, r, m2, m3, m4, Siren_counter, S_fondo
    pygame.mixer.music.stop()
    for i in range(0, 16, 1):
        if i > 7:
            window.fill(darkblue)
            if i % 2 == 0:
                window.fill(lightskyblue)
            draw_mapa()
            mostrar_puntaje_y_vida(puntaje, vidas)
            pygame.draw.rect(window, yellow, [
                             Player_X, Player_Y, cuadros, cuadros], border_radius=30)
            pygame.display.update()
        clock.tick(5)

    for i in range(0, 3, 1):
        if i == 2:
            window.fill(black)
            pygame.display.update()
        clock.tick(1.5)

    m2 = 0
    m3 = 0
    m4 = 0

    Siren_counter = 0
    S_fondo = "siren_11.wav"

    r = 999
    agarrados = 0
    for element in puntitos:
        element[2] = 0
    restart()


# demás
firstX = 0  # con esta variable se sabrá si la última tecla pulsada corresponde a un movimiento X o Y y saber la prioridad
firstX_G = True  # lo mismo con los fantasmas

# t con esta variable se sabrá en la funcion limites_mapa si se requiere para el jugador o un fantasma

desplazar_X = True  # usaré estas variables para permitir los movimientos tanto del jugador como de los fantasmas y no se salgan del mapa
desplazar_Y = True

desplazamiento_X = 0  # usaré estas variables para cambiar el desplazamiento tanto del jugador como de los fantasmas y no se salgan del mapa
desplazamiento_Y = 0

desplazar_X_P = True
desplazar_Y_P = True

pygame.display.update()

# usaremos estas variables para indicar cuando se comen un fantasma y éste tiene que "salir" del centro
salidaG1 = True
salidaG2 = True
salidaG3 = True
salidaG4 = True

Mega_Pastilla_agarrada = False

vidas = 2

Siren_counter = 0  # para saber cuando cambiar el sonido de fondo

start()
pygame.mixer.music.play(999)

pygame.mouse.set_visible(0)

# eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # cantidad expresada en "cuadros" que recorre el jugador
        recorrido = cuadros*0.125

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                ritmo = 5
            elif event.key == pygame.K_1:
                ritmo = 1
            elif event.key == pygame.K_3:
                ritmo = 10
            elif event.key == pygame.K_4:
                ritmo = 25

            if event.key == pygame.K_LEFT:
                desplazamiento_X_Player = recorrido*-1

                firstX = True
            elif event.key == pygame.K_RIGHT:
                desplazamiento_X_Player = recorrido

                firstX = True
            elif event.key == pygame.K_UP:
                desplazamiento_Y_Player = recorrido*-1

                firstX = False
            elif event.key == pygame.K_DOWN:
                desplazamiento_Y_Player = recorrido

                firstX = False

    draw_mapa()
    limites_mapa(Player_X, Player_Y, desplazamiento_X_Player,
                 desplazamiento_Y_Player, None, None, 0)

    # redibujar al jugador (según su desplazamiento)

    # si la última tecla pulsada corresponde a un movimiento de X
    if firstX == True:
        if desplazar_X_P == True:  # si en la casilla se permite el movimiento, se detiene Y y continúa X
            desplazamiento_Y_Player = 0
            Player_X += desplazamiento_X_Player
        if desplazar_Y_P == True:  # si no se permite (aún), se continúa Y
            Player_Y += desplazamiento_Y_Player
    # si la última tecla pulsada corresponde a un movimiento de Y
    else:
        if desplazar_Y_P == True:  # si en la casilla se permite el movimiento, se detiene X y continúa Y
            desplazamiento_X_Player = 0
            Player_Y += desplazamiento_Y_Player
        if desplazar_X_P == True:  # si no se permite (aún), se continúa X
            Player_X += desplazamiento_X_Player

    dibujar_puntos()
    mostrar_puntaje_y_vida(puntaje, vidas)

    # miramos si el jugador está pasando por el tunel, luego se redibuja según sus coordenadas

    if Player_X == (cuadros*-0.5) and desplazamiento_X_Player < 0:
        Player_X += (cuadros*18.5)
    if Player_X == (cuadros*18.5) and desplazamiento_X_Player > 0:
        Player_X += (cuadros*-18.5)

    pygame.draw.rect(
        window, yellow, [Player_X, Player_Y, cuadros, cuadros], border_radius=30)

    # ahora se mira el movimiento de los fantasmas, que estén dentro del limite y se redibujan

    # recordar que cada fantasma en la lista tiene:
    # [xg, yg, gcolor, gdesplazamiento_X, gdesplazamiento_Y, desplazar_X_G, desplazar_Y_G, comible]

    f = 1  # contador para saber qué fantasma estamos revisando
    for element in ghosts:
        limites_mapa(element[0], element[1], element[3],
                     element[4], element[5], element[6], 1)
        movimiento_fantasmas()
        limites_mapa(element[0], element[1], element[3],
                     element[4], element[5], element[6], 1)

        if firstX_G == True:
            # si en la casilla se permite el movimiento, se detiene Y y continúa X
            if element[5] == True:
                element[4] = 0
                element[0] += element[3]
            # si no se permite (aún), se continúa Y
            if element[6] == True:
                element[1] += element[4]

        # si la última tecla pulsada corresponde a un movimiento de Y
        else:
            # si en la casilla se permite el movimiento, se detiene X y continúa Y
            if element[6] == True:
                element[3] = 0
                element[1] += element[4]
            # si no se permite (aún), se continúa X
            if element[5] == True:
                element[0] += element[3]

    # con esto verificamos si los fantasmas están en posicion de "salida" para sacarlos de la "carcél"
    # una vez salgan de allí, pasarán a su movimiento normal

    # además, cuando ya no estén en posición de "salida" se toma un número random
    # para saber si van a la izquierda o derecha, y se sigue el movimiento

    z = 1  # un contador para saber cuál fantasma estamos revisando
    for element in ghosts:
        if z == 4:
            if element[0] == cuadros*10 and element[1] == cuadros*9:
                salidaG4 = True
            elif element[0] == cuadros*9 and element[1] == cuadros*7:
                salidaG4 = False
                element[3] = random.randrange(-1, 2, 2)*recorrido
        elif z == 3:
            if element[0] == cuadros*9 and element[1] == cuadros*9:
                salidaG3 = True
            elif element[0] == cuadros*9 and element[1] == cuadros*7:
                salidaG3 = False
                element[3] = random.randrange(-1, 2, 2)*recorrido
        elif z == 2:
            if element[0] == cuadros*8 and element[1] == cuadros*9:
                salidaG2 = True
            elif element[0] == cuadros*9 and element[1] == cuadros*7:
                salidaG2 = False
                element[3] = random.randrange(-1, 2, 2)*recorrido
        elif z == 1:
            if element[0] == cuadros*9 and element[1] == cuadros*9:
                salidaG1 = True
            if element[0] == cuadros*9 and element[1] == cuadros*7:
                salidaG1 = False
                element[3] = random.randrange(-1, 2, 2)*recorrido

        z += 1

    # esta funcion se llamará al inicio para que los fantasmas salgan
    salida_fantasmas(salidaG1, salidaG2, salidaG3, salidaG4)

    # miramos si un fantasma está pasando por el tunel, luego se redibuja según sus coordenadas
    for element in ghosts:
        if element[0] == (cuadros*-0.5) and element[3] < 0:
            element[0] += (cuadros*18.5)
        if element[0] == (cuadros*18.5) and element[3] > 0:
            element[0] += (cuadros*-18.5)

    redibujar_ghosts()

    pygame.display.update()

    colision_player_fantasma()

    Siren_counter += 1
    for i in range(1, 6, 1):
        if Siren_counter == 600:
            S_fondo = "siren_3.wav"
        elif Siren_counter == 1200:
            S_fondo = "siren_4.wav"
        elif Siren_counter == 1600:
            S_fondo = "siren_5.wav"
        if (r >= duracion_MP) and (Siren_counter % 600 == 0 or Siren_counter == 1600) and (Siren_counter < 1601):

            pygame.mixer.music.load(S_fondo)
            pygame.mixer.music.play(999)

    window.fill(darkblue)
    clock.tick(ritmo)
