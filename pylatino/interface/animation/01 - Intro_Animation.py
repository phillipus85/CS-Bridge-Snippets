"""
Este tutorial es el código guía para los conceptos de animación de Pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este módulo es una introducción a los conceptos de animación de Stanford en Python e incluye:
        - PARTE 1: Crear un lienzo Y una pelota para animar.
        - PARTE 2: Definir variables de juego.
        - PARTE 3: Aplicar un ciclo para crear la animación.
        - PARTE 4: Implementar detección de colisiones, rebote y como finalizar el juego.
        - PARTE 5: Terminar la animación y cerrar el lienzo.
NOTAS:
    - Principios de animacion y diseño a usar:
        - Estirar y Comprimir
        - Anticipación
        - Puesta en Escena
        - Acción Directa y Pose a Pose
        - Acciones Complementarias y Superpuestas
        - Ritmo

    - la relación entre las partes y los principios de animación son:
        - PARTE 1: Crear un lienzo Y una pelota para animar. (Puesta en Escena)
        - PARTE 2: Definir variables de juego. (Acción Directa y Pose a Pose)
        - PARTE 3: Aplicar un ciclo para crear la animación. (Ritmo)
        - PARTE 4: Implementar detección de colisiones, rebote y como finalizar el juego. (Estirar y Comprimir, Anticipación, Acciones Complementarias y Superpuestas)
        - PARTE 5: Terminar la animación y cerrar el lienzo. (Puesta en Escena)
"""
# from src.graphics import Canvas as Lienzo
# from stanfordpy.graphics import Canvas as Lienzo
from stanfordpy.graphics import Lienzo
# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo
from time import sleep as esperar

# dimeniones del lienzo
ANCHO_MAX_X = 300
ALTO_MAX_Y = 500

# Radio de la pelota.
RADIO_PELOTA = 40

# La velocidad inicial de los objetos en la dirección x.
VEL_INICIAL_X = 5

# La velocidad inicial de los objetos en la dirección y.
VEL_INICIAL_Y = 5

# Pausa entre los fotogramas, contado en segundos.
PAUSA = 1 / 60


def main():
    """main ejecuta el programa principal
    """
    # TODO PARTE 1: Crear un lienzoy y pelota
    # crear el lienzo con dimensiones
    arena = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # posicion de la pelota en el centro del lienzo
    pos_pelota_x = ANCHO_MAX_X // 2
    pos_pelota_y = ALTO_MAX_Y // 2

    # color de la pelota
    color = "azul"

    # crear la pelota con posicion, radio y color
    pelota = arena.crear_ovalo(pos_pelota_x,
                               pos_pelota_y,
                               pos_pelota_x + RADIO_PELOTA,
                               pos_pelota_y + RADIO_PELOTA,
                               color=color)

    # TODO PARTE 2: definir variables de juegoq
    # condicion para continuar el juego
    en_juego = True

    # definir la velocidad inicial de la pelota
    vel_pelota_x = VEL_INICIAL_X
    vel_pelota_y = VEL_INICIAL_Y

    # ciclo de juego
    # TODO PARTE 3: Aplicar un ciclo para crear la animación.
    while en_juego:
        # invoco la funcion moverse del lienzo
        arena.mover(pelota, vel_pelota_x, vel_pelota_y)

        # recupero la posicion de la pelota del lienzo
        pos_x = arena.obtener_x_izquierda(pelota)
        pos_y = arena.obtener_y_superior(pelota)
        # print(f"posicion x: {pos_x}, posicion y: {pos_y}")

        # pausa entre fotogramas
        esperar(PAUSA)

        # condiciones de colision
        # TODO PARTE 4: implementar detectar colisiones y rebotar.

        # 1) si choca con el borde derecho
        if pos_x > ANCHO_MAX_X - RADIO_PELOTA:
            # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
            vel_pelota_x = vel_pelota_x * -1

        # 2) si choca con el borde inferior
        if pos_y > ALTO_MAX_Y - RADIO_PELOTA:
            # ir hacia arriba, teniendo en cuenta el radio de la pelota
            vel_pelota_y = vel_pelota_y * -1
            # condicion para terminar el juego, si toca el borde inferior
            # en_juego = False

        # 3) si choca con el borde izquierdo
        if pos_x < 0.0:
            # ir hacia la derecha
            vel_pelota_x = vel_pelota_x * -1

        # 4) si choca con el borde superior
        if pos_y < 0.0:
            # ir hacia abajo
            vel_pelota_y = vel_pelota_y * -1

    # finalizar el juego
    # TODO PARTE 5: Terminar la animación y cerrar el lienzo.
    arena.crear_texto(ANCHO_MAX_X // 2,
                      ALTO_MAX_Y // 2,
                      "¡El Juego a Terminado!",
                      fuente="Arial",
                      tamano=24,
                      color="rojo",
                      ancla="center")
    esperar(5)
    # cerrar el lienzo
    # lienzo.mainloop()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
