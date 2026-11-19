import unittest

from entidades.cliente import Cliente
from servicios.servicios_especializados import ReservaSala
from reservas.reserva import Reserva


class PruebasSistema(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(
            "C001",
            "Carlos Pérez",
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

    def test_crear_cliente(self):
        self.assertEqual(self.cliente.nombre, "Carlos Pérez")

    def test_crear_reserva(self):
        self.assertEqual(self.reserva.estado, "Pendiente")

    def test_confirmar_reserva(self):
        self.reserva.confirmar()
        self.assertEqual(self.reserva.estado, "Confirmada")

    def test_cancelar_reserva(self):
        self.reserva.cancelar()
        self.assertEqual(self.reserva.estado, "Cancelada")

    def test_procesar_reserva(self):
        self.reserva.confirmar()
        total = self.reserva.procesar()

        self.assertGreater(total, 0)
        self.assertEqual(self.reserva.estado, "Procesada")


if __name__ == "__main__":
    unittest.main()