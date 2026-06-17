# ESTE ES UN JUEGO DONDE EL USUARIO DEBE ATRAPAR 10 GOTAS DE AGUA
from stanfordpy.graphics.graphics import Lienzo
import random
import time
import pathlib


ANCHO_GOTA = 25
ANCHO_BALDE = 55
ALTO_BALDE = 55
ANCHO_BARRA = 50
ALTO_BARRA = 100
ALTO_PASO = 10


def crear_barras_progreso(lienzo, x, y, es_rojo):
    # Agregamos contorno="" al final para que Tkinter no falle al dibujar los bloques de progreso
    barra = lienzo.crear_rectangulo(
        x, y, x + ANCHO_BARRA, y + ALTO_PASO, contorno="")
    if es_rojo == 1:
        lienzo.establecer_color_relleno(barra, 'red')
    else:
        lienzo.establecer_color_relleno(barra, 'green')
    return barra


def mover_balde(lienzo, balde):
    raton_x = lienzo.get_mouse_x()
    nuevo_x = raton_x - ANCHO_BALDE / 2
    # Movemos la imagen a la altura de juego deseada (530)
    lienzo.mover_hacia(balde, nuevo_x, 530)


def fisica_gotas(lienzo, vy, balde, lista_gotas):
    puntos_perdidos = 0
    puntos_ganados = 0

    for par_gota in lista_gotas[:]:
        for parte in par_gota:
            lienzo.mover(parte, 0, vy)

        y_superior = lienzo.get_top_y(par_gota[0])
        x_izquierdo = lienzo.get_left_x(par_gota[0])

        # Colisión Suelo
        if y_superior + ANCHO_GOTA >= 600:
            for parte in par_gota:
                lienzo.eliminar(parte)
            lista_gotas.remove(par_gota)
            puntos_perdidos += 1

        # Colisión Balde
        elif y_superior + ANCHO_GOTA >= lienzo.get_top_y(balde) and \
            (x_izquierdo >= lienzo.get_left_x(balde)-15 and
             x_izquierdo <= lienzo.get_left_x(balde) + ANCHO_BALDE):
            for parte in par_gota:
                lienzo.eliminar(parte)
            lista_gotas.remove(par_gota)
            puntos_ganados += 1

    return puntos_ganados, puntos_perdidos


def crear_gota(lienzo, ancho):
    px = random.randint(50, 550)
    gota = lienzo.crear_ovalo(px, -50, px + ancho, -50 + ancho)
    brillo = lienzo.crear_ovalo(px + 5, -44, px + 12, -37)
    lienzo.establecer_color_relleno(gota, 'cyan')
    lienzo.establecer_color_relleno(brillo, 'white')
    lienzo.establecer_color_contorno(gota, '')
    return [gota, brillo]


def main():
    lienzo = Lienzo(600, 600)

    # 1. EL FONDO PRIMERO
    rect = lienzo.crear_rectangulo(0, 0, 600, 600, contorno="")
    lienzo.establecer_color_relleno(rect, "#494972")

    # CAMBIO: Usar crear_imagen en lugar de crear_imagen_con_tamano porque el thinker se recetea
    path_to_image = str(pathlib.Path(__file__).parent / "assets" / "fondo.gif")
    fondo = lienzo.crear_imagen(0, 0, path_to_image)

    # 2. EL BALDE COMO IMAGEN REAL
    path_to_bucket = str(pathlib.Path(__file__).parent / "assets" / "balde.gif")
    balde = lienzo.crear_imagen(260, 530, path_to_bucket)

    # Marcos de barras de interfaz
    lienzo.crear_rectangulo(0, 0, ANCHO_BARRA, ALTO_BARRA, contorno="")
    lienzo.crear_rectangulo(600 - ANCHO_BARRA, 0, 600, ALTO_BARRA, contorno="")

    vida = 20
    puntaje = 20
    velocidad_y = 8
    lista_gotas = []
    temporizador = 0

    print("--- INICIO DEL JUEGO ---")
    
    time.sleep(2)  # Pausa inicial para que el jugador se prepare

    while vida > 0 and puntaje > 0:
        mover_balde(lienzo, balde)

        temporizador += 1
        if temporizador % 15 == 0:
            lista_gotas.append(crear_gota(lienzo, ANCHO_GOTA))

        # ahora lo hago es con la imgaen no con el blade armado porque ya funcionoa la imagen

        ganados, perdidos = fisica_gotas(
            lienzo, velocidad_y, balde, lista_gotas)

        if perdidos > 0:
            crear_barras_progreso(lienzo, 0, ALTO_BARRA - (22 - vida)*5, 1)
            vida -= 2
            print(f"¡Gota perdida! Vida restante: {vida}")

        if ganados > 0:
            crear_barras_progreso(lienzo, 600 - ANCHO_BARRA,
                                  ALTO_BARRA - (22 - puntaje)*5, 0)
            puntaje -= 2
            print(f"¡Gota atrapada! Puntos para ganar: {puntaje}")

        time.sleep(1/60)

    # Resultado final

    final_msg = "VICTORIA" if vida > 0 else "GAME OVER"
    print(f"\n*** RESULTADO: {final_msg} ***")

    res = lienzo.crear_texto(300, 300, final_msg, tamano=40, ancla="center")
    lienzo.establecer_color_relleno(res, "white")

    lienzo.mainloop()


if __name__ == '__main__':
    main()
