from tkinter import *
from hardware.marcos_pantalla import marcos
from hardware.marcos_pantalla import pantallas
from hardware.botones import boton


class Calculadora:
    @classmethod
    def crear_vista(cls, color, color_letra, color_solucion, color_in, tamanio_ventana):

        altura = 100
        ancho = 276
        cls.calculadora = Tk()
        cls.calculadora.geometry(tamanio_ventana)
        cls.calculadora.resizable(0, 0)  # para poder hacerla grande se cambia a 1,1
        cls.calculadora.config(bg=color)
        cls.calculadora.title("Calculadora")

        aritmetica = StringVar()
        respuesta = StringVar()

        marco1, marco2, marco3, marco4 = marcos.crear_marcos(
            cls.calculadora, altura, ancho, color_in, color
        )

        solucion = pantallas.pantalla_solucion(marco2, respuesta, color_solucion)
        pantalla = pantallas.pantalla_in(marco2, aritmetica, color_in, color_letra)

        # Los siguientes comandos son para establecer coordenadas, otra opcion podria
        # ser usar numpy
        botones_ = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        bo = boton.crear_bot()
        botones_ = bo.crear_botones(marco4, color, color_letra, aritmetica)

        cls.calculadora.mainloop()
