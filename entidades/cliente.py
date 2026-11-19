
from datetime import datetime
from entidades.entidad import Entidad
from entidades.validaciones import (
    validar_texto,
    validar_documento,
    validar_correo,
    validar_telefono
)


class Cliente(Entidad):
    """
    Representa a un cliente registrado en el sistema Software FJ.

    Hereda de Entidad y almacena los datos personales del cliente,
    aplicando validaciones para garantizar la calidad de la información.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):
        """
        Inicializa un cliente con sus datos personales.

        Args:
            identificador: Código único del cliente.
            nombre: Nombre completo del cliente.
            documento: Número de identificación.
            correo: Dirección de correo electrónico.
            telefono: Número de contacto.
        """

        # Inicializa el identificador heredado de la clase Entidad.
        super().__init__(identificador)

        # Valida y almacena los datos personales del cliente.
        self._nombre = validar_texto(nombre, "nombre")
        self._documento = validar_documento(documento)
        self._correo = validar_correo(correo)
        self._telefono = validar_telefono(telefono)

        # Registra automáticamente la fecha y hora de creación.
        self._fecha_registro = datetime.now()

        # Comprueba que todos los datos del cliente sean válidos.
        self.validar()

    @property
    def nombre(self):
        """Retorna el nombre del cliente."""
        return self._nombre

    @property
    def documento(self):
        """Retorna el documento de identificación del cliente."""
        return self._documento

    @property
    def correo(self):
        """Retorna el correo electrónico del cliente."""
        return self._correo

    @property
    def telefono(self):
        """Retorna el teléfono de contacto del cliente."""
        return self._telefono

    @property
    def fecha_registro(self):
        """Retorna la fecha y hora en que se registró el cliente."""
        return self._fecha_registro

    def validar(self):
        """
        Verifica que los datos personales del cliente sean correctos.

        Returns:
            True si todas las validaciones se completan correctamente.

        Raises:
            ValueError: Si alguno de los datos no cumple las reglas
            establecidas en el módulo de validaciones.
        """

        # Ejecuta las validaciones correspondientes a cada dato.
        validar_texto(self.nombre, "nombre")
        validar_documento(self.documento)
        validar_correo(self.correo)
        validar_telefono(self.telefono)

        return True

    def obtener_informacion(self):
        """
        Retorna un diccionario con toda la información del cliente.

        Combina los datos heredados de Entidad con los atributos
        específicos del cliente.
        """

        # Obtiene la información general de la clase padre.
        informacion = super().obtener_informacion()

        # Agrega los datos personales y la fecha de registro.
        informacion.update({
            "nombre": self.nombre,
            "documento": self.documento,
            "correo": self.correo,
            "telefono": self.telefono,
            "fecha_registro": self.fecha_registro.isoformat()
        })

        return informacion

    def __str__(self):
        """Retorna una representación textual del cliente."""
        return f"Cliente: {self.nombre} - Documento: {self.documento}"