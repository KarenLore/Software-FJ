
from datetime import datetime

from entidades.cliente import Cliente
from servicios.servicio import Servicio
from servicios.calculadora_costos import CalculadoraCostos

from excepciones.excepciones_personalizadas import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    EstadoReservaError,
    ProcesamientoReservaError,
    registrar_evento,
    registrar_error,
    registrar_excepcion
)


class Reserva:
    """
    Representa una reserva realizada por un cliente en Software FJ.

    Administra la creación, confirmación, cancelación y procesamiento
    de reservas, además de calcular su costo y registrar los eventos
    y errores que ocurren durante su ejecución.
    """

    # Define los estados permitidos para una reserva.
    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Procesada"
    )

    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        fecha_reserva=None
    ):
        """
        Inicializa una reserva asociada a un cliente y un servicio.

        Args:
            identificador: Código único de la reserva.
            cliente: Objeto de tipo Cliente.
            servicio: Objeto de una clase derivada de Servicio.
            fecha_reserva: Fecha de la reserva; si no se proporciona,
                se utiliza la fecha y hora actuales.

        Raises:
            ValueError: Si el identificador no es válido.
            ClienteInvalidoError: Si el cliente no es una instancia de Cliente.
            ServicioInvalidoError: Si el servicio no es una instancia de Servicio.
        """

        # Comprueba que la reserva tenga un identificador.
        if not identificador:
            raise ValueError("El identificador de la reserva es obligatorio.")

        # Verifica que el cliente pertenezca a la clase Cliente.
        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "La reserva necesita un cliente válido."
            )

        # Verifica que el servicio pertenezca a Servicio o una clase derivada.
        if not isinstance(servicio, Servicio):
            raise ServicioInvalidoError(
                "La reserva necesita un servicio válido."
            )

        # Inicializa los atributos encapsulados de la reserva.
        self._identificador = str(identificador)
        self._cliente = cliente
        self._servicio = servicio
        self._fecha_reserva = fecha_reserva or datetime.now()

        # Toda reserva comienza en estado pendiente y sin total calculado.
        self._estado = "Pendiente"
        self._total = None

        # Registra la creación correcta de la reserva.
        registrar_evento(
            f"Reserva {self.identificador} creada correctamente."
        )

    @property
    def identificador(self):
        """Retorna el identificador único de la reserva."""
        return self._identificador

    @property
    def cliente(self):
        """Retorna el cliente asociado a la reserva."""
        return self._cliente

    @property
    def servicio(self):
        """Retorna el servicio asociado a la reserva."""
        return self._servicio

    @property
    def fecha_reserva(self):
        """Retorna la fecha y hora de creación de la reserva."""
        return self._fecha_reserva

    @property
    def estado(self):
        """Retorna el estado actual de la reserva."""
        return self._estado

    @property
    def total(self):
        """Retorna el valor total calculado de la reserva."""
        return self._total

    def confirmar(self):
        """
        Confirma una reserva que se encuentra pendiente.

        Returns:
            True si la reserva se confirma correctamente.

        Raises:
            EstadoReservaError: Si la reserva no está pendiente.
        """

        # Solo se permite confirmar reservas pendientes.
        if self.estado != "Pendiente":
            registrar_error(
                f"No se pudo confirmar la reserva {self.identificador}."
            )
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        # Actualiza el estado de la reserva.
        self._estado = "Confirmada"

        # Registra el evento de confirmación.
        registrar_evento(
            f"Reserva {self.identificador} confirmada."
        )

        return True

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.

        Returns:
            True si la cancelación se realiza correctamente.

        Raises:
            EstadoReservaError: Si la reserva ya fue procesada o cancelada.
        """

        # Verifica que la reserva se encuentre en un estado cancelable.
        if self.estado not in ("Pendiente", "Confirmada"):
            registrar_error(
                f"No se pudo cancelar la reserva {self.identificador}."
            )
            raise EstadoReservaError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        # Actualiza el estado de la reserva.
        self._estado = "Cancelada"

        # Registra el evento de cancelación.
        registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

        return True

    def calcular_total(self, descuento=0.0, impuesto=0.19):
        """
        Calcula el valor total de la reserva.

        Utiliza la CalculadoraCostos para aplicar el descuento
        y el impuesto correspondiente al servicio asociado.
        """
        return CalculadoraCostos.calcular_total(
            self.servicio,
            descuento,
            impuesto
        )

    def procesar(self, descuento=0.0, impuesto=0.19):
        """
        Procesa una reserva previamente confirmada.

        Calcula el costo total, cambia el estado a procesada
        y registra los eventos o errores que se presenten.

        Args:
            descuento: Porcentaje de descuento expresado como decimal.
            impuesto: Porcentaje de impuesto expresado como decimal.

        Returns:
            El valor total de la reserva procesada.

        Raises:
            EstadoReservaError: Si la reserva no está confirmada.
            ProcesamientoReservaError: Si ocurre un error durante
                el cálculo o procesamiento.
        """

        try:
            # Verifica que la reserva esté confirmada antes de procesarla.
            if self.estado != "Confirmada":
                raise EstadoReservaError(
                    "La reserva debe estar confirmada para procesarse."
                )

            # Calcula y almacena el valor total de la reserva.
            self._total = self.calcular_total(
                descuento,
                impuesto
            )

        except EstadoReservaError:
            # Registra el error cuando la reserva tiene un estado incorrecto.
            registrar_error(
                f"Estado incorrecto al procesar reserva {self.identificador}."
            )
            raise

        except Exception as error:
            # Registra los detalles de cualquier otro error inesperado.
            registrar_excepcion(
                f"Error al procesar reserva {self.identificador}."
            )

            # Encadena la excepción original para conservar su causa.
            raise ProcesamientoReservaError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            # Se ejecuta cuando el procesamiento termina correctamente.
            self._estado = "Procesada"

            registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Total: ${self._total}"
            )

            return self._total

        finally:
            # Registra la finalización del intento, haya sido exitoso o no.
            registrar_evento(
                f"Finalizó el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )

    def obtener_informacion(self):
        """
        Retorna los datos principales de la reserva en un diccionario.
        """
        return {
            "identificador": self.identificador,
            "cliente": self.cliente.nombre,
            "servicio": self.servicio.nombre,
            "fecha_reserva": self.fecha_reserva.isoformat(),
            "estado": self.estado,
            "total": self.total
        }

    def __str__(self):
        """Retorna una descripción textual de la reserva."""
        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )