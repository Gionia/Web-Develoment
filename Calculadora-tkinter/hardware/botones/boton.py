from tkinter import *


class crear_bot:
    simbolo = ""

    def escribir(self, simb, aritmetica):
        self.simbolo = self.simbolo + simb
        aritmetica = aritmetica.set(self.simbolo)

    def crear_botones(self, marco, color, color_letra, aritmetica):

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
        print(boton)
        for rows, columns, simb in cord_simb:
            boton[i] = Button(marco, text=simb)
            boton[i].config(
                font=("Arial", 15), padx=25, pady=7, bg=color, fg=color_letra
            )
            boton[i].grid(row=rows, column=columns, padx=2, pady=2)
            i += 1

        boton[0].configure(command=lambda: self.escribir("7", aritmetica))
        boton[1].configure(command=lambda: self.escribir("8", aritmetica))
        boton[2].configure(command=lambda: self.escribir("9", aritmetica))
        boton[3].configure(command=lambda: self.escribir("+", aritmetica))
        boton[4].configure(command=lambda: self.escribir("4", aritmetica))
        boton[5].configure(command=lambda: self.escribir("5", aritmetica))
        boton[6].configure(command=lambda: self.escribir("6", aritmetica))
        boton[7].configure(command=lambda: self.escribir("-", aritmetica))
        boton[8].configure(command=lambda: self.escribir("1", aritmetica))
        boton[9].configure(command=lambda: self.escribir("2", aritmetica))
        boton[10].configure(command=lambda: self.escribir("3", aritmetica))
        boton[11].configure(command=lambda: self.escribir("x", aritmetica))
        boton[12].configure(command=lambda: self.escribir("0", aritmetica))
        boton[13].configure(command=lambda: self.escribir(".", aritmetica))
        boton[14].configure(command=lambda: self.escribir("=", aritmetica))
        boton[15].configure(command=lambda: self.escribir("/", aritmetica))

        return boton
