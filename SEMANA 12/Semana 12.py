# Tarea semana 12: Sistema de Gestión de Biblioteca Digital

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()


    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está registrado.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")


    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("El libro no existe en la biblioteca.")


    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")


    def baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario eliminado: {eliminado}")
        else:
            print("El usuario no existe.")


    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")


    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                return
        print("Ese libro no está prestado a este usuario.")


    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor.lower() in libro.info[0].lower()) or \
               (criterio == "autor" and valor.lower() in libro.info[1].lower()) or \
               (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(str(libro))
        return resultados if resultados else ["No se encontraron resultados."]


    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"- {libro}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")

if __name__ == "__main__":
    # Crear biblioteca
    biblio = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "123")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "456")
    libro3 = Libro("la vaca lola","Costeñita","Infantil","598")

    # Agregar libros
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    # Registrar usuario
    user1 = Usuario("Carlos", "U001")
    biblio.registrar_usuario(user1)

    user2 = Usuario("Lilibeth", "U002")
    biblio.registrar_usuario(user2)

    user3 = Usuario("Andrea","U003")
    biblio.registrar_usuario(user3)

    # Prestar libro
    biblio.prestar_libro("U001", "123")
    biblio.prestar_libro("U003","598")

    # Listar libros prestados
    biblio.listar_libros_prestados("U001")
    biblio.listar_libros_prestados("U003")

    # Buscar libros por categoría
    print(biblio.buscar_libro("categoria", "fábula"))

    # Devolver libro
    biblio.devolver_libro("U001", "123")
    biblio.devolver_libro("U003","598")
