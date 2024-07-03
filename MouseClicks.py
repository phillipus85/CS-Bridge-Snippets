"""Poner círculos cuando haga clic."""
from src.graficos import Canvas as Lienzo
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
    # texto del contador de pelotas
    pelotas_lt_txt = lienzo.crear_texto(_n_balls_pos_txt_x,
                                        _n_balls_pos_txt_y,
                                        str(_cur_len))
    # configurar la fuente del texto
    lienzo.establecer_fuente(pelotas_lt_txt, "Menlo", 48)
    # CIclo de juego
    while _playing:
        """Obtener una lista de los clics recientes y dibújalos."""
        _clicks = lienzo.obtener_nuevos_clics_mouse()
        # _tecla = lienzo.obtener_tecla_presionada()
        print(_tecla)
        # revisar los clicks del mouse para poner un circulo nuevo
        for click in _clicks:
            # obtener la posicion del click
            # IMPORTANTE: se invoca con .x y .y solo en local
            # _pos_mouse_x = click[0]
            # _pos_mouse_y = click[1]
            _pos_mouse_x = click.x
            _pos_mouse_y = click.y
            # crear la pelota con posicion, radio y color
            _pelota = lienzo.crear_ovalo(_pos_mouse_x,
                                         _pos_mouse_y,
                                         _pos_mouse_x + RADIO_PELOTA,
                                         _pos_mouse_y + RADIO_PELOTA,
                                         # _colour)
                                         fill=_colour)
            # agregar la nueva pelota a la lista
            PELOTAS_LT.append(_pelota)
        # actualizar el contador de pelotas
        if _cur_len < len(PELOTAS_LT):
            # actualizar el contador
            _cur_len = len(PELOTAS_LT)
            # actualizar el texto del contador
            lienzo.establecer_texto(pelotas_lt_txt, str(_cur_len))
        # IMPORTANTE: solo se necesita en local
        lienzo.update()


if __name__ == '__main__':
    main()
