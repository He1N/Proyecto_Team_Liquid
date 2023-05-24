import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import subprocess


# Ventana principal
root = tk.Tk()
root.configure(bg="#6cc3d2")

# Tamaño de pantalla
root.geometry("1920x1080")

# Cargar el archivo Excel existente
try:
    excel_file = pd.ExcelFile('registro.xlsx', engine='openpyxl')
    dataframes = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}
except FileNotFoundError:
    # Si el archivo no existe, crea un diccionario vacío de DataFrames
    dataframes = {}

# Función para agregar un estudiante a una hoja específica
def agregar_estudiante(codigo, nombre, apellido, nota1, nota2, nota3, hoja):
    # Crear un nuevo DataFrame con los datos del estudiante
    nuevo_estudiante = pd.DataFrame({'ID': [codigo],'Nombre': [nombre], 'Apellido': [apellido], 'Nota1': [nota1], 'Nota2': [nota2], 'Nota3': [nota3]})
    
    # Obtener el DataFrame de la hoja especificada
    hoja_df = dataframes.get(hoja)
    
    # Si la hoja no existe, crear una nueva con el nuevo estudiante
    if hoja_df is None:
        dataframes[hoja] = nuevo_estudiante
    else:
        # Agregar el nuevo estudiante al DataFrame de la hoja existente
        hoja_df = pd.concat([hoja_df, nuevo_estudiante], ignore_index=True)
        dataframes[hoja] = hoja_df


    # Guardar los cambios en el archivo Excel
    with pd.ExcelWriter('registro.xlsx', engine='openpyxl') as writer:
        for sheet_name, df in dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False, startrow=0)
        writer.save()


# Titulo
title = tk.Label(
    root,
    text="REGISTRAR NUEVO ESTUDIANTE",
    background="#6cd2d1",
    relief="solid",
    borderwidth=3,
    font=("e Explosive Attack", 39, "bold"),
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

# DATOS
# CODIGO DE ESTUDIANTE
codigo = tk.Label(text="CÓDIGO DE ESTUDIANTE:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
codigo.place(x=45, y=240)
# NOMBRES
nombre = tk.Label(text="NOMBRES:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nombre.place(x=445, y=340)
# APELLIDOS
apellido = tk.Label(text="APELLIDOS:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
apellido.place(x=45, y=340)
# NOTA 1
nota1 = tk.Label(text="NOTA 1:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nota1.place(x=45, y=440)
# NOTA 2
nota2 = tk.Label(text="NOTA 2:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nota2.place(x=45, y=520)
# NOTA 3
nota3 = tk.Label(text="NOTA 3:", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
nota3.place(x=45, y=600)

user = tk.Label(text="Foto del Estudiante", font=("HELVETICA", 18, "bold"), bg="#6cd2d1")
user.place(x=1090, y=220)

# CUADRO DE TEXTO
codigo_texto = tk.Entry(root, width=30, font=("arial", 16), relief="solid")
codigo_texto.place(x=45, y=290)
nombre_texto = tk.Entry(root, width=30, font=("arial", 16), relief="solid")
nombre_texto.place(x=445, y=390)
apellido_texto = tk.Entry(root, width=30, font=("arial", 16), relief="solid")
apellido_texto.place(x=45, y=390)
nota1_texto = tk.Entry(root, width=8, font=("arial", 16), relief="solid")
nota1_texto.place(x=180, y=445)
nota2_texto = tk.Entry(root, width=8, font=("arial", 16), relief="solid")
nota2_texto.place(x=180, y=525)
nota3_texto = tk.Entry(root, width=8, font=("arial", 16), relief="solid")
nota3_texto.place(x=180, y=605)


# IMAGEN 1
# Cargar la imagen
image1 = Image.open("icons/usuario.png")
image1 = image1.resize((480, 480))
photo1 = ImageTk.PhotoImage(image1)

# Crear una etiqueta para mostrar la imagen
image_label1 = tk.Label(root, image=photo1, bg="#6cd2d1")
image_label1.place(x=970, y=260)

def procesar_evento(event):
    agregar_estudiante(codigo_texto.get(), nombre_texto.get(), apellido_texto.get(), nota1_texto.get(), nota2_texto.get(), nota3_texto.get(), 'Estudiantes')

codigo_texto.bind("<Return>", procesar_evento)
nombre_texto.bind("<Return>", procesar_evento)
apellido_texto.bind("<Return>", procesar_evento)
nota1_texto.bind("<Return>", procesar_evento)
nota2_texto.bind("<Return>", procesar_evento)
nota3_texto.bind("<Return>", procesar_evento)

# Boton agregar
boton_agregar = tk.Button(root, text="AGREGAR ESTUDIANTE", font=("arial", 15, "bold"), command=lambda: agregar_estudiante(codigo_texto.get(), nombre_texto.get(), apellido_texto.get(), nota1_texto.get(), nota2_texto.get(), nota3_texto.get(), 'Estudiantes'))
boton_agregar.place(x=45, y=690)

#volver al menu
def abrir_archivo():
    archivo = "gui.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    root.destroy()  # Cierra la ventana actual
    subprocess.call(["python", archivo])

boton1 = tk.Button(root, text="VOLVER AL MENÚ PRINCIPAL",font=("arial",15,"bold"),command=abrir_archivo)
boton1.place(x=680,y=700)

root.mainloop()
