from tkinter import *


def crear(calculadora, altura, ancho, color, bd=None, relief=None):
    marco = Frame(calculadora, height=altura, width=ancho)
    marco.config(bd=bd, relief=relief, bg=color)
    marco.pack(side=TOP, anchor=CENTER)

    return marco


def crear_marcos(calculadora, altura, ancho, color_in, color):
    sep = (altura / 10, ancho, color)  # Los frames que sirven como separadores
    features = [sep, (altura, ancho, color_in), sep, (altura * 3, ancho, color)]
    n = 0
    marco = [0, 0, 0, 0]
    for alt, an, col in features:
        marco[n] = crear(calculadora, alt, an, col)
        n += 1

    return marco[0], marco[1], marco[2], marco[3]

