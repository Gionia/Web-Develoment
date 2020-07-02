from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Recopilando datos")
texto = Label(window, text="Ingrese su email:")
texto.config(font=("Arial", 15), fg="green", pady=5)
texto.grid(row=0, column=0)


def get_dato():
    answer.set(dato.get())  # funcion para obtener un dato


"""
dato y answer son dos objetos StringVar ambos tienen metodos getrs y seters
la funcion get_dato obtiene el valor de dato(StringVar) y lo asigna a answer usando
el metodo .set en answer
"""

dato = StringVar()  # Estas son variables globales
answer = StringVar()

respuesta = Entry(window, textvariable=dato)  # Para recoger dato se usa textvariable
respuesta.config(font=("Arial", 15), fg="black")
respuesta.grid(row=0, column=1)

texto2 = Label(window, text="Su email es: ")
texto2.config(font=("Arial", 15), fg="green", pady=5)
texto2.grid(row=1, column=1)

Button(window, text="Mostrar dato", command=get_dato).grid(row=2, column=1)

texto_dato = Label(window, textvariable=answer)  # Para recoger dato se usa textvariable
texto_dato.grid(row=3, column=1)

window.mainloop()
