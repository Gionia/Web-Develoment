from tkinter import *

window = Tk()
window.geometry("600x600")

marco = Frame(window, width=600, height=600)
marco.config(bg="grey")
marco.pack(side=TOP, fill=X, expand=YES, anchor=N)

marco_left = Frame(marco, width=200, height=200)
marco_left.config(bg="red")
marco_left.pack(side=LEFT, anchor=NW)

marco_right = Frame(marco, width=200, height=200)
marco_right.config(bg="yellow")
marco_right.pack(side=RIGHT, anchor=N)

marco1 = Frame(window, width=600, height=600)
marco1.config(bg="white")
marco1.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)

marco1_left = Frame(marco1, width=200, height=200)
marco1_left.config(bg="blue")
marco1_left.pack(side=LEFT, anchor=S)

marco1_right = Frame(marco1, width=200, height=200)
marco1_right.config(bg="green")
marco1_right.pack(side=RIGHT, anchor=N)

window.mainloop()
