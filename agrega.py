import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from conexion import *
import pandas as pd
import subprocess
import customtkinter

# Ventana principal
root = tk.Tk()
root.configure(bg="#f8f7f9")

# Tamaño de pantalla
db = database()
cursor = db.connection.cursor()
root.geometry("1920x1080")

# Declaracion de las variables
id_escuela = int()
id_depa = int()
id_provincia = int()
id_distrito = int()
id_via = int()
id_zona = int()

#GUI
fondo =Image.open("icons/fondo7.png")
fondop = ImageTk.PhotoImage(fondo)
fondol = tk.Label(root, image=fondop)
fondol.place(x=900,y=0)
label2 = customtkinter.CTkFrame(root,width=890,height=710,fg_color="#f7f7f6",corner_radius=24)
label2.place(x=590,y=45)
label1 = customtkinter.CTkFrame(root,width=870,height=700,fg_color="white",corner_radius=24,bg_color="#f7f7f6")
label1.place(x=600,y=50)

perfil = Image.open("icons/perfil.png")
perfil = perfil.resize((520,810))
perfilphoto = ImageTk.PhotoImage(perfil)

perfilabel = tk.Label(root, image=perfilphoto,bg="white")
perfilabel.place(x=0,y=0)

#Subtitulos-labels
datos = tk.Label(text="Datos del Estudiante",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
datos.place(x=820,y=35)
codigo = tk.Label(text="Código del Estudiante",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
codigo.place(x=540,y=85)
nombres = tk.Label(text="Nombres",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
nombres.place(x=540,y=135)
apellidos = tk.Label(text="Apellidos",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
apellidos.place(x=540,y=185)
fecha = tk.Label(text="Fecha de nacimiento",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
fecha.place(x=540,y=235)
dni = tk.Label(text="DNI",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
dni.place(x=540,y=285)
sex = tk.Label(text="Sexo",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
sex.place(x=540,y=335)
telefono = tk.Label(text="Teléfono",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
telefono.place(x=540,y=385)
correo = tk.Label(text="Correo institucional",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
correo.place(x=540,y=435)
correo_p = tk.Label(text="Correo personal",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
correo_p.place(x=540,y=485)
escuela = tk.Label(text="Escuela",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
escuela.place(x=540,y=535)
ciclo = tk.Label(text="Ciclo",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
ciclo.place(x=540,y=585)
turno = tk.Label(text="Turno",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
turno.place(x=690,y=585)
seccion = tk.Label(text="Sección",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
seccion.place(x=800,y=585)

# DIRECCION DEL ESTUDIANTE
direccion = tk.Label(text="Dirección",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
direccion.place(x=1140,y=85)
departamento = tk.Label(text="Departamento",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
departamento.place(x=980,y=135)
provincia = tk.Label(text="Provincia",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
provincia.place(x=980,y=185)
distrito = tk.Label(text="Distrito",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
distrito.place(x=980,y=235)
tipo_zona = tk.Label(text="Tipo de zona",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
tipo_zona.place(x=980,y=285)
nom_zona = tk.Label(text="Nombre de zona",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
nom_zona.place(x=980,y=335)
tipo_via = tk.Label(text="Tipo de via",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
tipo_via.place(x=980,y=385)
nom_via = tk.Label(text="Nombre de via",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
nom_via.place(x=980,y=435)
numero = tk.Label(text="Número",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
numero.place(x=980,y=485)
referencia = tk.Label(text="Referencia",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
referencia.place(x=980,y=535)

#nota1 = tk.Label(text="Nota 1",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
#nota1.place(x=700,y=400)
#nota2 = tk.Label(text="Nota 2",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
#nota2.place(x=700,y=480)
#nota3 = tk.Label(text="Nota 3",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
#nota3.place(x=700,y=560)

# CUADRO DE TEXTO
codigo_texto = customtkinter.CTkEntry(root, width=140, font=("arial", 20),placeholder_text="2022-119230",fg_color="#FAF9F9",text_color="black")
codigo_texto.place(x=740, y=90)
nombre_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="Javier Matias",fg_color="#FAF9F9",text_color="black")
nombre_texto.place(x=640, y=140)
apellido_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="Olivera Huacca",fg_color="#FAF9F9",text_color="black")
apellido_texto.place(x=640, y=190)
fecha_texto = customtkinter.CTkEntry(root, width=160, font=("arial", 20),placeholder_text="AAAA-MM-DD",fg_color="#FAF9F9",text_color="black")
fecha_texto.place(x=740, y=240)
dni_texto = customtkinter.CTkEntry(root, width=120, font=("arial", 20),placeholder_text="24156326",fg_color="#FAF9F9",text_color="black")
dni_texto.place(x=580, y=290)
sexo_texto = ttk.Combobox(root, values=("M", "F"),state="readonly",width=2)
sexo_texto.place(x= 600,y = 347)
telefono_texto = customtkinter.CTkEntry(root, width=120, font=("arial", 20),placeholder_text="923421523",fg_color="#FAF9F9",text_color="black")
telefono_texto.place(x=640, y=390)
correo_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="jmolivera@unjbg.edu.pe",fg_color="#FAF9F9",text_color="black")
correo_texto.place(x=720, y=440)
correo_p_texto = customtkinter.CTkEntry(root, width=260, font=("arial", 20),placeholder_text="javiermatias24@gmail.com",fg_color="#FAF9F9",text_color="black")
correo_p_texto.place(x=700, y=490)

# COMANDO PARA ESCUELA DESDE LA BASE DE DATOS 
consulta = "SELECT nom_escuela FROM escuela"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
escuela_texto = ttk.Combobox(root, values= datos,state="readonly",width=5,height=5)
escuela_texto.place(x= 620,y = 547)

ciclo_texto = ttk.Combobox(root, values=("PRIMER", "SEGUNDO", "TERCER", "CUARTO", "QUINTO", "SEXTO", "OCTAVO", "NOVENO", "DECIMO"),state="readonly",width=10,height=4)
ciclo_texto.place(x= 600,y = 597)
turno_texto = ttk.Combobox(root, values=("M", "T"),state="readonly",width=2)
turno_texto.place(x= 750,y = 597)
seccion_texto = ttk.Combobox(root, values=("A", "B"),state="readonly",width=2)
seccion_texto.place(x= 880,y = 597)

# DIRECCION_TEXTO
consulta = "SELECT nom_departamento FROM departamento"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
departamento_texto = ttk.Combobox(root, values=datos,state="readonly",width=30)
departamento_texto.place(x= 1140,y = 145)

consulta = "SELECT nom_provincia FROM provincia"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
provincia_texto = ttk.Combobox(root, values=datos,state="readonly",width=20)
provincia_texto.place(x= 1140,y = 195)

consulta = "SELECT nom_distrito FROM distrito"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
distrito_texto = ttk.Combobox(root, values=datos,state="readonly",width=20)
distrito_texto.place(x= 1140,y = 245)

consulta = "SELECT tipo_zona FROM zona"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
tipo_zona_texto = ttk.Combobox(root, values=datos,state="readonly",width=30)
tipo_zona_texto.place(x= 1140,y = 295)
nom_zona_texto = customtkinter.CTkEntry(root, width=210, font=("arial", 20),placeholder_text="Las Américas",fg_color="#FAF9F9",text_color="black")
nom_zona_texto.place(x=1140, y=345)

consulta = "SELECT tipo_via FROM via"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
tipo_via_texto = ttk.Combobox(root, values=datos,state="readonly",width=20)
tipo_via_texto.place(x= 1140,y = 395)
nom_via_texto = customtkinter.CTkEntry(root, width=210, font=("arial", 20),placeholder_text="Calle Zela",fg_color="#FAF9F9",text_color="black")
nom_via_texto.place(x=1140, y=445)

numero_texto = customtkinter.CTkEntry(root, width=130, font=("arial", 20),placeholder_text="Mz:z lte:4",fg_color="#FAF9F9",text_color="black")
numero_texto.place(x=1080, y=495)
referencia_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 20),placeholder_text="Cerca del grifo",fg_color="#FAF9F9",text_color="black")
referencia_texto.place(x=1100, y=545)

def obtener_id_escuela(event):
    global id_escuela
    nombre_escuela = escuela_texto.get()
    consultaa = "SELECT idescuela FROM escuela WHERE nom_escuela = %s"
    cursor.execute(consultaa, (nombre_escuela,))
    resultado = cursor.fetchone()
    id_escuela = resultado[0]

# Asociar evento de selección al combobox
escuela_texto.bind("<<ComboboxSelected>>", obtener_id_escuela)

def enlazar_evento_depa(event):
    global id_depa,id_provincia
    nombre_depa = departamento_texto.get()
    consultab = "SELECT iddepartamento FROM departamento WHERE nom_departamento = %s"
    cursor.execute(consultab, (nombre_depa,))
    resultado = cursor.fetchone()
    id_depa = resultado[0]
    query = "SELECT nom_provincia FROM provincia WHERE departamento_iddepartamento = %s"
    cursor.execute(query, (id_depa,))
    datos = [fila[0] for fila in cursor]
    provincia_texto['values'] = datos

# Asociar evento de selección al combobox
departamento_texto.bind("<<ComboboxSelected>>", enlazar_evento_depa)

def enlazar_evento_provincia(event):
    global id_provincia
    nombre_provi = provincia_texto.get()
    consultab = "SELECT idprovincia FROM provincia WHERE nom_provincia = %s"
    cursor.execute(consultab, (nombre_provi,))
    resultado = cursor.fetchone()
    id_provincia = resultado[0]
    query = "SELECT nom_distrito FROM distrito WHERE provincia_idprovincia = %s"
    cursor.execute(query, (id_provincia,))
    datos = [fila[0] for fila in cursor]
    distrito_texto['values'] = datos

# Asociar evento de selección al combobox
provincia_texto.bind("<<ComboboxSelected>>", enlazar_evento_provincia)

def obtener_id_distrito(event):
    global id_distrito
    nombre_distrito = distrito_texto.get()
    consultac = "SELECT iddistrito FROM distrito WHERE nom_distrito = %s"
    cursor.execute(consultac, (nombre_distrito,))
    resultado = cursor.fetchone()
    id_distrito = resultado[0]

# Asociar evento de selección al combobox
distrito_texto.bind("<<ComboboxSelected>>", obtener_id_distrito)

def obtener_id_zona(event):
    global id_zona
    nombre_zona = tipo_zona_texto.get()
    consultac = "SELECT idzona FROM zona WHERE tipo_zona = %s"
    cursor.execute(consultac, (nombre_zona,))
    resultado = cursor.fetchone()
    id_zona = resultado[0]

# Asociar evento de selección al combobox
tipo_zona_texto.bind("<<ComboboxSelected>>", obtener_id_zona)

def obtener_id_via(event):
    global id_via
    nombre_via = tipo_via_texto.get()
    consultab = "SELECT idvia FROM via WHERE tipo_via = %s"
    cursor.execute(consultab, (nombre_via,))
    resultado = cursor.fetchone()
    id_via = resultado[0]

# Asociar evento de selección al combobox
tipo_via_texto.bind("<<ComboboxSelected>>", obtener_id_via)

#nota1_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 25),placeholder_text="0",fg_color="#FAF9F9",text_color="black")
#nota1_texto.place(x=1030, y=410)
#nota2_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 25),placeholder_text="0",fg_color="#FAF9F9",text_color="black")
#nota2_texto.place(x=1030, y=490)
#nota3_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 25),placeholder_text="0",fg_color="#FAF9F9",text_color="black")
#nota3_texto.place(x=1030, y=570)

# Boton agregar
#boton_agregar = tk.Button(root, text="AGREGAR ESTUDIANTE", font=("arial", 15, "bold"), command=lambda: agregar_estudiante(codigo_texto.get(), nombre_texto.get(), apellido_texto.get(), nota1_texto.get(), nota2_texto.get(), nota3_texto.get(), 'Estudiantes'))

#volver al menu
def abrir_archivo():
    #archivo = "app.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    db.cursor.close()
    db.connection.close()
    root.destroy()  # Cierra la ventana actual

#LIMPIAR LOS TEXTOS Y COMBOBOX
def limpiar():

    textos = [codigo_texto,nombre_texto,apellido_texto,fecha_texto,dni_texto,telefono_texto,correo_texto,correo_p_texto,nom_via_texto,nom_zona_texto,numero_texto,referencia_texto]
    comboboxes = [sexo_texto,escuela_texto, ciclo_texto, turno_texto,seccion_texto,departamento_texto,provincia_texto,distrito_texto,tipo_zona_texto,tipo_via_texto]  # Reemplaza con tus propios comboboxes

    for combobox in comboboxes:
        combobox.set("")

    for texto in textos:
        texto.delete(0, tk.END)

# FUNCION PARA AGREGAR TODOS LOS DATOS DEL ESTUDIANTE A LA BASE DE DATO
def agregar_estudiante():
    sql = "INSERT INTO estudiante(codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,escuela_idescuela) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(codigo_texto.get(),nombre_texto.get(),apellido_texto.get(),fecha_texto.get(),dni_texto.get(),sexo_texto.get(),turno_texto.get(),seccion_texto.get(),id_escuela)
    db.cursor.execute(sql)
    db.connection.commit()
    sqla = "INSERT INTO telefono(num_telefono,estudiante_codigo) VALUES ('{0}','{1}')".format(telefono_texto.get(),codigo_texto.get())
    db.cursor.execute(sqla)
    db.connection.commit()
    sqlb = "INSERT INTO correo(nom_correo,estudiante_codigo) VALUES ('{0}','{1}')".format(correo_texto.get(),codigo_texto.get())
    db.cursor.execute(sqlb)
    db.connection.commit()
    sqlba = "INSERT INTO correo(nom_correo,estudiante_codigo) VALUES ('{0}','{1}')".format(correo_p_texto.get(),codigo_texto.get())
    db.cursor.execute(sqlba)
    db.connection.commit()
    sqlc = "INSERT INTO direccion(nom_zona,nom_via,numero,referencia,estudiante_codigo,via_idvia,zona_idzona,departamento_iddepartamento,provincia_idprovincia,distrito_iddistrito) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(nom_zona_texto.get(),nom_via_texto.get(),numero_texto.get(),referencia_texto.get(),codigo_texto.get(),id_via,id_zona,id_depa,id_provincia,id_distrito)
    db.cursor.execute(sqlc)
    db.connection.commit()
    limpiar()
    Guardar = tk.Label(text="REGISTRO GUARDADO",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="purple")
    Guardar.place(x=980,y=600)
    Guardar.after(2000, lambda: Guardar.place_forget())

atras = customtkinter.CTkButton(root, text="Volver al Menú",font=("arial",24,"bold"),command = lambda:abrir_archivo())
atras.place(x=800,y=680)
registrar = customtkinter.CTkButton(root, text="Registrar Estudiante",font=("arial",24,"bold"),command = lambda:agregar_estudiante())
registrar.place(x=1100,y=680)

root.mainloop()
