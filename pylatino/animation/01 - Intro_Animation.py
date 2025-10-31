"""
Este tutorial es el código guía para los conceptos de animación de Pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este módulo es una introducción a los conceptos de animación de Stanford en Python e incluye:
        - PARTE 1: Crear un lienzo (Función Lienzo()).
        - PARTE 2: Dibujar formas un círculo (función crear_ovalo()) para simular una pelota.
        - PARTE 3: Aplicar geometría (Centrar elementos en el lienzo).
        PARTE 1, 2, 3 REPETIVIOO, YA ESTA LISTO EN OTRO TUTORIAL

        - PARTE 4: Modificar elementos, cambio de posición (función mover())
        - PARTE 5: Aplicar un bucle para crear la animación.
        - PARTE 6: Aplicar condiciones para detectar colisiones y rebotar.
        - PARTE 7: terminar la animación y cerrar el lienzo, seleccionar una pared al azar, resaltar con un color y si colisionan terminar el juego.

NOTAS:
    - Principios de dibujo y diseño a usar:
        - Uso de formas
        - Manejo de colores
        - Composición
        - Movimiento

    - Las partes del tutorial están relacionadas con los principios de dibujo y diseño:
        PARTE 1, PARTE 2 y PARTE 3 están relacionadas con el uso de formas, manejo de colores y composición.
        PARTE 4, PARTE 5 y PARTE 6 están relacionadas con el manejo de colores, composición y movimiento.

    - Retratar a Karel es el ejercicio final para aplicar todos los conceptos aprendidos en las partes anteriores.
    - El código está comentado para facilitar la comprensión de los conceptos.
"""
# from src.graphics import Canvas as Lienzo
# from stanfordpy.graphics import Canvas as Lienzo
from stanfordpy.graphics import Lienzo
# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo
from time import sleep as esperar

# Radio de la pelota.
RADIO_PELOTA = 40

# Pausa entre los fotogramas, en segundos.
PAUSA = 1 / 60

# La velocidad de la pelota en la dirección x.
VEL_PELOTA_X = -5

# La velocidad de la pelota en la dirección y.
VEL_PELOTA_Y = -5

# dimeniones del lienzo
ANCHO_MAX_X = 500
ALTO_MAX_Y = 800


def main():
    """main ejecuta el programa principal
    """
    # TODO PARTE 1: Crear un lienzo.
    # crear el lienzo con dimensiones
    arena = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)
    # TODO PARTE 2: Dibujar formas básicas (círculos).
    # posicionar la pelota en el centro del lienzo
    pos_pelota_x = ANCHO_MAX_X // 2
    pos_pelota_y = ALTO_MAX_Y // 2
    # color de la pelota
    color = "azul"

    # color = arena.get_random_color()
    # crear la pelota con posicion, radio y color
    # IMPORTANTE: en local el color es con fill, en WEB IDE es una propiedad
    # TODO PARTE 3: Aplicar geometría (Centrar elementos en el lienzo).
    pelota = arena.crear_ovalo(pos_pelota_x,
                               pos_pelota_y,
                               pos_pelota_x + RADIO_PELOTA,
                               pos_pelota_y + RADIO_PELOTA,
                               color=color)
    # condicion para continuar el juego
    en_juego = True

    # definir la velocidad inicial de la pelota
    _dx = VEL_PELOTA_X
    _dy = VEL_PELOTA_Y
    # ciclo de juego
    # TODO PARTE 5: Aplicar un bucle para crear la animación.
    while en_juego:
        # invoco la funcion moverse del lienzo
        arena.mover(pelota, _dx, _dy)
        # recupero la posicion de la pelota del lienzo
        _px = arena.get_left_x(pelota)
        _py = arena.get_top_y(pelota)
        # print(f"posicion x: {_px}, posicion y: {_py}")

        # pausa entre fotogramas
        esperar(PAUSA)

        # condicion de colision
        # TODO PARTE 6: Aplicar condiciones para detectar colisiones y rebotar.
        # 1) si colisiona con el borde derecho
        if _px > ANCHO_MAX_X - RADIO_PELOTA:
            # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
            _dx = _dx * -1

        # 2) si colisiona con el borde inferior
        if _py > ALTO_MAX_Y - RADIO_PELOTA:
            # ir hacia arriba, teniendo en cuenta el radio de la pelota
            _dy = _dy * -1
            # condicion para terminar el juego, si toca el borde inferior
            en_juego = False

        # 3) si colisiona con el borde izquierdo
        if _px < 0.0:
            # ir hacia la derecha
            _dx = _dx * -1

        # 4) si colisiona con el borde superior
        if _py < 0.0:
            # ir hacia abajo
            _dy = _dy * -1

        # actualizar el lienzo
        # IMPORTANTE: solo se necesita en local
        # lienzo.update()

    # finalizar el juego
    # TODO PARTE 7: Terminar la animación y cerrar el lienzo.
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
