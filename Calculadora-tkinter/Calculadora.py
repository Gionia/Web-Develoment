from tkinter import *
from os import path
from hardware import marcos

color = "#323a4d"  # color de la calculadora
color_letra = "#dce0e8"

altura = 100
ancho = 276

calculadora = Tk()
calculadora.geometry("298x285")
calculadora.resizable(0, 0)  # para poder hacerla grande se cambia a 1,1
calculadora.config(bg=color)
calculadora.title("Calculadora")

aritmetica = StringVar()
respuesta = StringVar()

sep = (altura / 10, ancho, color)
features = [sep, (altura, ancho, "gray2"), sep, (altura * 3, ancho, color)]
n = 0
marco = [0, 0, 0, 0]
for alt, an, col in features:
    marco[n] = marcos.Marco(calculadora)
    marco[n] = marco[n].crear(alt, an, col)
    n += 1

"""
separacion = marcos.Marco(calculadora)
separacion = separacion.crear(altura / 10, ancho, color)

marco1 = marcos.Marco(calculadora)
marco1 = marco1.crear(altura, ancho, "gray2")

separacion2 = marcos.Marco(calculadora)
separacion2 = separacion2.crear(altura / 10, ancho, color)

marco2 = marcos.Marco(calculadora)
marco2 = marco2.crear(altura * 3, ancho, color)
"""

# Se encuentra los botones

solucion = Label(marco[1], textvariable=respuesta)
solucion.config(font=("Arial", 12), bg="#27292e", bd=1, relief=SOLID)
solucion.grid(row=0, column=0, ipadx=136, ipady=8)

pantalla = Entry(marco[1], textvariable=aritmetica)
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
    boton[i] = Button(marco[2], text=simb)
    boton[i].config(font=("Arial", 15), padx=25, pady=7, bg=color, fg=color_letra)
    boton[i].grid_size()
    boton[i].grid(row=rows, column=columns, padx=2, pady=2)
    i += 1

calculadora.mainloop()

