import tkinter as tk
from tkinter import ttk

#ventana principal
root = tk.Tk()
root.configure(bg="#6cc3d2")

#tamaño de pantalla
root.geometry("1920x1080")

#Titulo
title = tk.Label(
    root,
    text="PROGRAMA DIGITAL DE REGISTRO DE NOTAS",
    background="#6cd2d1",
    relief="solid",
    borderwidth=3,
    font=("e Explosive Attack", 36, "bold"	),
    fg="#184e4e",
    width="40",
    height="2",
    pady="10"
)

title.place(x=50, y=50)
title.pack()

# Lanzamos el loop principal de la ventana
root.mainloop()