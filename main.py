from src.graphics import Canvas as Lienzo
from time import sleep as esperar
from random import randint

ANCHURA_LIENZO = 500
ALTURA_LIENZO = 600
# Crear constantes menu principal
ALTURA_CADA_LETRA = 100
ANCHURA_CUBO = 30
TITULO_ESPACIO_ARRIBA = 100
ESPACIO_ENTRE_LETRAS = 10
START_ANCHO = 150
START_ALTO = 50

N_LADRILLOS_EN_UNA_FILA = 10

# Cuantas filas hay de ladrillos.
N_FILAS = 10

# Cuanto espacio hay entre ladrillos de vecinos, en píxeles.
ESPACIO_LADRILLO = 5

# Altura de cada ladrillo, en píxeles.
ALTURA_LADRILLO = 8

# Ancho de cada ladrillo, en píxeles.
ANCHO_LADRILLO = int(ANCHURA_LIENZO - (N_LADRILLOS_EN_UNA_FILA + 1) * ESPACIO_LADRILLO) // N_LADRILLOS_EN_UNA_FILA

ESPACIO_LADRILLO_ABAJO = ALTURA_LIENZO - 80
ESPACIO_TEXTO_ABAJO = ESPACIO_LADRILLO_ABAJO - 20


# Aqui van las propiedades de la nave :D
ANCHO_NAVE = 34
ALTURA_NAVE = 38
VELOCIDAD_DISPARO_X = 10
VELOCIDAD_DISPARO_Y = 1000
ANCHO_DISPARO = 7
ALTURA_DISPARO = 7
ZONA_SPAWN_ENEMIGOS = ALTURA_LIENZO / 3
VELOCIDAD_ENEMIGO = 10


def crear_titulo(lienzo, tamaño, color):
    titulo = lienzo.crear_texto(ANCHURA_LIENZO // 2,
                                TITULO_ESPACIO_ARRIBA,
                                text='ROX',
                                font=('Segoe UI Bold', tamaño),
                                fill=color)
    return titulo


def crear_start_button(lienzo):
    x1 = ANCHURA_LIENZO // 2 - START_ANCHO // 2
    y1 = ALTURA_LIENZO // 2 - START_ALTO // 2
    x2 = x1 + START_ANCHO
    y2 = y1 + START_ALTO
    start = lienzo.crear_rectangulo(x1, y1, x2, y2, fill="yellow")
    lienzo.crear_texto(ANCHURA_LIENZO // 2,
                       ALTURA_LIENZO // 2,
                       text='START GAME',
                       font=('Comic Sans MS', 13),
                       fill="black")
    return start


def detectar_click_start(lienzo, start):
    click_on_star = False
    mouse_click = lienzo.obtener_ultimo_clic_mouse()
    print(mouse_click)
    if mouse_click is not None:
        print(mouse_click)
        mouse_start_x = mouse_click.x
        mouse_start_y = mouse_click.y
        click_superpuesto = lienzo.encontrar_superposiciones(mouse_start_x,
                                                             mouse_start_y,
                                                             mouse_start_x,
                                                             mouse_start_y)
        print(click_superpuesto)
        for click in click_superpuesto:
            if click == start:
                # print('click')
                lienzo.eliminar_todo()
                click_on_star = True
                break
    return click_on_star


def color_fondo_func(lienzo, color):
    color_fondo = lienzo.establecer_color_fondo_lienzo(color)
    return color_fondo


def crear_barra_carga(lienzo, color, tamaño_texto):
    # TODO ojo esto consume muchos recursos!!!!
    x1_texto = ANCHURA_LIENZO // 2 - tamaño_texto // 2
    y1_texto = ALTURA_LIENZO - ESPACIO_TEXTO_ABAJO
    cargando = lienzo.crear_texto(x1_texto,
                                  y1_texto,
                                  text="Loading.",
                                  font=('Cambria', tamaño_texto),
                                  fill=color)

    for i in range(N_LADRILLOS_EN_UNA_FILA):
        x1 = ESPACIO_LADRILLO + (ESPACIO_LADRILLO + ANCHO_LADRILLO) * i
        y1 = ESPACIO_LADRILLO_ABAJO - (ESPACIO_LADRILLO + ALTURA_LADRILLO)
        x2 = x1 + ANCHO_LADRILLO
        y2 = y1 + ALTURA_LADRILLO
        lienzo.crear_rectangulo(x1, y1, x2, y2, fill=color)
        lienzo.establecer_texto(cargando, "Loading...")
        esperar(0.1)
        lienzo.establecer_texto(cargando, "Loading..")
        esperar(0.1)
        lienzo.establecer_texto(cargando, "Loading.")
        esperar(0.1)


def crear_nave(lienzo):
    izquierda_x = ANCHURA_LIENZO // 2 - ANCHO_NAVE // 2
    superior_y = ALTURA_LIENZO // 2 - ALTURA_NAVE // 2
    nave = lienzo.crear_imagen_con_tamaño(izquierda_x,
                                          superior_y,
                                          ANCHO_NAVE,
                                          ALTURA_NAVE,
                                          'galaga_ship.png')
    return nave


# TODO FALTA ARREGLAR DESDE ACA
def disparar(lienzo, nave):
    clic_disparo = lienzo.obtener_ultimo_clic_mouse()
    if clic_disparo is not None:
        x_izq = lienzo.obtener_x_izq(nave)
        y_sup = lienzo.obtener_y_sup(nave)
        x1_disparo = x_izq + ANCHO_NAVE // 2 - 3
        y1_disparo = y_sup + ALTURA_NAVE // 2
        x2_disparo = x1_disparo + ALTURA_DISPARO
        y2_disparo = y1_disparo + ANCHO_DISPARO
        disparo = lienzo.crear_rectangulo(x1_disparo,
                                          y1_disparo,
                                          x2_disparo,
                                          y2_disparo,
                                          fill='white',
                                          color='#DC143C')
        return disparo


def mover_disparos(lienzo, lista_disparos):
    for disparo in lista_disparos:
        if disparo is not None:
            x_disparo = lienzo.obtener_x_izq(disparo)
            y_disparo = lienzo.obtener_y_sup(disparo)
            x2_disparo = x_disparo + ANCHO_DISPARO
            y2_disparo = y_disparo + ALTURA_DISPARO
            lienzo.moverse_hacia(disparo, x_disparo, (y_disparo - 10))
            if y_disparo <= 25:
                lista_disparos.remove(disparo)
                lienzo.eliminar(disparo)


def matar_enemigos(lienzo, colisiones, nave, disparos, disparo, enemigo):
    if disparo != None:
        enemigos_eliminados = 0
        for objeto in colisiones: 
            if objeto != nave:
                lienzo.eliminar(objeto)
                disparos.remove(disparo)
                lienzo.eliminar(disparo)
                enemigos_eliminados += 1
        return enemigos_eliminados
    else:
        return 0


def encontrar_colisiones(lienzo, disparo, fondo, nave):
    if disparo != None:
        x_disparo = lienzo.obtener_x_izq(disparo)
        y_disparo = lienzo.obtener_y_sup(disparo)
        x2_disparo = x_disparo + ANCHO_DISPARO
        y2_disparo = y_disparo + ALTURA_DISPARO
        colisiones = lienzo.encontrar_superposiciones(x_disparo, y_disparo, x2_disparo, y2_disparo)
        colisiones.remove(disparo)
        colisiones.remove(fondo)
        return colisiones
        print(colisiones)


def movimiento_nave(lienzo, nave):
    mouse_x = lienzo.obtener_mouse_x()
    mouse_y = lienzo.obtener_mouse_y()
    if mouse_x >= ANCHURA_LIENZO - ANCHO_NAVE:
        mouse_x = ANCHURA_LIENZO - ANCHO_NAVE
    lienzo.moverse_hacia(nave, mouse_x, mouse_y)


def crear_enemigo(lienzo, n_enemigos=10):
    lista_enemigos = []
    for i in range(n_enemigos):
        pos_izq_x = randint(0, ANCHURA_LIENZO - ANCHO_NAVE)
        pos_sup_y = randint(0, int(ZONA_SPAWN_ENEMIGOS))
        enemigo = lienzo.crear_imagen_con_tamaño(pos_izq_x,
                                                 pos_sup_y,
                                                 ANCHO_NAVE,
                                                 ALTURA_NAVE,
                                                 'Enemigo_1.png')
        lista_enemigos.append(enemigo)
    return lista_enemigos


def chocada_contra_pared_horizontal(lienzo, enemigo):
    # Comprobar y devolver si la pelota chocó contra una pared horizontal
    x_enemigo = lienzo.obtener_x(enemigo)
    if x_enemigo <= 0 or x_enemigo >= ANCHURA_LIENZO - ANCHO_NAVE:
        return True
    else:
        return False


def mover_enemigo(lienzo, lista_enemigos, enemigo, direccion, velocidad):
    for enemigo in lista_enemigos:
        x_enemigo = lienzo.obtener_x_izq(enemigo)
        y_enemigo = lienzo.obtener_y_sup(enemigo)
        x2_enemigo = x_enemigo + ANCHO_NAVE
        y2_enemigo = y_enemigo + ALTURA_NAVE
        if direccion == 1:
            lienzo.moverse(enemigo, velocidad, 0)
        elif direccion == 2:
            lienzo.moverse(enemigo, -velocidad, 0)


def main():
    lienzo = Lienzo(ANCHURA_LIENZO, ALTURA_LIENZO)
    fondo = lienzo.crear_imagen_con_tamaño(0,
                                           0,
                                           ANCHURA_LIENZO,
                                           ALTURA_LIENZO,
                                           'starry.png')

    contorno_titulo = crear_titulo(lienzo, 109, '#9ACD32')
    titulo = crear_titulo(lienzo, 100, '#8A2BE2')
    start = crear_start_button(lienzo)
    print(start)
    end_intro = False

    while end_intro is False:
        end_intro = detectar_click_start(lienzo,
                                         start)
        esperar(0.02)
        lienzo.update()

    color_fondo = color_fondo_func(lienzo, '#191970')
    # TODO esta funcion esta consumiendo mucha memoria!!!
    loading = True
    while loading:
        crear_barra_carga(lienzo, "white", 25)
        lienzo.update()
        loading = False
    # crear_barra_carga(lienzo, "white", 25)
    # # '''
    lienzo.eliminar_todo()
    fondo = lienzo.crear_imagen_con_tamaño(0,
                                           0,
                                           ANCHURA_LIENZO,
                                           ALTURA_LIENZO,
                                           'starry.png')
    nave = crear_nave(lienzo)
    lista_enemigos = crear_enemigo(lienzo)
    enemigos_restantes = len(lista_enemigos)
    print(nave, lista_enemigos, enemigos_restantes)
    while enemigos_restantes > 0:
        movimiento_nave(lienzo, nave)
        # disparo = disparar(lienzo, nave)
        esperar(0.02)
        lienzo.update()

    #     lista_disparos = []
    #     lista_disparos.append(disparo)
    #     colisiones = encontrar_colisiones(lienzo, disparo, fondo, nave)
    #     enemigos_restantes -= matar_enemigos(lienzo, colisiones, nave, lista_disparos, disparo, lista_enemigos)
    #     mover_disparos(lienzo, lista_disparos)
    #     mover_enemigo(lienzo, lista_enemigos, enemigo, 1, VELOCIDAD_ENEMIGO)
    # while enemigos_eliminados_totales <= 10:
    # #     movimiento_nave(lienzo, nave)
    # #     '''
    # #     disparo = disparar(lienzo, nave)
    # #     lista_disparos.append(disparo)
    # #     colisiones = encontrar_colisiones(lienzo, disparo, fondo, nave)
    # #     print(colisiones)
    # #     enemigos_eliminados_totales += matar_enemigos(lienzo, colisiones, nave, disparo, enemigo)
    # #     mover_disparos(lienzo, lista_disparos)
    # #     '''
    # #     esperar(0.02)
    # #     print(lista_enemigos)
    lienzo.mainloop()


if __name__ == '__main__':
    main()
