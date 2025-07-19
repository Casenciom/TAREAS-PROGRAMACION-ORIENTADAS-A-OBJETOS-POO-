# sistema_reservas_hotel.

# Clase que representa a una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero            # Número de habitación
        self.tipo = tipo                # Tipo de habitación (Ej: sencilla, doble, suite)
        self.precio = precio            # Precio por noche
        self.disponible = True          # Estado de disponibilidad

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Marca la habitación como disponible nuevamente."""
        self.disponible = True
        print(f"Habitación {self.numero} ha sido liberada.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio} - {estado}"


# Clase que representa una reserva de habitación
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        """Calcula el costo total de la reserva."""
        return self.habitacion.precio * self.dias

    def mostrar_detalle(self):
        """Imprime un resumen de la reserva."""
        print(f"Reserva para {self.cliente}")
        print(self.habitacion)
        print(f"Días: {self.dias}")
        print(f"Total a pagar: ${self.calcular_total()}")


# Clase que gestiona las operaciones del hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print(f"Habitaciones disponibles en {self.nombre}:")
        for hab in self.habitaciones:
            if hab.disponible:
                print(hab)

    def buscar_habitacion_disponible(self, tipo):
        """Busca la primera habitación disponible de un tipo específico."""
        for hab in self.habitaciones:
            if hab.tipo == tipo and hab.disponible:
                return hab
        return None


# === Programa principal ===

# Crear un hotel y habitaciones
hotel = Hotel("==Hotel Hilton Colon==")

hotel.agregar_habitacion(Habitacion(101, "sencilla", 40))
hotel.agregar_habitacion(Habitacion(102, "doble", 60))
hotel.agregar_habitacion(Habitacion(103, "suite", 120))

# Mostrar habitaciones disponibles
hotel.mostrar_habitaciones_disponibles()

# Cliente desea reservar una habitación doble
habitacion_reservada = hotel.buscar_habitacion_disponible("doble")

if habitacion_reservada:
    habitacion_reservada.reservar()
    reserva = Reserva("Carlos Asencio y esposa", habitacion_reservada, 5)
    reserva.mostrar_detalle()
else:
    print("No hay habitaciones del tipo solicitado disponibles.")

# Liberar habitación después de su uso
habitacion_reservada.liberar()

# Verificar disponibilidad nuevamente
hotel.mostrar_habitaciones_disponibles()
