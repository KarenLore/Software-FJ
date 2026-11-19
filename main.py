
from entidades.cliente import Cliente
from servicios.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)
from reservas.reserva import Reserva


def mostrar_menu():
    print("\n" + "=" * 45)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 45)
    print("1. Registrar cliente")
    print("2. Mostrar servicios")
    print("3. Crear y procesar reserva de ejemplo")
    print("4. Salir")


def ejecutar_sistema():
    cliente = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del cliente: ")
                documento = input("Documento: ")
                correo = input("Correo electrónico: ")
                telefono = input("Teléfono: ")

                cliente = Cliente(
                    "CLI-001",
                    nombre,
                    documento,
                    correo,
                    telefono
                )

                print("\nCliente registrado correctamente.")
                print(cliente)

            elif opcion == "2":
                servicios = [
                    ReservaSala(
                        "SER-001", "Reserva de sala",
                        "Sala de reuniones", 50000, 10, 2
                    ),
                    AlquilerEquipo(
                        "SER-002", "Alquiler de equipos",
                        "Equipos tecnológicos", 30000, 2, 3
                    ),
                    Asesoria(
                        "SER-003", "Asesoría tecnológica",
                        "Asesoría especializada", 80000,
                        "Tecnología", 2
                    )
                ]

                print("\nSERVICIOS DISPONIBLES")
                for servicio in servicios:
                    print(
                        f"{servicio.nombre} - "
                        f"Costo: ${servicio.calcular_costo():,.2f}"
                    )

            elif opcion == "3":
                if cliente is None:
                    print("Primero debe registrar un cliente.")
                    continue

                servicio = ReservaSala(
                    "SER-001", "Reserva de sala",
                    "Sala de reuniones", 50000, 10, 2
                )

                reserva = Reserva("RES-001", cliente, servicio)
                reserva.confirmar()
                total = reserva.procesar()

                print("\nReserva procesada correctamente.")
                print(reserva)
                print(f"Total a pagar: ${total:,.2f}")

            elif opcion == "4":
                print("Gracias por utilizar Software FJ.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as error:
            print(f"Error de validación: {error}")

        except Exception as error:
            print(f"Se presentó un error: {error}")


if __name__ == "__main__":
    ejecutar_sistema()
