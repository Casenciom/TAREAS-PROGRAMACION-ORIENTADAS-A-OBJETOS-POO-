# Función para ingresar las temperaturas diarias en la programacion orientada a objetos

class ClimaSemanal:
    def __init__(self):
        self._temperaturas = []

    # Encapsulamiento
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        if not self._temperaturas:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"El promedio de temperatura semanal es: {promedio:.2f} °C")

# Herencia
class ClimaExtendido(ClimaSemanal):
    def max_temperatura(self):
        return max(self._temperaturas) if self._temperaturas else None

# Programa principal
def main():
    print("== Programa con Programación Orientada a Objetos ==")
    clima = ClimaExtendido()
    clima.ingresar_temperaturas()
    clima.mostrar_resultado()
    print(f"Temperatura máxima de la semana: {clima.max_temperatura()} °C")

main()
