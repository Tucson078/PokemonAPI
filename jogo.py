import tkinter
from ApiPoke import Pokemon
import requests
from PIL import Image,ImageTk
from io import BytesIO
import tkinter as tk
from random import randint
from Jogador import Jugador
from pantalla import Pantalla


class Juego:
    
    def __init__(self):
        self.pantalla = Pantalla()
        self.jugador1 = Jugador()
        self.jugador2 = Jugador()
        pkInicial1 = self.jugador1.mochila[0]
        pkInicial2 = self.jugador2.mochila[0]

        for banco in range(len(self.pantalla.bancoDeSuplentes)):
            self.pantalla.insertarFoto(self.pantalla.bancoDeSuplentes[banco], self.jugador1.mochila[banco].img )
        self.pantalla.insertarFoto(self.pantalla.lp7,pkInicial1.imgEspalda)
        self.pantalla.insertarFoto(self.pantalla.lp3,pkInicial2.img)
        self.pantalla.mostrarInfo(pkInicial1, pkInicial2)
        self.pantalla.juego.mainloop()

        
        
        








a = Juego()
