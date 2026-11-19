"""
Archivo principal del Sistema Integral de Gestión de Clientes,
Servicios y Reservas de la empresa Software FJ.

Este módulo permite interactuar con el sistema mediante un menú
en consola, desde el cual se pueden registrar clientes, consultar
servicios disponibles y crear y procesar reservas.

Integra las clases desarrolladas en los módulos de entidades,
servicios y reservas.
"""

# Importa la clase Cliente para registrar y administrar
# la información de los clientes del sistema.
from entidades.cliente import Cliente

# Importa los diferentes tipos de servicios especializados
# disponibles en la aplicación.
from servicios.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

# Importa la clase Reserva para crear, confirmar
# y procesar las reservas realizadas por los clientes.
from reservas.reserva import Reserva


def mostrar_menu():
    """
    Presenta en pantalla el menú principal del sistema.

    Muestra las opciones disponibles para que el usuario
    pueda seleccionar la operación que desea realizar.
    """

    # Imprime el encabezado principal del sistema.
    print("\n" + "=" * 45)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 45)

    # Muestra las opciones de funcionamiento.
    print("1. Registrar cliente")
    print("2. Mostrar servicios")
    print("3. Crear y procesar reserva de ejemplo")
    print("4. Salir")


def ejecutar_sistema():
    """
    Controla el funcionamiento general del programa.

    Mantiene activo el menú principal mediante un ciclo while,
    recibe las opciones ingresadas por el usuario y ejecuta
    las operaciones correspondientes.

    También utiliza bloques try/except para controlar errores
    de validación y otras excepciones durante la ejecución.
    """

    # Inicializa la variable cliente sin información.
    # Se asignará un objeto Cliente cuando el usuario
    # realice correctamente el registro.
    cliente = None

    # Mantiene el menú activo hasta que el usuario seleccione salir.
    while True:

        # Presenta las opciones disponibles.
        mostrar_menu()

        # Solicita al usuario la opción que desea ejecutar.
        opcion = input("Seleccione una opción: ")

        # Inicia el bloque de control de excepciones.
        # Permite manejar errores sin finalizar inesperadamente
        # la ejecución del programa.
        try:

            # OPCIÓN 1: REGISTRAR CLIENTE
            if opcion == "1":

                # Solicita los datos personales del cliente.
                nombre = input("Nombre del cliente: ")
                documento = input("Documento: ")
                correo = input("Correo electrónico: ")
                telefono = input("Teléfono: ")

                # Crea un objeto Cliente utilizando los datos ingresados.
                # La clase Cliente realiza las validaciones correspondientes.
                cliente = Cliente(
                    "CLI-001",
                    nombre,
                    documento,
                    correo,
                    telefono
                )

                # Informa que el registro se realizó correctamente.
                print("\nCliente registrado correctamente.")

                # Muestra la información del cliente registrado.
                print(cliente)

            # OPCIÓN 2: MOSTRAR SERVICIOS
            elif opcion == "2":

                # Crea una lista con los tres tipos de servicios
                # especializados que ofrece la empresa Software FJ.
                servicios = [

                    # Servicio de reserva de salas.
                    ReservaSala(
                        "SER-001", "Reserva de sala",
                        "Sala de reuniones", 50000, 10, 2
                    ),

                    # Servicio de alquiler de equipos tecnológicos.
                    AlquilerEquipo(
                        "SER-002", "Alquiler de equipos",
                        "Equipos tecnológicos", 30000, 2, 3
                    ),

                    # Servicio de asesoría tecnológica.
                    Asesoria(
                        "SER-003", "Asesoría tecnológica",
                        "Asesoría especializada", 80000,
                        "Tecnología", 2
                    )
                ]

                # Presenta el encabezado de los servicios disponibles.
                print("\nSERVICIOS DISPONIBLES")

                # Recorre la lista y muestra el nombre y costo
                # calculado de cada servicio.
                for servicio in servicios:
                    print(
                        f"{servicio.nombre} - "
                        f"Costo: ${servicio.calcular_costo():,.2f}"
                    )

            # OPCIÓN 3: CREAR Y PROCESAR UNA RESERVA
            elif opcion == "3":

                # Verifica que exista un cliente registrado.
                # Si no existe, informa al usuario y vuelve al menú.
                if cliente is None:
                    print("Primero debe registrar un cliente.")
                    continue

                # Crea un servicio de reserva de sala
                # que será utilizado para el ejemplo.
                servicio = ReservaSala(
                    "SER-001", "Reserva de sala",
                    "Sala de reuniones", 50000, 10, 2
                )

                # Crea una reserva asociando el cliente registrado
                # con el servicio seleccionado.
                reserva = Reserva("RES-001", cliente, servicio)

                # Cambia el estado de la reserva a Confirmada.
                reserva.confirmar()

                # Procesa la reserva y obtiene el valor total a pagar.
                total = reserva.procesar()

                # Informa que el procesamiento fue exitoso.
                print("\nReserva procesada correctamente.")

                # Muestra los datos de la reserva.
                print(reserva)

                # Presenta el valor total calculado.
                print(f"Total a pagar: ${total:,.2f}")

            # OPCIÓN 4: SALIR DEL SISTEMA
            elif opcion == "4":

                # Muestra el mensaje de despedida.
                print("Gracias por utilizar Software FJ.")

                # Finaliza el ciclo y termina el menú.
                break

            # CONTROL DE OPCIONES NO VÁLIDAS
            else:

                # Informa cuando el usuario ingresa
                # una opción que no está disponible.
                print("Opción no válida. Intente nuevamente.")

        # Captura errores relacionados con valores y validaciones.
        except ValueError as error:
            print(f"Error de validación: {error}")

        # Captura otras excepciones que puedan presentarse
        # durante la ejecución de las operaciones.
        except Exception as error:
            print(f"Se presentó un error: {error}")


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

# Comprueba si este archivo se está ejecutando directamente.
# Si es así, inicia el sistema llamando a ejecutar_sistema().
# Esto permite importar sus funciones desde otros módulos
# sin iniciar automáticamente el menú.
if __name__ == "__main__":
    ejecutar_sistema()