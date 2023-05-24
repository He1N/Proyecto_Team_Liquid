import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

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
title.place(x=170, y=40)


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

#Subtitulos-labels
agregar = tk.Label(text="AGREGAR ESTUDIANTE",font=("arial",15,"bold"),bg="#6cd2d1")
agregar.place(x=45,y=240)

editar = tk.Label(text="EDITAR ESTUDIANTE",font=("arial",15,"bold"),bg="#6cd2d1")
editar.place(x=360,y=240)

eliminar = tk.Label(text="ELIMINAR ESTUDIANTE",font=("arial",15,"bold"),bg="#6cd2d1")
eliminar.place(x=650,y=240)

buscar = tk.Label(text="BUSCAR ESTUDIANTE",font=("arial",15,"bold"),bg="#6cd2d1")
buscar.place(x=955,y=240)

reporte1 = tk.Label(text="REPORTE DE",font=("arial",15,"bold"),bg="#6cd2d1")
reporte1.place(x=1290,y=230)
reporte2= tk.Label(text="ESTUDIANTES",font=("arial",15,"bold"),bg="#6cd2d1")
reporte2.place(x=1290,y=260)

#Implementando imagenes
#IMAGEN 1
# Cargar la imagen
image1 = Image.open("E:/Universidad/Compi/icons/agrega.png")
image1 = image1.resize((200, 200))
photo1 = ImageTk.PhotoImage(image1)

# Crear una etiqueta para mostrar la imagen
image_label1 = tk.Label(root, image=photo1,bg="#6cd2d1")
image_label1.place(x=65,y=310)

#IMAGEN 2
image2 = Image.open("E:/Universidad/Compi/icons/editar.png")
image2 = image2.resize((200, 200))
photo2 = ImageTk.PhotoImage(image2)

image_label2 = tk.Label(root, image=photo2,bg="#6cd2d1")
image_label2.place(x=365,y=310)

#IMAGEN 3
image3 = Image.open("E:/Universidad/Compi/icons/eliminar.png")
image3 = image3.resize((200, 200))
photo3 = ImageTk.PhotoImage(image3)

image_label3 = tk.Label(root, image=photo3,bg="#6cd2d1")
image_label3.place(x=665,y=310)

#IMAGEN 4
image4 = Image.open("E:/Universidad/Compi/icons/buscar.png")
image4 = image4.resize((200, 200))
photo4 = ImageTk.PhotoImage(image4)

image_label4 = tk.Label(root, image=photo4,bg="#6cd2d1")
image_label4.place(x=965,y=310)

#IMAGEN 5
image5 = Image.open("E:/Universidad/Compi/icons/reporte.png")
image5 = image5.resize((200, 200))
photo5 = ImageTk.PhotoImage(image5)

image_label5 = tk.Label(root, image=photo5,bg="#6cd2d1")
image_label5.place(x=1265,y=310)

#IMAGEN LIQUID
liquid = Image.open("icons/liquid.png")
liquid = liquid.resize((130, 130))
photo6 = ImageTk.PhotoImage(liquid)

image_label6 = tk.Label(root, image=photo6,bg="#6cc3d2")
image_label6.place(x=15,y=30)

#MINIDESCRIPCION
#TEXTO1
texto1_p1 = tk.Label(text="Permite crear nuevos",font=("arial",14),bg="#6cd2d1")
texto1_p1.place(x=75,y=540)
texto1_p2 = tk.Label(text="registros de estudiantes.",font=("arial",14),bg="#6cd2d1")
texto1_p2.place(x=65,y=570)
#TEXTO2
texto2_p1 = tk.Label(text="Permite editar información",font=("arial",14),bg="#6cd2d1")
texto2_p1.place(x=350,y=540)
texto2_p2 = tk.Label(text="del registro de estudiantes.",font=("arial",14),bg="#6cd2d1")
texto2_p2.place(x=350,y=570)
#TEXTO3
texto3_p1 = tk.Label(text="Permite eliminar información",font=("arial",14),bg="#6cd2d1")
texto3_p1.place(x=640,y=540)
texto3_p2 = tk.Label(text="del registro de estudiantes.",font=("arial",14),bg="#6cd2d1")
texto3_p2.place(x=650,y=570)
#TEXTO4 - BUSQUEDA
texto4_p1 = tk.Label(text="Permite buscar estudiantes",font=("arial",14),bg="#6cd2d1")
texto4_p1.place(x=950,y=540)
texto4_p2 = tk.Label(text="del registro.",font=("arial",14),bg="#6cd2d1")
texto4_p2.place(x=1010,y=570)
#TEXTO5
texto4_p1 = tk.Label(text="Permite generar un",font=("arial",14),bg="#6cd2d1")
texto4_p1.place(x=1290,y=540)
texto4_p2 = tk.Label(text="reporte de estudiantes.",font=("arial",14),bg="#6cd2d1")
texto4_p2.place(x=1270,y=570)

def abrir_archivo_buscar():
    archivo = "busqueda_gui.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    root.destroy()  # Cierra la ventana actual
    subprocess.call(["python", archivo])

def abrir_archivo_agregar():
    archivo = "agrega.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    root.destroy()  # Cierra la ventana actual
    subprocess.call(["python", archivo])

def abrir_archivo_modificar():
    archivo="modificar.py"
    root.destroy()
    subprocess.call(["python", archivo])

#BOTONES DE ACCION
#BOTON 1
boton1 = tk.Button(root, text="AGREGAR",font=("arial",15,"bold"),command=abrir_archivo_agregar)
boton1.place(x=110,y=620)
#BOTON 2
boton1 = tk.Button(root, text="EDITAR",font=("arial",15,"bold"),command=abrir_archivo_modificar)
boton1.place(x=420,y=620)
#BOTON 3
boton1 = tk.Button(root, text="ELIMINAR",font=("arial",15,"bold"))
boton1.place(x=720,y=620)
#BOTON 4
boton1 = tk.Button(root, text="BUSCAR",font=("arial",15,"bold"),command=abrir_archivo_buscar)
boton1.place(x=1020,y=620)
#BOTON 5
boton1 = tk.Button(root, text="GENERAR",font=("arial",15,"bold"))
boton1.place(x=1320,y=620)




# Lanzamos el loop principal de la ventana
root.mainloop()