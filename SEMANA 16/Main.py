import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Inventario - Mi Tienda Online")

        self.inventario = Inventario()


        info = tk.Label(root, text="Estudiante: Carlos Asencio Miranda\nCarrera: Ingeniería en TI\nParalelo: A", font=("Arial", 21))
        info.pack(pady=10)

        # Menú
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        menu_productos = tk.Menu(menubar, tearoff=0)
        menu_productos.add_command(label="Administrar Productos", command=self.abrir_productos)
        menu_productos.add_command(label="Salir", command=root.quit)
        menubar.add_cascade(label="Opciones", menu=menu_productos)


        root.bind("<Escape>", lambda e: root.quit())

    def abrir_productos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Productos")


        tk.Label(ventana, text="ID").grid(row=0, column=0)
        tk.Label(ventana, text="Nombre").grid(row=1, column=0)
        tk.Label(ventana, text="Cantidad").grid(row=2, column=0)
        tk.Label(ventana, text="Precio").grid(row=3, column=0)

        id_entry = tk.Entry(ventana)
        nombre_entry = tk.Entry(ventana)
        cantidad_entry = tk.Entry(ventana)
        precio_entry = tk.Entry(ventana)

        id_entry.grid(row=0, column=1)
        nombre_entry.grid(row=1, column=1)
        cantidad_entry.grid(row=2, column=1)
        precio_entry.grid(row=3, column=1)


        cols = ("ID", "Nombre", "Cantidad", "Precio")
        self.tree = ttk.Treeview(ventana, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.grid(row=6, column=0, columnspan=4, pady=10)

        self.refrescar_tabla()


        def seleccionar_producto(event):
            seleccionado = self.tree.selection()
            if seleccionado:
                valores = self.tree.item(seleccionado)["values"]
                id_entry.delete(0, tk.END)
                id_entry.insert(0, valores[0])
                nombre_entry.delete(0, tk.END)
                nombre_entry.insert(0, valores[1])
                cantidad_entry.delete(0, tk.END)
                cantidad_entry.insert(0, valores[2])
                precio_entry.delete(0, tk.END)
                precio_entry.insert(0, valores[3])

        self.tree.bind("<<TreeviewSelect>>", seleccionar_producto)


        def agregar():
            try:
                producto = Producto(
                    id_entry.get(),
                    nombre_entry.get(),
                    int(cantidad_entry.get()),
                    float(precio_entry.get())
                )
                self.inventario.agregar(producto)
                self.refrescar_tabla()
            except ValueError:
                messagebox.showerror("Error", "Datos inválidos")

        def eliminar():
            seleccionado = self.tree.selection()
            if seleccionado:
                id_producto = self.tree.item(seleccionado)["values"][0]
                self.inventario.eliminar(id_producto)
                self.refrescar_tabla()

        def modificar():
            seleccionado = self.tree.selection()
            if seleccionado:
                id_producto = self.tree.item(seleccionado)["values"][0]

                nombre = nombre_entry.get().strip()
                cantidad = cantidad_entry.get().strip()
                precio = precio_entry.get().strip()

                # Solo convertir a número si no están vacíos
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                self.inventario.modificar(
                    id_producto,
                    nombre if nombre else None,
                    cantidad,
                    precio
                )
                self.refrescar_tabla()

        def listar():
            self.refrescar_tabla()
            messagebox.showinfo("Listado", "Se han listado todos los productos.")

        # Botones
        tk.Button(ventana, text="Agregar", command=agregar).grid(row=4, column=0, pady=5)
        tk.Button(ventana, text="Modificar", command=modificar).grid(row=4, column=1, pady=5)
        tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=4, column=2, pady=5)
        tk.Button(ventana, text="Listar", command=listar).grid(row=4, column=3, pady=5)


        ventana.bind("<Delete>", lambda e: eliminar())

    def refrescar_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for p in self.inventario.listar():
            self.tree.insert("", "end", values=(p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio()))

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
