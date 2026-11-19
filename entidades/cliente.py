from datetime import datetime
from entidades.entidad import Entidad
from entidades.validaciones import (
    validar_texto,
    validar_documento,
    validar_correo,
    validar_telefono
)


class Cliente(Entidad):

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self._nombre = validar_texto(nombre, "nombre")
        self._documento = validar_documento(documento)
        self._correo = validar_correo(correo)
        self._telefono = validar_telefono(telefono)
        self._fecha_registro = datetime.now()

        self.validar()

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    @property
    def fecha_registro(self):
        return self._fecha_registro

    def validar(self):
        validar_texto(self.nombre, "nombre")
        validar_documento(self.documento)
        validar_correo(self.correo)
        validar_telefono(self.telefono)
        return True

    def obtener_informacion(self):
        informacion = super().obtener_informacion()

        informacion.update({
            "nombre": self.nombre,
            "documento": self.documento,
            "correo": self.correo,
            "telefono": self.telefono,
            "fecha_registro": self.fecha_registro.isoformat()
        })

        return informacion

    def __str__(self):
        return f"Cliente: {self.nombre} - Documento: {self.documento}"