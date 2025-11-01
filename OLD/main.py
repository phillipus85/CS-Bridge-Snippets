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
ANCHO_DISPARO = 10
ALTURA_DISPARO = 10
ZONA_SPAWN_ENEMIGOS = ALTURA_LIENZO / 3
VELOCIDAD_ENEMIGO = 10


def crear_titulo(lienzo, tamaño, color):
    titulo = lienzo.crear_texto(ANCHURA_LIENZO // 2,
                                TITULO_ESPACIO_ARRIBA,
                                text="ROX",
                                font=("Segoe UI Bold", tamaño),
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
                       text="START GAME",
                       font=("Comic Sans MS", 13),
                       fill="black")
    return start


def detectar_click_start(lienzo, start):
    click_on_star = False
    mouse_click = lienzo.obtener_ultimo_clic_mouse()
    if mouse_click is not None:
        mouse_start_x = mouse_click.x
        mouse_start_y = mouse_click.y
        click_superpuesto = lienzo.encontrar_superposiciones(mouse_start_x,
                                                             mouse_start_y,
                                                             mouse_start_x,
                                                             mouse_start_y)
        for click in click_superpuesto:
            if click == start:
                lienzo.eliminar_todo()
                click_on_star = True
                break
    return click_on_star


def color_fondo_func(lienzo, color):
    lienzo.establecer_color_fondo_lienzo(color)


def estado_texto_juego(lienzo, texto_carga, texto):
    lienzo.establecer_texto(texto_carga, texto)


def estado_barra_carga(lienzo, estado_carga, i, color):
    x1 = ESPACIO_LADRILLO + (ESPACIO_LADRILLO + ANCHO_LADRILLO) * i
    y1 = ESPACIO_LADRILLO_ABAJO - (ESPACIO_LADRILLO + ALTURA_LADRILLO)
    x2 = x1 + ANCHO_LADRILLO
    y2 = y1 + ALTURA_LADRILLO
    rectangulo = lienzo.crear_rectangulo(x1, y1, x2, y2, fill=color)
    estado_carga.append(rectangulo)


def pintar_carga(lienzo, estado_carga, i, color, texto_carga, texto):
    estado_texto_juego(lienzo, texto_carga, texto)
    estado_barra_carga(lienzo, estado_carga, i, color)


def crear_nave(lienzo):
    izquierda_x = ANCHURA_LIENZO // 2 - ANCHO_NAVE // 2
    superior_y = ALTURA_LIENZO // 2 - ALTURA_NAVE // 2
    nave = lienzo.crear_imagen_con_tamaño(izquierda_x,
                                          superior_y,
                                          ANCHO_NAVE,
                                          ALTURA_NAVE,
                                          "galaga_ship.png")
    return nave


# TODO FALTA ARREGLAR DESDE ACA


def disparar(lienzo, nave):
    clic_disparo = lienzo.obtener_ultimo_clic_mouse()
    disparo = None
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
                                          fill="white",
                                          outline="#DC143C")
    # esperar(0.02)
    return disparo


def mover_objeto(lienzo, objeto, dx, dy):
    """mover_objeto() mueve el objeto en el lienzo.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.
        dx (int): es el desplazamiento en x.
        dy (int): es el desplazamiento en y.
    """
    lienzo.moverse(objeto, dx, dy)


def obtener_posicion_objeto(lienzo, objeto):
    """obtener_posicion_objeto() obtiene la posición de la objeto en el lienzo.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.

    Returns:
        tuple: una tupla con la posición del objeto.
    """
    _tx = lienzo.obtener_x_izq(objeto)
    _ty = lienzo.obtener_y_sup(objeto)
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
    if tx >= ANCHURA_LIENZO - ANCHO_NAVE:
        # ir hacia la izquierda, teniendo en cuenta el radio de la pelota
        dx = -3
    # 2) si colisiona con el borde inferior
    if ty >= ALTURA_LIENZO - ALTURA_NAVE:
        # ir hacia arriba, teniendo en cuenta el radio de la pelota
        dy = -3
    # 3) si colisiona con el borde izquierdo
    if tx <= 0.0:
        # ir hacia la derecha
        dx = 3
    # 4) si colisiona con el borde superior
    if ty <= 0.0:
        # ir hacia abajo
        dy = 3
    # retornar las nuevas velocidades
    return (dx, dy)


def mover_disparos(lienzo, lista_disparos):
    for disparo in lista_disparos:
        x_disparo, y_disparo = obtener_posicion_objeto(lienzo, disparo)
        mover_objeto(lienzo, disparo, 0, -10)
        if y_disparo <= 0:
            lista_disparos.remove(disparo)
            lienzo.eliminar(disparo)


def eliminar_enemigos(lienzo,
                      lista_cotactos,
                      lista_disparos,
                      lista_enemigos,
                      lista_velocidades):
    # variables de trabajo
    i = 0
    # indice del disparo a borrar
    # idx_d = None
    # indice del enemigo a borrar
    idx_e = None
    # si hay impactos
    if len(lista_cotactos) > 0:
        # recorrer los impactos
        eliminado = False
        while i < len(lista_cotactos) and not eliminado:
            # obtener el contacto
            contacto = lista_cotactos[i]
            # obtener el enemigo y el disparo
            enemigo, disparo = contacto
            # si hay enemigos
            if len(lista_enemigos) > 0:
                # si el enemigo esta en la lista de enemigos
                if enemigo in lista_enemigos:
                    # eliminar el enemigo del lienzo
                    lienzo.eliminar(enemigo)
                    idx_e = lista_enemigos.index(enemigo)
                    # eliminar el enemigo de la lista de enemigos
                    lista_enemigos.remove(enemigo)
                    # eliminar la velocidad del enemigo
                    lista_velocidades.pop(idx_e)
                    eliminado = True
            # si hay disparos
            if len(lista_disparos) > 0:
                # si el disparo esta en la lista de disparos
                if disparo in lista_disparos:
                    # eliminar el disparo del lienzo
                    lienzo.eliminar(disparo)
                    # eliminar el disparo de la lista de disparos
                    lista_disparos.remove(disparo)
                    # idx_d = i
            # incrementar el contador
            i += 1
    # devolver la cantidad de enemigos restantes junto a las listas actualizadas
    ans = (
        len(lista_enemigos),
        lista_enemigos,
        lista_velocidades,
        lista_disparos
    )
    return ans


def verificar_disparos_con_impactos(lienzo,
                                    lista_disparos,
                                    lista_enemigos,
                                    fondo,
                                    nave):
    total_impactos = []
    for disparo in lista_disparos:
        lista_impactos = verificar_impactos_enemigos(lienzo,
                                                     disparo,
                                                     lista_enemigos,
                                                     fondo,
                                                     nave)
        lista_impactos = ignorar_otros_enemigos(lista_impactos, lista_enemigos)
        total_impactos.extend(lista_impactos)
    return total_impactos


def verificar_impactos_enemigos(lienzo,
                                disparo,
                                lista_enemigos,
                                fondo,
                                nave):
    # lista de contactos con el enemigo, la tupla enemigo y disparo
    contactos_enemigo = list()
    for enemigo in lista_enemigos:
        # encontrar los impactos que sufre el enemigo
        impactos_enemigo = encontrar_impacto_enemigo(lienzo,
                                                     enemigo,
                                                     fondo,
                                                     nave)
        # si hay impactos
        if len(impactos_enemigo) > 0:
            # ver si el disparo esta en la lista de impactos del enemigo
            if disparo in impactos_enemigo:
                # agregar el contacto a la lista de impactados
                contacto = (enemigo, disparo)
                contactos_enemigo.append(contacto)
    # devolver los contactos con el enemigo
    return contactos_enemigo


def encontrar_impacto_enemigo(lienzo, enemigo, fondo, nave):
    impactos = list()
    x_disparo = lienzo.obtener_x_izq(enemigo)
    y_disparo = lienzo.obtener_y_sup(enemigo)
    x2_disparo = x_disparo + ANCHO_NAVE
    y2_disparo = y_disparo + ALTURA_NAVE
    # revisa si hay colisiones dentro del area del enemigo
    colisiones = lienzo.encontrar_superposiciones(x_disparo,
                                                  y_disparo,
                                                  x2_disparo,
                                                  y2_disparo)
    colisiones = list(colisiones)
    # ignorando el fondo
    if fondo in colisiones:
        colisiones.remove(fondo)
    # ignorando la nave
    if nave in colisiones:
        colisiones.remove(nave)
    # si hay colisiones
    if len(colisiones) > 0:
        # las colisiones que hay son impactos
        impactos = colisiones
    # devuelva los impactos en el enemigo
    return impactos


def ignorar_otros_enemigos(impactos, lista_enemigos):
    impactados = list()
    for impacto in impactos:
        if impacto not in lista_enemigos:
            impactados.append(impacto)
    return impactados


def verificar_nave_viva(lienzo,
                        nave,
                        lista_enemigos,
                        lista_disparos,
                        fondo):
    vivo = True
    lista_impactos = verificar_impactos_a_nave(lienzo,
                                               nave,
                                               lista_enemigos,
                                               fondo)
    lista_impactos = ignorar_otros_disparos(lista_impactos, lista_disparos)
    print("lista_impactos filtrados:", lista_impactos)
    if len(lista_impactos) > 0:
        vivo = False
    return vivo


def verificar_impactos_a_nave(lienzo,
                              nave,
                              lista_enemigos,
                              fondo):
    impactos_nave = list()
    for enemigo in lista_enemigos:
        impactos = encontrar_impactos_nave(lienzo, nave, fondo)
        if enemigo in impactos:
            contacto = (nave, enemigo)
            impactos_nave.append(contacto)
    return impactos_nave


def encontrar_impactos_nave(lienzo, nave, fondo):
    impactos = list()
    x_disparo = lienzo.obtener_x_izq(nave)
    y_disparo = lienzo.obtener_y_sup(nave)
    x2_disparo = x_disparo + ANCHO_NAVE
    y2_disparo = y_disparo + ALTURA_NAVE
    # revisa si hay colisiones dentro del area del enemigo
    colisiones = lienzo.encontrar_superposiciones(x_disparo,
                                                  y_disparo,
                                                  x2_disparo,
                                                  y2_disparo)
    colisiones = list(colisiones)
    # ignorando el fondo
    if fondo in colisiones:
        colisiones.remove(fondo)
    # si hay colisiones
    if len(colisiones) > 0:
        # las colisiones que hay son impactos
        impactos = colisiones
    # devuelva los impactos en el enemigo
    return impactos


def ignorar_otros_disparos(impactos, lista_disparos):
    impactados = list()
    for impacto in impactos:
        if impacto not in lista_disparos:
            impactados.append(impacto)
    return impactados


def mover_nave(lienzo, nave):
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
                                                 "Enemigo_1.png")
        lista_enemigos.append(enemigo)
    return lista_enemigos


def iniciar_movimiento_enemigo(lista_enemigos):
    lista_velocidades = []
    for enemigo in lista_enemigos:
        vx = randint(-4, 4)
        vy = randint(-4, 4)
        if vx == 0:
            vx = 1
        if vy == 0:
            vy = 1
        vel = (vx, vy)
        lista_velocidades.append(vel)
    return lista_velocidades


def mover_enemigos(lienzo, lista_enemigos, lista_vel_enemigos):
    # si la cantidad de enemigos es igual a la cantidad de velocidades
    if len(lista_enemigos) == len(lista_vel_enemigos):
        # esto evita inconsistencias en memoria
        i = 0
        while i < len(lista_enemigos):
            enemigo = lista_enemigos[i]
            vel = lista_vel_enemigos[i]
            vx, vy = vel
            pos_x, pos_y = obtener_posicion_objeto(lienzo, enemigo)
            mover_objeto(lienzo, enemigo, vx, vy)
            vx, vy = verificar_colision_extremos(pos_x, pos_y, vx, vy)
            vel = (vx, vy)
            lista_vel_enemigos[i] = vel
            i += 1


def main():
    # configurar el inicio
    lienzo = Lienzo(ANCHURA_LIENZO, ALTURA_LIENZO)
    fondo = lienzo.crear_imagen_con_tamaño(0,
                                           0,
                                           ANCHURA_LIENZO,
                                           ALTURA_LIENZO,
                                           "starry.png")
    contorno_titulo = crear_titulo(lienzo, 109, "#9ACD32")
    titulo = crear_titulo(lienzo, 100, "#8A2BE2")
    start = crear_start_button(lienzo)
    end_intro = False

    # bucle de inicio
    while end_intro is False:
        end_intro = detectar_click_start(lienzo,
                                         start)
        esperar(0.02)
        lienzo.update()

    # configurar pantalla de carga
    color_fondo_func(lienzo, "#020403")
    tamaño_texto = 25
    color = "white"
    txtld = "Loading"
    x1_texto = ANCHURA_LIENZO // 2 - tamaño_texto // 2
    y1_texto = ALTURA_LIENZO - ESPACIO_TEXTO_ABAJO
    cargando = lienzo.crear_texto(x1_texto,
                                  y1_texto,
                                  text=txtld,
                                  font=("Cambria", tamaño_texto),
                                  fill=color)
    estado_carga = list()
    loading = True
    i = 0
    # animar carga del juego
    while loading:
        txtld += "."
        pintar_carga(lienzo, estado_carga, i, color, cargando, txtld)
        lienzo.update()
        if i >= N_LADRILLOS_EN_UNA_FILA:
            loading = False
        i += 1
        esperar(0.1)
        lienzo.update()
    # refrescar la pantalla
    lienzo.eliminar_todo()
    # configurar el fondo del juego
    fondo = lienzo.crear_imagen_con_tamaño(0,
                                           0,
                                           ANCHURA_LIENZO,
                                           ALTURA_LIENZO,
                                           "starry.png")
    # crear la nave, los enemigos e iniciar el juego
    nave = crear_nave(lienzo)
    lista_enemigos = crear_enemigo(lienzo, n_enemigos=10)
    lista_vel_enemigos = iniciar_movimiento_enemigo(lista_enemigos)
    # lista para los disparos en pantalla
    lista_disparos = []
    # reconocer enemigos por eliminar
    enemigos_restantes = len(lista_enemigos)
    print(f"nave: {nave},",
          f"enemigos: {lista_enemigos},",
          f"n_enemigos: {enemigos_restantes}")
    vivo = True
    # mientras existan enemigos y la nave este viva
    while enemigos_restantes > 0 and vivo is True:
        # revisar si la nave colisiona con los enemigos
        vivo = verificar_nave_viva(lienzo,
                                   nave,
                                   lista_enemigos,
                                   lista_disparos,
                                   fondo)
        # revisar si hay disparos
        disparo = disparar(lienzo, nave)
        # si hay disparos
        if disparo is not None:
            # agregar el disparo a la lista de disparos activos
            lista_disparos.append(disparo)
            print("lista_disparos:", lista_disparos)

        # mover los disparos en pantalla
        if len(lista_disparos) > 0:
            # revisar si hay contacto de los disparos con los enemigos
            contactos = verificar_disparos_con_impactos(lienzo,
                                                        lista_disparos,
                                                        lista_enemigos,
                                                        fondo,
                                                        nave)
            # si hay contactos con los enemigos
            if len(contactos) > 0:
                print("contactos", contactos)
                print("lista_enemigos:", lista_enemigos)
                # actualizar la cantidad de enemigos restantes
                ans = eliminar_enemigos(lienzo,
                                        contactos,
                                        lista_disparos,
                                        lista_enemigos,
                                        lista_vel_enemigos)
                # mantener la memoria de lo actualizado
                enemigos_restantes = ans[0]
                lista_enemigos = ans[1]
                lista_vel_enemigos = ans[2]
                lista_disparos = ans[3]
            # mover los disparos en pantalla
            mover_disparos(lienzo, lista_disparos)
        # revisar el movimiento de la nave
        mover_nave(lienzo, nave)
        # mover los enemigos en pantalla
        mover_enemigos(lienzo, lista_enemigos, lista_vel_enemigos)
        # actualizar lienzo
        esperar(1 / 60)
        lienzo.update()

    lienzo.eliminar_todo()
    y1_texto = ALTURA_LIENZO // 2
    if vivo is False:
        print("PERDIÓ!!!")
        txtld = "PERDISTE :("
        cargando = lienzo.crear_texto(x1_texto,
                                      y1_texto,
                                      text=txtld,
                                      font=("Cambria", tamaño_texto),
                                      fill=color)
    else:
        print("GANE!!!!")
        txtld = "GANASTE :D"
        cargando = lienzo.crear_texto(x1_texto,
                                      y1_texto,
                                      text=txtld,
                                      font=("Cambria", tamaño_texto),
                                      fill=color)
    lienzo.mainloop()


if __name__ == "__main__":
    main()
