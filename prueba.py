import tkinter as tk
from ApiPoke import Pokemon
import requests
from PIL import Image,ImageTk
from io import BytesIO

def mostrar_imagen_desde_url (url):
        response = requests.get(url)
        imagen_data = BytesIO(response.content)
        image = Image.open(imagen_data)
        photo = ImageTk.PhotoImage(image)
        label_imagen.config(image=photo)
        label_imagen.image = photo

Ventana = tk.Tk()
Ventana.title("Imagen desde URL")

label