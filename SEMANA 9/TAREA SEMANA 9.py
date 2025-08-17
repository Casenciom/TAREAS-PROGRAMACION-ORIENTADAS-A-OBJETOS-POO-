# Tarea semana 9
# Clase Producto Sistema de Gestión de Inventarios
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):

        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # ***** Métodos Getters (obtener valores de los atributos) *****

    def get_id(self):
        return self.id_producto
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio
    # ***** Métodos Setters (modificar valores de los atributos) *****
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio
    # Representación del producto en forma de texto
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

# Clase Inventario

class Inventario:
    def __init__(self):

        self.productos = []
# Añade un nuevo producto al inventario validando que el ID no se repita.
    def agregar_producto(self, producto):

        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        print(" Producto agregado con éxito.")
# Elimina un producto del inventario según su ID.
    def eliminar_producto(self, id_producto):

        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(" Producto eliminado con éxito.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):

        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(" Producto actualizado con éxito.")
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
# Menú Interactivo en Consola

def menu():
    # Se crea una instancia de Inventario para gestionar los productos

    inventario = Inventario()

    while True:
        # Mostrar menú de opciones

        print("\n***** SISTEMA DE GESTIÓN DE INVENTARIOS MI TIENDITA MAS AHORRO *****")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        # ***** Opción 1: Agregar un nuevo producto *****

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

        # ***** Opción 2: Eliminar un producto por ID *****

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # ***** Opción 3: Actualizar cantidad y/o precio de un producto *****

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

        # ***** Opción 4: Buscar producto por nombre parcial *****

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        # ***** Opción 5: Mostrar todos los productos en inventario *****
        elif opcion == "5":
            inventario.mostrar_todos()

        # ***** Opción 6: Salir del programa *****
        elif opcion == "6":
            print(" Saliendo del sistema... Adios")
            break

        # ***** Manejo de opción inválida *****
        else:
            print(" Opción no válida, intente de nuevo.")


# Punto de entrada del programa

if __name__ == "__main__":
    # Ejecutar el menú principal
    menu()
