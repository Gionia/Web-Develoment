from tkinter import *
import os.path


class APP:
    def __init__(self, title, size, resizable):
        self.title = title
        self.size = size
        self.resizable = resizable

    def cargar(self):
        self.ventana = Tk()
        self.ventana.geometry(self.size)
        self.ventana.title("Primer GUI")

        if self.resizable:
            self.ventana.resizable(1, 1)
        else:
            self.ventana.resizable(0, 0)

    def add_text(self, texto):
        text = Label(self.ventana, text=texto)
        text.config(fg="red", bg="yellow")
        text.pack()

    def mostrar(self):
        self.ventana.mainloop()


ventanita = APP("Primera app", "750x450", True)
print(ventanita)
ventanita.cargar()
for i in range(10):
    ventanita.add_text("Si se pudo")
ventanita.mostrar()

