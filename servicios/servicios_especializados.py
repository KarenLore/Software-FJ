
from servicios.servicio import Servicio


class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de salas de reuniones.

    Hereda los atributos y métodos generales de Servicio
    e implementa su propio cálculo de costos.
    """

    def __init__(self, identificador, nombre, descripcion,
                 tarifa_base, capacidad, horas):
        """Inicializa una reserva de sala con su capacidad y duración."""

        # Inicializa los atributos heredados de la clase Servicio.
        super().__init__(identificador, nombre, descripcion, tarifa_base)

        # Valida que la capacidad y las horas sean valores positivos.
        if capacidad <= 0 or horas <= 0:
            raise ValueError("La capacidad y las horas deben ser positivas.")

        # Almacena los atributos específicos de la reserva de sala.
        self._capacidad = capacidad
        self._horas = horas

    @property
    def capacidad(self):
        """Retorna la capacidad de la sala."""
        return self._capacidad

    @property
    def horas(self):
        """Retorna la cantidad de horas reservadas."""
        return self._horas

    def calcular_costo(self):
        """Calcula el costo multiplicando la tarifa por las horas."""
        return self.tarifa_base * self.horas

    def obtener_informacion(self):
        """Retorna la información general y específica de la sala."""

        # Recupera la información heredada de Servicio.
        datos = super().obtener_informacion()

        # Agrega los datos propios de la reserva de sala.
        datos.update({
            "tipo": "Reserva de sala",
            "capacidad": self.capacidad,
            "horas": self.horas,
            "costo": self.calcular_costo()
        })
        return datos


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos tecnológicos.

    Hereda las características generales de Servicio y calcula
    el costo según la cantidad de equipos y los días de alquiler.
    """

    def __init__(self, identificador, nombre, descripcion,
                 tarifa_base, cantidad, dias):
        """Inicializa el alquiler con la cantidad y los días solicitados."""

        # Inicializa los atributos comunes del servicio.
        super().__init__(identificador, nombre, descripcion, tarifa_base)

        # Comprueba que la cantidad y los días sean positivos.
        if cantidad <= 0 or dias <= 0:
            raise ValueError("La cantidad y los días deben ser positivos.")

        # Almacena los atributos específicos del alquiler.
        self._cantidad = cantidad
        self._dias = dias

    @property
    def cantidad(self):
        """Retorna la cantidad de equipos alquilados."""
        return self._cantidad

    @property
    def dias(self):
        """Retorna la duración del alquiler en días."""
        return self._dias

    def calcular_costo(self):
        """
        Calcula el costo total del alquiler.

        Multiplica la tarifa base por la cantidad de equipos
        y por el número de días.
        """
        return self.tarifa_base * self.cantidad * self.dias

    def obtener_informacion(self):
        """Retorna la información general y específica del alquiler."""

        # Obtiene los datos comunes de la clase padre.
        datos = super().obtener_informacion()

        # Incorpora la información propia del alquiler de equipos.
        datos.update({
            "tipo": "Alquiler de equipos",
            "cantidad": self.cantidad,
            "dias": self.dias,
            "costo": self.calcular_costo()
        })
        return datos


class Asesoria(Servicio):
    """
    Representa el servicio de asesoría especializada.

    Hereda las características de Servicio y agrega la especialidad
    y la cantidad de horas de asesoría.
    """

    def __init__(self, identificador, nombre, descripcion,
                 tarifa_base, especialidad, horas):
        """Inicializa una asesoría con su especialidad y duración."""

        # Inicializa los atributos heredados de Servicio.
        super().__init__(identificador, nombre, descripcion, tarifa_base)

        # Valida que la duración de la asesoría sea positiva.
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        # Comprueba que se haya indicado una especialidad.
        if not especialidad:
            raise ValueError("La especialidad es obligatoria.")

        # Almacena los atributos particulares de la asesoría.
        self._especialidad = especialidad
        self._horas = horas

    @property
    def especialidad(self):
        """Retorna el área de especialización de la asesoría."""
        return self._especialidad

    @property
    def horas(self):
        """Retorna la cantidad de horas de asesoría."""
        return self._horas

    def calcular_costo(self):
        """Calcula el costo de la asesoría según las horas contratadas."""
        return self.tarifa_base * self.horas

    def obtener_informacion(self):
        """Retorna la información general y específica de la asesoría."""

        # Recupera la información común de la clase Servicio.
        datos = super().obtener_informacion()

        # Agrega los datos particulares de la asesoría.
        datos.update({
            "tipo": "Asesoría",
            "especialidad": self.especialidad,
            "horas": self.horas,
            "costo": self.calcular_costo()
        })
        return datos