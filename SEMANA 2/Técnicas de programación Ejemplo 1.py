# EJEMPLO #1

from abc import ABC, abstractmethod

# Abstracción
class Animal(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación

    def get_nombre(self):
        return self.__nombre

    @abstractmethod
    def hacer_sonido(self):  # Método abstracto
        pass

# Herencia y Polimorfismo
class Leon(Animal):
    def hacer_sonido(self):  # Polimorfismo
        return f"{self.get_nombre()} ruge"

class Loro(Animal):
    def hacer_sonido(self):  # Polimorfismo
        return f"{self.get_nombre()} dice: ¡Hola!"

# Uso de las clases
animales = [Leon("Simba"), Loro("Kiki")]

for animal in animales:
    print(animal.hacer_sonido())