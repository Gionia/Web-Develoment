from tkinter import *
from PIL import Image
from PIL import ImageTk
from os import path

window = Tk()
window.geometry("750x750")
ruta = path.abspath("imagenes/code.png")
imagen = Image.open(ruta)  # Se extrae la ruta
render = ImageTk.PhotoImage(imagen)  # Se pasa a tkinter
Label(window, image=render).pack()  # Se junta con la ventana
window.mainloop()

