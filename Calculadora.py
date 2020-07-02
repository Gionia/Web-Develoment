from tkinter import *
from PIL import ImageTk
from PIL import Image
from os import path

color = "#323a4d"  # color de la calculadora
color_letra = "#dce0e8"

calculadora = Tk()
calculadora.geometry("298x285")
calculadora.resizable(0, 0)  # para poder hacerla grande se cambia a 1,1
calculadora.config(bg=color)
calculadora.title("Calculadora")

aritmetica = StringVar()
respuesta = StringVar()

separacion = Frame(calculadora, height=10, width=298)
separacion.config(bg=color)
separacion.pack()

# En este marco se encuentran donde se muestra la solucion y donde se escribe peticion
marco = Frame(calculadora, height=100, width=276)
marco.config(bd=1, relief=SOLID, bg="gray2")
marco.pack_propagate(False)
marco.pack(side=TOP, anchor=CENTER)

separacion2 = Frame(calculadora, height=10, width=298)
separacion2.config(bg=color)
separacion2.pack()

# Se encuentra los botones
marco2 = Frame(calculadora, height=300)
marco2.config(bg=color)
# marco2.config(bd=3, relief=SOLID)
marco2.pack(side=TOP, anchor=CENTER)

solucion = Label(marco, textvariable=respuesta)
solucion.config(font=("Arial", 12), bg="#27292e", bd=1, relief=SOLID)
solucion.grid(row=0, column=0, ipadx=136, ipady=8)

pantalla = Entry(marco, textvariable=aritmetica)
pantalla.config(
    font=("Arial", 15),
    bg="#383a45",
    insertbackground=color_letra,
    fg=color_letra,
    justify="right",
)
pantalla.grid(row=1, column=0, ipadx=35, ipady=8)

"""
Los siguientes comandos son para establecer coordenadas, otra opcion podria
ser usar numpy
"""
fila = [0, 0, 0, 0]
col = [0, 1, 2, 3]
col_ = col.copy()
fila_ = fila.copy()

j = 1

for item in fila_:
    for i in col_:
        col.append(item + i)
        fila.append(item + j)
    j += 1

simbolo = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    " -",
    "1",
    "2",
    "3",
    "x",
    "0",
    " .",
    "=",
    "/ ",
]
cord_simb = list(zip(fila, col, simbolo))
i = 0
boton = list(range(16))

for rows, columns, simb in cord_simb:
    boton[i] = Button(marco2, text=simb)
    boton[i].config(font=("Arial", 15), padx=25, pady=7, bg=color, fg=color_letra)
    boton[i].grid(row=rows, column=columns, padx=2, pady=2)
    i += 1

calculadora.mainloop()

