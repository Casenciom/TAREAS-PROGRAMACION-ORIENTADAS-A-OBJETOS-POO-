#TAREA SEMANA 13 Creación de una Aplicación GUI Básica

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def agregar_datos():
    nombre = entrada_nombre.get().strip()
    apellido = entrada_apellido.get().strip()
    edad = entrada_edad.get().strip()

    if nombre and apellido and edad.isdigit():
        tabla_datos.insert('', tk.END, values=(nombre, apellido, edad))

        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Datos inválidos", "Por favor ingrese datos válidos (edad numérica).")

def limpiar_tabla():
    for item in tabla_datos.get_children():
        tabla_datos.delete(item)

ventana = tk.Tk()
ventana.title("Sistema de Registro")
ventana.geometry("600x600")
ventana.configure(bg="white")  # si quieres color de fondo, usa bg

style = ttk.Style()
style.configure("Treeview", anchor="center", rowheight=25)
style.configure("Treeview.Heading", anchor="center")

label_nombre = tk.Label(ventana, text="Ingrese su nombre")
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

label_apellido = tk.Label(ventana, text="Ingrese su apellido")
label_apellido.pack(pady=5)
entrada_apellido = tk.Entry(ventana, width=30)
entrada_apellido.pack()

label_edad = tk.Label(ventana, text="Ingrese su edad")
label_edad.pack(pady=5)
entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack()

boton_agregar = tk.Button(ventana, text="Agregar", bg="yellow", command=agregar_datos)
boton_agregar.pack(pady=10)

tabla_datos = ttk.Treeview(
    ventana,
    columns=("Nombre", "Apellido", "Edad"),
    show="headings",
    height=8
)
tabla_datos.heading("Nombre", text="Nombre")
tabla_datos.heading("Apellido", text="Apellido")
tabla_datos.heading("Edad", text="Edad")

tabla_datos.column("Nombre", anchor="center", width=180)
tabla_datos.column("Apellido", anchor="center", width=180)
tabla_datos.column("Edad", anchor="center", width=80)

tabla_datos.pack(padx=10, pady=10, fill='x')

boton_limpiar = tk.Button(ventana, text="Limpiar", bg="lightblue", command=limpiar_tabla)
boton_limpiar.pack(pady=5)

ventana.mainloop()
