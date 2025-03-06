import tkinter as tk
from tkinter import scrolledtext, ttk
from lexer import analizar_texto

# Función para analizar el código y mostrarlo en la tabla
def analizar_codigo():
    texto_codigo = entrada_texto.get("1.0", tk.END).strip()  # Obtener el contenido
    if not texto_codigo:
        return  # No hacer nada si está vacío

    resultado = analizar_texto(texto_codigo)  # Llamar a lexer.py

    # Limpiar la tabla antes de agregar nuevos datos
    for item in tabla.get_children():
        tabla.delete(item)

    # Dividir el resultado en líneas y agregar cada token a la tabla
    lineas = resultado.split("\n")[2:]  # Omitimos el encabezado de la tabla
    for linea in lineas:
        if linea.strip():  # Evitar líneas vacías
            partes = linea.split("\t")  # Usamos tabulación como separador
            if len(partes) >= 3:  # Nos aseguramos de que haya tres elementos
                token = partes[0]  # El primer elemento es el token
                categoria = partes[1]  # Segundo elemento: categoría
                linea_numero = partes[2]  # Tercer elemento: número de línea
                tabla.insert("", "end", values=(token, categoria, linea_numero))  # Insertar en la tabla

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador léxico")  # Título de la ventana
ventana.geometry("1200x800")  # Establecer tamaño de la ventana

# Etiqueta para ingresar el texto
etiqueta = tk.Label(ventana, text="Ingresa el lexema:")
etiqueta.pack()  # Agregar a la ventana

# Área de texto para ingresar código
entrada_texto = scrolledtext.ScrolledText(ventana, width=70, height=20)  # Configuración del tamaño
entrada_texto.pack()  # Agregar a la ventana

# Botón para analizar el código
boton_analizar = tk.Button(ventana, text="Analizar código", command=analizar_codigo)
boton_analizar.pack(pady=10)  # Margen vertical de 10 píxeles

# Crear la tabla (Treeview) con tres columnas
tabla = ttk.Treeview(ventana, columns=("Token", "Categoría", "Línea"), show="headings")
tabla.heading("Token", text="Token")
tabla.heading("Categoría", text="Categoría")
tabla.heading("Línea", text="Línea")
tabla.column("Token", width=200)
tabla.column("Categoría", width=200)
tabla.column("Línea", width=80)
tabla.pack(expand=True, fill="both")  # Expandir y llenar el espacio disponible

# Ejecutar la aplicación
ventana.mainloop()
