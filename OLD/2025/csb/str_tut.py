def encontrar_palabras_largas(palabra: list, n: int = 7) -> list:
    """encontrar_palabras_largas encuentra palabras con más de n caracteres.

    Args:
        palabra (list): lista de palabras.
        n (int): número mínimo de caracteres.

    Returns:
        list: lista de palabras que tienen más de n caracteres.
    """
    res = []
    for p in palabra:
        if len(p) >= n:
            res.append(p)
    # return [p for p in palabra if len(p) > n]
    return res


if __name__ == "__main__":
    # texto = "Quiero leer 5 libros. ¡Rayuela, Ficciones, Aura, Delirio y dioses menores en Python!"
    texto = "Quiero leer 4 libros. Rayuela, Ficciones, Aura, Delirio. ¡Y lo haré en Python!"
    alt = texto
    print(texto)
    palabras = texto.split()
    texto = " ".join(palabras)
    # print(recostruido)
    print(palabras)
    # poner todo en minusculas
    texto = texto.upper()
    print(texto)
    texto = texto.lower()
    # quitar simbolos de puntuación
    texto = texto.strip(".,¡!")
    texto = texto.replace("¡", "")
    print(texto)
    # separar palabras
    palabras = texto.split()
    print(palabras)

    palabras = [palabra.strip(".,¡!") for palabra in palabras]
    print(palabras)
    largas = encontrar_palabras_largas(palabras, 7)
    print(largas)

    # proc = alt.lower()
    # frases = proc.split(".")

    # palabras = []
    # for frase in frases:
    #     print(frase)
    #     frase = frase.strip(".,¡!")
    #     frase = frase.replace("¡", "")
    #     palabras.extend(frase.split())

    # print(palabras)

    # print("rayuela" in palabras)

    # palabras = ["inteligencia", "leer", "placer", "transforma", "forma"]
    n = 7
    palabras_largas = list(filter(lambda p: len(p) >= n, palabras))
    print(palabras_largas)
