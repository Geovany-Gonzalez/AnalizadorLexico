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
    #python
    "def", "class", "if", "elif", "else", "while", "for", "break",
    "continue", "import", "from", "try", "except",
    "finally", "and", "or", "not", "is", "in"
    #javascript
    "function", "var", "let", "const",
    "return","catch",
    "new", "delete", "extends", "super", "this", "null",
    "undefined", "true", "false","export"
    #java
    "public", "private", "protected", "static", "void",
    "switch", "case", "package","implements"
    #c/c++
    "int", "float", "double", "decimal", "string",
    "readonly", "abstract", "interface", "namespace"
}

#Operadores comunes en (matemáticos, lógicos y asignación)
operadores = {
    "+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=",
    "<=", "&&", "||", "<<", ">>"
     "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "%"
     
}

#Símbolos utilizados en expresiones (paréntesis y llaves)
simbolos = {"(", ")", "{", "}", "[", "]"}

#Signos de puntuación
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
    #python
    "def", "class", "if", "elif", "else", "while", "for", "break",
    "continue", "import", "from", "try", "except",
    "finally", "and", "or", "not", "is", "in"
    #javascript
    "function", "var", "let", "const",
    "return","catch",
    "new", "delete", "extends", "super", "this", "null",
    "undefined", "true", "false","export"
    #java
    "public", "private", "protected", "static", "void",
    "switch", "case", "package","implements"
    #c/c++
    "int", "float", "double", "decimal", "string",
    "readonly", "abstract", "interface", "namespace"
}

#Operadores comunes en (matemáticos, lógicos y asignación)
operadores = {
    "+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=",
    "<=", "&&", "||", "<<", ">>"
     "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "%"
     
}

#Símbolos utilizados en expresiones (paréntesis y llaves)
simbolos = {"(", ")", "{", "}", "[", "]"}

#Signos de puntuación
signos_puntuacion = {",", ";", ":"}
