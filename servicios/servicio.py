from abc import ABC, abstractmethod


class Servicio(ABC):

    def _init_(self, identificador, nombre, descripcion, tarifa_base):
        if not identificador or not nombre:
            raise ValueError("El identificador y el nombre son obligatorios.")

        if tarifa_base <= 0:
            raise ValueError("La tarifa base debe ser mayor que cero.")

        self._identificador = str(identificador)
        self._nombre = nombre
        self._descripcion = descripcion
        self._tarifa_base = float(tarifa_base)

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @abstractmethod
    def calcular_costo(self):
        pass

    def obtener_informacion(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "tarifa_base": self.tarifa_base
        }

    def _str_(self):
        return f"{self.nombre}: {self.descripcion}"