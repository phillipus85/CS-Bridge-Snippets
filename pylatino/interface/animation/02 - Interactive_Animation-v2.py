"""
Este tutorial es el código guía para los conceptos de animación de Pylatino 2025.

RESUMEN DEL TUTORIAL:
    Codigo guía para crear una animación interactiva simple en Python usando el módulo StanfordPy
        - PARTE 1: Escribir las funciones para crear objetos (pelota y paletas).
        - PARTE 2: Escribir la función para obtener la posición de los objetos.
        - PARTE 3: Escribir las funciones para mover los objetos.
        - PARTE 4: Escribir la función para detectar colisiones y rebotar con los bordes.
        - PARTE 5: Escribir la función detectar colisiones entre objetos (pelota y paletas).
        - PARTE 6: Controlar la pala con el mouse.
        - PARTE 7: Implementar el ciclo principal del juego
        - PARTE 8: Mover la pala enemiga automáticamente.
        - PARTE 9: Implementar como finalizar el juego.

NOTAS:
    - Principios de animacion y diseño a usar:
        - Estirar y Comprimir
        - Anticipación
        - Puesta en Escena
        - Acción Directa y Pose a Pose
        - Acciones Complementarias y Superpuestas
        - Ritmo

    - la relación entre las partes y los principios de animación son:
        1. Crear objetos -> Puesta en Escena
        2. Obtener posición -> Puesta en Escena
        3. Mover objetos -> Acción Directa y Pose a Pose
        4. Rebotar en bordes -> Estirar/Comprimir + Anticipación
        5. Colisiones entre objetos -> Acciones Complementarias/Superpuestas
        6. Paleta con mouse -> Acción Directa + Ritmo
        7. Ciclo del juego -> Ritmo
        8. Paleta enemiga -> Ritmo + Acciones Complementarias
        9. Final del juego -> Puesta en Escena
"""
# from src.graphics import Canvas as Lienzo
# from stanfordpy.graphics import Canvas as Lienzo
from stanfordpy.graphics import Lienzo
# IMPORTANTE: Si se ejecuta en un entorno diferente a la terminal de python
# from graphics import Lienzo
from time import sleep as esperar

# dimeniones del lienzo
ANCHO_MAX_X = 300
ALTO_MAX_Y = 500

# Radio de la pelota.
DIAMETRO_DISCO = 40

# dimensiones de la pala
ANCHO_PALA = 60
ALTO_PALA = 20

# La velocidad inicial de los objetos en la dirección x.
VEL_INICIAL_X = 5

# La velocidad inicial de los objetos en la dirección y.
VEL_INICIAL_Y = 5

# Pausa entre los fotogramas, contado en segundos.
PAUSA = 1 / 60


######################################################
# FUNCIONES PARA CREAR OBJETOS
######################################################

# TODO PARTE 1: Funciones para crear un el disco y las palas de juego.
def crear_disco(lienzo, pos_x, pos_y, diametro, color_fig, contorno_fig):
    """crear_disco crea una pelota en el lienzo dado.

    Args:
        lienzo (Lienzo): El lienzo donde se crea la pelota.
        pos_x (int): La posición x inicial de la pelota.
        pos_y (int): La posición y inicial de la pelota.
        diametro (int): El diametro de la pelota.
        color_fig (str): El color de la pelota.
        contorno_fig (str): El color del contorno de la pelota.

    Returns:
        objeto_pelota (int): El objeto pelota creado en el lienzo.
    """
    pelota = lienzo.crear_ovalo(pos_x,
                                pos_y,
                                pos_x + diametro,
                                pos_y + diametro,
                                color=color_fig,
                                contorno=contorno_fig)
    return pelota


def crear_pala(lienzo, pos_x, pos_y, largo, alto, color_fig, contorno_fig):
    """crear_pala crea una pala en el lienzo dado.

    Args:
        lienzo (Lienzo): El lienzo donde se crea la pala.
        pos_x (int): La posición x inicial de la pala.
        pos_y (int): La posición y inicial de la pala.
        largo (int): El largo de la pala.
        alto (int): El alto de la pala.
        color_fig (str): El color de la pala.
        contorno_fig (str): El color del contorno de la pala.

    Returns:
        objeto_paleta (int): El objeto pala creado en el lienzo.
    """
    pala = lienzo.crear_rectangulo(pos_x,
                                   pos_y,
                                   pos_x + largo,
                                   pos_y + alto,
                                   color=color_fig,
                                   contorno=contorno_fig)
    return pala


######################################################
# FUNCIONES PARA OBTENER LA POSICION DE LOS OBJETOS
######################################################


# TODO PARTE 2: Funciones para obtener la posición de los objetos en el lienzo.
def obtener_posicion_objeto(lienzo, objeto):
    """obtener_posicion obtener_posicion obtiene la posición horizontal y vertical (x, y) del objeto en el lienzo.

    Args:
        lienzo (Lienzo): El lienzo donde se encuentra el objeto.
        objeto (str): ID del objeto en el lienzo.

    Returns:
        tuple: una tupla con la posición (x, y) del objeto.
    """
    x = lienzo.obtener_x_izquierda(objeto)
    y = lienzo.obtener_y_superior(objeto)
    # return x, y
    return (x, y)


######################################################
# FUNCIONES PARA MOVER OBJETOS
######################################################

# TODO PARTE 3: Funciones para mover los objetos en el lienzo.
def mover_objeto(lienzo, objeto, vel_x, vel_y):
    """mover_objeto() mueve horizontal y verticalmente (x, y) el objeto en el lienzo según las velocidades dadas.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo): es el objeto a mover.
        vel_x (int): es el desplazamiento en x.
        vel_y (int): es el desplazamiento en y.
    """
    lienzo.moverse(objeto, vel_x, vel_y)


# TODO PARTE 6: Funciones para mover la pala con el mouse.
def mover_pala(lienzo, pala):
    """mover_pala() mueve la pala horizontalmente en el lienzo.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Rectangulo): es el objeto a mover.
    """
    # obtener la posicion del mouse en x
    x = lienzo.obtener_mouse_x()
    # limitar el movimiento de la pala dentro del lienzo
    x = max(ANCHO_PALA // 2, x)
    x = min(lienzo.obtener_anchura_lienzo() - ANCHO_PALA // 2, x)
    # solo se mueve horizontalmente en x
    lienzo.mover_hacia(pala,
                       x - ANCHO_PALA // 2,
                       lienzo.obtener_y_superior(pala))


######################################################
# FUNCIONES PARA DETECTAR COLISIONES
######################################################

# TODO PARTE 4: Funciones para detectar colisiones con los bordes del lienzo.

def verificar_colisiones_arena(lienzo, objeto, pos_x, pos_y, vel_x, vel_y):
    """verificar_colisiones_arena() verifica la colisión con los extremos del lienzo, cambiando la dirección de las velocidades horizontal y vertical (x, y) si es necesario.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (Ovalo, Rectangulo): es el objeto a mover.
        pos_x (float): posición x del objeto.
        pos_y (float): posición y del objeto.
        vel_x (int): desplazamiento en x.
        vel_y (int): desplazamiento en y.

    Returns:
        tuple: una tupla con las nuevas velocidades y el estado activo del objeto (vel_x, vel_y, activo).
    """
    ancho_lienzo = lienzo.obtener_anchura_lienzo()
    alto_lienzo = lienzo.obtener_altura_lienzo()
    largo_objeto = lienzo.obtener_ancho(objeto)
    alto_objeto = lienzo.obtener_altura(objeto)
    activo = True

    # 1) si choca con el borde derecho
    if pos_x > ancho_lienzo - largo_objeto:
        vel_x = vel_x * -1

    # 2) si choca con el borde inferior
    if pos_y > alto_lienzo - alto_objeto:
        vel_y = vel_y * -1
        # vel_y = 0
        # vel_x = 0
        activo = False

    # 3) si choca con el borde izquierdo
    if pos_x < 0.0:
        vel_x = vel_x * -1

    # 4) si choca con el borde superior
    if pos_y < 0.0:
        vel_y = vel_y * -1
        # vel_y = 0
        # vel_x = 0
        activo = False

    return (vel_x, vel_y, activo)


# TODO PARTE 5: Funciones para detectar colisiones entre objetos.
def verificar_colisiones_objeto(lienzo, objeto):
    """verificar_colisiones_objeto verifica las colisiones del objeto con otros objetos en el lienzo.

    Args:
        lienzo (Lienzo): es el espacio de dibujo interactivo.
        objeto (str): es el objeto a verificar colisiones.

    Returns:
        list: una lista con los IDs de los objetos que colisionan con el objeto dado.
    """
    # obtener las coordenadas del objeto para verificar colisiones (x1, y1)
    x_izq = lienzo.obtener_x_izq(objeto)
    y_sup = lienzo.obtener_y_sup(objeto)
    # obtener dimensiones del objeto para verificar colisiones (x2, y2)
    ancho = lienzo.obtener_ancho(objeto)
    alto = lienzo.obtener_altura(objeto)
    # encontrar colisiones con otros objetos en el lienzo
    colisiones = lienzo.encontrar_superposiciones(x_izq,
                                                  y_sup,
                                                  x_izq + ancho,
                                                  y_sup + alto)
    # convertir el resultado a una lista
    # colisiones = list(colisiones)
    return colisiones


def main():
    """main ejecuta el programa principal
    """
    # crear el lienzo con dimensiones
    arena = Lienzo(ANCHO_MAX_X, ALTO_MAX_Y)

    # posicion de la disco en el centro del lienzo
    px_disco = ANCHO_MAX_X // 2
    py_disco = ALTO_MAX_Y // 2

    # color de la disco
    color_disco = "azul"
    # contorno de la disco
    contorno = "verde"

    # crear la disco con posicion, diametro y color
    disco = crear_disco(arena,
                        px_disco,
                        py_disco,
                        DIAMETRO_DISCO,
                        color_disco,
                        contorno)

    # definir la velocidad inicial de la disco
    vx_disco = VEL_INICIAL_X
    vy_disco = VEL_INICIAL_Y

    # posicion inicial de la pala uno
    px_pala_a = (ANCHO_MAX_X - ANCHO_PALA) // 2
    py_pala_a = ALTO_MAX_Y - ALTO_PALA - 10

    # crear la pala uno, del usuario
    pala_a = crear_pala(arena,
                        px_pala_a,
                        py_pala_a,
                        ANCHO_PALA,
                        ALTO_PALA,
                        color_fig="negro",
                        contorno_fig="celeste")

    # posicion inicial de la pala dos
    px_pala_b = (ANCHO_MAX_X - ANCHO_PALA) // 2
    py_pala_b = 10

    # crear la pala dos, del enemigo
    pala_b = crear_pala(arena,
                        px_pala_b,
                        py_pala_b,
                        ANCHO_PALA,
                        ALTO_PALA,
                        color_fig="negro",
                        contorno_fig="rojo")

    # definir la velocidad inicial de la pala dos
    vx_pala_b = 2.3
    vy_pala_b = 0

    # # imprimir objetos creados
    # print(f"Disco ID: {disco}")
    # print(f"Paleta A (Azul) ID: {pala_a}")
    # print(f"Paleta B (Rojo) ID: {pala_b}")

    # condicion para continuar el juego
    en_juego = True

    # TODO PARTE 7: Implementar el ciclo principal del juego
    # ciclo de juego
    while en_juego is True:
        # invoco la funcion moverse del lienzo
        mover_objeto(arena, disco, vx_disco, vy_disco)

        # recupero la posicion de la disco del lienzo
        px_disco, py_disco = obtener_posicion_objeto(arena, disco)

        # condiciones de colision y fin de juego
        vx_disco, vy_disco, en_juego = verificar_colisiones_arena(arena,
                                                                  disco,
                                                                  px_disco,
                                                                  py_disco,
                                                                  vx_disco,
                                                                  vy_disco)

        # TODO PARTE 8: Mover la pala enemiga automáticamente.
        # mover la pala dos automaticamente
        mover_objeto(arena, pala_b, vx_pala_b, vy_pala_b)

        # obtener la posicion de la pala dos
        px_pala_b, py_pala_b = obtener_posicion_objeto(arena,
                                                       pala_b)

        # verificar colision de la pala dos con los bordes
        vx_pala_b, vy_pala_b, _ = verificar_colisiones_arena(arena,
                                                             pala_b,
                                                             px_pala_b,
                                                             py_pala_b,
                                                             vx_pala_b,
                                                             vy_pala_b)

        # cambiar la velocidad de la pala en el sentido de la disco
        # si la disco esta a la derecha de la pala
        if (px_disco + DIAMETRO_DISCO) // 2 > (px_pala_b + ANCHO_PALA) // 2:
            vx_pala_b = abs(vx_pala_b)
        # si la disco esta a la izquierda de la pala
        elif (px_disco + DIAMETRO_DISCO) // 2 < (px_pala_b + ANCHO_PALA) // 2:
            vx_pala_b = abs(vx_pala_b) * -1

        # mover la pala uno con el mouse
        mover_pala(arena, pala_a)

        # detectar colisiones de la disco con las paletas
        colisiones = verificar_colisiones_objeto(arena, disco)
        # print(f"Colisiones: {colisiones}")

        # procesar colisiones
        if len(colisiones) > 1:
            # print(f"Colision detectada: {colisiones}")
            # vy_disco = -1 * vy_disco
            if colisiones[1] == pala_a or colisiones[1] == pala_b:
                vy_disco = vy_disco * -1

        # pausa entre fotogramas
        esperar(PAUSA)

    # TODO PARTE 9: Implementar como finalizar el juego.
    # finalizar el juego
    arena.crear_texto(ANCHO_MAX_X // 2,
                      ALTO_MAX_Y // 2,
                      "¡Fin del Juego!",
                      fuente="Arial",
                      tamano=24,
                      color="rojo",
                      ancla="center")
    esperar(5)


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
