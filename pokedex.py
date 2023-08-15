
from tkinter import *
from ApiPoke import *


app = Tk()
app.title("Pokedex")
#app.resizable(height=0,width=0)
#app.geometry("400x600")

bt1 = Button(app,text="boton")

bt1.pack()

imagen = PhotoImage(file = "pokedex.png")

background = Label(image = imagen, text = "Imagen S.O de fondo")

background.place(x = 0, y = 0, relwidth = 1, relheight = 1)




app.mainloop()