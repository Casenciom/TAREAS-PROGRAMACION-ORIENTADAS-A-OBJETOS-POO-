# EJEMPLO #2


# Abstracción
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.__nombre = nombre  # Encapsulación
        self.__id_empleado = id_empleado  # Encapsulación
        self.__salario_base = 470  # Encapsulación

    # Encapsulación
    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id_empleado

    def get_salario_base(self):
        return self.__salario_base

    # Método de abstraccion
    def calcular_salario(self):
        raise NotImplementedError("Método abstracto")

    # Método concreto
    def mostrar_informacion(self):
        print(f"ID: {self.__id_empleado}")
        print(f"Nombre: {self.__nombre}")
        print(f"Salario: ${self.calcular_salario():.2f}")


# Herencia - EmpleadoTiempoCompleto hereda de Empleado

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, bono):
        super().__init__(nombre, id_empleado)
        self.__bono = bono  # Encapsulación

    # Implementación de método abstracto
    def calcular_salario(self):
        return self.get_salario_base() * 1.5 + self.__bono


# Herencia
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, id_empleado, horas_trabajadas):
        super().__init__(nombre, id_empleado)
        self.__horas_trabajadas = horas_trabajadas  # Encapsulación

    # Implementación de método abstracto
    def calcular_salario(self):
        return self.get_salario_base() * 0.8 * self.__horas_trabajadas


# Polimorfismo
def procesar_nomina(empleados):
    total_nomina = 0
    for empleado in empleados:
        empleado.mostrar_informacion()  # Llamada polimórfica
        total_nomina += empleado.calcular_salario()
    print(f"\nTotal nómina: ${total_nomina:.2f}")


# Uso del sistema
empleados = [
    EmpleadoTiempoCompleto("Ana Pérez", "0001", 500),
    EmpleadoPorHoras("Carlos Ruiz", "0002", 40),
    EmpleadoTiempoCompleto("Luisa Gómez", "0003", 300)
]

# Polimorfismo - misma función para diferentes tipos de empleado
procesar_nomina(empleados)
