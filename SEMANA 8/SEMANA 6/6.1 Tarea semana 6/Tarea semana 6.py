# Ejercicio semana 6 de POO
# Clase base: Empleados
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre          # Encapsulación: atributo privado
        self.__salario = salario        # Encapsulación: atributo privado

    # Metodo para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Metodo para obtener el salario
    def get_salario(self):
        return self.__salario

    # Metodo pata obtener la información
    def mostrar_info(self):
        print(f"Empleado: {self.__nombre}, Salario: ${self.__salario}")

    # METODO POLIMORFICO
    def calcular_bono(self):
        return self.__salario * 0.10


# Clase derivada: Gerente (hereda de Empleado)
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Sobrescribimos el metodo mostrar info
    def mostrar_info(self):
        print(f"Gerente: {self.get_nombre()}, Departamento: {self.departamento}, Salario: ${self.get_salario()}")

    # Polimorfismo: sobrescribimos el metodo calcular bono
    def calcular_bono(self):
        return self.get_salario() * 0.20


# Clase derivada: Desarrollador (hereda de Empleado)
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        print(f"Desarrollador: {self.get_nombre()}, Lenguaje: {self.lenguaje}, Salario: ${self.get_salario()}")

    def calcular_bono(self):
        return self.get_salario() * 0.15


# Programa principal
if __name__ == "__main__":
    # Instanciamos objetos
    empleado1 = Empleado("José Hernadez", 1200)
    gerente1 = Gerente("María Veliz", 2000, "Ventas")
    desarrollador1 = Desarrollador("Carlos Asencio", 1500, "Python")

    # Mostramos la información y bonificaciones
    empleados = [empleado1, gerente1, desarrollador1]

    print("INFORMACIÓN DE EMPLEADOS Y BONIFICACIÓN:\n")
    for emp in empleados:
        emp.mostrar_info()
        print(f"Bono: ${emp.calcular_bono():.2f}\n")
