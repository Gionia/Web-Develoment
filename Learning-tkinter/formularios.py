from tkinter import *

window = Tk()
window.geometry("500x700")
encabezado = Label(window, text="Formulario | Creado por Giovanny")
encabezado.config(font=("Arial", 15), bg="gray", fg="white", padx=110, pady=25)
encabezado.grid(row=0, column=0, columnspan=15)

items = (("¿Cuál es tu nombre", 1), ("¿Dónde vives?", 2), ("¿En dónde estudias?", 3))

for preguntas, rows in items:

    # Se crea el texto que le pedira algo al usuario
    pregunta1 = Label(window, text=preguntas)
    pregunta1.config(font=("Arial", 15))
    pregunta1.grid(row=rows, column=0, sticky=NW, pady=10)

    # Aqui ingresara los datos el usuario
    campo_texto = Entry(window)
    campo_texto.config(font=("Arial", 15))
    campo_texto.grid(row=rows, column=1, sticky=W, ipady=5, ipadx=5)

pregunta1 = Label(window, text="que hace")
pregunta1.config(font=("Arial", 15))
pregunta1.grid(row=4, column=0, sticky=NW, pady=5)

# Aqui ingresara los datos el usuario
campo_texto = Text(window)
campo_texto.config(font=("Arial", 12), height=5, width=25)
campo_texto.grid(row=4, column=1, sticky=W, ipady=10, ipadx=5)

# se crea un boton
boton = Button(window, text="Enviar")
boton.grid(row=5, column=1)
boton.config(bg="gray", pady=10)


window.mainloop()
