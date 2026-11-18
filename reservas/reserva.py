
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

        if not identificador:
            raise ValueError("El identificador de la reserva es obligatorio.")

        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "La reserva necesita un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise ServicioInvalidoError(
                "La reserva necesita un servicio válido."
            )

        self._identificador = str(identificador)
        self._cliente = cliente
        self._servicio = servicio
        self._fecha_reserva = fecha_reserva or datetime.now()
        self._estado = "Pendiente"
        self._total = None

        registrar_evento(
            f"Reserva {self.identificador} creada correctamente."
        )

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha_reserva(self):
        return self._fecha_reserva

    @property
    def estado(self):
        return self._estado

    @property
    def total(self):
        return self._total

    def confirmar(self):

        if self.estado != "Pendiente":
            registrar_error(
                f"No se pudo confirmar la reserva {self.identificador}."
            )
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"

        registrar_evento(
            f"Reserva {self.identificador} confirmada."
        )

        return True

    def cancelar(self):

        if self.estado not in ("Pendiente", "Confirmada"):
            registrar_error(
                f"No se pudo cancelar la reserva {self.identificador}."
            )
            raise EstadoReservaError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self._estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

        return True

    def calcular_total(self, descuento=0.0, impuesto=0.19):
        return CalculadoraCostos.calcular_total(
            self.servicio,
            descuento,
            impuesto
        )

    def procesar(self, descuento=0.0, impuesto=0.19):

        try:

            if self.estado != "Confirmada":
                raise EstadoReservaError(
                    "La reserva debe estar confirmada para procesarse."
                )

            self._total = self.calcular_total(
                descuento,
                impuesto
            )

        except EstadoReservaError:
            registrar_error(
                f"Estado incorrecto al procesar reserva {self.identificador}."
            )
            raise

        except Exception as error:
            registrar_excepcion(
                f"Error al procesar reserva {self.identificador}."
            )

            raise ProcesamientoReservaError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self._estado = "Procesada"

            registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Total: ${self._total}"
            )

            return self._total

        finally:
            registrar_evento(
                f"Finalizó el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )

    def obtener_informacion(self):

        return {
            "identificador": self.identificador,
            "cliente": self.cliente.nombre,
            "servicio": self.servicio.nombre,
            "fecha_reserva": self.fecha_reserva.isoformat(),
            "estado": self.estado,
            "total": self.total
        }

    def __str__(self):
        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
