"""Crear una pelota y hacerla rebotar en la pared."""
from src.graphics import Canvas as Lienzo
# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo
from time import sleep as esperar

# Radio de la pelota.
RADIO_PELOTA = 20

# Pausa entre los fotogramas, en segundos.
PAUSA = 0.02

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
    # Crear el lienzo
    lienzo = Lienzo(MAX_CANVAS_X, MAX_CANVAS_Y)
    # posicionar la pelota en el centro del lienzo
    _poss_ball_x = MAX_CANVAS_X // 2
    _poss_ball_y = MAX_CANVAS_Y // 2
    # color de la pelota
    _colour = "blue"
    # crear la pelota con posicion, radio y color
    # IMPORTANTE: en local el color es con fill, en WEB IDE es una propiedad
    pelota = lienzo.create_oval(_poss_ball_x,
                                _poss_ball_y,
                                _poss_ball_x + RADIO_PELOTA,
                                _poss_ball_y + RADIO_PELOTA,
                                # _colour)
                                fill=_colour)
    # condicion para continuar el juego
    _playing = True
    crash = False
    # definir la velocidad inicial de la pelota
    _dx = VELOCIDAD_PELOTA_X
    _dy = VELOCIDAD_PELOTA_Y
    # ciclo de juego
    while _playing and not crash:
        # invoco la funcion moverse del lienzo
        lienzo.move(pelota, _dx, _dy)
        # recupero la posicion de la pelota del lienzo
        _tx = lienzo.get_left_x(pelota)
        _ty = lienzo.get_top_y(pelota)
        # IMPORTANTE: en local los nombres de las funciones son diferentes
        # _tx = lienzo.obtener_x_izq(pelota)
        # _ty = lienzo.obtener_y_sup(pelota)
        # pausa entre fotogramas
        esperar(PAUSA)
        # condicion de colision
        # 1) si colisiona con el borde derecho
        if _tx >= MAX_CANVAS_X - RADIO_PELOTA:
            # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
            _dx = _dx * -1
            # crash = True

        # 2) si colisiona con el borde inferior
        if _ty >= MAX_CANVAS_Y - RADIO_PELOTA:
            # ir hacia arriba, teniendo en cuenta el radio de la pelota
            _dy = _dy * -1
            # crash = True

        # 3) si colisiona con el borde izquierdo
        if _tx <= 0.0:
            # ir hacia la derecha
            _dx = _dx * -1
            # crash = True

        # 4) si colisiona con el borde superior
        if _ty <= 0.0:
            # ir hacia abajo
            _dy = _dy * -1
            # crash = True
        # actualizar el lienzo
        # IMPORTANTE: solo se necesita en local
        lienzo.update()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
