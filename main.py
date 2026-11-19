
import os

# Importamos la clase Cliente para registrar los clientes.
from entidades.cliente import Cliente

# Importamos las funciones que permiten validar los datos
# antes de continuar solicitando el siguiente campo.
from entidades.validaciones import (
    validar_texto,
    validar_documento,
    validar_correo,
    validar_telefono
)

# Importamos los tres tipos de servicios especializados.
from servicios.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

# Importamos la clase Reserva para gestionar las reservas.
from reservas.reserva import Reserva


def limpiar_consola():
    """
    Limpia la pantalla de la terminal.
    En Windows utiliza cls y en otros sistemas clear.
    """
    os.system("cls" if os.name == "nt" else "clear")


def volver_al_menu():
    """
    Permite regresar al menú principal cuando el usuario
    presiona la tecla 0.
    """
    while True:
        opcion = input("\nPresione 0 para volver al menú: ")

        if opcion == "0":
            limpiar_consola()
            break
        else:
            print("Opción incorrecta. Debe presionar 0.")


def mostrar_menu():
    """
    Muestra las opciones principales del sistema Software FJ.
    """
    print("\n" + "=" * 45)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 45)
    print("1. Registrar cliente")
    print("2. Mostrar servicios")
    print("3. Crear y procesar reserva")
    print("4. Salir")
    print("=" * 45)


def ejecutar_sistema():
    """
    Ejecuta el sistema mediante un menú interactivo.
    Permite registrar clientes, consultar servicios
    y crear y procesar varias reservas.
    """

    # Variable que almacena el cliente registrado.
    cliente = None

    # Contador para generar identificadores únicos de reservas.
    contador_reservas = 1

    # Ciclo principal del menú.
    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        # Se limpia la pantalla para mostrar únicamente
        # el apartado correspondiente a la opción seleccionada.
        limpiar_consola()

        try:

            # ------------------------------------------------
            # OPCIÓN 1: REGISTRAR CLIENTE
            # ------------------------------------------------
            if opcion == "1":

                print("\nREGISTRO DE CLIENTE")
                print("-" * 45)

                # Se solicita y valida el nombre.
                # Si es incorrecto, no continúa con el documento.
                nombre = input("Nombre del cliente: ")
                nombre = validar_texto(nombre, "nombre")

                # Se solicita y valida el documento.
                documento = input("Documento: ")
                documento = validar_documento(documento)

                # Se solicita y valida el correo electrónico.
                # Si el correo es inválido, no solicita el teléfono.
                correo = input("Correo electrónico: ")
                correo = validar_correo(correo)

                # Se solicita y valida el teléfono.
                telefono = input("Teléfono: ")
                telefono = validar_telefono(telefono)

                # Se crea el objeto Cliente con los datos validados.
                cliente_nuevo = Cliente(
                    "CLI-001",
                    nombre,
                    documento,
                    correo,
                    telefono
                )

                # Se almacena el cliente registrado.
                cliente = cliente_nuevo

                print("\nCliente registrado correctamente.")
                print(cliente)

                volver_al_menu()

            # ------------------------------------------------
            # OPCIÓN 2: MOSTRAR SERVICIOS
            # ------------------------------------------------
            elif opcion == "2":

                # Se crean los servicios disponibles.
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

                print("\nSERVICIOS DISPONIBLES")
                print("-" * 45)

                # Se recorre la lista y se calcula el costo
                # de cada servicio mediante polimorfismo.
                for servicio in servicios:

                    print(f"\nNombre: {servicio.nombre}")
                    print(f"Descripción: {servicio.descripcion}")
                    print(
                        f"Costo: ${servicio.calcular_costo():,.2f}"
                    )

                volver_al_menu()

            # ------------------------------------------------
            # OPCIÓN 3: CREAR Y PROCESAR RESERVA
            # ------------------------------------------------
            elif opcion == "3":

                # Se verifica que exista un cliente registrado.
                if cliente is None:

                    print("\nPrimero debe registrar un cliente.")
                    volver_al_menu()
                    continue

                # Se muestran los servicios disponibles
                # para que el usuario pueda escoger uno.
                print("\nTIPOS DE SERVICIOS DISPONIBLES")
                print("-" * 45)
                print("1. Reserva de sala")
                print("2. Alquiler de equipos")
                print("3. Asesoría tecnológica")

                tipo_servicio = input(
                    "\nSeleccione el servicio que desea reservar: "
                )

                # Según la selección se crea el servicio correspondiente.
                if tipo_servicio == "1":

                    servicio = ReservaSala(
                        "SER-001",
                        "Reserva de sala",
                        "Sala de reuniones",
                        50000,
                        10,
                        2
                    )

                elif tipo_servicio == "2":

                    servicio = AlquilerEquipo(
                        "SER-002",
                        "Alquiler de equipos",
                        "Equipos tecnológicos",
                        30000,
                        2,
                        3
                    )

                elif tipo_servicio == "3":

                    servicio = Asesoria(
                        "SER-003",
                        "Asesoría tecnológica",
                        "Asesoría especializada",
                        80000,
                        "Tecnología",
                        2
                    )

                else:

                    # Si la selección no corresponde a ningún servicio,
                    # se informa al usuario y se regresa al menú.
                    print("\nOpción de servicio no válida.")
                    volver_al_menu()
                    continue

                # Se genera un identificador diferente para cada reserva.
                identificador_reserva = (
                    f"RES-{contador_reservas:03d}"
                )

                # Se crea la reserva con el cliente y el servicio elegido.
                reserva = Reserva(
                    identificador_reserva,
                    cliente,
                    servicio
                )

                # Se confirma la reserva antes de procesarla.
                reserva.confirmar()

                # Se procesa la reserva y se calcula el total.
                total = reserva.procesar()

                # Se incrementa el contador después de procesar
                # correctamente la reserva.
                contador_reservas += 1

                # Se muestran los resultados de la operación.
                print("\nRESERVA PROCESADA CORRECTAMENTE")
                print("-" * 45)
                print(f"Identificador: {reserva.identificador}")
                print(f"Cliente: {cliente.nombre}")
                print(f"Servicio seleccionado: {servicio.nombre}")
                print(f"Estado: {reserva.estado}")
                print(f"Total a pagar: ${total:,.2f}")

                volver_al_menu()

            # ------------------------------------------------
            # OPCIÓN 4: SALIR DEL SISTEMA
            # ------------------------------------------------
            elif opcion == "4":

                print("\nGracias por utilizar Software FJ.")
                break

            # ------------------------------------------------
            # OPCIÓN NO VÁLIDA
            # ------------------------------------------------
            else:

                print("\nOpción no válida. Intente nuevamente.")
                volver_al_menu()

        # Manejo de errores de validación.
        except ValueError as error:

            print(f"\nError de validación: {error}")
            volver_al_menu()

        # Manejo de otros errores inesperados.
        except Exception as error:

            print(f"\nSe presentó un error: {error}")
            volver_al_menu()


# Punto de entrada principal del programa.
# Ejecuta el sistema cuando se inicia este archivo.
if __name__ == "__main__":
    ejecutar_sistema()