# Tarea: Registro básico de datos personales
# Este programa  nos permitira ingresar y mostrar datos personales de un usuario:
# colocando nombre, edad, estatura, y si tiene licencia de conducir.

def registrar_usuario():
    """
    Solicita al usuario sus datos personales y los muestra en pantalla.
    """
    # Solicitamos el nombre tipo de dato: string
    nombre = input("Ingrese su nombre completo: ")

    # Solicitamos la edad tipo de dato: int
    edad = int(input("Ingrese su edad: "))

    # Solicitamos la estatura tipo de dato: float
    estatura = float(input("Ingrese su estatura en metros (ej. 1.75): "))

    # Preguntamos si tiene licencia de conducir: boolean
    tiene_licencia = input("¿Tiene licencia de conducir? (sí/no): ").lower() == "sí"

    # Muestra los datos ingresados
    print("\n--- Datos Registrados ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Estatura: {estatura} m")
    print(f"Tiene licencia de conducir: {tiene_licencia}")

# Llamada a la función principal
registrar_usuario()