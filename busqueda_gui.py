import tkinter as tk
from tkinter import ttk,Text,Label
from tkinter import *
from PIL import Image, ImageTk
from conexion import *
import pandas as pd
import subprocess
import customtkinter

#ventana principal
root = tk.Tk()
root.configure(bg="#f8f7f9")

#tamaño de pantalla
root.geometry("1920x1080")

#Declaración de variables
db = database()
cursor = db.connection.cursor()
lista = ttk.Treeview()
lista_a = ttk.Treeview()
lista_b = ttk.Treeview()
i = int()

#GUI
label2 = customtkinter.CTkFrame(root,width=860,height=690,fg_color="#f7f7f6",corner_radius=24)
label2.place(x=350,y=45)
label1 = customtkinter.CTkFrame(root,width=840,height=680,fg_color="white",corner_radius=24,bg_color="#f7f7f6")
label1.place(x=350,y=50)

#####
buscar = tk.Label(text="Buscar el Estudiante",font=("Bahnschrift Condensed",30,"bold"),bg="white",fg="purple")
buscar.place(x=620,y=85)
codigo = tk.Label(text="Código del Estudiante",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
codigo.place(x=400,y=170)
codigo_texto = customtkinter.CTkEntry(root, width=140, font=("arial", 20),placeholder_text="2022-119230",fg_color="#FAF9F9",text_color="black")
codigo_texto.place(x=700, y=185)

#volver al menu
def abrir_archivo():
    cursor.close()
    db.connection.close()
    root.destroy()  # Cierra la ventana actual

#Buscar un estudiante por su codigo
def buscar_por_id():    

    global lista,lista_a,lista_b,i
    id_estudiante = codigo_texto.get()
    consulta = "SELECT * FROM estudiante WHERE codigo = %s"
    cursor.execute(consulta, (id_estudiante,))
    resultados = cursor.fetchone()
    sql = "SELECT TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) FROM estudiante WHERE codigo = %s" 
    cursor.execute(sql, (id_estudiante,))
    edad = cursor.fetchone()
    
    if resultados:

        #Si hay registros de la consulta entonces muestralo a trave de un treeview en formato columnas
        if (i > 0):
            lista.place_forget()
            lista_a.place_forget()
            lista_b.place_forget()

        lista = ttk.Treeview(root, columns=(1,2,3,4,5,6,7,8),show="headings",height=2)
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("Treeview.Heading",background="black",relief="flat",foreground="white")
        lista.heading(1, text="Código")
        lista.heading(2, text="Nombres")
        lista.heading(3, text="Apellidos")
        lista.heading(4, text="Edad")
        lista.heading(5, text="DNI")
        lista.heading(6, text="Sexo")
        lista.heading(7, text="Turno")
        lista.heading(8, text="Sección")
        lista.column(1,width=80,anchor=CENTER)
        lista.column(2,width=140,anchor=CENTER)
        lista.column(3,width=140,anchor=CENTER)
        lista.column(4,width=40,anchor=CENTER)
        lista.column(5,width=80,anchor=CENTER)
        lista.column(6,width=80,anchor=CENTER)
        lista.column(7,width=80,anchor=CENTER)
        lista.column(8,width=80,anchor=CENTER)

        item = lista.insert('', 'end', values=resultados)
        lista.set(item, column=4, value=edad)
        lista.place(x=360,y=320)

        consulta = "SELECT num_telefono FROM estudiante e INNER JOIN telefono t ON e.codigo = t.estudiante_codigo WHERE codigo = %s"
        cursor.execute(consulta, (id_estudiante,))
        a = cursor.fetchall()

        sql = "SELECT nom_correo FROM estudiante e INNER JOIN correo c ON e.codigo = c.estudiante_codigo WHERE codigo = %s ORDER BY SUBSTRING(nom_correo, INSTR(nom_correo, '@')+1) DESC"
        cursor.execute(sql, (id_estudiante,))
        b = cursor.fetchall()

        query = "SELECT nom_escuela FROM escuela e INNER JOIN estudiante es ON es.escuela_idescuela = e.idescuela WHERE codigo = %s"
        cursor.execute(query, (id_estudiante,))
        c = cursor.fetchall()

        query_a = "SELECT nom_facultad FROM facultad f INNER JOIN escuela e ON e.facultad_idfacultad = f.idfacultad INNER JOIN estudiante es ON es.escuela_idescuela = e.idescuela WHERE codigo = %s"
        cursor.execute(query_a, (id_estudiante,))
        d = cursor.fetchall()        

        query_b = "SELECT nom_departamento,nom_provincia,nom_distrito FROM estudiante es INNER JOIN direccion di ON es.codigo = di.estudiante_codigo INNER JOIN departamento d ON di.departamento_iddepartamento = d.iddepartamento INNER JOIN provincia p ON di.provincia_idprovincia = p.idprovincia INNER JOIN distrito dis ON di.distrito_iddistrito = dis.iddistrito WHERE codigo = %s"
        cursor.execute(query_b, (id_estudiante,))
        e = cursor.fetchall()        

        lista_a = ttk.Treeview(root, columns=(1,2,3,4,5,6),show="headings",height=2)
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("Treeview.Heading",background="black",relief="flat",foreground="white")
        lista_a.heading(1, text="Teléfono")
        lista_a.heading(2, text="Correo institucional")
        lista_a.heading(3, text="Correo personal")
        lista_a.heading(4, text="Escuela")
        lista_a.heading(5, text="Facultad")
        lista_a.heading(6, text="Departamento-Provincia-Distrito")
        lista_a.column(1,width=80,anchor=CENTER)
        lista_a.column(2,width=180,anchor=CENTER)
        lista_a.column(3,width=180,anchor=CENTER)
        lista_a.column(4,width=60,anchor=CENTER)
        lista_a.column(5,width=60,anchor=CENTER)
        lista_a.column(6,width=240,anchor=CENTER)

        tupla = a + b + c + d + e
        lista_a.insert('','end',values = tupla)
        lista_a.place(x=360,y=400)


        consulta = "SELECT tipo_zona,nom_zona,tipo_via,nom_via,numero,referencia FROM direccion di INNER JOIN via v ON di.via_idvia = v.idvia INNER JOIN zona z ON di.zona_idzona = z.idzona INNER JOIN estudiante es ON es.codigo = di.estudiante_codigo WHERE codigo = %s"
        cursor.execute(consulta, (id_estudiante,))
        a = cursor.fetchone()

        lista_b = ttk.Treeview(root, columns=(1,2,3,4,5,6),show="headings",height=2)
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("Treeview.Heading",background="black",relief="flat",foreground="white")
        lista_b.heading(1, text="Tipo de zona")
        lista_b.heading(2, text="Nombre de zona")
        lista_b.heading(3, text="Tipo de via")
        lista_b.heading(4, text="Nombre de via")
        lista_b.heading(5, text="Número")
        lista_b.heading(6, text="Referencia")
        lista_b.column(1,width=180,anchor=CENTER)
        lista_b.column(2,width=100,anchor=CENTER)
        lista_b.column(3,width=180,anchor=CENTER)
        lista_b.column(4,width=100,anchor=CENTER)
        lista_b.column(5,width=100,anchor=CENTER)
        lista_b.column(6,width=120,anchor=CENTER)

        lista_b.insert('','end',values = a)
        lista_b.place(x=360,y=480)

        i = i+1        
    else:
        if lista:
            lista.place_forget()  # Ocultar la lista existente
            lista_a.place_forget()  # Ocultar la lista existente
            lista_b.place_forget()  # Ocultar la lista existente

        no_encontrado = tk.Label(text="NO EXISTE NINGÚN ESTUDIANTE CON ESE CÓDIGO ",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="red")
        no_encontrado.place(x=440,y=400)
        no_encontrado_a = tk.Label(text="EN LA BASE DE DATOS" ,font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="red")
        no_encontrado_a.place(x=600,y=440)
        no_encontrado.after(2000, lambda: no_encontrado.place_forget())
        no_encontrado_a.after(2000, lambda: no_encontrado_a.place_forget())

# BOTONES DE COMANDOS
atras = customtkinter.CTkButton(root, text="Volver al Menú",font=("arial",24,"bold"),command = lambda:abrir_archivo())
atras.place(x=650,y=660)
buscar = customtkinter.CTkButton(root, text="Buscar Estudiante",font=("arial",24,"bold"),command=lambda: buscar_por_id())
buscar.place(x=630,y=260)

fondo =Image.open("icons/fondo8.png")
fondop = ImageTk.PhotoImage(fondo)
fondol = tk.Label(root, image=fondop)
fondol.place(x=0,y=0)

fondo1 =Image.open("icons/fondo9.png")
fondop1 = ImageTk.PhotoImage(fondo1)
fondol1 = tk.Label(root, image=fondop1)
fondol1.place(x=1200,y=0)

root.mainloop()