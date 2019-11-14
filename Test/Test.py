from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("520x480")
root.config(bg="#A1EEFB")

title = Frame(root, width=300, height=50,bg="red")
title.grid()

head = Frame(root,width=500, height=100,bg="red")
head.grid()

ttk.Label(title,text="Bienvenidos al BlackJack").grid(column=1,row=3)
ttk.Label(title, text="prueba").grid(column=1, row=5)


root.mainloop()
