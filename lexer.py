import re  # Importamos la librería de expresiones regulares
from config import palabras_reservadas, operadores, simbolos, signos_puntuacion  # Importamos las listas

def analizar_texto(texto):
    """
    Recibe un código fuente como texto y lo analiza léxicamente,
    ignorando los comentarios y asignando el número de línea a cada token.

    Devuelve una tabla con los tokens, sus categorías y su número de línea.
    """
    # Eliminar comentarios antes de analizar los tokens
    texto = re.sub(r"//.*", "", texto)  # Eliminar comentarios de una línea (// ...)
    texto = re.sub(r"/\*.*?\*/", "", texto, flags=re.DOTALL)  # Eliminar comentarios de múltiples líneas (/* ... */)

    # Dividir el código en líneas para obtener el número de línea
    lineas = texto.split("\n")

    # Estructura del resultado en formato de tabla
    resultado = "TOKEN\t\tCATEGORÍA\tLÍNEA\n"
    resultado += "-" * 40 + "\n"

    # Analizar línea por línea
    for num_linea, linea in enumerate(lineas, start=1):  # `num_linea` empieza en 1
        # Expresión regular mejorada para incluir cadenas de texto
        patron = r"\".*?\"|[a-zA-Z_][a-zA-Z0-9_]*|\d+|[{}()\[\],;:+\-*/=!<>]|<<|>>|==|!="
        tokens = re.findall(patron, linea)  # Buscar tokens en la línea actual

        # Clasificar cada token
        for token in tokens:
            if token.startswith('"') and token.endswith('"'):  # Si empieza y termina con `"`
                categoria = "Cadena de texto"
            elif token in palabras_reservadas:
                categoria = "Palabra reservada"
            elif token in operadores:
                categoria = "Operador"
            elif token in simbolos:
                categoria = "Símbolo"
            elif token in signos_puntuacion:
                categoria = "Signo de puntuación"
            elif token.isdigit():  # Si el token es un número
                categoria = "Constante"
            else:
                categoria = "Identificador"

            # Agregar token, categoría y número de línea al resultado
            resultado += f"{token}\t{categoria}\t{num_linea}\n"

    return resultado  # Devolvemos el resultado en forma de tabla.
