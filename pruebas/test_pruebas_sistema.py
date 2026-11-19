
import unittest

from entidades.cliente import Cliente
from servicios.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)
from reservas.reserva import Reserva
from excepciones.excepciones_personalizadas import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    EstadoReservaError
)


class PruebasSistema(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(
            "C001",
            "Carlos Perez",
            "12345678",
            "carlos@gmail.com",
            "3001234567"
        )

        self.servicio = ReservaSala(
            "S001",
            "Sala de reuniones",
            "Sala para reuniones empresariales",
            50000,
            10,
            2
        )

        self.reserva = Reserva(
            "R001",
            self.cliente,
            self.servicio
        )

    # PRUEBAS DE CLIENTES

    def test_01_crear_cliente(self):
        self.assertEqual(self.cliente.nombre, "Carlos Perez")

    def test_02_cliente_correo_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("C002", "Ana", "12345678",
                    "correo_invalido", "3001234567")

    def test_03_cliente_documento_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("C003", "Ana", "123",
                    "ana@gmail.com", "3001234567")

    # PRUEBAS DE SERVICIOS

    def test_04_calcular_costo_sala(self):
        self.assertEqual(self.servicio.calcular_costo(), 100000)

    def test_05_calcular_costo_equipo(self):
        equipo = AlquilerEquipo(
            "S002", "Computadores", "Alquiler",
            30000, 2, 3
        )
        self.assertEqual(equipo.calcular_costo(), 180000)

    def test_06_calcular_costo_asesoria(self):
        asesoria = Asesoria(
            "S003", "Asesoria", "Asesoria tecnica",
            80000, "Tecnologia", 2
        )
        self.assertEqual(asesoria.calcular_costo(), 160000)

    # PRUEBAS DE RESERVAS

    def test_07_crear_reserva(self):
        self.assertEqual(self.reserva.estado, "Pendiente")

    def test_08_confirmar_reserva(self):
        self.reserva.confirmar()
        self.assertEqual(self.reserva.estado, "Confirmada")

    def test_09_cancelar_reserva(self):
        self.reserva.cancelar()
        self.assertEqual(self.reserva.estado, "Cancelada")

    def test_10_procesar_reserva(self):
        self.reserva.confirmar()
        total = self.reserva.procesar()

        self.assertEqual(total, 119000)
        self.assertEqual(self.reserva.estado, "Procesada")

    def test_11_procesar_reserva_sin_confirmar(self):
        with self.assertRaises(EstadoReservaError):
            self.reserva.procesar()

    def test_12_confirmar_reserva_cancelada(self):
        self.reserva.cancelar()

        with self.assertRaises(EstadoReservaError):
            self.reserva.confirmar()

    # PRUEBAS DE VALIDACIONES DE RESERVA

    def test_13_cliente_invalido(self):
        with self.assertRaises(ClienteInvalidoError):
            Reserva("R002", "Cliente incorrecto", self.servicio)

    def test_14_servicio_invalido(self):
        with self.assertRaises(ServicioInvalidoError):
            Reserva("R003", self.cliente, "Servicio incorrecto")


if __name__ == "__main__":
    unittest.main(verbosity=2)
