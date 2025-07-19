# Función para ingresar las temperaturas diarias en la programacion tradicional
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal en la programacion tradicional
def main():
    print("== Programa tradicional para promedio semanal del clima ==")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio de temperatura semanal es: {promedio:.2f} °C")

main()
