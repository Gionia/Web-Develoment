from tkinter import *


def pantalla_solucion(marco, respuesta, color_solucion):
    solucion = Label(marco, textvariable=respuesta)
    solucion.config(font=("Arial", 12), bg=color_solucion, bd=1, relief=SOLID)
    solucion.grid_propagate(False)
    solucion.grid(row=0, column=0, ipadx=136, ipady=8)
    return solucion


def pantalla_in(marco, aritmetica, color_in, color_letra):
    pantalla = Entry(marco, textvariable=aritmetica)
    pantalla.config(
        font=("Arial", 15),
        bg=color_in,
        insertbackground=color_letra,
        fg=color_letra,
        justify="right",
    )
    pantalla.grid(row=1, column=0, ipadx=35, ipady=8)
