import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from conexion import *
import pandas as pd
import subprocess
import customtkinter
# Función para eliminar al estudiante por ID
import tkinter.messagebox as messagebox

#CONECTAR A LA BASE DE DATOS
db = database()
cursor = db.connection.cursor()
j = int()

# Ventana principal
root = tk.Tk()
root.configure(bg="#f8f7f9")

# Tamaño de pantalla
root.geometry("1920x1080")

#gui
label2 = customtkinter.CTkFrame(root,width=970,height=730,fg_color="#f7f7f6",corner_radius=24)
label2.place(x=500,y=40)
label1 = customtkinter.CTkFrame(root,width=940,height=720,fg_color="white",corner_radius=24,bg_color="#f7f7f6")
label1.place(x=490,y=45)

perfileditar = Image.open("icons/eliminarfondo.png")
perfileditar = perfileditar.resize((450,800))
editarphoto = ImageTk.PhotoImage(perfileditar)

editarlabel = tk.Label(root, image=editarphoto,bg="white")
editarlabel.place(x=-1,y=0)

codigo = tk.Label(text="Código del Estudiante",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
codigo.place(x=600,y=70)

codigo_texto = customtkinter.CTkEntry(root, width=140, font=("arial", 20),placeholder_text="2022-119230",fg_color="#FAF9F9",text_color="black")
codigo_texto.place(x=900, y=80)

#MOSTRAR DATOS DEL ESTUDIANTE BUSCADO SI LO ENCUENTRA
def mostrar_fila():
    global resultados_texto1,j
    id_estudiante = codigo_texto.get()
    consulta = "SELECT * FROM estudiante WHERE codigo = %s"
    cursor.execute(consulta, (id_estudiante,))
    resultados = cursor.fetchone()
    columnas = list()
    columnas = ["Código: ","Nombres: ","Apellidos: ","Fecha de nacimiento: ","DNI: ","Sexo: ","Turno: ","Sección: ","Facultad: ","Escuela: "]

    if (j > 0):    
        resultados_texto1.delete("1.0", tk.END)

    if resultados:

        for i in range(0, 8):
            resultados_texto1.insert(tk.END, columnas[i] + str(resultados[i]) + '\n')

        consulta = "SELECT nom_facultad,nom_escuela FROM escuela e INNER JOIN estudiante es ON e.idescuela = es.escuela_idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE codigo = %s"
        cursor.execute(consulta, (id_estudiante,))
        resultados = cursor.fetchone()
        for i in range(0, 2):
            resultados_texto1.insert(tk.END, columnas[8+i] + str(resultados[i]) + '\n')
            
    elif resultados == '':

        no_encontrado = tk.Label(text="CÓDIGO NO INGRESADO",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="red")
        no_encontrado.place(x=500,y=620)
        no_encontrado.after(4000, lambda: no_encontrado.place_forget())

    else:
        no_encontrado = tk.Label(text="EL ESTUDIANTE NO SE HA ENCONTRADO EN LA BASE DE DATOS",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="red")
        no_encontrado.place(x=500,y=620)
        no_encontrado.after(4000, lambda: no_encontrado.place_forget())

    j= j+1

resultados_texto1 = tk.Text(root, width=30, height=10,font=("arial",18,"bold"),bg="#FAF9F9")
resultados_texto1.place(x=790, y=300)
root.columnconfigure(0, weight=1)

boton_mostrar = customtkinter.CTkButton(root, text="Mostrar Datos",font=("arial",24,"bold"),command=lambda:mostrar_fila() )
boton_mostrar.place(x=600, y=145)

#datos actuales
datos_actuales = tk.Label(text="Datos Actuales",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
datos_actuales.place(x=900, y=220)


def eliminar_estudiante_por_id():
    # Obtener el ID del estudiante a eliminar
    id_estudiante = codigo_texto.get()
    consulta = "SELECT * FROM estudiante WHERE codigo = %s"
    cursor.execute(consulta, (id_estudiante,))
    resultados = cursor.fetchone()
    # Verificar si se encontraron resultados
    if resultados:

        # Mostrar una ventana emergente para confirmar la eliminación
        confirmacion = messagebox.askquestion("Confirmar eliminación", "¿Desea eliminar al estudiante?")
        if confirmacion == 'yes':
            fk = "SET FOREIGN_KEY_CHECKS = 0"
            db.cursor.execute(fk)
            db.connection.commit()
            delete = "DELETE FROM correo WHERE correo.estudiante_codigo = %s"
            db.cursor.execute(delete, (id_estudiante,))
            db.connection.commit()
            delete = "DELETE FROM telefono WHERE telefono.estudiante_codigo = %s"
            db.cursor.execute(delete, (id_estudiante,))
            db.connection.commit()
            delete = "DELETE FROM direccion WHERE direccion.estudiante_codigo = %s"
            db.cursor.execute(delete, (id_estudiante,))
            db.connection.commit()
            delete = "DELETE FROM estudiante WHERE codigo = %s"
            db.cursor.execute(delete, (id_estudiante,))
            db.connection.commit()
            fk = "SET FOREIGN_KEY_CHECKS = 1"
            db.cursor.execute(fk)
            db.connection.commit()

            resultados_texto1.delete(1.0, tk.END)
            eliminado = tk.Label(text="EL ESTUDIANTE HA SIDO ELIMINADO DE LA BASE DE DATOS",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
            eliminado.place(x=580,y=620)
            eliminado.after(2000, lambda: eliminado.place_forget())
            

#volver al menu
def abrir_archivo():
    db.cursor.close()
    db.connection.close()
    root.destroy()  # Cierra la ventana actual

atras = customtkinter.CTkButton(root, text="Volver al Menú",font=("arial",24,"bold"),command = lambda:abrir_archivo())
atras.place(x=680,y=700)
eliminar = customtkinter.CTkButton(root, text="Eliminar del Registro",font=("arial",24,"bold"),command = lambda:eliminar_estudiante_por_id())
eliminar.place(x=1100,y=700)

root.mainloop()
