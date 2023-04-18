from tkinter import *
import random

pagina = Tk()
pagina.title("lista Aleatoria")
pagina.geometry("500x500")
pagina.configure(background="#264653")
ttl = Label(pagina, text="Generador de Numeros Aleatorio", bg="#2a9d8f", fg="white")
ttl.place(relx=0.5, rely=0.03, anchor=CENTER,)
stl = Label(pagina, text=".", bg="#2a9d8f", fg="white")
stl.place(relx=0.5, rely=0.09, anchor=CENTER,)
txt = Label(pagina, text=".", bg="#2a9d8f", fg="white")
txt.place(relx=0.5, rely=0.15, anchor=CENTER,)
def fn():
    vn = random.sample(range(-100,100),7)
    stl["text"] = "La lista es :" + str(vn)
    vn.sort()
    txt["text"]  = "Ordenada de menor a mayor: " + str(vn)
btn = Button(pagina, text="Generar", bg="#e76f51", fg="white", command=fn)
btn.place(relx=0.5, rely=0.23, anchor=CENTER,)









pagina.mainloop()

