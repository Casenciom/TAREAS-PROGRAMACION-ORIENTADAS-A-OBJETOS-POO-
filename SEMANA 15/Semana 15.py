# Tarea: Conceptos fundamentales de manejo de eventos

import tkinter as tk
from tkinter import messagebox

class ListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas de Carlos Asencio")
        self.root.geometry("400x400")

        self.tareas = []

        self.entry_tarea = tk.Entry(root, width=30)
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea)  # Enter añade tarea

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.btn_agregar = tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(btn_frame, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(btn_frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        self.listbox = tk.Listbox(root, width=45, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-1>", self.marcar_completada)  # Doble clic marca completada

    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def marcar_completada(self, event=None):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto += " Completado "
            self.listbox.insert(tk.END, texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
