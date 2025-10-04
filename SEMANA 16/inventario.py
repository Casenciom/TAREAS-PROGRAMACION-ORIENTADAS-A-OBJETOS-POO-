import json
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar()

    def agregar(self, producto: Producto):
        self.productos[producto.get_id()] = producto
        self.guardar()

    def eliminar(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()

    def modificar(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            p = self.productos[id_producto]
            if nombre: p.set_nombre(nombre)
            if cantidad is not None: p.set_cantidad(cantidad)
            if precio is not None: p.set_precio(precio)
            self.guardar()

    def listar(self):
        return list(self.productos.values())

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump({k: vars(v) for k, v in self.productos.items()}, f, indent=4)

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = {k: Producto(**v) for k, v in data.items()}
        except FileNotFoundError:
            self.productos = {}
