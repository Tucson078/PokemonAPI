import tkinter
from ApiPoke import Pokemon
import requests
from PIL import Image,ImageTk
from io import BytesIO
import tkinter as tk
from random import randint
from Jogador import Jugador

class Juego:
    
    jugador1 = Jugador()
    jugador2 = Jugador()    

    def __init__(self):
        self.juego = tkinter.Tk()
        self.juego.title("Jogo?")
        self.juego.geometry("500x600")
        self.juego.resizable(False,False)

        self.FramePadre = tkinter.Frame(self.juego,bg="White")
        self.FramePadre.grid(column=0,row=1)

        self.Pelea = tkinter.Frame(self.FramePadre, bg="Black",width=500,height=600)
        self.Pelea.grid()

        

        self.juego.mainloop()

a = Juego()
