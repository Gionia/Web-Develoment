from tkinter import *

window = Tk()
window.geometry("500x500")
text = Label(window, text="Welcome to my software")
text.config(fg="white", bg="black", padx=500, pady=15, font=("Arial", 30))
text.pack()

text1 = Label(window, text="Enunciado")
text1.config(fg="white", bg="orange", pady=100, font=("Arial", 18), cursor="spider")
text1.pack(side=TOP, fill=X, expand=YES)

window.mainloop()
