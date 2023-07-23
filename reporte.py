import tkinter as tk
from tkinter import ttk,Label
from tkinter import *
from PIL import Image, ImageTk
from conexion import *
import pandas as pd
import subprocess
import customtkinter
import tabulate as tb
from tkinter import StringVar

db = database()
cursor = db.connection.cursor()

# Ventana principal
root = tk.Tk()
root.configure(bg="#f8f7f9")

a_nio = StringVar()
opcion = StringVar()
opcion_o = StringVar()
sex = StringVar()
tur = StringVar()
esc = StringVar()
fal = StringVar()
depa = StringVar()
forma_o = StringVar()
lista = ttk.Treeview()
i = int()
id_escuela = int()
id_facultad = int()
id_depa = int()

ordenar_texto = None
codigo_texto = None
nombre_texto = None
apellidos_texto = None
sexo_texto = None
turno_texto = None
forma_texto = None
escuela_texto = None
facultad_texto = None
departamento_texto = None

ordenar = None
nombres = None
anio = None
apellidos = None
sexo = None
turno = None
forma = None
escuela = None
facultad = None
departamento = None

perfileditar = Image.open("icons/reportefondo.png")
perfileditar = perfileditar.resize((450,800))
editarphoto = ImageTk.PhotoImage(perfileditar)

editarlabel = tk.Label(root, image=editarphoto,bg="white")
editarlabel.place(x=-1,y=0)

#fondo imagen
fondo7 = Image.open("icons/fondo7.png")
#perfileditar = perfileditar.resize((450,800))
fondo7photo = ImageTk.PhotoImage(fondo7)

fondolabel = tk.Label(root, image=fondo7photo,bg="white")
fondolabel.place(x=1000,y=0)

#gui
label2 = customtkinter.CTkFrame(root,width=970,height=730,fg_color="#f7f7f6",corner_radius=24)
label2.place(x=500,y=40)
label1 = customtkinter.CTkFrame(root,width=940,height=720,fg_color="white",corner_radius=24,bg_color="#f7f7f6")
label1.place(x=490,y=45)

reporte = tk.Label(text="Generar Reporte de Estudiantes",font=("Bahnschrift Condensed",30,"bold"),bg="white",fg="purple")
reporte.place(x=560,y=80)

# Tamaño de pantalla
root.geometry("1920x1080")

from PIL import ImageGrab

from PIL import Image, ImageTk

filtro = tk.Label(text="Filtro",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
filtro.place(x=540,y=140)
filtro_texto = ttk.Combobox(root, values=("todos","codigo","nombre","apellido","sexo","turno","facultad","escuela","departamento"),textvariable = opcion,state="readonly",width=20,height=5)
filtro_texto.place(x= 620,y = 150)

#Crear labels y combobox dinamicos de acuerdo a la opcion del combobox filtro_texto
def enlazar_evento(event):

    global codigo_texto, anio, nombre_texto, nombres, apellidos, apellidos_texto, sexo, sexo_texto, turno, turno_texto, escuela, escuela_texto

    ocultar()

    if opcion.get() == "codigo":

        anio = tk.Label(text="Año",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        anio.place(x=780,y=140)
        codigo_texto = ttk.Combobox(root, values=("2019","2020","2021","2022","2023"),textvariable = a_nio,state="readonly",width=6)
        codigo_texto.place(x= 825,y = 150)
        
    elif opcion.get() == "nombre":

        nombres = tk.Label(text="Nombres",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        nombres.place(x=780,y=140)
        nombre_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="Javier Matias",fg_color="#FAF9F9",text_color="black")
        nombre_texto.place(x=900, y=145)

    elif opcion.get() == "apellido":

        apellidos = tk.Label(text="Apellidos",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        apellidos.place(x=780,y=140)
        apellidos_texto = customtkinter.CTkEntry(root, width=240, font=("arial", 20),placeholder_text="Olivera Huacca",fg_color="#FAF9F9",text_color="black")
        apellidos_texto.place(x=900, y=145)
    
    elif opcion.get() == "sexo":

        sexo = tk.Label(text="Sexo",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        sexo.place(x=780,y=140)
        sexo_texto = ttk.Combobox(root, values=("M","F"),textvariable = sex,state="readonly",width=4)
        sexo_texto.place(x= 840,y = 150)

    elif opcion.get() == "turno":

        turno = tk.Label(text="Turno",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        turno.place(x=780,y=140)
        turno_texto = ttk.Combobox(root, values=("T","M"),textvariable = tur,state="readonly",width=4)
        turno_texto.place(x= 840,y = 150) 

    elif opcion.get() == "facultad":

        facultad = tk.Label(text="Facultad",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        facultad.place(x=780,y=140)
        query = "SELECT nom_facultad FROM facultad"
        db.cursor.execute(query)
        datos = [fila[0] for fila in db.cursor] 
        facultad_texto = ttk.Combobox(root, values=datos,textvariable = fal,state="readonly",width=6)
        facultad_texto.place(x= 880,y = 150)

        # Asociar evento de selección al combobox
        facultad_texto.bind("<<ComboboxSelected>>", obtener_id_facultad)

    elif opcion.get() == "escuela":

        escuela = tk.Label(text="Escuela",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        escuela.place(x=780,y=140)
        query = "SELECT nom_escuela FROM escuela"
        db.cursor.execute(query)
        datos = [fila[0] for fila in db.cursor] 
        escuela_texto = ttk.Combobox(root, values=datos,textvariable = esc,state="readonly",width=6)
        escuela_texto.place(x= 880,y = 150)

        # Asociar evento de selección al combobox
        escuela_texto.bind("<<ComboboxSelected>>", obtener_id_escuela)

    elif opcion.get() == "departamento":

        departamento = tk.Label(text="Departamento",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        departamento.place(x=780,y=140)
        query = "SELECT nom_departamento FROM departamento"
        db.cursor.execute(query)
        datos = [fila[0] for fila in db.cursor] 
        departamento_texto = ttk.Combobox(root, values=datos,textvariable = depa,state="readonly",width=24)
        departamento_texto.place(x= 940,y = 150)

        # Asociar evento de selección al combobox
        departamento_texto.bind("<<ComboboxSelected>>", obtener_id_depa)

# Asociar evento de selección al combobox
filtro_texto.bind("<<ComboboxSelected>>", enlazar_evento)

def ocultar():
 
    # Ocultar los widgets si ya existen

    global codigo_texto, anio, nombre_texto, nombres, apellidos, apellidos_texto, sexo, sexo_texto, turno, turno_texto, ordenar, ordenar_texto, escuela, escuela_texto, facultad, facultad_texto, departamento, departamento_texto

    labels = [nombres, anio, apellidos, sexo, turno, escuela, facultad, departamento]
    textos = [codigo_texto,nombre_texto,apellidos_texto, sexo_texto, turno_texto, escuela_texto, facultad_texto, departamento_texto]

    for label in labels:
        if label is not None:
            label.place_forget()

    for texto in textos:
        if texto is not None:
            texto.place_forget()

def obtener_id_escuela(event):
    global id_escuela
    nombre_escuela = esc.get()
    consultaa = "SELECT idescuela FROM escuela WHERE nom_escuela = %s"
    cursor.execute(consultaa, (nombre_escuela,))
    resultado = cursor.fetchone()
    if resultado != None:
        id_escuela = resultado[0]
    else:
        id_escuela = 0

def obtener_id_facultad(event):
    global id_facultad
    nombre_facultad = fal.get()
    consultaa = "SELECT idfacultad FROM facultad WHERE nom_facultad = %s"
    cursor.execute(consultaa, (nombre_facultad,))
    resultado = cursor.fetchone()
    if resultado != None:
        id_facultad = resultado[0]
    else:
        id_facultad = 0

def obtener_id_depa(event):
    global id_depa
    nombre_depa = depa.get()
    consultaa = "SELECT iddepartamento FROM departamento WHERE nom_departamento = %s"
    cursor.execute(consultaa, (nombre_depa,))
    resultado = cursor.fetchone()
    if resultado != None:
        id_depa = resultado[0]
    else:
        id_depa = 0

def ordenar_reporte():

    global ordenar, ordenar_texto, forma, forma_texto

    if opcion.get() != "":
        ordenar = tk.Label(text="Ordenar",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        ordenar.place(x=540,y=190)
        ordenar_texto = ttk.Combobox(root, values=("codigo","nombre","apellido","sexo","turno","facultad","escuela","departamento"),textvariable = opcion_o,state="readonly",width=20,height=5)
        ordenar_texto.place(x= 630,y = 200)
        forma = tk.Label(text="Forma",font=("Bahnschrift Condensed",20,"bold"),bg="white",fg="black")
        forma.place(x=800,y=190)
        forma_texto = ttk.Combobox(root, values=("Ascendente","Descendente"),textvariable = forma_o,state="readonly",width=14)
        forma_texto.place(x= 880,y = 200)

#Funcion para realizar consultas en mysql
def generar_reporte():

    global codigo_texto, nombre_texto, guardar, apellidos_texto, ordenar, ordenar_texto, forma, forma_texto,i 

    if ordenar_texto is not None:
        ordenar.place_forget()
        ordenar_texto.place_forget()
    if forma_texto is not None:
        forma.place_forget()
        forma_texto.place_forget()

    ocultar()

    if opcion.get() == "todos":
        
        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad"
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento ORDER BY "+opcion_o.get() + " " + fo

        cursor.execute(query)
        resultados = cursor.fetchall()
    
        if resultados:
            crear_interfaz_consultas("0",resultados)
        else:
            no_reporte = tk.Label(text="NO HAY REPORTES",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="red")
            no_reporte.place(x=840,y=340)
            no_reporte.after(2000, lambda: no_reporte.place_forget())
            if i > 0:
                lista.place_forget()

    elif opcion.get() == "codigo":

        guardar = a_nio.get()
        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.codigo LIKE '%{}%'".format(guardar)
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE es.codigo LIKE '%{}%' ORDER BY ".format(guardar) +opcion_o.get() + " " + fo

        cursor.execute(query)
        resultados = cursor.fetchall()
        evaluar_resultado(guardar,resultados)

    elif opcion.get() == "nombre":

        guardar = nombre_texto.get()
        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.nombre LIKE '%{}%'".format(guardar)
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE es.nombre LIKE '%{}%' ORDER BY ".format(guardar) +opcion_o.get() + " " + fo

        cursor.execute(query)
        resultados = cursor.fetchall()
        evaluar_resultado(guardar,resultados)

    elif opcion.get() == "apellido":

        guardar = apellidos_texto.get()
        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.apellido LIKE '%{}%'".format(guardar)
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE es.apellido LIKE '%{}%' ORDER BY ".format(guardar) +opcion_o.get() + " " + fo

        cursor.execute(query)
        resultados = cursor.fetchall()
        evaluar_resultado(guardar,resultados)

    elif opcion.get() == "sexo":

        guardar = sex.get()
        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.sexo =%s"
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE es.sexo =%s ORDER BY " +opcion_o.get() + " " + fo

        cursor.execute(query,(guardar,))
        resultados = cursor.fetchall()
        evaluar_resultado(guardar,resultados)

    elif opcion.get() == "turno":

        guardar = tur.get()
        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.turno =%s"
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE es.turno =%s ORDER BY "+opcion_o.get() + " " + fo

        cursor.execute(query,(guardar,))
        resultados = cursor.fetchall()
        evaluar_resultado(guardar,resultados)

    elif opcion.get() == "escuela":

        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.escuela_idescuela =%s"
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE es.escuela_idescuela =%s ORDER BY "+opcion_o.get() + " " + fo

        cursor.execute(query,(id_escuela,))
        resultados = cursor.fetchall()
        evaluar_resultado(id_escuela,resultados)

    elif opcion.get() == "facultad":

        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE e.facultad_idfacultad =%s"
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE e.facultad_idfacultad =%s ORDER BY "+opcion_o.get() + " " + fo

        cursor.execute(query,(id_facultad,))
        resultados = cursor.fetchall()
        evaluar_resultado(id_facultad,resultados)
        
    elif opcion.get() == "departamento":

        if opcion_o.get() == "":
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE d.departamento_iddepartamento =%s"
        else:
            fo = sub_forma()
            evaluar_ordenar()
            query = "SELECT codigo,nombre,apellido,fecha_nacimiento,nro_dni,sexo,turno,seccion,nom_facultad,nom_escuela FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE d.departamento_iddepartamento =%s ORDER BY "+opcion_o.get() + " " + fo

        cursor.execute(query,(id_depa,))
        resultados = cursor.fetchall()
        evaluar_resultado(id_depa,resultados)
        
    opcion_o.set("")
    forma_o.set("")

#Evalua la forma de ordenar
def sub_forma():
    if forma_o.get() == "Ascendente":
        fo = forma_o.get()[0:3]
    else:
        fo = forma_o.get()[0:4]
    return fo

#Evalua el resultado de la query
def evaluar_resultado(guardar,resultados):
    global i
    if resultados:
        crear_interfaz_consultas(guardar,resultados)
    else:
        no_reporte = tk.Label(text="NO HAY REPORTES",font=("Bahnschrift Condensed",28,"bold"),bg="white",fg="red")
        no_reporte.place(x=840,y=340)
        no_reporte.after(2000, lambda: no_reporte.place_forget())
        if i > 0:
            lista.place_forget()


#evaluar ordenar
def evaluar_ordenar():
    if opcion_o.get() == "escuela":
        opcion_o.set("nom_escuela")
    elif opcion_o.get() == "facultad":
        opcion_o.set("nom_facultad")
    elif opcion_o.get() == "departamento": 
        opcion_o.set("nom_departamento")

#Crear la interfaz del reporte
def crear_interfaz_consultas(guardar,resultados):
    global lista,i

    if i > 0:
       lista.place_forget()

    if opcion.get() != "todos":
        if opcion.get() != "escuela" and opcion.get() != "facultad" and opcion.get() != "departamento":
            sql = "SELECT TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) FROM estudiante es where es.{} LIKE '%{}%'".format(opcion.get(), guardar)
            cursor.execute(sql)
            edad = cursor.fetchall()
            consulta = "SELECT count(*) FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.{} LIKE '%{}%'".format(opcion.get(), guardar)
            cursor.execute(consulta)
        else:
            if opcion.get() == "escuela":

                opcion.set("escuela_idescuela")
                sql = "SELECT TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) FROM estudiante es where es.{} = %s".format(opcion.get())
                cursor.execute(sql,(guardar,))
                edad = cursor.fetchall()
                consulta = "SELECT count(*) FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE es.{} = %s".format(opcion.get())
                cursor.execute(consulta,(guardar,))

            elif opcion.get() == "facultad":
    
                opcion.set("facultad_idfacultad")
                sql = "SELECT TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad where e.{} = %s".format(opcion.get())
                cursor.execute(sql,(guardar,))
                edad = cursor.fetchall()
                consulta = "SELECT count(*) FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad WHERE e.{} = %s".format(opcion.get())
                cursor.execute(consulta,(guardar,))

            elif opcion.get() == "departamento":

                opcion.set("departamento_iddepartamento")
                sql = "SELECT TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) FROM estudiante es INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento where d.{} = %s".format(opcion.get())
                cursor.execute(sql,(guardar,))
                edad = cursor.fetchall()
                consulta = "SELECT count(*) FROM estudiante es INNER JOIN direccion d ON es.codigo = d.estudiante_codigo INNER JOIN departamento de ON d.departamento_iddepartamento = de.iddepartamento WHERE d.{} = %s".format(opcion.get())
                cursor.execute(consulta,(guardar,))

        cantidad_registros = cursor.fetchall()
        cantidad = cantidad_registros[0]

    else:
        sql = "SELECT TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) FROM estudiante"
        cursor.execute(sql)
        edad = cursor.fetchall()

        consulta = "SELECT count(*) FROM estudiante es INNER JOIN escuela e ON es.escuela_idescuela = e.idescuela INNER JOIN facultad f ON e.facultad_idfacultad = f.idfacultad "
        cursor.execute(consulta)
        cantidad_registros = cursor.fetchall()
        cantidad = cantidad_registros[0]

    lista = ttk.Treeview(root, columns=(1,2,3,4,5,6,7,8,9,10),show="headings",height=cantidad)
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
    lista.heading(9, text="Facultad")
    lista.heading(10, text="Escuela")
    lista.column(1,width=80,anchor=CENTER)
    lista.column(2,width=140,anchor=CENTER)
    lista.column(3,width=140,anchor=CENTER)
    lista.column(4,width=40,anchor=CENTER)
    lista.column(5,width=80,anchor=CENTER)
    lista.column(6,width=80,anchor=CENTER)
    lista.column(7,width=80,anchor=CENTER)
    lista.column(8,width=80,anchor=CENTER)
    lista.column(9,width=60,anchor=CENTER)
    lista.column(10,width=60,anchor=CENTER)
    
    for j,resultado in enumerate(resultados):
        item = lista.insert('', 'end', values=resultado)
        lista.set(item, column=4, value=edad[j])
        lista.place(x=480,y=240)
    
    i = i+1
    opcion.set("")

# Volver al menu
def abrir_archivo():
    db.cursor.close()
    db.connection.close()
    root.destroy()  # Cierra la ventana actual

atras = customtkinter.CTkButton(root, text="Volver al Menú", font=("arial", 24, "bold"), command=lambda: abrir_archivo())
atras.place(x=680, y=700)
reporte = customtkinter.CTkButton(root, text="Generar Reporte", font=("arial", 24, "bold"),command=lambda: generar_reporte())
reporte.place(x=1000, y=700)
order = customtkinter.CTkButton(root, text="Ordenar", font=("arial", 24, "bold"),command=lambda: ordenar_reporte())
order.place(x=1200, y=145)

root.mainloop()
