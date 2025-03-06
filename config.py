#El objetivo de este archivo es almacenar listas de palabras clave, símbolos y signos de puntuación
# que utilizaremos para el análisis léxico

"""
Aquí definimos listas de:
- Palabras reservadas
- Operadores comunes
- Símbolos
- Signos de puntuación

"""

# Palabras reservadas de (palabras clave del lenguaje)
palabras_reservadas = {
    "if", "else", "while", "for", "return",
    "int", "float", "double", "char", "bool",
    "void", "cout"
}

#Operadores comunes en (matemáticos, lógicos y asignación)
operadores = {
    "+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=",
    "<=", "&&", "||", "<<", ">>"
}

#Símbolos utilizados en expresiones (paréntesis y llaves)
simbolos = {"(", ")", "{", "}", "[", "]"}

#Signos de puntuación
signos_puntuacion = {",", ";", ":"}