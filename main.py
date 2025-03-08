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
ventana.title("Analizador Léxico")  # Título de la ventana
ventana.geometry("1200x800")  # Establecer tamaño de la ventana
ventana.config(bg="#2C3E50")  # Color de fondo azul marino

# Estilo general de la fuente
fuente = ("Arial", 12)

# Etiqueta para ingresar el texto
etiqueta = tk.Label(ventana, text="Ingresa el código:", fg="white", bg="#2C3E50", font=("Arial", 14))
etiqueta.pack(pady=10)  # Agregar a la ventana

# Área de texto para ingresar código
entrada_texto = scrolledtext.ScrolledText(ventana, width=70, height=20, font=fuente, bg="#ECF0F1", fg="#2C3E50", bd=2, relief="groove")
entrada_texto.pack(pady=10)  # Agregar a la ventana

# Botón para analizar el código
boton_analizar = tk.Button(ventana, text="Analizar código", command=analizar_codigo, font=("Arial", 12), bg="#3498DB", fg="white", relief="raised", bd=2)
boton_analizar.pack(pady=20)  # Margen vertical de 20 píxeles

# Crear la tabla (Treeview) con tres columnas
tabla = ttk.Treeview(ventana, columns=("Token", "Categoría", "Línea"), show="headings", height=10)
tabla.heading("Token", text="Token")
tabla.heading("Categoría", text="Categoría")
tabla.heading("Línea", text="Línea")
tabla.column("Token", width=200, anchor="w")
tabla.column("Categoría", width=200, anchor="w")
tabla.column("Línea", width=80, anchor="center")

# Estilo para la tabla
tabla.tag_configure("even", background="#D5DBDB")
tabla.tag_configure("odd", background="#BDC3C7")

tabla.pack(expand=True, fill="both", padx=20, pady=10)  # Expandir y llenar el espacio disponible

# Agregar estilo personalizado a las columnas
for col in tabla["columns"]:
    tabla.heading(col, text=col, anchor="center")
    tabla.column(col, anchor="center")

# Ejecutar la aplicación
ventana.mainloop()