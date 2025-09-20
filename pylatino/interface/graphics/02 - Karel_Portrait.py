"""
Este tutorial es el codigo guia para los conceptos de graficos-stanford para pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este tutorial es la integracion de todos los conceptos gráficos de Stanford en Python para pylatino 2025 donde retrataremos a karel con formas y colores basicos.
    Incluye:
        - PARTE 1: Crear un lienzo (Funcion Lienzo()).
        - PARTE 2: Planear el dibujo de karel (descomposicion, pintar por partes, conectar/retomar funciones).
        - PARTE 3: Dibujar formas basicas (rectangulos y cuadrados) en el lienzo (funciones crear_ovalo() y crear_rectangulo()).
        - PARTE 4: Aplicar geometria (Centrar elementos en el lienzo).
        - PARTE 5: Modificar elementos, cambio de color (funcion establecer_color_relleno())

NOTAS:
    - Principios de dibujo y diseño a usar:
        - Uso de formas
        - Manejo de colores
        - Composición
        - Movimiento
    - retomar el concepto de despomposicion, pintar por partes, conectar/retomar funciones.
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


# definicion de funciones para dibujar las partes de karel
def dibujar_cuerpo(lienzo, pos_x, pos_y, ancho, alto):
    """dibujar_cuerpo dibuja el cuerpo de karel en el lienzo
    """
    # pintar el cuerpo de karel con un rectangulo
    cuerpo = lienzo.create_rectangle(pos_x,
                                     pos_y,
                                     pos_x + ancho,
                                     pos_y + alto,
                                     color="white",
                                     outline="black")
    return cuerpo


def dibujar_pantalla(lienzo, pos_x, pos_y, ancho, alto):
    """dibujar_pantalla dibuja la pantalla de karel en el lienzo
    """
    # pintar la pantalla de karel con un rectangulo
    # pintar la pantalla de karel con un rectangulo blanco y borde negro
    pantalla = lienzo.create_rectangle(pos_x - 5,
                                       pos_y - 5,
                                       pos_x + ancho - 5,
                                       pos_y + alto - 5,
                                       color="grey",
                                       outline="black")
    return pantalla


def dibujar_floppy(lienzo, pos_x, pos_y, ancho, alto):
    """dibujar_floppy dibuja el floppy de karel en el lienzo
    """
    # pintar el floppy disk de karel con un rectangulo
    pass


def dibujar_pierna_izquierda(lienzo, ancho, alto, pos_x, pos_y):
    """dibujar_pierna_izquierda dibuja la pierna y el pie izquierda de karel en el lienzo
    """
    # pintar pierna izquierda de karel con un rectangulo
    pass


def dibujar_pierna_derecha(lienzo, ancho, alto, pos_x, pos_y):
    """dibujar_pierna_derecha dibuja la pierna y el pie derecha de karel en el lienzo
    """
    # pintar pierna derecha de karel con un rectangulo
    pass


# definicion de la funcion principal

def main():
    """main ejecuta el programa principal
    """
    # Crear el lienzo
    # TODO PARTE 1: Crear un lienzo.
    cuadro = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # TODO PARTE 2: dibujar cuerpo de karel con rectangulos y cuadrados
    # Definir dimensiones del cuerpo de Karel
    ancho_cuerpo = 80  # ancho del cuerpo
    alto_cuerpo = 110  # alto del cuerpo (más alto que ancho)

    # Calcular posición para centrar el cuerpo
    pos_x_cuerpo = (ANCHO_MAX_X - ancho_cuerpo) // 2
    # Ajustado para dejar espacio para las piernas
    pos_y_cuerpo = (ALTO_MAX_Y - alto_cuerpo - 40) // 2

    # pintar el cuerpo de karel con un rectangulo blanco y bordes negros
    cuerpo_karel = cuadro.create_rectangle(pos_x_cuerpo,
                                           pos_y_cuerpo,
                                           pos_x_cuerpo + ancho_cuerpo,
                                           pos_y_cuerpo + alto_cuerpo,
                                           color="white",
                                           outline="black")

    # Dimensiones de la pantalla
    ancho_pantalla = 40  # ancho de la pantalla
    alto_pantalla = 55   # alto de la pantalla

    # Calcular posición para centrar la pantalla en el cuerpo
    pos_x_pantalla = pos_x_cuerpo + (ancho_cuerpo - ancho_pantalla) // 2
    pos_y_pantalla = pos_y_cuerpo + 15  # Un poco debajo del borde superior

    # pintar la pantalla de karel con un rectangulo blanco y borde negro
    pantalla_karel = cuadro.create_rectangle(pos_x_pantalla - 5,
                                             pos_y_pantalla,
                                             pos_x_pantalla + ancho_pantalla - 5,
                                             pos_y_pantalla + alto_pantalla,
                                             color="grey",
                                             outline="black")

    # pintar el floppy disk de karel con un rectangulo negro y borde gris
    floppy_karel = cuadro.create_rectangle(pos_x_pantalla + 10,
                                           pos_y_pantalla + 70,
                                           pos_x_pantalla + 45,
                                           pos_y_pantalla + 75,
                                           color="black",
                                           outline="black")

    # Dimensiones de las piernas y pies
    ancho_pierna = 10
    alto_pierna = 10
    ancho_pie = 30
    alto_pie = 10

    # Calcular posiciones para la pierna izquierda
    pos_x_pierna_izq = pos_x_cuerpo + ancho_pantalla * 4 // 5
    pos_y_pierna_izq = pos_y_cuerpo + alto_cuerpo

    # pintar pierna izquierda de karel con un rectangulo
    pierna_izquierda = cuadro.create_rectangle(pos_x_pierna_izq,
                                               pos_y_pierna_izq,
                                               pos_x_pierna_izq + ancho_pierna,
                                               pos_y_pierna_izq + alto_pierna,
                                               color="black",
                                               outline="black")

    # pintar pie izquierdo de karel con un rectangulo
    pie_izquierdo = cuadro.create_rectangle(pos_x_pierna_izq,
                                            pos_y_pierna_izq + alto_pierna,
                                            pos_x_pierna_izq + ancho_pie,
                                            pos_y_pierna_izq + alto_pierna + alto_pie,
                                            color="black",
                                            outline="black")

    # Calcular posiciones para la pierna derecha
    # Sale del lado izquierdo del cuerpo
    pos_x_pierna_der = pos_x_cuerpo - alto_pierna
    pos_y_pierna_der = pos_y_cuerpo + alto_cuerpo * 2 // 3

    # pintar pierna derecha de karel con un rectangulo
    pierna_derecha = cuadro.create_rectangle(pos_x_pierna_der,
                                             pos_y_pierna_der,
                                             pos_x_pierna_der + ancho_pierna,
                                             pos_y_pierna_der + alto_pierna,
                                             color="black",
                                             outline="black")
    print(pos_x_pierna_der, pos_y_pierna_der)
    print(pos_x_pierna_der + ancho_pierna, pos_y_pierna_der + alto_pierna,)
    # pintar pie derecho de karel con un rectangulo
    pie_derecho = cuadro.create_rectangle(pos_x_pierna_der,
                                          pos_y_pierna_der,
                                          pos_x_pierna_der - ancho_pierna,
                                          pos_y_pierna_der + ancho_pie,
                                          color="black",
                                          outline="black")

    figuras = [
        cuerpo_karel,
        pantalla_karel,
        floppy_karel,
        pierna_izquierda,
        pie_izquierdo,
        pierna_derecha,
        pie_derecho
    ]

    for forma in figuras:
        # cuadro.set_fill_color(forma, cuadro.get_random_color())
        print(forma)
        # cuadro.set_outline_color(forma, cuadro.get_random_color())

    # cerrar el lienzo
    cuadro.mainloop()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
