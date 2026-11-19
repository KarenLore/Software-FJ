"""
Archivo principal del Sistema Integral de Gestión de Clientes,
Servicios y Reservas de la empresa Software FJ.

Permite registrar clientes, consultar servicios disponibles
y crear y procesar reservas mediante un menú interactivo.
"""

# Importa os para limpiar la pantalla de la consola.
import os

# Importa la clase Cliente.
from entidades.cliente import Cliente

# Importa las funciones para validar los datos del cliente.
from entidades.validaciones import (
    validar_texto,
    validar_documento,
    validar_correo,
    validar_telefono
)

# Importa los servicios especializados disponibles.
from servicios.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

# Importa la clase Reserva para gestionar las reservas.
from reservas.reserva import Reserva


def limpiar_consola():
    """
    Limpia la pantalla de la consola según el sistema operativo.
    """

    os.system("cls" if os.name == "nt" else "clear")


def volver_al_menu():
    """
    Espera que el usuario presione 0 para regresar
    al menú principal.
    """

    while True:
        opcion = input(
            "\nPresione 0 para volver al menú principal: "
        )

        if opcion == "0":
            break

        print("Opción no válida. Debe presionar 0.")


def mostrar_menu():
    """
    Presenta las opciones principales del sistema.
    """

    print("\n" + "=" * 50)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 50)
    print("1. Registrar cliente")
    print("2. Mostrar servicios")
    print("3. Crear y procesar reserva de ejemplo")
    print("4. Salir")
    print("=" * 50)


def ejecutar_sistema():
    """
    Controla el funcionamiento general del programa.

    Permite registrar clientes, consultar servicios,
    procesar reservas y controlar posibles excepciones.
    """

    # Variable que almacena el cliente registrado.
    cliente = None

    # Mantiene activo el menú hasta que el usuario decida salir.
    while True:

        limpiar_consola()
        mostrar_menu()

        # Solicita la opción que desea ejecutar el usuario.
        opcion = input("\nSeleccione una opción: ")

        # =================================================
        # OPCIÓN 1: REGISTRAR CLIENTE
        # =================================================

        if opcion == "1":

            limpiar_consola()

            print("=" * 50)
            print("             REGISTRO DE CLIENTE")
            print("=" * 50)

            try:
                # Solicita y valida el nombre del cliente.
                nombre = input("Nombre del cliente: ")
                nombre = validar_texto(nombre, "nombre")

                # Solicita y valida el documento.
                documento = input("Documento: ")
                documento = validar_documento(documento)

                # Solicita y valida el correo electrónico.
                correo = input("Correo electrónico: ")
                correo = validar_correo(correo)

                # Solicita y valida el teléfono.
                telefono = input("Teléfono: ")
                telefono = validar_telefono(telefono)

                # Crea el cliente solamente cuando todos
                # los datos han superado las validaciones.
                cliente_nuevo = Cliente(
                    "CLI-001",
                    nombre,
                    documento,
                    correo,
                    telefono
                )

                # Guarda el cliente registrado correctamente.
                cliente = cliente_nuevo

                print("\n¡Cliente registrado correctamente!")
                print("-" * 50)
                print(cliente)
                print("-" * 50)

            except ValueError as error:

                # Muestra el primer error de validación encontrado.
                print("\n¡No fue posible registrar el cliente!")
                print(f"Motivo: {error}")

            except Exception as error:

                # Captura otros errores inesperados.
                print("\nSe presentó un error durante el registro.")
                print(f"Detalle: {error}")

            # Espera que el usuario decida regresar al menú.
            volver_al_menu()

        # =================================================
        # OPCIÓN 2: MOSTRAR SERVICIOS
        # =================================================

        elif opcion == "2":

            limpiar_consola()

            try:
                # Crea los tres servicios especializados.
                servicios = [
                    ReservaSala(
                        "SER-001",
                        "Reserva de sala",
                        "Sala de reuniones",
                        50000,
                        10,
                        2
                    ),

                    AlquilerEquipo(
                        "SER-002",
                        "Alquiler de equipos",
                        "Equipos tecnológicos",
                        30000,
                        2,
                        3
                    ),

                    Asesoria(
                        "SER-003",
                        "Asesoría tecnológica",
                        "Asesoría especializada",
                        80000,
                        "Tecnología",
                        2
                    )
                ]

                print("=" * 50)
                print("             SERVICIOS DISPONIBLES")
                print("=" * 50)

                # Recorre la lista y muestra la información
                # y el costo calculado de cada servicio.
                for servicio in servicios:

                    print(f"\nServicio: {servicio.nombre}")
                    print(f"Descripción: {servicio.descripcion}")

                    print(
                        f"Costo: ${servicio.calcular_costo():,.2f}"
                    )

                    print("-" * 50)

            except Exception as error:

                # Informa si ocurre algún problema al mostrar servicios.
                print("\nNo fue posible mostrar los servicios.")
                print(f"Detalle: {error}")

            volver_al_menu()

        # =================================================
        # OPCIÓN 3: CREAR Y PROCESAR RESERVA
        # =================================================

        elif opcion == "3":

            limpiar_consola()

            print("=" * 50)
            print("          PROCESAMIENTO DE RESERVA")
            print("=" * 50)

            try:
                # Verifica que exista un cliente registrado.
                if cliente is None:

                    print("\nPrimero debe registrar un cliente.")

                else:
                    # Crea el servicio que se utilizará
                    # para realizar la reserva de ejemplo.
                    servicio = ReservaSala(
                        "SER-001",
                        "Reserva de sala",
                        "Sala de reuniones",
                        50000,
                        10,
                        2
                    )

                    # Crea la reserva relacionando el cliente
                    # registrado con el servicio seleccionado.
                    reserva = Reserva(
                        "RES-001",
                        cliente,
                        servicio
                    )

                    # Confirma la reserva antes de procesarla.
                    reserva.confirmar()

                    # Procesa la reserva y calcula el valor total.
                    total = reserva.procesar()

                    print("\n¡Reserva procesada correctamente!")
                    print("-" * 50)
                    print(reserva)
                    print(f"\nTotal a pagar: ${total:,.2f}")
                    print("-" * 50)

            except ValueError as error:

                # Controla errores relacionados con valores.
                print("\nError de validación:")
                print(error)

            except Exception as error:

                # Controla otros errores durante el procesamiento.
                print("\nSe presentó un error al procesar la reserva.")
                print(f"Detalle: {error}")

            volver_al_menu()

        # =================================================
        # OPCIÓN 4: SALIR DEL SISTEMA
        # =================================================

        elif opcion == "4":

            limpiar_consola()

            print("=" * 50)
            print(" ¡Gracias por utilizar Software FJ!")
            print("=" * 50)

            break

        # =================================================
        # OPCIÓN NO VÁLIDA
        # =================================================

        else:

            print("\nOpción no válida. Intente nuevamente.")
            volver_al_menu()


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

# Ejecuta el sistema cuando el archivo se inicia directamente.
if __name__ == "__main__":
    ejecutar_sistema()