
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta base para las entidades del sistema Software FJ.

    Define una estructura común para las entidades que se gestionan
    en el sistema, estableciendo un identificador único y métodos
    que deben implementar las clases derivadas.
    """

    def __init__(self, identificador):
        """
        Inicializa una entidad con su identificador único.

        Args:
            identificador: Código que permite identificar la entidad.

        Raises:
            ValueError: Si el identificador no es proporcionado.
        """

        # Comprueba que el identificador sea obligatorio.
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        # Almacena el identificador como atributo encapsulado.
        self._identificador = str(identificador)

    @property
    def identificador(self):
        """Permite consultar el identificador de la entidad."""
        return self._identificador

    @abstractmethod
    def validar(self):
        """
        Método abstracto para validar los datos de una entidad.

        Cada clase que herede de Entidad debe implementar
        su propia lógica de validación.
        """
        pass

    def obtener_informacion(self):
        """
        Retorna la información general de la entidad.

        Returns:
            Un diccionario que contiene el identificador.
        """
        return {
            "identificador": self.identificador
        }
