
import logging
from pathlib import Path


class ClienteInvalidoError(Exception):
    """Se presenta cuando los datos del cliente no son válidos."""
    pass


class ServicioInvalidoError(Exception):
    """Se presenta cuando un servicio no es válido."""
    pass


class ReservaNoEncontradaError(Exception):
    """Se presenta cuando no se encuentra una reserva."""
    pass


class EstadoReservaError(Exception):
    """Se presenta cuando una operación no corresponde al estado."""
    pass


class ProcesamientoReservaError(Exception):
    """Se presenta cuando ocurre un error al procesar una reserva."""
    pass


# Configuración del registro de eventos y errores.
RUTA_LOGS = Path(__file__).resolve().parent.parent / "logs"
RUTA_LOGS.mkdir(parents=True, exist_ok=True)

RUTA_ARCHIVO_LOG = RUTA_LOGS / "sistema.log"

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

if not logger.handlers:
    manejador = logging.FileHandler(
        RUTA_ARCHIVO_LOG,
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    logger.info(mensaje)


def registrar_error(mensaje):
    logger.error(mensaje)


def registrar_excepcion(mensaje):
    logger.exception(mensaje)
