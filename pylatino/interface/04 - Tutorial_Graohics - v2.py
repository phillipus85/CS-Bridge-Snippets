

# importaciones necesarias
from stanfordpy.graphics import Lienzo
from time import sleep as esperar

ANCHO_LIENZO = 550
ALTO_LIENZO = 550

DIAMETRO_CIRCULO = 160
# usar radio del círculo
LADO_CUADRADO = (2)**(1 / 2) * (DIAMETRO_CIRCULO // 2)
HIPO_TRIANGULO = (3)**(1 / 2) * (DIAMETRO_CIRCULO // 2)
ALTO_TRIANGULO = (3)**(1 / 2) / 2 * HIPO_TRIANGULO
BASE_TRIANGULO = HIPO_TRIANGULO / 2


def main():
    # cambiar el nombre para no confundir Lienzo con lienzo.
    hoja = Lienzo(ANCHO_LIENZO, ALTO_LIENZO)
    # posición del título
    pos_x_titulo = 20
    pos_y_titulo = 20

    # agregar texto/título del ejercicio
    titulo = hoja.crear_texto(pos_x_titulo,
                              pos_y_titulo,
                              "HORA DE PROGRAMAR: Geométrico!",
                              fuente="consolas",
                              color="rojo",
                              tamano=24,
                              ancla="nw",)
    #   jugar con el tamanho y el ancla=["N","S","NE", ...]

    # posición del círculo
    pos_x_circulo = (ANCHO_LIENZO - DIAMETRO_CIRCULO) // 2
    pos_y_circulo = (ALTO_LIENZO - DIAMETRO_CIRCULO) // 2

    # crear el circulo principal
    circulo = hoja.crear_ovalo(pos_x_circulo,
                               pos_y_circulo,
                               pos_x_circulo + DIAMETRO_CIRCULO,
                               pos_y_circulo + DIAMETRO_CIRCULO,
                               color="dorado",
                               contorno="dorado",)

    # posición del cuadrado inscrito
    pos_x_cuadrado = (ANCHO_LIENZO - LADO_CUADRADO) // 2
    pos_y_cuadrado = (ALTO_LIENZO - LADO_CUADRADO) // 2

    # crear el cuadrado inscrito
    cuadrado = hoja.crear_rectangulo(pos_x_cuadrado,
                                     pos_y_cuadrado,
                                     pos_x_cuadrado + LADO_CUADRADO,
                                     pos_y_cuadrado + LADO_CUADRADO,
                                     color="azul",
                                     contorno="azul",)

    # crear el triangulo/poligono de 3 lados inscrito
    pos_x_punto_a_triangulo = ANCHO_LIENZO // 2
    pos_y_punto_a_triangulo = (ALTO_LIENZO - DIAMETRO_CIRCULO) // 2
    pos_x_punto_b_triangulo = ANCHO_LIENZO // 2 + BASE_TRIANGULO
    pos_y_punto_b_triangulo = (ALTO_LIENZO - DIAMETRO_CIRCULO) // 2 + ALTO_TRIANGULO
    pos_x_punto_c_triangulo = ANCHO_LIENZO // 2 - BASE_TRIANGULO
    pos_y_punto_c_triangulo = (ALTO_LIENZO - DIAMETRO_CIRCULO) // 2 + ALTO_TRIANGULO

    print(pos_x_punto_a_triangulo, pos_y_punto_a_triangulo)
    print(pos_x_punto_b_triangulo, pos_y_punto_b_triangulo)
    print(pos_x_punto_c_triangulo, pos_y_punto_c_triangulo)

    triangulo = hoja.create_polygon(pos_x_punto_a_triangulo,
                                    pos_y_punto_a_triangulo,
                                    pos_x_punto_b_triangulo, pos_y_punto_b_triangulo,
                                    pos_x_punto_c_triangulo, pos_y_punto_c_triangulo,
                                    color="violeta",)

    esperar(1)
    # cerrar el lienzo
    hoja.mainloop()

if __name__ == '__main__':
    main()
