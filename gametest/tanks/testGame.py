from ...src.graphics import Canvas as Lienzo

from random import randint
import random
from time import sleep as esperar


ANCHURA_LIENZO = 640
ALTURA_LIENZO = 360

TAMAÑO_TANQUES = 40
ESPACIO_BORDE_ARRIBA = 45

ANCHO_BORDE = 10

CENTRO_X_CAMPO_JUEGO = (ALTURA_LIENZO - (ANCHO_BORDE * 2 - ESPACIO_BORDE_ARRIBA)) / 2
ALTO_OBS = ALTURA_LIENZO / 6.5
ANCHO_OBS = ALTO_OBS / 2.5
DISTANCI_OBS_BORDES_HORIZONTALES = 70
POCISIONTANQUEROJO = ANCHURA_LIENZO * 9 / 10
POCISIONTANQUEAZUL = ANCHURA_LIENZO / 10 - TAMAÑO_TANQUES


def main():
    lienzo = Lienzo(ANCHURA_LIENZO, ALTURA_LIENZO)
    crearfondo(lienzo)
    crearborde(lienzo)
    crearobstaculos(lienzo)
    red = creartanquerojo(lienzo)
    blue = creartanqueazul(lienzo)
    juego = True

    while juego:

        # azul moverse
        esperar(0.1)
        # tecla = lienzo.obtener_ultimo_clic_teclado()
        tecla = lienzo.obtener_nuevos_clics_teclado()
        # print(prueba)
        # mover azul !!!
        print(tecla)
        izq = lienzo.obtener_x_izq(blue)
        arriba = lienzo.obtener_y_sup(blue)
        x_izq = izq     # Coordenada x izquierda de la pelota.
        y_sup = arriba      # Coordenada y superior de la pelota.
        x_der = izq + TAMAÑO_TANQUES        # Coordenada x derecha de la pelota.
        y_inf = arriba + TAMAÑO_TANQUES     # Coordenada y inferior de la pelota.

        if "d" in tecla:
            blue = lienzo.eliminar(blue)
            blue = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                  CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                  TAMAÑO_TANQUES,
                                                  TAMAÑO_TANQUES,
                                                  "Blue_Tank_Right.png")
            lienzo.moverse_hacia(blue, x_izq + 3, y_sup)

        if "w" in tecla:
            blue = lienzo.eliminar(blue)
            blue = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                  CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                  TAMAÑO_TANQUES,
                                                  TAMAÑO_TANQUES,
                                                  "Blue_Tank_Up.png")
            lienzo.moverse_hacia(blue, x_izq, y_sup - 3)

        if "a" in tecla:
            blue = lienzo.eliminar(blue)
            blue = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                  CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                  TAMAÑO_TANQUES,
                                                  TAMAÑO_TANQUES,
                                                  "Blue_Tank.png")
            lienzo.moverse_hacia(blue, x_izq - 3, y_sup)

        if "s" in tecla:
            blue = lienzo.eliminar(blue)
            blue = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                  CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                  TAMAÑO_TANQUES,
                                                  TAMAÑO_TANQUES,
                                                  "Blue_Tank_Down.png")
            lienzo.moverse_hacia(blue, x_izq, y_sup + 3)

        # mover rojo !!!
        print(tecla)
        izq = lienzo.obtener_x_izq(red)
        arriba = lienzo.obtener_y_sup(red)
        x_izq = izq  # Coordenada x izquierda de la pelota.
        y_sup = arriba  # Coordenada y superior de la pelota.
        x_der = izq + TAMAÑO_TANQUES  # Coordenada x derecha de la pelota.
        y_inf = arriba + TAMAÑO_TANQUES  # Coordenada y inferior de la pelota.

        if "ArrowRight" in tecla:
            red = lienzo.eliminar(red)
            red = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                 CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                 TAMAÑO_TANQUES,
                                                 TAMAÑO_TANQUES,
                                                 "Red_Tank_Right.png")
            lienzo.moverse_hacia(red, x_izq + 3, y_sup)

        if "ArrowUp" in tecla:
            red = lienzo.eliminar(red)
            red = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                 CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                 TAMAÑO_TANQUES,
                                                 TAMAÑO_TANQUES,
                                                 "Red_Tank_Up.png")
            lienzo.moverse_hacia(red, x_izq, y_sup - 3)

        if "ArrowLeft" in tecla:

            red = lienzo.eliminar(red)
            red = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                 CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                 TAMAÑO_TANQUES,
                                                 TAMAÑO_TANQUES,
                                                 "Red_Tank.png")

            lienzo.moverse_hacia(red, x_izq - 3, y_sup)

        if "ArrowDown" in tecla:
            red = lienzo.eliminar(red)
            red = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                                 CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                                 TAMAÑO_TANQUES,
                                                 TAMAÑO_TANQUES,
                                                 "Red_Tank_Down.png")

            lienzo.moverse_hacia(red, x_izq, y_sup + 3)

    # Creamos el tanque rojo
    imagen = lienzo.crear_imagen_con_tamaño(ANCHURA_LIENZO / 5,
                                            ALTURA_LIENZO / 2 - TAMAÑO_TANQUES / 2,
                                            TAMAÑO_TANQUES,
                                            TAMAÑO_TANQUES,
                                            "Red_Tank.png")


# crear obstaculos
def crearobstaculos(lienzo):

    color = "#D68722"

    obstaculo_arriba = lienzo.crear_rectangulo(ANCHURA_LIENZO / 2 - ANCHO_OBS / 2,
                                               (CENTRO_X_CAMPO_JUEGO - DISTANCI_OBS_BORDES_HORIZONTALES) - ALTO_OBS / 2,
                                               ANCHURA_LIENZO / 2 + ANCHO_OBS / 2,
                                               (CENTRO_X_CAMPO_JUEGO - DISTANCI_OBS_BORDES_HORIZONTALES) + ALTO_OBS / 2,
                                               color)
    obstaculo_abajo = lienzo.crear_rectangulo(ANCHURA_LIENZO / 2- ANCHO_OBS / 2,
                                              (ALTURA_LIENZO - DISTANCI_OBS_BORDES_HORIZONTALES - ANCHO_BORDE) - ALTO_OBS / 2,
                                              ANCHURA_LIENZO / 2 + ANCHO_OBS / 2,
                                              (ALTURA_LIENZO - DISTANCI_OBS_BORDES_HORIZONTALES - ANCHO_BORDE) + ALTO_OBS /2,
                                              color)
    obstaculo_izquierda = lienzo.crear_rectangulo(ANCHURA_LIENZO / 4 - ALTO_OBS/2 + 50,
                                                  CENTRO_X_CAMPO_JUEGO - ANCHO_OBS / 2,
                                                  ANCHURA_LIENZO / 4 + ALTO_OBS / 2 + 50,
                                                  CENTRO_X_CAMPO_JUEGO + ANCHO_OBS / 2,
                                                  color)
    obstaculo_izquierda = lienzo.crear_rectangulo(3*ANCHURA_LIENZO / 4 - ALTO_OBS / 2 - 50,
                                                  CENTRO_X_CAMPO_JUEGO - ANCHO_OBS / 2,
                                                  3 * ANCHURA_LIENZO / 4 + ALTO_OBS / 2 - 50,
                                                  CENTRO_X_CAMPO_JUEGO + ANCHO_OBS / 2, color)


# Funcion que delimita el area de juego, #B0670B, #D68722
def crearborde(lienzo):
    color = "#D68722"
    superior = lienzo.crear_rectangulo(0,
                                       ESPACIO_BORDE_ARRIBA,
                                       ANCHURA_LIENZO,
                                       ESPACIO_BORDE_ARRIBA + ANCHO_BORDE,
                                       color)

    izquierdo = lienzo.crear_rectangulo(0,
                                        ESPACIO_BORDE_ARRIBA,
                                        ANCHO_BORDE,
                                        ALTURA_LIENZO,
                                        color)

    inferior = lienzo.crear_rectangulo(0,
                                       ALTURA_LIENZO - ANCHO_BORDE,
                                       ANCHURA_LIENZO,
                                       ALTURA_LIENZO,
                                       color)

    derecha = lienzo.crear_rectangulo(ANCHURA_LIENZO - ANCHO_BORDE,
                                      ESPACIO_BORDE_ARRIBA,
                                      ANCHURA_LIENZO,
                                      ALTURA_LIENZO,
                                      color)


# Funcion pr crear fondo, #A7F219, "#B7BF30"
def crearfondo(lienzo):
    color = "#A7F219"
    fondo = lienzo.crear_rectangulo(0,
                                    0,
                                    ANCHURA_LIENZO,
                                    ALTURA_LIENZO,
                                    color)
    return fondo

def creartanquerojo(lienzo):
    imagen = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEROJO,
                                            CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                            TAMAÑO_TANQUES,
                                            TAMAÑO_TANQUES,
                                            "Red_Tank.png")

    return imagen


def creartanqueazul(lienzo):
    imagen = lienzo.crear_imagen_con_tamaño(POCISIONTANQUEAZUL,
                                            CENTRO_X_CAMPO_JUEGO - TAMAÑO_TANQUES / 2,
                                            TAMAÑO_TANQUES,
                                            TAMAÑO_TANQUES,
                                            "Blue_Tank_Right.png")
    return imagen


if __name__ == "__main__":
    main()
