# usa graficos, funciones, flujo de control, algoritmos y estructuras
"""
la animacion toma un arreglo de libros y sigue los siguiente pasos:
    1) crea un lienzo de 400x400
    2) crea la repisa vacia
    3) agrega libros en la repisa
    4) selecciona un criterio de orden para los libro y los ordena
    5) elimina al asar un libro hasta dejar la repisa vacia
    6) reinicia el proceso en el paso 3)

la idea es practicar los conceptos de estructuras de datos, despomposicion, algoritmos, funciones y flujo de control para hacer el programa
"""
# imports nativos
from time import sleep as esperar
import random

# import de CS Bridge Graphics
from stanfordpy.graphics import create_canvas
# from stanfordpy.graphics import crear_lienzo


# from graphics import Lienzo

ANCHO_LIENZO = 400
ALTO_LIENZO = 400
PAUSA = 1 / 16


def seleccionar_libro(libros: list) -> dict:
    """seleccionar_libro elige un libro al azar de una lista de libros.

    Args:
        libros (list): lista de libros disponibles.

    Returns:
        dict: un libro seleccionado al azar de la lista, o None si la lista está vacía.
    """
    libro = None
    if libros:
        libro = random.choice(libros)
    return libro


def extraer_libro(libros: list) -> dict:
    """extraer_libro elimina un libro al azar de una lista de libros.

    Args:
        libros (list): lista de libros disponibles.

    Returns:
        dict: un libro eliminado al azar de la lista, o None si la lista está vacía.
    """
    libro = None
    if libros:
        idx = random.randint(0, len(libros) - 1)
        libro = libros.pop(idx)
    return libro


def seleccionar_criterio_orden(libro: dict) -> str:
    llave = None
    if libro:
        # selecciona una llave al azar de las llaves del libro
        llaves = list(libro.keys())
        idx = random.randint(0, len(llaves) - 1)
        llave = llaves[idx]
    return llave


def criterio_orden_libro(criterio):
    def key_func(libro):
        return libro.get(criterio, '')
    return key_func


def ordenar_libros(repisa: list, criterio: str) -> list:
    """ordenar_libros ordena una lista de libros por un criterio dado.

    Args:
        repisa (list): lista de libros en la repisa.
        criterio (str): criterio por el cual ordenar los libros.

    Returns:
        list: lista de libros ordenada por el criterio dado.
    """
    if not repisa or not criterio:
        return repisa
    # return sorted(repisa, key=lambda libro: libro.get(criterio, ''))
    return sorted(repisa, key=criterio_orden_libro(criterio))


def adicionar_libro(repisa: list, libro: dict) -> None:
    """adicionar_libro adiciona un libro al final de la repisa.

    Args:
        repisa (list): lista de libros en la repisa.
        libro (dict): libro disponible
    """
    repisa.append(libro)


def crear_repisa(interfaz, repisa: list) -> None:
    objetos = []
    return interfaz, objetos


def actualizar_repisa(interfaz, objetos: list) -> list:
    return objetos


def main():
    # inicializa la repisa de libros, list + dict
    libros = [
        {
            "titulo": "Rayuela",
            "autor": "Julio Cortázar",
            "paginas": 746,
            "publicado": "junio 16, 2008",
            "ISBN": 9788437624747,
            "online": False,
        },
        {
            "titulo": "Ficciones",
            "autor": "Jorge Luis Borges",
            "paginas": 218,
            "publicado": "enero 1, 1997",
            "ISBN": 9788420633121,
            "online": True,
        },
        {
            "titulo": "Aura",
            "autor": "Carlos Fuentes",
            "paginas": 79,
            "publicado": "enero 1, 1996",
            "ISBN": 9580425140,
            "online": True,
        },
        {
            "titulo": "Delirio",
            "autor": "Laura Restrepo",
            "paginas": 311,
            "publicado": "enero 1, 2013",
            "ISBN": 9789584233134,
            "online": False,
        },
        {
            "titulo": "Poesía completa",
            "autor": "Maria Mercedes Carranza",
            "paginas": 158,
            "publicado": "enero 1, 2019",
            "ISBN": 9789585404410,
            "online": False,
        },
    ]

    # crea repisa vacia
    repisa = list()
    # creo el lienzo vacio
    interfaz = create_canvas(ANCHO_LIENZO, ALTO_LIENZO)
    # dibujar repisa vacia y guardar listado de figuras de la interfaz
    interfaz, objetos = crear_repisa(interfaz, repisa)
    trabajar = True
    while trabajar:
        # seleccionar un libro al azar de la lista de libros
        libro = extraer_libro(libros)
        # selecciona una propiedad/llave para ordenar los libros de la lista
        propiedad = seleccionar_criterio_orden(libro)
        # agrega el libro a la repisa
        adicionar_libro(repisa, libro)
        # ordenar la repisa por la propiedad seleccionada
        repisa = ordenar_libros(repisa, propiedad)
        orden = str()
        for libro in repisa:
            orden += "'" + str(libro[propiedad]) + "', "
        print(orden, propiedad)
        # si no hay libros disponibles
        if len(libros) == 0:
            # limpiar la repisa
            libros = repisa
            repisa = []
            print("limpio", len(libros), len(repisa))
        # actualizar el dibujo de la repisa en la interfaz
        objetos = actualizar_repisa(interfaz, objetos)
        # esperar un poco
        esperar(1.0)
        # IMPORTANTE: solo se necesita en local
        # interfaz.()
        # cerrar el lienzo
        # interfaz.mainloop()


if __name__ == '__main__':
    main()
