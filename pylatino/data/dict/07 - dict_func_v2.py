"""
Este modulo es el codigo guia para los conceptos de diccionario de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo introduce los diccionarios en Python e incluye:
        - PARTE 1: Retomando el concepto llave-valor, crear diccionarios.
        - PARTE 2: Propiedades del diccionario: keys, values, items.
        - PARTE 3: Iterar sobre diccionarios (keys, values, items).


NOTAS:
    - Un diccionario almacena pares (llave, valor).
    - Las llaves suelen ser strings o números (deben ser inmutables, es decir no cambiar).
    - Acceso y modificación son muy rápidas.
"""


# definicion de la funcion principal
def main():
    print("===== Funciones en diccionarios =====")

    # TODO PARTE 1: retomando el concepto llave-valor
    print("\n--- PARTE 1: Pareja Llave-valor ---")

    # Diccionario simple: {titulo: autor}
    autores_por_titulo = {
        "Rayuela": "Julio Cortázar",
        "Ficciones": "Jorge Luis Borges",
        "Aura": "Carlos Fuentes",
        "Delirio": "Laura Restrepo",
    }
    print("* Diccionario (titulo: autor):")
    print("\tdict:", autores_por_titulo)

    # TODO PARTE 2: propiedades del diccionario: keys, values, items
    print("\n--- PARTE 2: Acceso y modificación directa ---")

    items = autores_por_titulo.items()
    print("\titems():", items)

    keys = autores_por_titulo.keys()
    print("\tkeys():", keys)

    values = autores_por_titulo.values()
    print("\tvalues():", values)

    # TODO PARTE 3: iterar sobre diccionarios (keys, values, items)
    print("\n--- PARTE 3: Iterar sobre diccionarios ---")
    print("\n* Iterar sobre items:")
    for titulo, autor in autores_por_titulo.items():
        print("\tTítulo:", titulo, "| Autor:", autor)

    print("\n* Iterar sobre keys y modificar valores:")
    for titulo in autores_por_titulo.keys():
        print("\tTítulo (key):", titulo)

    print("\n* Modificando los títulos a mayúsculas:")
    for titulo in autores_por_titulo:
        print("\tTítulo (sinónimo):", titulo)
        libro = autores_por_titulo[titulo]
        print("\tLibro obtenido:", libro)
        autores_por_titulo[titulo] = libro.upper()
        print("\tLibro modificado:", autores_por_titulo[titulo])

    print("\nAhora los autores:", autores_por_titulo)

    print("\n* Iterar sobre values:")
    for autor in autores_por_titulo.values():
        print("\tAutor (value):", autor)


if __name__ == "__main__":
    main()
    print("============================================================")
    print("Fin de las funciones con diccionarios.")
