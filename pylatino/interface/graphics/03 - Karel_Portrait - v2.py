"""
Este tutorial es el codigo guia para los conceptos de graficos-stanford para pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este tutorial es la integracion de todos los conceptos gráficos de Stanford en Python para pylatino 2025 donde retrataremos a karel con formas y colores basicos.
    Incluye:
        - PARTE 1: Crear un lienzo (Funcion Lienzo()).
        - PARTE 2: Planear el dibujo de karel (descomposicion, dibujar por partes, conectar/retomar funciones).

         PARRTIR ACA!!!!

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
    # abstraccion
    # crear una funcion para paralelogramos (cuadrados y rectangulos)
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
ANCHO_MAX_X = 300
ALTO_MAX_Y = 300


# definicion de funciones especificas para pintar figuras

def pintar_figura(lienzo,
                  pos_x,
                  pos_y,
                  largo,
                  alto,
                  color_fig="blanco",
                  contorno_fig="negro"):
    """Dibuja una figura en cuadrada/rectangular en el lienzo. Puede usarse para dibujar el cuerpo, pantalla, floppy disk, piernas y pies de karel.
    """
    # dibujar una parte del cuerpo de Karel con un rectángulo
    figura = lienzo.crear_rectangulo(pos_x,
                                     pos_y,
                                     pos_x + largo,
                                     pos_y + alto,
                                     color=color_fig,
                                     contorno=contorno_fig)
    return figura


# definición de la funcion principal

def main():
    """main ejecuta el programa principal
    """
    # TODO: PARTE 1: Crear el lienzo
    # Crear el lienzo
    retrato = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # TODO: PARTE 2: Planear el dibujo de Karel, recordar descomposición y funciones
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

    # Calcular centro del cuerpo y dejar espacio para las piernas
    pos_cuerpo_x = (ANCHO_MAX_X - ancho_cuerpo) // 2
    pos_cuerpo_y = (ALTO_MAX_Y - alto_cuerpo - 40) // 2

    # # dibujar el cuerpo de Karel con un rectángulo blanco y bordes negros
    # # # alternativa sin funcion pintar_figura
    # # definir color y contorno del cuerpo
    # cuerpo_karel = retrato.crear_rectangulo(pos_cuerpo_x,
    #                                         pos_cuerpo_y,
    #                                         pos_cuerpo_x + ancho_cuerpo,
    #                                         pos_cuerpo_y + alto_cuerpo,
    #                                         color="blanco",
    #                                         contorno="negro")

    # TODO: PARTE 3: Dibujar formas básicas en el lienzo
    # TODO: PARTE 4: Aplicar geometría (ubicar elementos en el lienzo)
    # dibujar el cuerpo de Karel con un rectángulo blanco y bordes negros
    # usando la funcion pintar_figura
    cuerpo_karel = pintar_figura(retrato,
                                 pos_cuerpo_x,
                                 pos_cuerpo_y,
                                 ancho_cuerpo,
                                 alto_cuerpo)

    # Dimensiones de la pantalla
    ancho_pantalla = 40  # ancho de la pantalla
    alto_pantalla = 60   # alto de la pantalla

    # Calcular posición para centrar la pantalla en el cuerpo
    pos_pantalla_x = pos_cuerpo_x + (ancho_cuerpo - ancho_pantalla) // 2 - 5
    pos_pantalla_y = pos_cuerpo_y + 10  # Un poco debajo del borde superior

    # dibujar la pantalla de Karel con un rectángulo blanco y borde negro
    pantalla_karel = None
    pantalla_karel = pintar_figura(retrato,
                                   pos_pantalla_x,
                                   pos_pantalla_y,
                                   ancho_pantalla,
                                   alto_pantalla)

    # dimensiones del floppy disk
    ancho_floppy = 35
    alto_floppy = 5

    pos_floppy_x = pos_cuerpo_x + (ancho_cuerpo - ancho_floppy) // 2 + 5
    pos_floppy_y = pos_cuerpo_y + alto_cuerpo - 25

    # dibujar el floppy disk de Karel con un rectángulo negro y borde gris
    floppy_karel = pintar_figura(retrato,
                                 pos_floppy_x,
                                 pos_floppy_y,
                                 ancho_floppy,
                                 alto_floppy,
                                 color_fig="negro")

    # Dimensiones de las piernas y pies
    ancho_pierna = 10
    alto_pierna = 10
    ancho_pie = 25
    alto_pie = 10

    # Calcular posiciones para la pierna izquierda
    pos_pierna_izq_x = pos_cuerpo_x + ancho_pantalla * 4 // 5
    pos_pierna_izq_y = pos_cuerpo_y + alto_cuerpo

    # dibujar pierna izquierda de Karel con un rectángulo
    pierna_izquierda = pintar_figura(retrato,
                                     pos_pierna_izq_x,
                                     pos_pierna_izq_y,
                                     ancho_pierna,
                                     alto_pierna,
                                     color_fig="negro")

    # calcular posicion para pie izquierdo
    pos_pie_izq_x = pos_pierna_izq_x
    pos_pie_izq_y = pos_pierna_izq_y + alto_pierna

    # dibujar pie izquierdo de Karel con un rectángulo
    pie_izquierdo = pintar_figura(retrato,
                                  pos_pie_izq_x,
                                  pos_pie_izq_y,
                                  ancho_pie,
                                  alto_pie,
                                  color_fig="negro")

    # Calcular posiciones para la pierna derecha
    # Sale del lado izquierdo del cuerpo
    pos_pierna_der_x = pos_cuerpo_x - alto_pierna
    pos_pierna_der_y = pos_cuerpo_y + alto_cuerpo * 2 // 3

    # dibujar pierna derecha de Karel con un rectángulo
    pierna_derecha = pintar_figura(retrato,
                                   pos_pierna_der_x,
                                   pos_pierna_der_y,
                                   ancho_pierna,
                                   alto_pierna,
                                   color_fig="negro")

    # calcular posicion para pie derecho
    pos_pie_der_x = pos_pierna_der_x
    pos_pie_der_y = pos_pierna_der_y

    # dibujar pie derecho de Karel con un rectángulo
    pie_derecho = pintar_figura(retrato,
                                pos_pie_der_x,
                                pos_pie_der_y,
                                -ancho_pierna,
                                ancho_pie,
                                color_fig="negro")

    # # TODO: PARTE 5: Modificar elementos, cambio de color
    # # cambiar colores de las figuras
    # retrato.establecer_color(cuerpo_karel,
    #                          retrato.obtener_color_aleatorio())
    # retrato.establecer_color(pantalla_karel,
    #                          retrato.obtener_color_aleatorio())
    # retrato.establecer_color(floppy_karel,
    #                          retrato.obtener_color_aleatorio())
    # retrato.establecer_color(pierna_izquierda,
    #                          retrato.obtener_color_aleatorio())
    # retrato.establecer_color_relleno(pie_izquierdo,
    #                                  retrato.obtener_color_aleatorio())
    # retrato.establecer_color_relleno(pierna_derecha,
    #                                  retrato.obtener_color_aleatorio())
    # retrato.establecer_color_relleno(pie_derecho,
    #                                  retrato.obtener_color_aleatorio())

    # cerrar el lienzo
    retrato.mainloop()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
