import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import subprocess
import customtkinter
from conexion import *

db = database()
cursor = db.connection.cursor()
j = int()
# Declaracion de las variables
id_escuela = int()
id_depa = int()
id_provincia = int()
id_distrito = int()
id_via = int()
id_zona = int()

# Ventana principal
root = tk.Tk()
root.configure(bg="#f8f7f9")
# Tamaño de pantalla
root.geometry("1920x1080")

label2 = customtkinter.CTkFrame(root,width=1080,height=730,fg_color="#f7f7f6",corner_radius=24)
label2.place(x=440,y=40)
label1 = customtkinter.CTkFrame(root,width=1050,height=720,fg_color="white",corner_radius=24,bg_color="#f7f7f6")
label1.place(x=450,y=45)

perfileditar = Image.open("icons/editarfondo.jpg")
perfileditar = perfileditar.resize((380,800))
editarphoto = ImageTk.PhotoImage(perfileditar)

editarlabel = tk.Label(root, image=editarphoto,bg="white")
editarlabel.place(x=-1,y=0)

resultados_texto1 = tk.Text(root, width=30, height=10,font=("arial",18,"bold"),bg="#FAF9F9")
resultados_texto1.place(x=900, y=350)
root.columnconfigure(0, weight=1)

# DATOS
# CODIGO DE ESTUDIANTE
codigo = tk.Label(text="Código del Estudiante",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
codigo.place(x=400,y=20)

# CUADRO DE TEXTO
codigo_texto = customtkinter.CTkEntry(root, width= 180, font=("arial", 25),placeholder_text="2022-119230",fg_color="#FAF9F9",text_color="black")
codigo_texto.place(x=680, y=32)

# NOMBRES
nombre = tk.Label(text="Nombres",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
nombre.place(x=400, y=85)
# APELLIDOS
apellido = tk.Label(text="Apellidos",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
apellido.place(x=400, y=135)
telefono = tk.Label(text="Teléfono",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
telefono.place(x=400,y=185)
correo_p = tk.Label(text="Correo personal",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
correo_p.place(x=400,y=235)
escuela = tk.Label(text="Escuela",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
escuela.place(x=400,y=285)
turno = tk.Label(text="Turno",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
turno.place(x=400,y=335)
seccion = tk.Label(text="Sección",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
seccion.place(x=510,y=335)

departamento = tk.Label(text="Departamento",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
departamento.place(x=400,y=385)
provincia = tk.Label(text="Provincia",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
provincia.place(x=400,y=435)
distrito = tk.Label(text="Distrito",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
distrito.place(x=400,y=485)
tipo_zona = tk.Label(text="Tipo de zona",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
tipo_zona.place(x=400,y=535)
nom_zona = tk.Label(text="Nombre de zona",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
nom_zona.place(x=400,y=585)
tipo_via = tk.Label(text="Tipo de via",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
tipo_via.place(x=900,y=85)
nom_via = tk.Label(text="Nombre de via",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
nom_via.place(x=900,y=135)
numero = tk.Label(text="Número",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
numero.place(x=900,y=185)
referencia = tk.Label(text="Referencia",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
referencia.place(x=900,y=235)

# NOTA 1
#nota1 = tk.Label(text="Nota 1",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
#nota1.place(x=400, y=170)
# NOTA 2
#nota2 = tk.Label(text="Nota 2",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
#nota2.place(x=400, y=220)
# NOTA 3
#nota3 = tk.Label(text="Nota 3",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
#nota3.place(x=400, y=270)

#datos actuales
datos_actuales = tk.Label(text="Datos Actuales",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="purple")
datos_actuales.place(x=900, y=285)

# CUADRO DE TEXTO
nombre_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="Javier Matias",fg_color="#FAF9F9",text_color="black")
nombre_texto.place(x=520, y=93)
apellido_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="Olivera Huacca",fg_color="#FAF9F9",text_color="black")
apellido_texto.place(x=520, y=143)
telefono_texto = customtkinter.CTkEntry(root, width=120, font=("arial", 20),placeholder_text="923421523",fg_color="#FAF9F9",text_color="black")
telefono_texto.place(x=520, y=193)
correo_p_texto = customtkinter.CTkEntry(root, width=260, font=("arial", 20),placeholder_text="javiermatias24@gmail.com",fg_color="#FAF9F9",text_color="black")
correo_p_texto.place(x=580, y=243)

# COMANDO PARA ESCUELA DESDE LA BASE DE DATOS 
consulta = "SELECT nom_escuela FROM escuela"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
escuela_texto = ttk.Combobox(root, values= datos,state="readonly",width=5,height=5)
escuela_texto.place(x= 480,y = 295)

turno_texto = ttk.Combobox(root, values=("M", "T"),state="readonly",width=2)
turno_texto.place(x= 470,y = 345)
seccion_texto = ttk.Combobox(root, values=("A", "B"),state="readonly",width=2)
seccion_texto.place(x= 590,y = 345)

# DIRECCION_TEXTO
consulta = "SELECT nom_departamento FROM departamento"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
departamento_texto = ttk.Combobox(root, values=datos,state="readonly",width=30)
departamento_texto.place(x= 540,y = 395)

consulta = "SELECT nom_provincia FROM provincia"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
provincia_texto = ttk.Combobox(root, values=datos,state="readonly",width=20)
provincia_texto.place(x= 500,y = 445)

consulta = "SELECT nom_distrito FROM distrito"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
distrito_texto = ttk.Combobox(root, values=datos,state="readonly",width=20)
distrito_texto.place(x= 500,y = 495)

consulta = "SELECT tipo_zona FROM zona"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
tipo_zona_texto = ttk.Combobox(root, values=datos,state="readonly",width=30)
tipo_zona_texto.place(x= 530,y = 545)
nom_zona_texto = customtkinter.CTkEntry(root, width=210, font=("arial", 20),placeholder_text="Las Américas",fg_color="#FAF9F9",text_color="black")
nom_zona_texto.place(x= 560, y= 595)

consulta = "SELECT tipo_via FROM via"
db.cursor.execute(consulta)
datos = [fila[0] for fila in db.cursor]
tipo_via_texto = ttk.Combobox(root, values=datos,state="readonly",width=20)
tipo_via_texto.place(x= 1020,y = 95)
nom_via_texto = customtkinter.CTkEntry(root, width=210, font=("arial", 20),placeholder_text="Calle Zela",fg_color="#FAF9F9",text_color="black")
nom_via_texto.place(x=1040, y= 140)

numero_texto = customtkinter.CTkEntry(root, width=130, font=("arial", 20),placeholder_text="Mz:z lte:4",fg_color="#FAF9F9",text_color="black")
numero_texto.place(x=990, y=190)
referencia_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 20),placeholder_text="Cerca del grifo",fg_color="#FAF9F9",text_color="black")
referencia_texto.place(x=1020, y=240)

#nota1_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 25),placeholder_text="0",fg_color="#FAF9F9",text_color="black")
#nota1_texto.place(x=500, y=360)
#nota2_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 25),placeholder_text="0",fg_color="#FAF9F9",text_color="black")
#nota2_texto.place(x=500, y=480)
#nota3_texto = customtkinter.CTkEntry(root, width=250, font=("arial", 25),placeholder_text="0",fg_color="#FAF9F9",text_color="black")
#nota3_texto.place(x=500, y=600)

#FUNCIONES:

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

        no_encontrado = tk.Label(text="CÓDIGO NO INGRESADO",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="red")
        no_encontrado.place(x=500,y=640)
        no_encontrado.after(4000, lambda: no_encontrado.place_forget())

    else:
        no_encontrado = tk.Label(text="EL ESTUDIANTE NO SE HA ENCONTRADO EN LA BASE DE DATOS",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="red")
        no_encontrado.place(x=500,y=640)
        no_encontrado.after(4000, lambda: no_encontrado.place_forget())

    j= j+1

# Función para buscar por ID y modificar los datos del estudiante
def modificar_estudiante():
    if nombre_texto.get() != "":
        query = "UPDATE estudiante SET nombre= %s where codigo = %s"
        valores = [nombre_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if apellido_texto.get() != "":
        query = "UPDATE estudiante SET apellido= %s where codigo = %s"
        valores = [apellido_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if telefono_texto.get() != "":
        query = "UPDATE telefono SET num_telefono= %s where estudiante_codigo = %s"
        valores = [apellido_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if correo_p_texto.get() != "":
        query = "UPDATE correo SET nom_correo = %s where estudiante_codigo = %s and nom_correo LIKE %s"
        dominio = '%gmail%'
        valores = [correo_p_texto.get(), codigo_texto.get(),dominio]
        cursor.execute(query,valores)
        db.connection.commit()
    if escuela_texto.get() != "":
        query = "UPDATE estudiante SET escuela_idescuela= %s where codigo = %s"
        valores = [id_escuela, codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if turno_texto.get() != "":
        query = "UPDATE estudiante SET turno= %s where codigo = %s"
        valores = [turno_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if seccion_texto.get() != "":
        query = "UPDATE estudiante SET seccion= %s where codigo = %s"
        valores = [seccion_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if departamento_texto.get() != "":
        query = "UPDATE direccion SET departamento_iddepartamento= %s where estudiante_codigo = %s"
        valores = [id_depa, codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if provincia_texto.get() != "":
        query = "UPDATE direccion SET provincia_idprovincia= %s where estudiante_codigo = %s"
        valores = [id_provincia, codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if distrito_texto.get() != "":
        query = "UPDATE direccion SET distrito_iddistrito = %s where estudiante_codigo = %s"
        valores = [id_distrito, codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if tipo_zona_texto.get() != "":
        query = "UPDATE direccion SET zona_idzona = %s where estudiante_codigo = %s"
        valores = [id_zona, codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if nom_zona_texto.get() != "":
        query = "UPDATE direccion SET nom_zona= %s where estudiante_codigo = %s"
        valores = [nom_zona_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if tipo_via_texto.get() != "":
        query = "UPDATE direccion SET via_idvia = %s where estudiante_codigo = %s"
        valores = [id_via, codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    if nom_via_texto.get() != "":
        query = "UPDATE direccion SET nom_via= %s where estudiante_codigo = %s"
        valores = [nom_via_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if numero_texto.get() != "":
        query = "UPDATE direccion SET numero= %s where estudiante_codigo = %s"
        valores = [numero_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()
    if referencia_texto.get() != "":
        query = "UPDATE direccion SET referencia= %s where estudiante_codigo = %s"
        valores = [referencia_texto.get(), codigo_texto.get()]
        cursor.execute(query,valores)
        db.connection.commit()    
    mostrar_fila()
    limpiar()

#LIMPIAR LOS TEXTOS Y COMBOBOX
def limpiar():

    textos = [nombre_texto,apellido_texto,telefono_texto,correo_p_texto,nom_via_texto,nom_zona_texto,numero_texto,referencia_texto]
    comboboxes = [escuela_texto, turno_texto,seccion_texto,departamento_texto,provincia_texto,distrito_texto,tipo_zona_texto,tipo_via_texto]  # Reemplaza con tus propios comboboxes

    for combobox in comboboxes:
        combobox.set("")

    for texto in textos:
        texto.delete(0, tk.END)

#volver al menu
def abrir_archivo():
    db.cursor.close()
    db.connection.close()
    root.destroy()  # Cierra la ventana actual

#BOTONES
atras = customtkinter.CTkButton(root, text="Volver al Menú",font=("arial",24,"bold"),command = lambda:abrir_archivo())
atras.place(x=680,y=700)
boton_modificar = customtkinter.CTkButton(root, text="Editar Datos",font=("arial",24,"bold"),command = lambda:modificar_estudiante())
boton_modificar.place(x=1100, y=700)
boton_busqueda = customtkinter.CTkButton(root, text="Buscar",font=("arial",24,"bold"),command=lambda:mostrar_fila())
boton_busqueda.place(x=880, y=32)

root.mainloop()
