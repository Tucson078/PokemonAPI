import tkinter as tk

def mi_comando(nombre):
    print(f"¡Hola, {nombre}!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Botón con Comando y Argumento")

# Crear un botón con un comando que pasa un argumento
nombre = "Usuario"
boton = tk.Button(ventana, text="Saludar", command=lambda: mi_comando(nombre))
boton.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
