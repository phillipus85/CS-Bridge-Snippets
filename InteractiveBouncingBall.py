"""Crear una pelota y hacerla rebotar en la pared."""
from src.graphics import Canvas as Lienzo
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

# lista de pelotas
PELOTAS_LT = list()


def detectar_clicks(canvas):
    """detectar_clicks() detecta los clicks del mouse en el lienzo.

    Args:
        canvas (Lienzo): es el espacio de dibujo interactivo.

    Returns:
        list: una lista de los clicks del mouse.
    """
    _clicks = canvas.obtener_nuevos_clics_mouse()
    return _clicks


def crear_pelota(canvas, lista, click, radio, color):
    """crear_pelota() crea una pelota en el lienzo.

    Args:
        canvas (Lienzo): es el espacio de dibujo interactivo.
        lista (list): lista de pelotas generadas y guardadas en el lienzo.
        click (<ButtonPress): evento de click del mouse con coordenadas.
        radio (int): radio de la pelota.
        color (str): nombre del color de la pelota.
    """
    # obtener la posicion del click
    # IMPORTANTE: se invoca con .x y .y solo en local
    # _x = click[0]
    # _y = click[1]
    _x = click.x
    _y = click.y
    # IMPORTANTE: en local el color es con fill, en WEB IDE es una propiedad
    # crear la pelota con posicion, radio y color
    _pelota = canvas.crear_ovalo(_x,
                                 _y,
                                 _x + radio,
                                 _y + radio,
                                 # color)
                                 fill=color)
    # agregar la nueva pelota a la lista
    lista.append(_pelota)


def mover_objeto(canvas, objeto, dx, dy):
    """mover_objeto() mueve el objeto en el lienzo.

    Args:
        canvas (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.
        dx (int): es el desplazamiento en x.
        dy (int): es el desplazamiento en y.
    """
    canvas.moverse(objeto, dx, dy)


def obtener_posicion_objeto(canvas, objeto):
    """obtener_posicion_objeto() obtiene la posición de la objeto en el lienzo.

    Args:
        canvas (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.

    Returns:
        tuple: una tupla con la posición del objeto.
    """
    _tx = canvas.obtener_x_izquierda(objeto)
    _ty = canvas.obtener_top_y(objeto)
    # IMPORTANTE: en local los nombres de las funciones son diferentes
    # _tx = canvas.obtener_x_izq(objeto)
    # _ty = canvas.obtener_y_sup(objeto)
    return (_tx, _ty)


def verificar_colision_extremos(tx, ty, dx, dy):
    """verificar_colision_extremos() verifica la colisión con los extremos.
    Args:
        tx (float): posición x del objeto.
        ty (float): posición y del objeto.
        dx (int): desplazamiento en x.
        dy (int): desplazamiento en y.
    """
    # condicion de colision
    # 1) si colisiona con el borde derecho
    if tx >= MAX_CANVAS_X - RADIO_PELOTA:
        # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
        dx = dx * -1
    # 2) si colisiona con el borde inferior
    if ty >= MAX_CANVAS_Y - RADIO_PELOTA:
        # ir hacia arriba, teniendo en cuenta el radio de la pelota
        dy = dy * -1
    # 3) si colisiona con el borde izquierdo
    if tx <= 0.0:
        # ir hacia la derecha
        dx = dx * -1
    # 4) si colisiona con el borde superior
    if ty <= 0.0:
        # ir hacia abajo
        dy = dy * -1
    # retornar las nuevas velocidades
    return (dx, dy)


def main():
    """main ejecuta el programa principal
    """
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
    # crear lista de las velocidades de las pelotas
    _vel_pelotas_lt = list()
    # definir la velocidad inicial de la pelota
    _dx = VELOCIDAD_PELOTA_X
    _dy = VELOCIDAD_PELOTA_Y
    # ciclo de juego
    while _playing:

        # obtener los clicks del mouse
        _clicks = detectar_clicks(lienzo)
        # ciclo para dibujar las pelotas con los clicks del mouse
        for click in _clicks:
            # print(click)
            crear_pelota(lienzo, PELOTAS_LT, click, RADIO_PELOTA, _colour)
            # crear tupla de velocidades de las pelotas
            _tv = (_dx, _dy)
            # agregar la nueva velocidad a la lista
            _vel_pelotas_lt.append(_tv)

        # ciclo de movimiento de las pelotas
        idx = 0
        for pelota, vel in zip(PELOTAS_LT, _vel_pelotas_lt):
            # mueve la pelota
            _dx, _dy = vel
            mover_objeto(lienzo, pelota, _dx, _dy)
            lienzo.moverse(pelota, _dx, _dy)
            # recupera la posicion de la pelota del lienzo
            _tx, _ty = obtener_posicion_objeto(lienzo, pelota)
            # verifica colision con los extremos del lienzo
            _dx, _dy = verificar_colision_extremos(_tx, _ty, _dx, _dy)
            _vel_pelotas_lt[idx] = (_dx, _dy)
            idx += 1

        # actualizar el contador de pelotas
        if _cur_len < len(PELOTAS_LT):
            # actualizar el contador
            _cur_len = len(PELOTAS_LT)
            # actualizar el texto del contador
            lienzo.establecer_texto(pelotas_lt_txt, str(_cur_len))

        # pausa entre fotogramas
        esperar(PAUSA)
        # actualizar el lienzo
        # IMPORTANTE: solo se necesita en local
        lienzo.update()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
