from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self._identificador = str(identificador)

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def validar(self):
        pass

    def obtener_informacion(self):
        return {
            "identificador": self.identificador
        }