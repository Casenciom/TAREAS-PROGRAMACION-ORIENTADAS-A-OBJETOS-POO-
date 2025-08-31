# Tarea semana 11 Sistema Avanzado de Gestión de Inventario

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Tuple, Optional
import json
import os

@dataclass
class Producto:
    id: int
    nombre: str
    cantidad: int
    precio: float

    def get_id(self) -> int:
        return self.id

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nuevo_nombre.strip()

    def get_cantidad(self) -> int:
        return self.cantidad

    def set_cantidad(self, nueva_cantidad: int) -> None:
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def get_precio(self) -> float:
        return self.precio

    def set_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = float(nuevo_precio)

    # Utilidad para serialización
    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> "Producto":
        return Producto(
            id=int(data["id"]),
            nombre=str(data["nombre"]),
            cantidad=int(data["cantidad"]),
            precio=float(data["precio"]),
        )

class Inventario:

    def __init__(self) -> None:
        self._productos: Dict[int, Producto] = {}
        self._indice_nombre: Dict[str, Set[int]] = {}


    def anadir_producto(self, producto: Producto) -> None:
        if producto.id in self._productos:
            raise KeyError(f"Ya existe un producto con ID {producto.id}.")
        self._productos[producto.id] = producto
        self._indexar_producto(producto)

    def eliminar_producto(self, id_producto: int) -> None:
        if id_producto not in self._productos:
            raise KeyError(f"No existe producto con ID {id_producto}.")
        prod = self._productos.pop(id_producto)
        self._desindexar_producto(prod)

    def actualizar_cantidad(self, id_producto: int, nueva_cantidad: int) -> None:
        prod = self._obtener_producto(id_producto)
        prod.set_cantidad(nueva_cantidad)

    def actualizar_precio(self, id_producto: int, nuevo_precio: float) -> None:
        prod = self._obtener_producto(id_producto)
        prod.set_precio(nuevo_precio)

    def actualizar_nombre(self, id_producto: int, nuevo_nombre: str) -> None:
        prod = self._obtener_producto(id_producto)
        self._desindexar_producto(prod)
        prod.set_nombre(nuevo_nombre)
        self._indexar_producto(prod)

    def buscar_por_nombre(self, termino: str) -> List[Producto]:

        clave = termino.strip().lower()
        ids: Set[int] = self._indice_nombre.get(clave, set())
        return [self._productos[i] for i in ids]

    def obtener_todos(self, orden: Optional[str] = None) -> List[Producto]:

        lista = list(self._productos.values())
        if orden == "id":
            lista.sort(key=lambda p: p.id)
        elif orden == "nombre":
            lista.sort(key=lambda p: p.nombre.lower())
        elif orden == "cantidad":
            lista.sort(key=lambda p: p.cantidad)
        elif orden == "precio":
            lista.sort(key=lambda p: p.precio)
        return lista

    def resumen_inventario(self) -> Tuple[int, float]:

        total_items = len(self._productos)
        valor_total = sum(p.cantidad * p.precio for p in self._productos.values())
        return (total_items, valor_total)

    def guardar_en_archivo(self, ruta: str) -> None:
        data = {
            "productos": [p.to_dict() for p in self._productos.values()]
        }
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            raise OSError(f"Error al guardar el archivo '{ruta}': {e}")

    def cargar_desde_archivo(self, ruta: str) -> None:
        if not os.path.exists(ruta):
            return
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"El archivo '{ruta}' no contiene JSON válido: {e}")
        except OSError as e:
            raise OSError(f"Error al leer el archivo '{ruta}': {e}")

        self._productos.clear()
        self._indice_nombre.clear()
        for d in data.get("productos", []):
            p = Producto.from_dict(d)
            self._productos[p.id] = p
            self._indexar_producto(p)

    def _obtener_producto(self, id_producto: int) -> Producto:
        if id_producto not in self._productos:
            raise KeyError(f"No existe producto con ID {id_producto}.")
        return self._productos[id_producto]

    def _indexar_producto(self, prod: Producto) -> None:
        clave = prod.nombre.strip().lower()
        if clave not in self._indice_nombre:
            self._indice_nombre[clave] = set()
        self._indice_nombre[clave].add(prod.id)

    def _desindexar_producto(self, prod: Producto) -> None:
        clave = prod.nombre.strip().lower()
        ids = self._indice_nombre.get(clave)
        if ids:
            ids.discard(prod.id)
            if not ids:
                self._indice_nombre.pop(clave, None)

ARCHIVO_DATOS = "inventario.json"


def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Debe ingresar un número entero.")


def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Debe ingresar un número (use punto decimal si aplica).")


def mostrar_producto(p: Producto) -> None:
    print(f"ID: {p.id} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: {p.precio:.2f}")


def menu() -> None:
    inv = Inventario()
    try:
        inv.cargar_desde_archivo(ARCHIVO_DATOS)
    except Exception as e:
        print(f" No se pudo cargar el inventario: {e}")

    while True:
        print("\n===== MENÚ INVENTARIO MI TIENDITA =====")
        print("1. Añadir producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Actualizar nombre")
        print("6. Buscar producto por nombre")
        print("7. Mostrar todos los productos")
        print("8. Resumen del inventario")
        print("9. Guardar inventario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                idp = input_int("ID (entero): ")
                nombre = input("Nombre: ").strip()
                cantidad = input_int("Cantidad: ")
                precio = input_float("Precio: ")
                prod = Producto(id=idp, nombre=nombre, cantidad=cantidad, precio=precio)
                inv.anadir_producto(prod)
                print(" Producto añadido.")
            except Exception as e:
                print(f" Error: {e}")

        elif opcion == "2":
            try:
                idp = input_int("ID a eliminar: ")
                inv.eliminar_producto(idp)
                print(" Producto eliminado.")
            except Exception as e:
                print(f" Error: {e}")

        elif opcion == "3":
            try:
                idp = input_int("ID del producto: ")
                cant = input_int("Nueva cantidad: ")
                inv.actualizar_cantidad(idp, cant)
                print(" Cantidad actualizada.")
            except Exception as e:
                print(f" Error: {e}")

        elif opcion == "4":
            try:
                idp = input_int("ID del producto: ")
                precio = input_float("Nuevo precio: ")
                inv.actualizar_precio(idp, precio)
                print(" Precio actualizado.")
            except Exception as e:
                print(f" Error: {e}")

        elif opcion == "5":
            try:
                idp = input_int("ID del producto: ")
                nombre = input("Nuevo nombre: ")
                inv.actualizar_nombre(idp, nombre)
                print("Nombre actualizado.")
            except Exception as e:
                print(f" Error: {e}")

        elif opcion == "6":
            termino = input("Nombre a buscar (exacto): ").strip()
            resultados = inv.buscar_por_nombre(termino)
            if resultados:
                print(f"\n▶ Resultados para '{termino}':")
                for p in resultados:
                    mostrar_producto(p)
            else:
                print(" No se encontraron productos con ese nombre.")

        elif opcion == "7":
            orden = input("Ordenar por [id|nombre|cantidad|precio] (o Enter): ").strip().lower() or None
            todos = inv.obtener_todos(orden=orden)
            if not todos:
                print("(Inventario vacío)")
            for p in todos:
                mostrar_producto(p)

        elif opcion == "8":
            total_items, valor_total = inv.resumen_inventario()  # tuple
            print(f"Artículos distintos: {total_items} | Valor total: {valor_total:.2f}")

        elif opcion == "9":
            try:
                inv.guardar_en_archivo(ARCHIVO_DATOS)
                print(f" Inventario guardado en '{ARCHIVO_DATOS}'.")
            except Exception as e:
                print(f" Error al guardar: {e}")

        elif opcion == "0":
            # Guardado al salir (opcional). Se puede comentar si no se desea.
            try:
                inv.guardar_en_archivo(ARCHIVO_DATOS)
                print(f" Cambios guardados en '{ARCHIVO_DATOS}'.")
            except Exception as e:
                print(f"  No se pudo guardar automáticamente: {e}")
            print(" ¡Hasta pronto!...Adios")
            break

        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()