class Jugador:
    #"""Clase que representa a un jugador en un juego. Se usa el constructor para inicializar al jugador,
   # y el destructor para mostrar un mensaje al final del juego."""

    def __init__(self, nombre):
        # Constructor: se ejecuta al crear un nuevo jugador
        self.nombre = nombre
        self.vida = 100
        self.puntaje = 0
        print(f"Jugador '{self.nombre}' ha ingresado al juego con {self.vida} puntos de vida.")

    def recibir_danio(self, cantidad):
        # Resta vida al jugador
        self.vida -= cantidad
        print(f"{self.nombre} recibió {cantidad} puntos de daño. Vida actual: {self.vida}")
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado.")

    def ganar_puntos(self, puntos):
        # Aumenta el puntaje del jugador
        self.puntaje += puntos
        print(f"{self.nombre} ganó {puntos} puntos. Puntaje total: {self.puntaje}")

    def __del__(self):
        # Destructor: se ejecuta al eliminar el objeto jugador
        print(f"Juego terminado para '{self.nombre}'. Puntaje final: {self.puntaje}")


# Programa principal
def main():
    print(" Iniciando el juego...")
    print(" Ready...?")
    jugador1 = Jugador("Carlos Asencio")
    jugador1.ganar_puntos(60)
    jugador1.recibir_danio(30)
    jugador1.recibir_danio(70)
    print("🏁 Fin del juego.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
