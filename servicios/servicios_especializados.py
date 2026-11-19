from servicios.servicio import Servicio


class ReservaSala(Servicio):

    def _init_(
        self, identificador, nombre, descripcion,
        tarifa_base, capacidad, horas
    ):
        super()._init_(
            identificador, nombre, descripcion, tarifa_base
        )

        if capacidad <= 0 or horas <= 0:
            raise ValueError("La capacidad y las horas deben ser positivas.")

        self._capacidad = capacidad
        self._horas = horas

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def horas(self):
        return self._horas

    def calcular_costo(self):
        return self.tarifa_base * self.horas

    def obtener_informacion(self):
        datos = super().obtener_informacion()
        datos.update({
            "tipo": "Reserva de sala",
            "capacidad": self.capacidad,
            "horas": self.horas,
            "costo": self.calcular_costo()
        })
        return datos


class AlquilerEquipo(Servicio):

    def _init_(
        self, identificador, nombre, descripcion,
        tarifa_base, cantidad, dias
    ):
        super()._init_(
            identificador, nombre, descripcion, tarifa_base
        )

        if cantidad <= 0 or dias <= 0:
            raise ValueError("La cantidad y los días deben ser positivos.")

        self._cantidad = cantidad
        self._dias = dias

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def dias(self):
        return self._dias

    def calcular_costo(self):
        return self.tarifa_base * self.cantidad * self.dias

    def obtener_informacion(self):
        datos = super().obtener_informacion()
        datos.update({
            "tipo": "Alquiler de equipos",
            "cantidad": self.cantidad,
            "dias": self.dias,
            "costo": self.calcular_costo()
        })
        return datos


class Asesoria(Servicio):

    def _init_(
        self, identificador, nombre, descripcion,
        tarifa_base, especialidad, horas
    ):
        super()._init_(
            identificador, nombre, descripcion, tarifa_base
        )

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        if not especialidad:
            raise ValueError("La especialidad es obligatoria.")

        self._especialidad = especialidad
        self._horas = horas

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def horas(self):
        return self._horas

    def calcular_costo(self):
        return self.tarifa_base * self.horas

    def obtener_informacion(self):
        datos = super().obtener_informacion()
        datos.update({
            "tipo": "Asesoría",
            "especialidad": self.especialidad,
            "horas": self.horas,
            "costo": self.calcular_costo()
        })
        return datos