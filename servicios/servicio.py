
from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio ofrecido por Software FJ.

    Define los atributos y métodos comunes que deben implementar
    los diferentes tipos de servicios del sistema.

    Aplica abstracción mediante ABC y abstractmethod, y encapsulación
    mediante atributos protegidos y propiedades.
    """

    def __init__(self, identificador, nombre, descripcion, tarifa_base):
        """
        Inicializa los datos generales de un servicio.

        Args:
            identificador: Código único del servicio.
            nombre: Nombre del servicio.
            descripcion: Descripción del servicio.
            tarifa_base: Valor económico inicial del servicio.
        """

        # Verifica que los datos obligatorios estén presentes.
        if not identificador or not nombre:
            raise ValueError("El identificador y el nombre son obligatorios.")

        # Comprueba que la tarifa tenga un valor positivo.
        if tarifa_base <= 0:
            raise ValueError("La tarifa base debe ser mayor que cero.")

        # Almacena los atributos de forma encapsulada.
        self._identificador = str(identificador)
        self._nombre = nombre
        self._descripcion = descripcion
        self._tarifa_base = float(tarifa_base)

    @property
    def identificador(self):
        """Retorna el identificador único del servicio."""
        return self._identificador

    @property
    def nombre(self):
        """Retorna el nombre del servicio."""
        return self._nombre

    @property
    def descripcion(self):
        """Retorna la descripción del servicio."""
        return self._descripcion

    @property
    def tarifa_base(self):
        """Retorna la tarifa base del servicio."""
        return self._tarifa_base

    @abstractmethod
    def calcular_costo(self):
        """
        Método abstracto para calcular el costo del servicio.

        Cada clase especializada debe implementar su propia
        fórmula de cálculo.
        """
        pass

    def obtener_informacion(self):
        """
        Retorna un diccionario con la información general del servicio.

        Este método puede ser ampliado por las clases especializadas.
        """
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "tarifa_base": self.tarifa_base
        }

    def __str__(self):
        """Retorna una representación textual del servicio."""
        return f"{self.nombre}: {self.descripcion}"