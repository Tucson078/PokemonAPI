
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
        self.pokedexx = tkinter.Tk()
        self.pokedexx.title("Pokedex")
        self.pokedexx.geometry("300x500")
        self.f1 = tkinter.Frame(self.pokedexx,bg="Red", width=300, height=50)
        self.f1.grid()
        self.f4 = tkinter.Label(self.pokedexx, text="Buscar Pokemon con su numero de ID",bg="White")
        self.f4.grid(column=0,row=4)

        self.f5 = tkinter.Entry(self.pokedexx,bg="White")
        self.f5.grid(column=0,row=5)

        self.bt1 = tkinter.Button(self.pokedexx, text="Buscar Pokemon",bg="White",command = self.BuscarPokemon)
        self.bt1.grid(column=0,row=6)

        self.f2 = tkinter.Label(self.pokedexx,bg ="White")
        self.f2.grid(column=0,row=2)

        self.f3 = tkinter.Label(self.pokedexx, bg="White")
        self.f3.grid(column=0,row=3)
        self.imagenpoke = tkinter.Label(self.f3, bg="White")
        self.imagenpoke.grid(column=0,row=3)
        self.datospoke = tkinter.Frame(self.f3,bg="White")
        self.datospoke.grid(column=1,row=3) 

        self.fila1 = tkinter.Label(self.datospoke,bg="White")
        self.fila2 = tkinter.Label(self.datospoke,bg="White")
        self.fila3 = tkinter.Label(self.datospoke,bg="White")
        self.fila4 = tkinter.Label(self.datospoke,bg="White")
        self.fila5 = tkinter.Label(self.datospoke,bg="White")
        self.fila6 = tkinter.Label(self.datospoke,bg="White")

        self.fila1.grid(column=0, row=0)
        self.fila2.grid(column=0, row=1)
        self.fila3.grid(column=0, row=2)
        self.fila4.grid(column=0, row=3)
        self.fila5.grid(column=0, row=4)
        self.fila6.grid(column=0, row=5)
           
        self.llamarPantalla()

    def llamarPantalla(self):
        self.a = Pokemon()
        self.a.obtenerDatosPoke(6)
        self.image_url = self.a.img
        self.vida = f"Vida : {self.a.vida}"
        self.atk = f"Atk : {self.a.atk}"
        self.defensa = f"Def : {self.a.defensa}"
        self.specialAtk = f"Special Atk : {self.a.specialAtk}"
        self.vel = f"Vel : {self.a.velocidad}"
        self.SpecialDef = f"Special Def : {self.a.specialDefensa}"

        self.f2.config(text = self.a.nombre)        

        self.fila1.config(text = self.vida)
        self.fila2.config(text = self.atk)
        self.fila3.config(text = self.defensa)
        self.fila4.config(text  = self.specialAtk)
        self.fila5.config(text = self.SpecialDef)
        self.fila6.config(text = self.vel)
    
        response = requests.get(self.image_url)
        print(self.image_url)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        photo = ImageTk.PhotoImage(image)
        self.imagenpoke.config(image=photo)
        self.imagenpoke.image = photo
        self.pokedexx.mainloop()

    def BuscarPokemon(self):
        self.a.obtenerDatosPoke(self.f5.get())
        self.f5.delete(first=0,last=tkinter.END)
        self.llamarPantalla()
    
a = Pokedex()

