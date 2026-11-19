"""
Módulo de excepciones personalizadas y registro de eventos y errores
del Sistema Integral de Gestión de Clientes, Servicios y Reservas
de la empresa Software FJ.
"""

# Importa el módulo logging para registrar eventos, errores y excepciones.
import logging

# Importa Path para administrar las rutas de los archivos y directorios.
from pathlib import Path


# ============================================================
# EXCEPCIONES PERSONALIZADAS
# ============================================================

class ClienteInvalidoError(Exception):
    """
    Excepción que se presenta cuando los datos ingresados
    para registrar o utilizar un cliente no son válidos.
    """
    pass


class ServicioInvalidoError(Exception):
    """
    Excepción que se presenta cuando un servicio no cumple
    con las condiciones necesarias para ser utilizado.
    """
    pass


class ReservaNoEncontradaError(Exception):
    """
    Excepción que se presenta cuando el sistema intenta
    consultar una reserva que no se encuentra registrada.
    """
    pass


class EstadoReservaError(Exception):
    """
    Excepción que se presenta cuando se intenta ejecutar
    una operación que no corresponde al estado actual
    de una reserva.
    """
    pass


class ProcesamientoReservaError(Exception):
    """
    Excepción que se presenta cuando ocurre un inconveniente
    durante el procesamiento de una reserva.
    """
    pass


# ============================================================
# CONFIGURACIÓN DEL REGISTRO DE EVENTOS Y ERRORES
# ============================================================

# Obtiene la ruta de la carpeta logs ubicada en el directorio
# principal del proyecto Software FJ.
RUTA_LOGS = Path(__file__).resolve().parent.parent / "logs"

# Crea la carpeta de registros si no existe.
# parents=True permite crear directorios intermedios.
# exist_ok=True evita errores si la carpeta ya está creada.
RUTA_LOGS.mkdir(parents=True, exist_ok=True)

# Define la ubicación y el nombre del archivo donde
# se almacenarán los registros del sistema.
RUTA_ARCHIVO_LOG = RUTA_LOGS / "sistema.log"

# Crea u obtiene el registrador identificado como SoftwareFJ.
logger = logging.getLogger("SoftwareFJ")

# Establece el nivel INFO para permitir el registro de
# eventos informativos, advertencias y errores.
logger.setLevel(logging.INFO)

# Comprueba que el registrador no tenga manejadores configurados.
# Esto evita que los mensajes se escriban varias veces.
if not logger.handlers:

    # Crea un manejador para guardar los registros en el archivo.
    # El parámetro utf-8 permite almacenar caracteres especiales.
    manejador = logging.FileHandler(
        RUTA_ARCHIVO_LOG,
        encoding="utf-8"
    )

    # Establece el formato de los mensajes registrados.
    # Incluye fecha, hora, nivel del registro y descripción.
    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Asigna el formato definido al manejador del archivo.
    manejador.setFormatter(formato)

    # Agrega el manejador al registrador para activar
    # el almacenamiento de los mensajes.
    logger.addHandler(manejador)


# ============================================================
# FUNCIONES PARA REGISTRAR EVENTOS Y ERRORES
# ============================================================

def registrar_evento(mensaje):
    """
    Registra un evento informativo en el archivo de logs.

    Se utiliza para dejar constancia de operaciones realizadas
    correctamente dentro del sistema.

    Parámetro:
        mensaje: Descripción del evento que se desea registrar.
    """

    # Registra el mensaje con nivel informativo INFO.
    logger.info(mensaje)


def registrar_error(mensaje):
    """
    Registra un error ocurrido durante la ejecución del sistema.

    Permite identificar situaciones en las que una operación
    no pudo realizarse correctamente.

    Parámetro:
        mensaje: Descripción del error presentado.
    """

    # Registra el mensaje con nivel ERROR.
    logger.error(mensaje)


def registrar_excepcion(mensaje):
    """
    Registra una excepción junto con la información técnica
    del error y su seguimiento de ejecución (traceback).

    Se utiliza principalmente dentro de bloques try/except
    para facilitar la identificación de fallos.

    Parámetro:
        mensaje: Descripción de la excepción ocurrida.
    """

    # Registra el mensaje y la información de la excepción activa.
    logger.exception(mensaje)