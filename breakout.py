from src.graphics import Canvas as Lienzo
from random import random
from time import sleep as esperar


# El tamaño del lienzo, en píxeles.
ANCHO_LIENZO = 450
ALTURA_LIENZO = 600

# Para Hito 1: Crear ladrillos

# Cuantos ladrillos hay en cada fila.
N_LADRILLOS_FILA = 10

# Cuantas filas hay de ladrillos.
N_FILAS = 10

# Cuanto espacio hay entre ladrillos de vecinos, en píxeles.
ESPACIO_LADRILLO = 5

# Altura de cada ladrillo, en píxeles.
ALTURA_LADRILLO = 8

# Ancho de cada ladrillo, en píxeles.
ANCHO_LADRILLO = int(ANCHO_LIENZO - (N_LADRILLOS_FILA + 1) * ESPACIO_LADRILLO) // N_LADRILLOS_FILA

# Desplazamiento de la fila de ladrillos superior desde la parte superior del canvas, en píxeles.
ESPACIO_LADRILLO_ARRIBA = 80

# Para Hito 2: Crear la pelota que rebota

# Radio de la pelota, en píxeles.
RADIO_PELOTA = 10

# La velocidad vertical inicial de la pelota.
VELOCIDAD_Y = 3

# La velocidad horizontal mínima y máxima.
# Tu velocidad inicial en la dirección x debe ser entre estos valores.
VELOCIDAD_X_MIN = -3
VELOCIDAD_X_MAX = 3

# Cuanto tiempo, en segundos, se espera entre fotogramas.
PAUSA = 1 / 30

# Para Hito 3: Crear la paleta

# El tamaño de la paleta.
ANCHO_PALETA = 60
ALTURA_PALETA = 10

# Desplazamiento de la paleta hacia arriba desde la pared inferior.
ESPACIO_PALETA_ABAJO = 30


def obtener_color_para_fila(k):
    colores = ["red", "orange", "yellow", "green", "blue"]
    return colores[(k // 2) % 5]


def crear_grilla_ladrillo(lienzo, y_offset):
    # y = y_offset
    for i in range(N_LADRILLOS_FILA):
        x = ESPACIO_LADRILLO + (ESPACIO_LADRILLO + ANCHO_LADRILLO) * i
        for j in range(N_FILAS):
            color = obtener_color_para_fila(j)
            # print(f"color: {color}")
            y = (ESPACIO_LADRILLO + ALTURA_LADRILLO) * j + y_offset
            lienzo.crear_rectangulo(x,
                                    y,
                                    x + ANCHO_LADRILLO,
                                    y + ALTURA_LADRILLO,
                                    fill=color)
        # memoria.append(ladrillo)


def crear_pelota(lienzo):
    cx = lienzo.obtener_anchura_lienzo() // 2
    cy = lienzo.obtener_altura_lienzo() // 2
    return lienzo.crear_ovalo(cx,
                              cy,
                              cx + RADIO_PELOTA * 2,
                              cy + RADIO_PELOTA * 2,
                              fill="black")


def obtener_velocidad_x_aleatoria():
    return random() * (VELOCIDAD_X_MAX - VELOCIDAD_X_MIN) + VELOCIDAD_X_MIN


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
    _tx = canvas.obtener_x_izq(objeto)
    _ty = canvas.obtener_y_sup(objeto)
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
    if tx >= ANCHO_LIENZO - RADIO_PELOTA * 2:
        # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
        dx = dx * -1
    # 2) si colisiona con el borde inferior
    if ty >= ALTURA_LIENZO - RADIO_PELOTA * 2:
        # ir hacia arriba, teniendo en cuenta el radio de la pelota
        print(f"ty: {ty}, ALTURA_LIENZO: {ALTURA_LIENZO}")
        dy = dy * -1
        dy = 0
        dx = 0
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


def crear_paleta(lienzo):
    cx = lienzo.obtener_anchura_lienzo() // 2
    y_inf = lienzo.obtener_altura_lienzo() - ESPACIO_PALETA_ABAJO
    return lienzo.crear_rectangulo(cx - ANCHO_PALETA // 2,
                                   y_inf - ALTURA_PALETA,
                                   cx + ANCHO_PALETA // 2,
                                   y_inf,
                                   fill="grey")


def mover_paleta(lienzo, paleta):
    x = lienzo.obtener_mouse_x()
    x = max(ANCHO_PALETA // 2, x)
    x = min(lienzo.obtener_anchura_lienzo() - ANCHO_PALETA // 2, x)
    lienzo.mover_hacia(paleta,
                       x - ANCHO_PALETA // 2,
                       lienzo.obtener_y_sup(paleta))


def encontrar_colisiones(lienzo, pelota):
    x_izq = lienzo.obtener_x_izq(pelota)
    y_sup = lienzo.obtener_y_sup(pelota)p
    colisiones = lienzo.encontrar_superposiciones(x_izq,
                                                  y_sup,
                                                  x_izq + 2 * RADIO_PELOTA,
                                                  y_sup + 2 * RADIO_PELOTA)
    colisiones = list(colisiones)
    return colisiones


def eliminar_ladrillos(lienzo, colisiones, paleta, pelota):
    total = 0
    if len(colisiones) > 1:
        for colision in colisiones:
            if colision not in [paleta, pelota]:
                print(f"paleta: {paleta}, {type(paleta)}")
                print(f"colision: {colision}, {type(colision)}")
                lienzo.eliminar(colision)
                total = total + 1
    return total


def informar_resultado(lienzo, ganado):
    if ganado:
        mensaje = "Has ganado!"
    else:
        mensaje = "Has perdido.\nJuegas otra vez?"
    w = lienzo.obtener_anchura_lienzo() // 2,
    h = lienzo.obtener_altura_lienzo() // 2
    texto = lienzo.crear_texto(w, h, mensaje)
    lienzo.establecer_fuente(texto, "Courier", 24)

# def pelota_en_juego(lienzo, pelota):


def main():
    lienzo = Lienzo(ANCHO_LIENZO, ALTURA_LIENZO)
    # ladrillos = list()
    # crear_ladrillos(lienzo, ESPACIO_LADRILLO_ARRIBA)
    crear_grilla_ladrillo(lienzo, ESPACIO_LADRILLO_ARRIBA)
    pelota = crear_pelota(lienzo)
    paleta = crear_paleta(lienzo)
    vy = VELOCIDAD_Y
    vx = obtener_velocidad_x_aleatoria()
    ladrillos_restantes = N_LADRILLOS_FILA * N_FILAS
    n_ladrillos = (ladrillos_restantes > 0)
    # lim_inferior = lienzo.obtener_y_sup(pelota) + 2 * RADIO_PELOTA
    # pelota_en_juego = lim_inferior < lienzo.obtener_altura_lienzo()
    while n_ladrillos > 0 and vx != 0 and vy != 0:
        mover_objeto(lienzo, pelota, vx, vy)
        tx, ty = obtener_posicion_objeto(lienzo, pelota)
        vx, vy = verificar_colision_extremos(tx, ty, vx, vy)
        # print(f"vx: {vx}, vy: {vy}")
        mover_paleta(lienzo, paleta)
        colisiones = encontrar_colisiones(lienzo, pelota)

        if len(colisiones) > 1:
            print(f"colisiones: {colisiones}")
            ladrillo_eliminados = eliminar_ladrillos(lienzo,
                                                     colisiones,
                                                     paleta,
                                                     pelota)
            ladrillos_restantes -= ladrillo_eliminados
            # print(f"paleta: {paleta}")
            vy = -1 * vy
            if colisiones[0] == paleta:
                vy = -1 * vy
        esperar(PAUSA)
        lienzo.update()
    informar_resultado(lienzo, ladrillos_restantes == 0)
    lienzo.mainloop()


if __name__ == '__main__':
    main()
