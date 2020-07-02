from tkinter import *


class Marco:
    def __init__(self, window):
        self.window = window

    def crear(self, altura, ancho, color, bd=None, relief=None):
        marco = Frame(self.window, height=altura, width=ancho)
        marco.config(bd=bd, relief=relief, bg=color)
        marco.pack(side=TOP, anchor=CENTER)
        return marco

