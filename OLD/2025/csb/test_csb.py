
from stanfordpy.graphics import create_canvas
# from stanfordpy.graphics import crear_lienzo


# from graphics import Lienzo

ANCHURA_LIENZO = 400
ALTURA_LIENZO = 400


def menu_repisa() -> int:
    # imprime en consola menu principal
    print("=== MENU DE LIBROS ===")
    print("\t1) Agregar libro al inicio.")
    print("\t2) Extraer libro del final.")
    print("\t3) Examinar libro en:")
    print("\t4) buscar libro por:")
    print("\t5) Ordenar repisa por:")
    print("\t6) Salir.")
    opt = int(input("seleccione la opción que necesite: "))
    # responde la selección del usuario
    return opt


def opt1(repisa: list, libro: dict) -> None:
    # agrega un libro al inicio de la repisa
    repisa.insert(0, libro)
    print(f"Libro {libro['titulo']} agregado al inicio de la repisa.")


def opt2(repisa: list) -> None:
    # extrae un libro del final de la repisa
    if repisa:
        libro = repisa.pop()
        print(f"Libro {libro['titulo']} extraído del final de la repisa.")
    else:
        print("La repisa está vacía, no se puede extraer ningún libro.")


def opt3(repisa: list, indice: int) -> None:
    # examina un libro en la repisa por su índice
    if 0 <= indice < len(repisa):
        libro = repisa[indice]
        msg = f"Examinando libro en el índice {indice}:"
        msg += f" {libro['titulo']} de {libro['autor']}."
        print(msg)
    else:
        print("Índice fuera de rango, no se puede examinar el libro.")


def opt4(repisa: list, llave: str, valor) -> None:
    # busca un libro en la repisa por una llave y un valor
    idx = buscar_idx_libro(repisa, llave, valor)
    if idx != -1:
        libro = repisa[idx]
        msg = f"Libro encontrado: {libro['titulo']} de {libro['autor']}."
        print(msg)
    else:
        print(f"No se encontró ningún libro con {llave} = {valor}.")


def opt5(repisa: list, llave: str) -> None:
    # ordena la repisa de libros por una llave específica
    ordenar_repisa(repisa, llave)
    print(f"Repisa ordenada por {llave}.")


def buscar_idx_libro(repisa: list, llave: str, valor) -> int:
    # entra una repisa con libros, la llave y el valor a buscar
    idx = -1
    i = 0
    for libro in repisa:
        campo = libro.get(llave)
        if campo == valor:
            idx = i
        i = i + 1
    # responde el indice donde esta el libro, -1 si no está
    return idx


def ordenar_repisa(repisa: list, llave: str) -> None:
    # ordena la repisa de libros por una llave específica
    try:
        repisa.sort(key=lambda libro: libro[llave])
        print(f"Repisa ordenada por {llave}.")
    except KeyError:
        print(f"La llave '{llave}' no existe en los libros.")


def main():
    # inicializa la repisa de libros, list + dict
    repisa = [
        {
            "titulo": "Rayuela",
            "autor": "Julio Cortázar",
            "paginas": 746,
            "publicacion": "junio 16, 2008",
            "ISBN": 9788437624747,
            "online": False,
        },
        {
            "titulo": "Ficciones",
            "autor": "Jorge Luis Borges",
            "paginas": 218,
            "publicacion": "enero 1, 1997",
            "ISBN": 9788420633121,
            "online": True,
        },
        {
            "titulo": "Aura",
            "autor": "Carlos Fuentes",
            "paginas": 79,
            "publicacion": "enero 1, 1996",
            "ISBN": 9580425140,
            "online": True,
        },
        {
            "titulo": "Delirio",
            "autor": "Laura Restrepo",
            "paginas": 311,
            "publicacion": "enero 1, 2013",
            "ISBN": 9789584233134,
            "online": False,
        },
    ]

    # libro de ejemplo para agregar al inicio
    libro = {
        "ttulo": " Poesía completa",
        "autor": "Maria Mercedes Carranza",
        "paginas": 158,
        "publicacion": "enero 1, 2019",
        "ISBN": 9789585404410,
        "online": False,
    }

    trabajar = True
    while trabajar:
        # imprime el menu de opciones
        opt = menu_repisa()

        if opt == 1:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            paginas = int(input("Ingrese el número de páginas: "))
            publicacion = input("Ingrese la fecha de publicación: ")
            ISBN = input("Ingrese el ISBN del libro: ")
            online = input("¿Está disponible en línea? (sí/no): ").lower() == 'sí'
            libro = {
                "titulo": titulo,
                "autor": autor,
                "paginas": paginas,
                "publicacion": publicacion,
                "ISBN": ISBN,
                "online": online,
            }
            opt1(repisa, libro)

        elif opt == 2:
            opt2(repisa)

        elif opt == 3:
            indice = int(input("Ingrese el índice del libro a examinar: "))
            opt3(repisa, indice)

        elif opt == 4:
            llave = input("Ingrese la llave a buscar (ej. 'titulo', 'autor'): ")
            valor = input(f"Ingrese el valor para {llave}: ")
            opt4(repisa, llave, valor)

        elif opt == 5:
            llave = input("Ingrese la llave por la que ordenar (ej. 'titulo', 'autor'): ")
            opt5(repisa, llave)

        elif opt == 6:
            print("Saliendo del programa.")
            trabajar = False

        else:
            print("Opción no válida, por favor intente de nuevo.")

    lienzo = create_canvas(ANCHURA_LIENZO, ALTURA_LIENZO)
    lienso
    lienzo.set_background_color("white")


if __name__ == '__main__':
    main()