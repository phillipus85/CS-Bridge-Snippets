"""
Este tutorial es el código guía para los conceptos de gráficos de Pylatino 2025.

RESUMEN DEL TUTORIAL:
    Este módulo es una introducción a los gráficos de Stanford en Python e incluye:
        - PARTE 1: Crear un lienzo (Función Lienzo()).
        - PARTE 2: Dibujar formas básicas (círculos y cuadrados) en el lienzo (funciones crear_ovalo() y crear_rectangulo()).
        - PARTE 3: Aplicar geometría (Centrar elementos en el lienzo).
        - PARTE 4: Modificar elementos, cambio de posición (función mover())
        - PARTE 5: Modificar y Eliminar elementos, cambio de color y borrar (función establecer_color_relleno() y eliminar())
        - PARTE 6: aplicar el SLEEP entre cambios para observar las modificaciones

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

# importaciones necesarias
from stanfordpy.graphics import Lienzo
# from src.graphics import Canvas as Lienzo
# from stanfordpy.graphics import Canvas as Lienzo

# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de Python
# from graphics import Lienzo
from time import sleep as esperar

# definición de funciones y variables especificas

# Diámetro de la circulo (pelota)
DIAMETRO_CIRCULO = 90

# Lado del cuadrado (caja)
LADO_CUADRADO = 100

# dimensiones del lienzo
# ANCHO y ALTO del lienzo
ANCHO_MAX_X = 400
ALTO_MAX_Y = 400

# definición de la función principal


def main():
    """main ejecuta el programa principal
    """
    # Crear el lienzo
    # TODO PARTE 1: Crear un lienzo.
    cuadro = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # TODO PARTE 2: Dibujar formas básicas (círculos y cuadrados).
    # definir la posición inicial del punto superior izquierdo.
    pos_forma_x = ANCHO_MAX_X // 2
    pos_forma_y = ALTO_MAX_Y // 2

    # TODO PARTE 3: Aplicar geometría (centrar elementos en el lienzo).
    # centrar el circulo en el lienzo
    # pos_forma_x = ANCHO_MAX_X // 2 - DIAMETRO_CIRCULO // 2
    # pos_forma_y = ALTO_MAX_Y // 2 - DIAMETRO_CIRCULO // 2

    # definir el cuadrado (caja)
    caja = cuadro.create_rectangle(pos_forma_x,  # - LADO_CUADRADO // 2,
                                   pos_forma_y,  # - LADO_CUADRADO // 2,
                                   pos_forma_x + LADO_CUADRADO,
                                   pos_forma_y + LADO_CUADRADO,
                                   color="rojo")

    # definir el circulo (pelota)
    pelota = cuadro.create_oval(pos_forma_x,  # - DIAMETRO_CIRCULO // 2,
                                pos_forma_y,  # - DIAMETRO_CIRCULO // 2,
                                pos_forma_x + DIAMETRO_CIRCULO,
                                pos_forma_y + DIAMETRO_CIRCULO,
                                color="azul")
    esperar(1)
    # TODO PARTE 4: Modificar la posición de formas del lienzo.
    # cambiar la posición del circulo
    cuadro.mover(pelota, -DIAMETRO_CIRCULO // 2, -DIAMETRO_CIRCULO // 2)
    esperar(1)
    # cambiar la posición del cuadrado
    cuadro.mover(caja, -LADO_CUADRADO // 2, -LADO_CUADRADO // 2)

    # TODO PARTE 5: Modificar propiedades y eliminar formas del lienzo.
    # cambiar el color del circulo
    esperar(1)
    cuadro.establecer_color_relleno(pelota, "verde")
    cuadro.establecer_color_contorno(pelota, "rojo")

    # cambiar el color del cuadrado
    esperar(1)
    cuadro.establecer_color_relleno(caja, "amarillo")
    cuadro.establecer_color_contorno(caja, "rojo")

    esperar(1)  # esperar 1 segundo antes de eliminar
    cuadro.eliminar(pelota)

    # TODO PARTE 6: aplicar el sleep entre cambios para observar las modificaciones
    esperar(1)  # esperar 1 segundo antes de eliminar
    cuadro.eliminar(caja)


if __name__ == '__main__':
    """main es la función principal del programa
    """
    main()
