"""
Este modulo es el codigo guia para los conceptos de graficos de pylatino 2025.

3.	Graphics:
    1.	Centrar figuras (geometría)
        i. Encontrar el centro en el canvas/lienzo.
        ii. Introducir formas cuadrado y círculos (¿poliedros hay?) Dejemos por el momento cuadrados y círculos
    1.	Colores y formas (retratar a Karel)
        i. Entender como configurar colores, texto, y otras personalizaciones.
    1.	Edición (cambiar colores y formas)
        i. Entender cómo se reconfiguran colores DESPUÉS de crear las formas



RESUMEN DEL MÓDULO
    Este módulo es una introducción a los gráficos en Python e incluye:
        - PARTE 1: Crear un lienzo.
        - PARTE 2: Dibujar formas básicas (círculos y cuadrados).
        - PARTE 3: Agregar elementos al lienzo.
        - PARTE 4: Modificar elementos del lienzo.
        - PARTE 5: Eliminar elementos del lienzo.
        - PARTE 6: Pintar a karel.

NOTAS:
    - No hay elementos duplicados en un lienzo.
    - Los lienzos son mutables, lo que significa que se pueden modificar después de su creación.
    - Los lienzos pueden contener elementos de diferentes tipos.
    - Ejemplo basado en libros latinoamericanos.
"""

# importaciones necesarias
from stanfordpy.graphics import Lienzo
# from src.graphics import Canvas as Lienzo
# from stanfordpy.graphics import Canvas as Lienzo

# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo
# from time import sleep as esperar

# definicion de funciones y variables especificas

# Radio de la circulo (pelota)
RADIO_CIRCULO = 90

# Lado del cuadrado (caja)
LADO_CUADRADO = 100

# dimeniones del lienzo
# ANCHO y ALTO del lienzo
ANCHO_MAX_X = 400
ALTO_MAX_Y = 400


# definicion de la funcion principal

def main():
    """main ejecuta el programa principal
    """
    # Crear el lienzo
    # TODO parte 1: Crear un lienzo.
    cuadro = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # TODO parte 2: Dibujar formas basicas (circulos y cuadrados).
    # definir la posicion inicial del circulo
    # posicionar la forma en el centro del lienzo
    _pos_forma_x = ANCHO_MAX_X // 2
    # - RADIO_CIRCULO // 2
    _pos_forma_y = ALTO_MAX_Y // 2
    # - RADIO_CIRCULO // 2

    # TODO parte 3: Agregar elementos al lienzo.
    # definir el cuadrado (caja)
    # cuadrado = cuadro.crear_rectangulo(_pos_forma_x,
    cuadrado = cuadro.create_rectangle(_pos_forma_x,
                                       _pos_forma_y,
                                       _pos_forma_x + LADO_CUADRADO,
                                       _pos_forma_y + LADO_CUADRADO,
                                       color="red")

    # definir el circulo (pelota)
    # circulo = cuadro.create_oval(_pos_forma_x,
    circulo = cuadro.create_oval(_pos_forma_x,
                                 _pos_forma_y,
                                 _pos_forma_x + RADIO_CIRCULO,
                                 _pos_forma_y + RADIO_CIRCULO,
                                 color="blue")

    # TODO parte 4: Modificar elementos del lienzo.
    # cambiar el color del circulo
    cuadro.establecer_color_relleno(circulo, "green")
    # cambiar el color del cuadrado
    cuadro.establecer_color_relleno(cuadrado, "yellow")
    # cambiar la posicion del circulo
    cuadro.mover(circulo, -RADIO_CIRCULO // 2, -RADIO_CIRCULO // 2)
    # cambiar la posicion del cuadrado
    cuadro.mover(cuadrado, -LADO_CUADRADO // 2, -LADO_CUADRADO // 2)

    # TODO parte 5: Eliminar elementos del lienzo.
    # cuadro.eliminar(circulo)
    cuadro.eliminar(cuadrado)

    # TODO parte 6: Pintar a karel.
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
                                             color="white",
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
        cuadro.establecer_color_relleno(forma, cuadro.get_random_color())
        print(forma)
        # cuadro.establecer_color_borde(forma, "black")

    # cerrar el lienzo
    cuadro.mainloop()


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
