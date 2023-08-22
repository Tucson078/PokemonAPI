
import tkinter
from ApiPoke import Pokemon
import requests
from PIL import Image,ImageTk
from io import BytesIO
import tkinter as tk


class Pokedex():
    nombrepoke = ""
    image_url = ""


    def __init__(self):
        self.a = Pokemon()
        self.a.obtenerDatosPoke()
        self.pokedexx = tkinter.Tk()
        self.pokedexx.title("Pokedex")
        self.pokedexx.resizable(height=0,width=0)
        self.pokedexx.geometry("300x500")
        self.image_url = self.a.img


        self.f1 = tkinter.Frame(self.pokedexx,bg="Red", width=300, height=50)
        self.f1.grid()

        self.f2 = tkinter.Label(self.pokedexx,text = self.nombrepoke, bg="White")
        self.f2.grid(column=0,row=2)

        self.imagenpoke = tkinter.Label(self.pokedexx, bg="White")
        self.imagenpoke.grid(column=0,row=3)
        self.datospoke = tkinter.Frame(self.pokedexx,bg="White")        

        self.fila1 = tkinter.Label(self.datospoke,text  = (self.a.vida))
        self.fila2 = tkinter.Label(self.datospoke,text = (self.a.atk))
        self.fila3 = tkinter.Label(self.datospoke, text = (self.a.defensa))
        self.fila4 = tkinter.Label(self.datospoke,text  = (self.a.specialAtk))
        self.fila5 = tkinter.Label(self.datospoke,text = (self.a.velocidad))
        self.fila1.grid(column=0, row=1)
        self.fila2.grid(column=0, row=2)
        self.fila3.grid(column=0, row=3)
        self.fila3.grid(column=0, row=4)
        self.fila3.grid(column=0, row=5)

        self.datospoke.grid(column=1,row=3)

        self.fila1.grid(column=0, row=0)
        self.fila2.grid(column=0, row=1)
        self.fila3.grid(column=0, row=2)
        self.fila4.grid(column=0, row=3)
        self.fila5.grid(column=0, row=4)


        response = requests.get(self.image_url)
        print(response)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        photo = ImageTk.PhotoImage(image)
        self.imagenpoke.config(image=photo)
        self.imagenpoke.image = photo
        self.pokedexx.mainloop()

        
a = Pokedex()