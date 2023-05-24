import pandas as pd
import tkinter as tk
from tkinter import ttk
import subprocess

#ventana principal
root = tk.Tk()                  
root.configure(bg="#6cc3d2")
a=" "
# Tamaño de pantalla
root.geometry("1920x1080")

#Titulo
title = tk.Label(
    root,
    text="MODIFICACIÓN DE ESTUDIANTE",
    background="#6cd2d1",
    relief="solid",
    borderwidth=3,
    font=("e Explosive Attack", 39, "bold"  ),
    fg="#184e4e",
    width="48",
    height="2",
    pady="10"
)
title.place(x=0, y=30)

frame = tk.Frame(root, bg='#6cd2d1', width=1920, height=580, borderwidth=3, relief="solid")
# Crea un canvas dentro del Frame
canvas = tk.Canvas(
    frame, 
    width=280, 
    height=500, 
    bd=0, 
    highlightthickness=0,
)
frame.place(x=0, y=200)


# Cargar el archivo Excel
excel_file = 'registro.xlsx'

# Leer el registro de estudiantes en un DataFrame
df_estudiantes = pd.read_excel(excel_file, sheet_name='Estudiantes')


# Función para buscar por ID y modificar los datos del estudiante
def modificar_estudiante(id):
    filtro = df_estudiantes['ID'] == id
    if filtro.any():
        nombre = nombre_texto.get()
        apellido = apellido_texto.get()
        nota1 = nota1_texto.get()
        nota2 = nota2_texto.get()
        nota3 = nota3_texto.get()
        # Modificar los datos del estudiante
        if nombre != "":
            df_estudiantes.loc[filtro, 'Nombre'] = nombre
        if apellido != "":
            df_estudiantes.loc[filtro, 'Apellido'] = apellido
        if nota1 != "":
            df_estudiantes.loc[filtro, 'Nota1'] = float(nota1)
        if nota2 != "":
            df_estudiantes.loc[filtro, 'Nota2'] = float(nota2)
        if nota3 != "":
            df_estudiantes.loc[filtro, 'Nota3'] = float(nota3)
        # Guardar los cambios en un nuevo archivo Excel
        df_estudiantes.to_excel('registro.xlsx', sheet_name='Estudiantes', index=False)

        # Calcular automáticamente el promedio
        #df_estudiantes.loc[filtro, 'Nota final'] = df_estudiantes.loc[filtro, ['Nota 1', 'Nota 2', 'Nota 3']].mean(axis=1)
        return True
    return False

def buscar_id():
    id = codigo_texto.get()
    if (df_estudiantes['ID'] == id).any():
        resultados_texto.delete('1.0', tk.END)  # Borrar el contenido actual del widget
        resultados_texto.insert(tk.END, "Estudiante encontrado.")
        # Llamar a la función modificar_estudiante
        modificar_estudiante(id)
    else:
        resultados_texto.delete('1.0', tk.END)  # Borrar el contenido actual del widget
        resultados_texto.insert(tk.END, "Estudiante no encontrado.")


# DATOS
# CODIGO DE ESTUDIANTE
codigo = tk.Label(text="CÓDIGO DE ESTUDIANTE:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
codigo.place(x=45, y=240)

# CUADRO DE TEXTO
codigo_texto = tk.Entry(root, width=30, font=("arial", 16), relief="solid")
codigo_texto.place(x=45, y=290)
   
resultados_texto = tk.Text(root, width=22, height=1,font=("Helveltica",19,"bold"))
resultados_texto.place(x=460, y=285)
resultados_texto.delete('1.0', tk.END)  # Borrar el contenido actual del widget 

boton_busqueda = tk.Button(root, text="BUSCAR", font=("arial", 15, "bold"), command=buscar_id)
boton_busqueda.place(x=45, y=350)



resultados_texto.insert(tk.END,a)
# Guardar los cambios en el archivo Excel
df_estudiantes.to_excel(excel_file, sheet_name='Estudiantes', index=False)

# NOMBRES
nombre = tk.Label(text="NOMBRES:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nombre.place(x=445, y=410)
# APELLIDOS
apellido = tk.Label(text="APELLIDOS:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
apellido.place(x=45, y=410)
# NOTA 1
nota1 = tk.Label(text="NOTA 1:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nota1.place(x=45, y=510)
# NOTA 2
nota2 = tk.Label(text="NOTA 2:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nota2.place(x=45, y=590)
# NOTA 3
nota3 = tk.Label(text="NOTA 3:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nota3.place(x=45, y=670)

# CUADRO DE TEXTO
nombre_texto = tk.Entry(root, width=30, font=("arial", 16), relief="solid")
nombre_texto.place(x=445, y=460)
apellido_texto = tk.Entry(root, width=30, font=("arial", 16), relief="solid")
apellido_texto.place(x=45, y=460)
nota1_texto = tk.Entry(root, width=8, font=("arial", 16), relief="solid")
nota1_texto.place(x=180, y=515)
nota2_texto = tk.Entry(root, width=8, font=("arial", 16), relief="solid")
nota2_texto.place(x=180, y=595)
nota3_texto = tk.Entry(root, width=8, font=("arial", 16), relief="solid")
nota3_texto.place(x=180, y=675)

def procesar_evento(event):
    modificar_estudiante(codigo_texto.get())

def procesar_evento1(event):
    buscar_id()

codigo_texto.bind("<Return>", procesar_evento1)
nombre_texto.bind("<Return>", procesar_evento)
apellido_texto.bind("<Return>", procesar_evento)
nota1_texto.bind("<Return>", procesar_evento)
nota2_texto.bind("<Return>", procesar_evento)
nota3_texto.bind("<Return>", procesar_evento)

boton_modificar = tk.Button(root, text="MODIFICAR ESTUDIANTE", font=("arial", 15, "bold"), command=lambda: modificar_estudiante(codigo_texto.get()))
boton_modificar.place(x=445, y=515)

#volver al menu
def abrir_archivo():
    archivo = "gui.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    root.destroy()  # Cierra la ventana actual
    subprocess.call(["python", archivo])

boton1 = tk.Button(root, text="VOLVER AL MENÚ PRINCIPAL",font=("arial",15,"bold"),command=abrir_archivo)
boton1.place(x=680,y=700)

root.mainloop()
