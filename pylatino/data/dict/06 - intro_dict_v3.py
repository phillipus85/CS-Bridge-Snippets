"""
Este modulo es el codigo guia para los conceptos de diccionario de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo introduce los diccionarios en Python e incluye:
        - PARTE 1: Concepto llave-valor, crear diccionarios y sinonimos.
        - PARTE 2: Acceso directo por llave + modificación directa.
        - PARTE 3: uso del comando IN y LEN para prevenir errores.
        - PARTE 4: Funciones básicas: get, update, pop.

NOTAS:
    - Un diccionario almacena pares (llave, valor).
    - Las llaves suelen ser strings o números (deben ser inmutables, es decir no cambiar).
    - Acceso y modificación son muy rápidas.
"""


# definicion de la funcion principal
def main():
    print("===== Introducción a diccionarios =====")

    # Datos base (mismos que en listas)
    repisa = [
        "Rayuela, Julio Cortázar",          # 0
        "Ficciones, Jorge Luis Borges",     # 1
        "Aura, Carlos Fuentes",             # 2
        "Delirio, Laura Restrepo",          # 3
    ]

    # # lista de titulos
    # titulos = [
    #     "Rayuela",
    #     "Ficciones",
    #     "Aura",
    #     "Delirio"
    # ]
    # # lista de autores
    # autores = [
    #     "Julio Cortázar",
    #     "Jorge Luis Borges",
    #     "Carlos Fuentes",
    #     "Laura Restrepo"
    # ]
    # variable para almacenar el autor, evito errrores en el esquema
    autor = None

    # TODO PARTE 1: Concepto llave-valor, crear diccionarios y sinonimos.
    print("\n--- PARTE 1: Llave-valor, crear diccionarios y sinónimos ---")

    # 1.1 Crear diccionarios vacíos
    # diccionario vacio
    repisa = {}

    # sinonimo con dict
    sinonimo = dict()

    # verificar contenido
    print("\t'repisa':", repisa, "'sinonimo':", sinonimo)
    print("\tTipo de 'repisa':", type(repisa), "y 'sinonimo':", type(sinonimo))
    print("\tSon diccionarios iguales vacios?", repisa == sinonimo)

    # 1.2 Crear diccionarios con datos
    # Diccionario literal: {titulo: autor}
    repisa = {
        "Rayuela": "Julio Cortázar",
        "Ficciones": "Jorge Luis Borges",
        "Aura": "Carlos Fuentes",
        "Delirio": "Laura Restrepo",
    }

    sinonimo = dict(repisa)  # sinonimo con dict()
    sinonimo = dict(
        Rayuela="Julio Cortázar",
        Ficciones="Jorge Luis Borges",
        Aura="Carlos Fuentes",
        Delirio="Laura Restrepo"
    )

    # verificar contenido
    print("\t'repisa':", repisa, "'sinonimo':", sinonimo)
    print("\tTipo de 'repisa':", type(repisa), "y 'sinonimo':", type(sinonimo))
    print("\tSon diccionarios iguales vacios?", repisa == sinonimo)

    # TODO PARTE 2: Acceso directo por llave + modificación directa.
    print("\n--- PARTE 2: Acceso y modificación directa por llaves---")

    # 2.1 Acceso directo por llave (rápido)
    titulo = "Rayuela"
    autor = repisa[titulo]

    print("\tAutor de 'Rayuela':", autor)

    # 2.2 Modificación directa
    autor_editado = "J. CORTÁZAR"
    repisa[titulo] = autor_editado

    print("\tAutor de 'Rayuela' (modificado):", repisa[titulo])

    # 2.3 Agregar nuevo libro directamente
    repisa["La hojarasca"] = "Gabriel García Márquez"

    print("\tAutor de 'La hojarasca':", repisa["La hojarasca"])
    print("\tDict después de agregar:", repisa)

    # 2.4 Consultar directamente llave que no existe, ERROR!!!
    # autor = repisa["Pedro Páramo"]  # KeyError

    # print("\tAutor de 'Pedro Páramo':", autor)

    # TODO PARTE 3: uso del comando IN y LEN para prevenir errores.
    print("\n--- PARTE 3: Uso de IN y LEN para prevenir errores ---")

    # 3.1 usar IN para verificar existencia de llave
    if "Aura" in repisa:
        print("\tAutor de 'Aura':", repisa["Aura"])
    else:
        print("\tTítulo no disponible")

    # 3.2 usar IN para verificar una llave inexistente
    if "Pedro Páramo" in repisa:
        print("\tAutor de 'Pedro Páramo':", repisa["Pedro Páramo"])
    else:
        print("\tTítulo no disponible")

    # 3.3 consultar el tamaño del diccionario
    cantidad_libros = len(repisa)
    print("\tTamaño de 'repisa':", cantidad_libros)

    # integrarlo a flujos de control para confirmar si una repisa está vacía
    if len(repisa) > 0:
        print("\tLa repisa tiene libros.")
    else:
        print("\tLa repisa está vacía.")

    # TODO PARTE 4: Funciones básicas: get, update, pop.
    print("\n--- PARTE 4: Funciones básicas (get, update, pop) ---")

    # 4.1 recuperar llave/autor
    titulo = "Ficciones"
    autor = repisa.get(titulo)
    print("\tAutor de 'Ficciones':", autor)

    # recuperar llave/autor inexistente
    autor = repisa.get("La Vorágine")
    print("\tAutor de 'La Vorágine':", autor)

    # recuperar llave/autor inexistente con valor por defecto
    autor = repisa.get("La Vorágine", "DESCONOCIDO")
    print("\tAutor de 'La Vorágine':", autor)

    # 4.2 agregar nuevo libro
    nuevo_libro = {
        "La Vorágine": "José Eustasio Rivera"
    }
    # actualizar el diccionario con el nuevo libro
    repisa.update(nuevo_libro)
    print("\tDict después de agregar nuevo libro:", repisa)

    # actualizar libros con nueva información
    nuevo_libro = {
        "La Vorágine": "José Eustasio Rivera",
        "Rayuela": "Julio Cortázar",
    }
    # actualizar el diccionario con el nuevo libro
    repisa.update(nuevo_libro)
    print("\tDict después de agregar nuevo libro:", repisa)

    # 4.3 eliminar un libro
    titulo = "Aura"
    autor_eliminado = repisa.pop(titulo)
    print("\tAutor eliminado de:", titulo, "es:", autor_eliminado)

    # eliminar llave inexistente, ERROR!
    autor_eliminado = repisa.pop(titulo, None)
    print("\tAutor eliminado de:", titulo, "es:", autor_eliminado)

    # eliminar llave inexistente, sin error
    autor_eliminado = repisa.pop(titulo, "DESCONOCIDO")
    print("\tAutor eliminado de:", titulo, "es:", autor_eliminado)


if __name__ == "__main__":
    main()
    print("============================================================")
    print("Fin de la introducción a diccionarios.")
