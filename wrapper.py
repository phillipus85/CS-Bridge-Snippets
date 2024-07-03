"""Poner círculos cuando haga clic."""
from src.graphics import Canvas as Lienzo
from time import sleep as esperar
# from src.graphics import Canvas as Lienzo
# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo


# dimeniones del lienzo
MAX_CANVAS_X = 460
MAX_CANVAS_Y = 500

# Radio de la pelota.
RADIO_PELOTA = 20

# lista de pelotas
PELOTAS_LT = list()


def main():
    # crear el lienzo
    lienzo = Lienzo(MAX_CANVAS_X, MAX_CANVAS_Y)
    # se define el color de la pelota
    _colour = "blue"
    # condicion para continuar el juego
    _playing = True
    # contador de pelotas
    _cur_len = len(PELOTAS_LT)
    # posicion del texto del contador de pelotas
    _n_balls_pos_txt_x = MAX_CANVAS_X // 2
    _n_balls_pos_txt_y = MAX_CANVAS_Y // 2

    while _playing:
        # print(_n_balls_pos_txt_x, _n_balls_pos_txt_y)
        lienzo.establecer_color_fondo_lienzo("black")
        esperar(0.02)
        # IMPORTANTE: solo se necesita en local
        lienzo.update()


if __name__ == '__main__':
    main()
