# Basado en "Beat peatry", URL: https://blog.trinket.io/writing-poetry-in-python/
# y en "Haiku Generator in Python", URL: https://www.101computing.net/haiku-generator-in-python/
# dependencias literarias
from random import choice
from random import randint

URL = "https://blog.trinket.io/writing-poetry-in-python/"

# lista de palabras importantes
adjetivos = [
    "borrascoso", "caluroso", "frio", "nublado", "lluvioso",
    "soleado", "amarillo", "azul", "verde", "gris", "blanco", "rojo",
    "negro", "emocionante", "productivo", "ingenioso", "interesante",
    "creativo", "elegante", "delicado", "complicado", "caótico", "ordenado",
    "divertido", "imperfecto", "curioso", "burlón", "entrometido", "disruptivo"
]

sustantivos = [
    "compañero", "Depto. de Sistemas", "oficina", "ML", "laboratorio", "Uniandes", "escritorio", "computador", "interfaz", "consola de comandos", "teclado", "pantalla", "balón", "cafe", "ventana"
]

intangibles = [
    "investigación", "sistema", "conciencia", "creatividad", "diagrama",
    "programa", "pixel", "código", "documentación", "proceso",
    "arquitectura", "software", "inteligencia artificial",
    "formato", "experimento", "artículo"
]

naturaleza = [
    "cielo", "estrella", "atardecer", "lluvia", "sol", "nube",
    "luna", "aire", "planta", "viento", "montaña", "calor",
    "arbol", "bosque", "Monserrate"
]

verbos = [
    "trabajar", "leer", "escribir", "dibujar", "programar", "diseñar",
    "organizar", "planear", "editar", "escapar", "dormir",
    "descansar", "comer", "molestar"
]

tiempos = [
    "mañana", "tarde", "noche", "día",
    "mes", "semana", "semestre", "mediodía"
]

estados = [
    "feliz", "concentrado", "distraído", "cansando", "entretenido",
    "aburrido", "alegre", "emocionado", "creativo", "calmado",
    "estresado", "fascinado", "desconcertado"
]

conectores = [
    "y", "pero", "si", "de", "entonces", "así", "luego", "mientras",
    "en", "para", "por", "a", "tal vez", "tal"
]


# Escojo palabra
def palabra(palabras):
    """palabra _summary_

    Args:
        palabras (_type_): _description_

    Returns:
        _type_: _description_
    """
    return palabras[randint(0, len(palabras) - 1)]


# Creo un poema que parece haiku
def poemaTipoHaiku():
    """poemaTipoHaiku _summary_

    Returns:
        _type_: _description_
    """
    haiku = palabra(adjetivos) + " " + palabra(sustantivos) + " " + palabra(conectores) + " " + palabra(intangibles) + " " + palabra(adjetivos) + ",\n"
    haiku = haiku + palabra(naturaleza) + " " + palabra(adjetivos) + ", " + palabra(verbos) + " " + palabra(estados) + " " + palabra(conectores) + " " + palabra(tiempos) + " " + palabra(adjetivos) + ",\n"
    haiku = haiku + palabra(conectores) + " " + palabra(sustantivos) + " " + palabra(adjetivos) + ", " + palabra(verbos) + " " + palabra(estados) + "."

    return haiku


# nombro lo que parece un haiku
def tituloHaiku(haiku):
    """tituloHaiku _summary_

    Args:
        haiku (_type_): _description_

    Returns:
        _type_: _description_
    """
    palabras = haiku.split()
    exclusiones = estados + conectores
    for pal in palabras:
        if pal in exclusiones:
            palabras.pop(palabras.index(pal))

    titulo = "\n" + "=" * 24
    titulo += " Me parece... " + choice(palabras)
    titulo += " " + "=" * 24
    return titulo


# escribir los poemas
if __name__ == "__main__":

    # intento 3 poemas
    for i in range(0, 5):

        haiku = str()
        haiku = poemaTipoHaiku()
        titulo = tituloHaiku(haiku)
        print(titulo)
        print(haiku)

    # creditos
    print("\n\nCreado por sa-artea & mp.apolinar10 @Uniandes")
    print("Basado en 'Beat peatry', URL: ", URL, "\n")
