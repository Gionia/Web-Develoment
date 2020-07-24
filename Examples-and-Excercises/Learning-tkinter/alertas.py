from tkinter import *
from tkinter import messagebox as Messagebox


def alerta():
    Messagebox.showwarning("Autodestruccion", "No debiste hacerlo!!!")


def Salir():
    respuesta = Messagebox.askquestion("Salir", "¿En verdad desea salir?")
    if respuesta == "yes":
        window.destroy()


window = Tk()
window.geometry("400x400")
texto = Label(window, text="Hola")
alerta = Button(window, text="No oprimas este boton!", command=alerta)
alerta.config(bg="red", fg="white", padx=100, pady=25)
alerta.pack()
salir = Button(window, text="Cerrar", command=Salir)
salir.config(pady=10, padx=10)
salir.pack(side=BOTTOM)


window.mainloop()
