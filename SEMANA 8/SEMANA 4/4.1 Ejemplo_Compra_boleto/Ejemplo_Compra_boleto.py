# Reserva_boletos_avion

# Clase que representa un vuelo
class Vuelo:
    def __init__(self, codigo, origen, destino, capacidad, precio):
        self.codigo = codigo            # Código del vuelo
        self.origen = origen            # Ciudad de salida
        self.destino = destino          # Ciudad de llegada
        self.capacidad = capacidad      # Asientos disponibles
        self.precio = precio            # Precio por boleto
        self.asientos_ocupados = 0

    def reservar_asiento(self):
        """Intenta reservar un asiento si hay disponibilidad."""
        if self.asientos_ocupados < self.capacidad:
            self.asientos_ocupados += 1
            return True
        else:
            print("No hay asientos disponibles en este vuelo.")
            return False

    def mostrar_info(self):
        """Muestra los detalles del vuelo."""
        print(f"Vuelo {self.codigo}: {self.origen} → {self.destino}")
        print(f"Precio: ${self.precio} - Asientos disponibles: {self.capacidad - self.asientos_ocupados}")

    def __str__(self):
        return f"{self.codigo} - {self.origen} a {self.destino} - ${self.precio}"


# Clase que representa un pasajero
class Pasajero:
    def __init__(self, nombre, pasaporte):
        self.nombre = nombre
        self.pasaporte = pasaporte

    def __str__(self):
        return f"{self.nombre} (Pasaporte: {self.pasaporte})"


# Clase que representa una reserva
class Reserva:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo

    def mostrar_resumen(self):
        """Muestra un resumen de la reserva."""
        print("\n=== RESUMEN DE RESERVA ===")
        print(f"Pasajero: {self.pasajero}")
        print(f"Vuelo: {self.vuelo}")
        print(f"Total pagado: ${self.vuelo.precio}")
        print("===========================")


# Clase que representa el sistema de la aerolínea
class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def mostrar_vuelos(self):
        print(f"\nVuelos disponibles - {self.nombre}")
        for vuelo in self.vuelos:
            vuelo.mostrar_info()

    def buscar_vuelo_por_codigo(self, codigo):
        for vuelo in self.vuelos:
            if vuelo.codigo == codigo:
                return vuelo
        return None


# === Programa principal ===

# Crear la aerolínea y vuelos
aerolinea = Aerolinea("AeroAmazonas")
aerolinea.agregar_vuelo(Vuelo("TAME", "Quito", "Guayaquil", 3, 120))
aerolinea.agregar_vuelo(Vuelo("AVIANCA", "Cuenca", "Quito", 2, 95))
aerolinea.agregar_vuelo(Vuelo("LATAM", "Tena", "Quito", 1, 110))

# Mostrar los vuelos disponibles
aerolinea.mostrar_vuelos()

# Crear pasajero
pasajero = Pasajero("Carlos Asencio", "0930495098")


# Simular reserva de vuelo
codigo_elegido = "AVIANCA"
vuelo_elegido = aerolinea.buscar_vuelo_por_codigo(codigo_elegido)

if vuelo_elegido and vuelo_elegido.reservar_asiento():
    reserva = Reserva(pasajero, vuelo_elegido)
    reserva.mostrar_resumen()
else:
    print("No se pudo completar la reserva.")

# Mostrar vuelos actualizados
aerolinea.mostrar_vuelos()
