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
#posicion del title
title.place(x=50, y=50)
title.pack()

for i in range(0,5):

# Crea un Frame en el lado izquierdo de la ventana
    frame = tk.Frame(root, bg="black", width=300, height=500,borderwidth=3)
# Crea un canvas dentro del Frame
    canvas = tk.Canvas(
    frame, 
    bg='#6cd2d1', 
    width=280, 
    height=500, 
    bd=0, 
    highlightthickness=0,
    )
    frame.place(x=(i*300)+20, y=200)
    canvas.pack()

# Lanzamos el loop principal de la ventana
root.mainloop()