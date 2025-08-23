# Tarea semana 10 - Sistema de Gestión de Inventarios Mejorado con Archivos CSV

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_file_format(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_file_format(linea):
        try:
            id_producto, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            return None


class Inventario:
    def __init__(self, archivo="inventario.cvs"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(p.to_file_format())
        except PermissionError:
            print(" Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    producto = Producto.from_file_format(linea)
                    if producto:
                        self.productos.append(producto)
        except FileNotFoundError:
            print(" Aviso: El archivo no existe, se creará uno nuevo al guardar.")
        except PermissionError:
            print(" Error: No se tienen permisos para leer el archivo.")

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(" Producto agregado y guardado en el archivo con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print(" Producto eliminado y archivo actualizado con éxito.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print(" Producto actualizado y archivo sincronizado con éxito.")
                return
        print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print(" Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Inventario completo:")
            for p in self.productos:
                print(p)


def menu():
    inventario = Inventario()

    while True:
        print("\n***** SISTEMA DE GESTIÓN DE INVENTARIOS - MI TIENDITA MÁS AHORRO *****")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print(" Error: cantidad y precio deben ser numéricos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            try:
                nueva_cantidad = input("Ingrese nueva cantidad (deje vacío para no cambiar): ")
                nuevo_precio = input("Ingrese nuevo precio (deje vacío para no cambiar): ")
                inventario.actualizar_producto(
                    id_producto,
                    nueva_cantidad=int(nueva_cantidad) if nueva_cantidad else None,
                    nuevo_precio=float(nuevo_precio) if nuevo_precio else None
                )
            except ValueError:
                print(" Error: cantidad y precio deben ser numéricos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo del sistema... Adiós")
            break
        else:
            print(" Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
