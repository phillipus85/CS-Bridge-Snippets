"""
Este tutorial es el código guía para los conceptos de animación de Pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este módulo es una introducción a los conceptos de animación de Stanford en Python e incluye:
        - PARTE 1: Escribir funcion para crear la pelota y las paletas.
        - PARTE 2: Escribir funcion para mover la pelota y las paletas.
        - PARTE 3: Crear funcion para detectar colisiones y rebotar.
        - PARTE 4: Escribir funcion para obtener la posición de los objetos.
        - PARTE 5: Implementar como finalizar el juego.

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
DIAMETRO_PELOTA = 40

# dimensiones de la paleta
LARGO_PALETA = 60
ALTO_PALETA = 20

# La velocidad inicial de los objetos en la dirección x.
VEL_INICIAL_X = 5

# La velocidad inicial de los objetos en la dirección y.
VEL_INICIAL_Y = 5

# Pausa entre los fotogramas, contado en segundos.
PAUSA = 1 / 60


def crear_pelota(lienzo: Lienzo,
                 pos_x: int,
                 pos_y: int,
                 radio: int,
                 color_fig: str,
                 contorno_fig: str) -> int:
    """crear_pelota crea una pelota en el lienzo dado.

    Args:
        lienzo (Lienzo): El lienzo donde se crea la pelota.
        pos_x (int): La posición x inicial de la pelota.
        pos_y (int): La posición y inicial de la pelota.
        radio (int): El radio de la pelota.
        color_fig (str): El color de la pelota.

    Returns:
        objeto_pelota (int): El objeto pelota creado en el lienzo.
    """
    pelota = lienzo.crear_ovalo(pos_x,
                                pos_y,
                                pos_x + radio,
                                pos_y + radio,
                                color=color_fig,
                                contorno=contorno_fig)
    return pelota


def crear_paleta(lienzo: Lienzo,
                 pos_x: int,
                 pos_y: int,
                 largo: int,
                 alto: int,
                 color_fig: str,
                 contorno_fig: str) -> int:
    """crear_paleta crea una paleta en el lienzo dado.

    Args:
        lienzo (Lienzo): El lienzo donde se crea la paleta.
        pos_x (int): La posición x inicial de la paleta.
        pos_y (int): La posición y inicial de la paleta.
        largo (int): El largo de la paleta.
        alto (int): El alto de la paleta.
        color_fig (str): El color de la paleta.
        contorno_fig (str): El color del contorno de la paleta.

    Returns:
        objeto_paleta (int): El objeto paleta creado en el lienzo.
    """
    paleta = lienzo.crear_rectangulo(pos_x,
                                     pos_y,
                                     pos_x + largo,
                                     pos_y + alto,
                                     color=color_fig,
                                     contorno=contorno_fig)
    return paleta


def obtener_posicion_objeto(lienzo: Lienzo, objeto: str) -> tuple:
    """obtener_posicion obtiene la posición (x, y) del objeto en el lienzo.

    Args:
        lienzo (Lienzo): El lienzo donde se encuentra el objeto.
        objeto (str): ID del objeto en el lienzo.

    Returns:
        tuple: una tupla con la posición (x, y) del objeto.
    """
    x = lienzo.obtener_x_izquierda(objeto)
    y = lienzo.obtener_y_superior(objeto)
    # return x, y
    return (x, y)


def mover_objeto(lienzo: Lienzo, objeto: str, dx: int, dy: int) -> None:
    """mover_objeto() mueve el objeto en el lienzo.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.
        dx (int): es el desplazamiento en x.
        dy (int): es el desplazamiento en y.
    """
    lienzo.moverse(objeto, dx, dy)


def verificar_colisiones_arena(lienzo: Lienzo,
                               objeto: str,
                               pos_x: float,
                               pos_y: float,
                               vel_x: int,
                               vel_y: int,
                               activo: bool) -> tuple:
    """verificar_colisiones_arena() verifica la colisión con los extremos del lienzo.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.
        pos_x (float): posición x del objeto.
        pos_y (float): posición y del objeto.
        vel_x (int): desplazamiento en x.
        vel_y (int): desplazamiento en y.
        activo (bool): indica si el objeto está activo.

    Returns:
        tuple: una tupla con las nuevas velocidades y el estado activo del objeto (vel_x, vel_y, activo).
    """
    ancho_lienzo = lienzo.obtener_anchura_lienzo()
    alto_lienzo = lienzo.obtener_altura_lienzo()
    largo_objeto = lienzo.obtener_ancho(objeto)
    alto_objeto = lienzo.obtener_altura(objeto)

    # 1) si choca con el borde derecho
    if pos_x > ancho_lienzo - largo_objeto:
        vel_x = vel_x * -1

    # 2) si choca con el borde inferior
    if pos_y > alto_lienzo - alto_objeto:
        vel_y = vel_y * -1
        vel_y = 0
        vel_x = 0
        activo = False

    # 3) si choca con el borde izquierdo
    if pos_x < 0.0:
        vel_x = vel_x * -1

    # 4) si choca con el borde superior
    if pos_y < 0.0:
        vel_y = vel_y * -1

    return (vel_x, vel_y, activo)


def verificar_colisiones_objetos(lienzo: Lienzo, objeto: str) -> list:
    x_izq = lienzo.obtener_x_izq(objeto)
    y_sup = lienzo.obtener_y_sup(objeto)
    ancho = lienzo.obtener_ancho(objeto)
    alto = lienzo.obtener_altura(objeto)
    colisiones = lienzo.encontrar_superposiciones(x_izq,
                                                  y_sup,
                                                  x_izq + ancho,
                                                  y_sup + alto)
    colisiones = list(colisiones)
    return colisiones



def main():
    """main ejecuta el programa principal
    """
    # TODO PARTE 1: Crear un lienzo y disco
    # crear el lienzo con dimensiones
    arena = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # posicion de la disco en el centro del lienzo
    p_disco_x = ANCHO_MAX_X // 2
    p_disco_y = ALTO_MAX_Y // 2

    # color de la disco
    color_disco = "azul"
    # contorno de la disco
    contorno = "verde"

    # crear la disco con posicion, radio y color
    disco = crear_pelota(arena,
                          p_disco_x,
                          p_disco_y,
                          DIAMETRO_PELOTA,
                          color_disco,
                          contorno)

    # TODO PARTE 2: definir variables de juegoq
    # condicion para continuar el juego
    en_juego = True

    # definir la velocidad inicial de la disco
    v_disco_x = VEL_INICIAL_X
    v_disco_y = VEL_INICIAL_Y

    # posicion inicial de la paleta uno
    p_pala_a_x = (ANCHO_MAX_X - LARGO_PALETA) // 2
    p_pala_a_y = ALTO_MAX_Y - ALTO_PALETA - 10

    # crear la paleta uno
    pala_a = crear_paleta(arena,
                          p_pala_a_x,
                          p_pala_a_y,
                          LARGO_PALETA,
                          ALTO_PALETA,
                          color_fig="negro",
                          contorno_fig="celeste")

    # posicion inicial de la paleta dos
    p_pala_b_x = (ANCHO_MAX_X - LARGO_PALETA) // 2
    p_pala_b_y = 10
    # crear la paleta dos
    pala_b = crear_paleta(arena,
                          p_pala_b_x,
                          p_pala_b_y,
                          LARGO_PALETA,
                          ALTO_PALETA,
                          color_fig="negro",
                          contorno_fig="rojo")

    v_pala_b_x = 3
    v_pala_b_y = 0

    # ciclo de juego
    # TODO PARTE 3: Aplicar un ciclo para crear la animación.
    while en_juego:
        # invoco la funcion moverse del lienzo
        mover_objeto(arena, disco, v_disco_x, v_disco_y)

        # recupero la posicion de la disco del lienzo
        p_disco_x, p_disco_y = obtener_posicion_objeto(arena,
                                                       disco)

        # condiciones de colision
        # TODO PARTE 4: implementar detectar colisiones y rebotar.
        v_disco_x, v_disco_y, en_juego = verificar_colisiones_arena(arena,
                                                                    disco,
                                                                    p_disco_x,
                                                                    p_disco_y,
                                                                    v_disco_x,
                                                                    v_disco_y,
                                                                    en_juego)

        # mover la paleta dos automaticamente
        mover_objeto(arena, pala_b, v_pala_b_x, v_pala_b_y)

        # obtener la posicion de la paleta dos
        p_pala_b_x, p_pala_b_y = obtener_posicion_objeto(arena,
                                                         pala_b)

        # verificar colision de la paleta dos con los bordes
        v_pala_b_x, v_pala_b_y, _ = verificar_colisiones_arena(arena,
                                                               pala_b,
                                                               p_pala_b_x,
                                                               p_pala_b_y,
                                                               v_pala_b_x,
                                                               v_pala_b_y,
                                                               True)

        # pausa entre fotogramas
        esperar(PAUSA)

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
