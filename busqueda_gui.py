import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import subprocess

#ventana principal
root = tk.Tk()
root.configure(bg="#6cc3d2")

#tamaño de pantalla
root.geometry("1920x1080")

excel_file = pd.ExcelFile('registro.xlsx')

# Crear un diccionario vacío para almacenar los DataFrames
dataframes = {}

# Iterar por cada hoja del archivo Excel
for sheet_name in excel_file.sheet_names:
    # Leer la hoja en un DataFrame y almacenarla en el diccionario usando el nombre de la hoja como clave
    dataframes[sheet_name] = pd.read_excel(excel_file, sheet_name)

# Función para buscar por ID en todos los DataFrames
def buscar_por_id(id):
    # Crear un DataFrame vacío para almacenar los resultados
    resultados = pd.DataFrame()
    # Iterar por cada clave y valor en el diccionario de DataFrames
    for clave, df in dataframes.items():
        # Filtrar el DataFrame por el ID
        resultado = df[df['ID'] == id]
        # Agregar el resultado al DataFrame de resultados
        resultados = pd.concat([resultados, resultado], ignore_index=True)

    # Seleccionar solo las columnas deseadas
    columnas_deseadas = ['ID', 'Nombre', 'Apellido', 'Nota1', 'Nota2', 'Nota3']
    resultados_seleccionados = resultados.loc[:, columnas_deseadas]

    # Devolver el DataFrame de resultados
    resultados_texto.delete('1.0', tk.END)  # Borrar el contenido actual del widget 
    resultados_texto.insert(tk.END, resultados_seleccionados.to_string(index=False))  # Insertar los resultados en el widget


#Titulo
title = tk.Label(
    root,
    text="BUSQUEDA DE ESTUDIANTE",
    background="#6cd2d1",
    relief="solid",
    borderwidth=3,
    font=("e Explosive Attack", 39, "bold"	),
    fg="#184e4e",
    width="48",
    height="2",
    pady="10"
)
title.place(x=0, y=30)

frame = tk.Frame(root, bg='#6cd2d1', width=1920, height=580,borderwidth=3,relief="solid")
# Crea un canvas dentro del Frame
canvas = tk.Canvas(
frame, 
width=280, 
height=500, 
bd=0, 
highlightthickness=0,
)
frame.place(x=0, y=200)

identificador = tk.Label(text="INGRESE EL CÓDIGO DEL ESTUDIANTE:",font=("HELVETICA",20,"bold"),bg="#6cd2d1")
identificador.place(x=45,y=240)


#####

identificador_texto = tk.Entry(root, width=15, font=("arial", 20), relief="solid")

identificador_texto.place(x=45, y=290)



def procesar_evento(event):
    buscar_por_id(identificador_texto.get())

identificador_texto.bind("<Return>", procesar_evento)

boton_busqueda = tk.Button(root, text="BUSCAR", font=("arial", 15, "bold"), command=lambda: buscar_por_id(identificador_texto.get()))
boton_busqueda.place(x=45, y=350)


resultados_texto = tk.Text(root, width=70, height=5,font=("arial",20,"bold"))
resultados_texto.place(x=45, y=400)
root.columnconfigure(0, weight=1)

#volver al menu
def abrir_archivo():
    archivo = "gui.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    root.destroy()  # Cierra la ventana actual
    subprocess.call(["python", archivo])

boton1 = tk.Button(root, text="VOLVER AL MENÚ PRINCIPAL",font=("arial",15,"bold"),command=abrir_archivo)
boton1.place(x=680,y=700)

root.mainloop()