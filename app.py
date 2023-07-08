import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

#customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
#customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = tk.Tk()  # create CTk window like you do with the Tk window
app.configure(bg="#ddecf1")
app.geometry("1920x1080")
app.title("PROGRAMA DIGITAL DE REGISTRO DE NOTAS")

#title
frame_title = customtkinter.CTkFrame(app,width=1170,height=140,fg_color="#f7f7f6",corner_radius=20)
frame_title.place(x=190,y=25)
frame_title = customtkinter.CTkFrame(app,width=1150,height=130,fg_color="white",corner_radius=20,bg_color="#f7f7f6")
frame_title.place(x=200,y=30)

title = customtkinter.CTkLabel(app,text="PROGRAMA DIGITAL DE REGISTRO DE NOTAS",fg_color="white",font=("e Explosive Attack",52,"bold"),anchor="center",width=30,height=2,pady=10,text_color="purple")
title.place(x=260, y=58)
#title_Extra
e1 = tk.Label(text="Cristian Arredondo    -    Edson Huallpa    -    Alejandro Flores    -    Marina Adco    -    Edson Peraza    -    Elias Flores",font=("arial",12),bg="white",fg="gray")
e1.place(x=360,y=120)


#frames
for i in range(0,5):
    frame1 = customtkinter.CTkLabel(master=app,width=290, height=510,fg_color="#f7f7f6",corner_radius=20)
    frame1.place(x=(i*300)+23, y=195)

for i in range(0,5):
    frame = customtkinter.CTkLabel(master=app,width=275, height=500,fg_color="white",corner_radius=20,bg_color="#f7f7f6")
    frame.place(x=(i*300)+30, y=200)

image_fondo1 = Image.open("E://Universidad/Compi/icons/fondo1.png")
image_fondo1 = image_fondo1.resize((260,260))
photo_fondo1 = ImageTk.PhotoImage(image_fondo1)

fondo1_label = tk.Label(app, image=photo_fondo1,bg="white")
fondo1_label.place(x=35,y=430)

image_fondo1_1 = Image.open("E://Universidad/Compi/icons/fondo1.png")
image_fondo1_1 = image_fondo1_1.resize((260,260))
photo_fondo1_1 = ImageTk.PhotoImage(image_fondo1_1)

fondo1_1_label = tk.Label(app, image=photo_fondo1_1,bg="white")
fondo1_1_label.place(x=335,y=430)  

image_fondo1_2 = Image.open("E://Universidad/Compi/icons/fondo1.png")
image_fondo1_2 = image_fondo1_2.resize((260,260))
photo_fondo1_2 = ImageTk.PhotoImage(image_fondo1_2)

fondo1_2_label = tk.Label(app, image=photo_fondo1_2,bg="white")
fondo1_2_label.place(x=635,y=430) 

image_fondo1_3 = Image.open("E://Universidad/Compi/icons/fondo1.png")
image_fondo1_3 = image_fondo1_3.resize((260,260))
photo_fondo1_3 = ImageTk.PhotoImage(image_fondo1_3)

fondo1_3_label = tk.Label(app, image=photo_fondo1_3,bg="white")
fondo1_3_label.place(x=935,y=430) 

image_fondo1_4 = Image.open("E://Universidad/Compi/icons/fondo1.png")
image_fondo1_4 = image_fondo1_4.resize((260,260))
photo_fondo1_4 = ImageTk.PhotoImage(image_fondo1_3)

fondo1_4_label = tk.Label(app, image=photo_fondo1_4,bg="white")
fondo1_4_label.place(x=1235,y=430) 

#Subtitulos-labels
agregar = tk.Label(text="Agregar Estudiante",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
agregar.place(x=65,y=240)

editar = tk.Label(text="Editar Estudiante",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
editar.place(x=380,y=240)

eliminar = tk.Label(text="Eliminar Estudiante",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
eliminar.place(x=660,y=240)

buscar = tk.Label(text="Buscar Estudiante",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
buscar.place(x=970,y=240)

reporte1 = tk.Label(text="Reporte de Estudiantes",font=("Bahnschrift Condensed",25,"bold"),bg="white",fg="purple")
reporte1.place(x=1236,y=240)


#Implementando imagenes
#IMAGEN 1
# Cargar la imagen

image_esis = Image.open("E://Universidad/Compi/icons/esis.png")
image_esis = image_esis.resize((140,140))
photo_esis = ImageTk.PhotoImage(image_esis)

esis_label = tk.Label(app, image=photo_esis,bg="#ddecf1")
esis_label.place(x=30,y=20)

image_team = Image.open("E://Universidad/Compi/icons/liquid1.png")
image_team = image_team.resize((120,135))
photo_team = ImageTk.PhotoImage(image_team)

team_label = tk.Label(app, image=photo_team,bg="#ddecf1")
team_label.place(x=1380,y=30)

image_fondo2 = Image.open("E://Universidad/Compi/icons/fondo2.png")
image_fondo2 = image_fondo2.resize((80,20))
photo_fondo2 = ImageTk.PhotoImage(image_fondo2)

fondo2_label = tk.Label(app, image=photo_fondo2,bg="white")
fondo2_label.place(x=125,y=220)

image_fondo3 = Image.open("E://Universidad/Compi/icons/fondo3.png")
image_fondo3 = image_fondo3.resize((80,25))
photo_fondo3 = ImageTk.PhotoImage(image_fondo3)

fondo3_label = tk.Label(app, image=photo_fondo3,bg="white")
fondo3_label.place(x=430,y=215)

image_fondo4 = Image.open("E://Universidad/Compi/icons/fondo4.png")
image_fondo4 = image_fondo4.resize((80,20))
photo_fondo4 = ImageTk.PhotoImage(image_fondo4)

fondo4_label = tk.Label(app, image=photo_fondo4,bg="white")
fondo4_label.place(x=730,y=220)

image_fondo5 = Image.open("E://Universidad/Compi/icons/fondo5.png")
image_fondo5 = image_fondo5.resize((80,17))
photo_fondo5 = ImageTk.PhotoImage(image_fondo5)

fondo5_label = tk.Label(app, image=photo_fondo5,bg="white")
fondo5_label.place(x=1020,y=220)

image_fondo6 = Image.open("E://Universidad/Compi/icons/fondo6.png")
image_fondo6 = image_fondo6.resize((80,20))
photo_fondo6 = ImageTk.PhotoImage(image_fondo6)

fondo6_label = tk.Label(app, image=photo_fondo6,bg="white")
fondo6_label.place(x=1330,y=220)

#imagenes frames circulares
image1 = Image.open("E:/Universidad/Compi/icons/agregar1.png")
image1 = image1.resize((220, 220))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("E:/Universidad/Compi/icons/editar1.png")
image2 = image2.resize((210, 210))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("E:/Universidad/Compi/icons/eliminar1.png")
image3 = image3.resize((220, 210))
photo3 = ImageTk.PhotoImage(image3)

image4 = Image.open("E:/Universidad/Compi/icons/buscar1.png")
image4 = image4.resize((220, 220))
photo4 = ImageTk.PhotoImage(image4)

image5 = Image.open("E:/Universidad/Compi/icons/reporte1.png")
image5 = image5.resize((220, 220))
photo5 = ImageTk.PhotoImage(image5)

# Crear una etiqueta para mostrar la imagen
image_label1 = tk.Label(app, image=photo1,bg="white")
image_label1.place(x=60,y=290)

image_label2 = tk.Label(app, image=photo2,bg="white")
image_label2.place(x=375,y=290)

image_label3 = tk.Label(app, image=photo3,bg="white")
image_label3.place(x=660,y=290)

image_label4 = tk.Label(app, image=photo4,bg="white")
image_label4.place(x=955,y=290)

image_label5 = tk.Label(app, image=photo5,bg="white")
image_label5.place(x=1265,y=290)
#MINIDESCRIPCION
#TEXTO1
texto1_p1 = tk.Label(text="Permite crear nuevos",font=("arial",14),bg="white",fg="purple")
texto1_p1.place(x=75,y=520)
texto1_p2 = tk.Label(text="registros de estudiantes.",font=("arial",14),bg="white",fg="purple")
texto1_p2.place(x=65,y=550)
#TEXTO2
texto2_p1 = tk.Label(text="Permite editar información",font=("arial",14),bg="white",fg="purple")
texto2_p1.place(x=360,y=520)
texto2_p2 = tk.Label(text="del registro de estudiantes.",font=("arial",14),bg="white",fg="purple")
texto2_p2.place(x=360,y=550)
#TEXTO3
texto3_p1 = tk.Label(text="Permite eliminar información",font=("arial",14),bg="white",fg="purple")
texto3_p1.place(x=650,y=520)
texto3_p2 = tk.Label(text="del registro de estudiantes.",font=("arial",14),bg="white",fg="purple")
texto3_p2.place(x=655,y=550)
#TEXTO4 - BUSQUEDA
texto4_p1 = tk.Label(text="Permite buscar estudiantes",font=("arial",14),bg="white",fg="purple")
texto4_p1.place(x=950,y=520)
texto4_p2 = tk.Label(text="del registro.",font=("arial",14),bg="white",fg="purple")
texto4_p2.place(x=1010,y=550)
#TEXTO5
texto4_p1 = tk.Label(text="Permite generar un",font=("arial",14),bg="white",fg="purple")
texto4_p1.place(x=1290,y=520)
texto4_p2 = tk.Label(text="reporte de estudiantes.",font=("arial",14),bg="white",fg="purple")
texto4_p2.place(x=1270,y=550)

def abrir_archivo_buscar():
    archivo = "hacer.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    #app.destroy()  # Cierra la ventana actual
    subprocess.call(["python", archivo])

#botones
button1 = customtkinter.CTkButton(app, text="Agregar",font=("arial",18,"bold"), command=abrir_archivo_buscar)
button1.place(x=100,y=610)
button1 = customtkinter.CTkButton(app, text="Editar",font=("arial",18,"bold"), command=abrir_archivo_buscar)
button1.place(x=410,y=610)
button1 = customtkinter.CTkButton(app, text="Eliminar",font=("arial",18,"bold"), command=abrir_archivo_buscar)
button1.place(x=705,y=610)
button1 = customtkinter.CTkButton(app, text="Buscar",font=("arial",18,"bold"), command=abrir_archivo_buscar)
button1.place(x=995,y=610)
button1 = customtkinter.CTkButton(app, text="Generar",font=("arial",18,"bold"), command=abrir_archivo_buscar)
button1.place(x=1295,y=610)
def cerrar():
    app.destroy()

button_cerrar= customtkinter.CTkButton(app,text="Cerrar",font=("arial",18),command=cerrar)
button_cerrar.place(x=700,y=750)


app.mainloop()