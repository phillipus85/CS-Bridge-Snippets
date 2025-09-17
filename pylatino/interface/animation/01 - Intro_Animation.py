"""
Este tutorial es el código guía para los conceptos de animación de Pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este módulo es una introducción a los conceptos de animación de Stanford en Python e incluye:
        - PARTE 1: Crear un lienzo (Función Lienzo()).
        - PARTE 2: Dibujar formas un círculo (función crear_ovalo()) para simular una pelota.
        - PARTE 3: Aplicar geometría (Centrar elementos en el lienzo).
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
VELOCIDAD_PELOTA_X = 5

# La velocidad de la pelota en la dirección y.
VELOCIDAD_PELOTA_Y = 5

# dimeniones del lienzo
MAX_CANVAS_X = 460
MAX_CANVAS_Y = 500


def main():
    """main ejecuta el programa principal
    """
    # TODO PARTE 1: Crear un lienzo.
    # crear el lienzo con dimensiones
    arena = Lienzo(MAX_CANVAS_X, MAX_CANVAS_Y)
    # TODO PARTE 2: Dibujar formas básicas (círculos).
    # posicionar la pelota en el centro del lienzo
    _poss_ball_x = MAX_CANVAS_X // 2
    _poss_ball_y = MAX_CANVAS_Y // 2
    # color de la pelota
    _colour = "violet"
    # _colour = arena.get_random_color()
    # crear la pelota con posicion, radio y color
    # IMPORTANTE: en local el color es con fill, en WEB IDE es una propiedad
    # TODO PARTE 3: Aplicar geometría (Centrar elementos en el lienzo).
    pelota = arena.create_oval(_poss_ball_x,
                               _poss_ball_y,
                               _poss_ball_x + RADIO_PELOTA,
                               _poss_ball_y + RADIO_PELOTA,
                               # _colour)
                               color=_colour)
    # condicion para continuar el juego
    _playing = True

    # definir la velocidad inicial de la pelota
    _dx = VELOCIDAD_PELOTA_X
    _dy = VELOCIDAD_PELOTA_Y
    # ciclo de juego
    # TODO PARTE 5: Aplicar un bucle para crear la animación.
    while _playing:
        # invoco la funcion moverse del lienzo
        arena.move(pelota, _dx, _dy)
        # recupero la posicion de la pelota del lienzo
        _tx = arena.get_left_x(pelota)
        _ty = arena.get_top_y(pelota)
        print(f"posicion x: {_tx}, posicion y: {_ty}")
        # IMPORTANTE: en local los nombres de las funciones son diferentes
        # _tx = arena.obtener_x_izq(pelota)
        # _ty = arena.obtener_y_sup(pelota)
        # pausa entre fotogramas
        esperar(PAUSA)
        # condicion de colision
        # TODO PARTE 6: Aplicar condiciones para detectar colisiones y rebotar.
        # 1) si colisiona con el borde derecho
        if _tx > MAX_CANVAS_X - RADIO_PELOTA:
            # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
            _dx = _dx * -1
            # crash = True

        # 2) si colisiona con el borde inferior
        if _ty > MAX_CANVAS_Y - RADIO_PELOTA:
            # ir hacia arriba, teniendo en cuenta el radio de la pelota
            _dy = _dy * -1
            # crash = True

        # 3) si colisiona con el borde izquierdo
        if _tx < 0.0:
            # ir hacia la derecha
            _dx = _dx * -1
            # crash = True

        # 4) si colisiona con el borde superior
        if _ty < 0.0:
            # ir hacia abajo
            _dy = _dy * -1
            # crash = True
        # actualizar el lienzo
        # IMPORTANTE: solo se necesita en local
        # lienzo.update()
        # condicion para terminar el juego
        # TODO PARTE 7: Terminar la animación y cerrar el lienzo.
        # if crash:
    # cerrar el lienzo
    # lienzo.mainloop()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
