"""
Este tutorial es el codigo guia para los conceptos de graficos-stanford para pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este tutorial es la integracion de todos los conceptos gráficos de Stanford en Python para pylatino 2025 donde retrataremos a karel con formas y colores basicos.
    Incluye:
        - PARTE 1: Crear un lienzo (Funcion Lienzo()).
        - PARTE 2: Planear el dibujo de karel (descomposicion, dibujar por partes, conectar/retomar funciones).
        - PARTE 3: Dibujar formas basicas de karel (rectangulos y cuadrados) en el lienzo (y crear_rectangulo()).
        - PARTE 4: Aplicar geometria (Centrar elementos en el lienzo).
        - PARTE 5: Modificar elementos, cambio de color (funcion establecer_color_relleno())

NOTAS:
    - Principios de dibujo y diseño a usar:
        - Uso de formas
        - Manejo de colores
        - Composición
        - Movimiento
    - retomar el concepto de despomposicion, dibujar por partes, conectar/retomar funciones.
    - Retratar a karel es es el ejercicio final para aplicar todos los conceptos aprendidos en las partes anteriores.
    - El codigo esta comentado para facilitar la comprension de los conceptos.
"""

# importaciones necesarias
from stanfordpy.graphics import Lienzo
# from src.graphics import Canvas as Lienzo
# from stanfordpy.graphics import Canvas as Lienzo

# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo
# from time import sleep as esperar

# definicion de funciones y variables especificas

# dimeniones del lienzo
# ANCHO y ALTO del lienzo
ANCHO_MAX_X = 400
ALTO_MAX_Y = 400


# definicion de funciones para retratar a karel por partes
def pintar_cuerpo(lienzo, p_x, p_y, largo, alto):
    """pintar_cuerpo dibuja el cuerpo de karel en el lienzo.
    """
    # dibujar el cuerpo de karel con un rectangulo
    cuerpo = lienzo.create_rectangle(p_x,
                                     p_y,
                                     p_x + largo,
                                     p_y + alto,
                                     color="white",
                                     outline="black")
    return cuerpo


def pintar_pantalla(lienzo, p_x, p_y, largo, alto):
    """pintar_pantalla dibuja la pantalla de karel en el lienzo.
    """
    # dibujar la pantalla de karel con un rectangulo
    pantalla = lienzo.create_rectangle(p_x - 5,
                                       p_y - 5,
                                       p_x + largo - 5,
                                       p_y + alto - 5,
                                       color="white",
                                       outline="black")
    return pantalla


def pintar_floppy(lienzo, p_x, p_y, largo, alto):
    """pintar_floppy dibuja el floppy de karel en el lienzo.
    """
    # dibujar el floppy disk de karel con un rectangulo
    floppy = lienzo.create_rectangle(p_x + 10,
                                     p_y + 70,
                                     p_x + 10 + largo,
                                     p_y + 70 + alto,
                                     color="black",
                                     outline="black")
    return floppy


def pintar_pierna_izquierda(lienzo, p_x, p_y, l_pierna, a_pierna):
    """pintar_pierna_izquierda dibuja la pierna izquierda de karel en el lienzo.
    """
    # dibujar pierna izquierda de karel con un rectangulo
    pierna = lienzo.create_rectangle(p_x,
                                     p_y,
                                     p_x + l_pierna,
                                     p_y + a_pierna,
                                     color="black",
                                     outline="black")
    return pierna


def pintar_pie_izquierdo(lienzo, p_x, p_y, a_pierna, l_pie, a_pie):
    """pintar_pie_izquierdo dibuja el pie izquierdo de karel en el lienzo.
    """
    # dibujar pie izquierdo de karel con un rectangulo
    pie = lienzo.create_rectangle(p_x,
                                  p_y + a_pierna,
                                  p_x + l_pie,
                                  p_y + a_pierna + a_pie,
                                  color="black",
                                  outline="black")
    return pie


def pintar_pierna_derecha(lienzo, p_x, p_y, l_pierna, a_pierna):
    """pintar_pierna_derecha dibuja la pierna derecha de karel en el lienzo.
    """
    # dibujar pierna derecha de karel con un rectangulo
    pierna = lienzo.create_rectangle(p_x,
                                     p_y,
                                     p_x + l_pierna,
                                     p_y + a_pierna,
                                     color="black",
                                     outline="black")
    return pierna


def pintar_pie_derecho(lienzo, p_x, p_y, l_pierna, l_pie):
    """pintar_pie_derecho dibuja el pie derecho de karel en el lienzo.
    """
    # dibujar pie derecho de karel con un rectangulo
    pie = lienzo.create_rectangle(p_x,
                                  p_y,
                                  p_x - l_pierna,
                                  p_y + l_pie,
                                  color="black",
                                  outline="black")
    return pie


# definicion de la funcion principal

def main():
    """main ejecuta el programa principal
    """
    # TODO: PARTE 1: Crear el lienzo
    # Crear el lienzo
    cuadro = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # TODO: PARTE 2: Planear el dibujo de karel, recordar descomposicion y conectar con funciones
    # Descomponer el dibujo en partes:
    #   1. Cuerpo
    #   2. Pantalla
    #   3. Floppy disk
    #   4. Pierna izquierda
    #   5. Pie izquierdo
    #   6. Pierna derecha
    #   7. Pie derecho

    # Definir dimensiones del cuerpo de Karel
    ancho_cuerpo = 80  # ancho del cuerpo
    alto_cuerpo = 110  # alto del cuerpo (más alto que ancho)

    # Calcular posición para centrar el cuerpo
    pos_x_cuerpo = (ANCHO_MAX_X - ancho_cuerpo) // 2
    # Ajustado para dejar espacio para las piernas
    pos_y_cuerpo = (ALTO_MAX_Y - alto_cuerpo - 40) // 2

    # TODO: PARTE 3: Dibujar formas basicas en el lienzo
    # TODO: PARTE 4: Aplicar geometria (centrar elementos en el lienzo)
    # dibujar el cuerpo de karel con un rectangulo blanco y bordes negros
    cuerpo_karel = pintar_cuerpo(cuadro,
                                 pos_x_cuerpo,
                                 pos_y_cuerpo,
                                 ancho_cuerpo,
                                 alto_cuerpo)

    # Dimensiones de la pantalla
    ancho_pantalla = 40  # ancho de la pantalla
    alto_pantalla = 55   # alto de la pantalla

    # Calcular posición para centrar la pantalla en el cuerpo
    pos_x_pantalla = pos_x_cuerpo + (ancho_cuerpo - ancho_pantalla) // 2
    pos_y_pantalla = pos_y_cuerpo + 15  # Un poco debajo del borde superior

    # dibujar la pantalla de karel con un rectangulo blanco y borde negro
    pantalla_karel = pintar_pantalla(cuadro,
                                     pos_x_pantalla,
                                     pos_y_pantalla,
                                     ancho_pantalla,
                                     alto_pantalla)

    # dimensiones del floppy disk
    ancho_floppy = 35
    alto_floppy = 5

    # dibujar el floppy disk de karel con un rectangulo negro y borde gris
    floppy_karel = pintar_floppy(cuadro,
                                 pos_x_pantalla,
                                 pos_y_pantalla,
                                 ancho_floppy,
                                 alto_floppy)

    # Dimensiones de las piernas y pies
    ancho_pierna = 10
    alto_pierna = 10
    ancho_pie = 30
    alto_pie = 10

    # Calcular posiciones para la pierna izquierda
    pos_x_pierna_izq = pos_x_cuerpo + ancho_pantalla * 4 // 5
    pos_y_pierna_izq = pos_y_cuerpo + alto_cuerpo

    # dibujar pierna izquierda de karel con un rectangulo
    pierna_izquierda = pintar_pierna_izquierda(cuadro,
                                               pos_x_pierna_izq,
                                               pos_y_pierna_izq,
                                               ancho_pierna,
                                               alto_pierna)

    # dibujar pie izquierdo de karel con un rectangulo
    pie_izquierdo = pintar_pie_izquierdo(cuadro,
                                         pos_x_pierna_izq,
                                         pos_y_pierna_izq,
                                         alto_pierna,
                                         ancho_pie,
                                         alto_pie)

    # Calcular posiciones para la pierna derecha
    # Sale del lado izquierdo del cuerpo
    pos_x_pierna_der = pos_x_cuerpo - alto_pierna
    pos_y_pierna_der = pos_y_cuerpo + alto_cuerpo * 2 // 3

    # dibujar pierna derecha de karel con un rectangulo
    pierna_derecha = pintar_pierna_derecha(cuadro,
                                           pos_x_pierna_der,
                                           pos_y_pierna_der,
                                           ancho_pierna,
                                           alto_pierna)

    # dibujar pie derecho de karel con un rectangulo
    pie_derecho = pintar_pie_derecho(cuadro,
                                     pos_x_pierna_der,
                                     pos_y_pierna_der,
                                     ancho_pierna,
                                     ancho_pie)

    # TODO: PARTE 5: Modificar elementos, cambio de color
    # cambiar colores de las figuras
    cuadro.set_fill_color(cuerpo_karel, cuadro.get_random_color())
    cuadro.set_fill_color(pantalla_karel, cuadro.get_random_color())
    cuadro.set_fill_color(floppy_karel, cuadro.get_random_color())
    cuadro.set_fill_color(pierna_izquierda, cuadro.get_random_color())
    cuadro.set_fill_color(pie_izquierdo, cuadro.get_random_color())
    cuadro.set_fill_color(pierna_derecha, cuadro.get_random_color())
    cuadro.set_fill_color(pie_derecho, cuadro.get_random_color())

    # cerrar el lienzo
    cuadro.mainloop()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
