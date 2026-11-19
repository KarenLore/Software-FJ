class CalculadoraCostos:

    IMPUESTO_GENERAL = 0.19

    @staticmethod
    def calcular_total(servicio, descuento=0.0, impuesto=0.19):
        """
        Calcula el costo de un servicio con descuento e impuesto.
        El descuento y el impuesto se expresan como decimales.
        """

        if not 0 <= descuento <= 1:
            raise ValueError("El descuento debe estar entre 0 y 1.")

        if not 0 <= impuesto <= 1:
            raise ValueError("El impuesto debe estar entre 0 y 1.")

        subtotal = servicio.calcular_costo()
        valor_descuento = subtotal * descuento
        subtotal_con_descuento = subtotal - valor_descuento
        valor_impuesto = subtotal_con_descuento * impuesto

        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)

    @staticmethod
    def calcular_sin_impuesto(servicio, descuento=0.0):
        return CalculadoraCostos.calcular_total(
            servicio, descuento, impuesto=0
        )

    @staticmethod
    def calcular_con_impuesto(servicio):
        return CalculadoraCostos.calcular_total(
            servicio,
            descuento=0,
            impuesto=CalculadoraCostos.IMPUESTO_GENERAL
        )

    @staticmethod
    def calcular_con_descuento(servicio, descuento):
        return CalculadoraCostos.calcular_total(
            servicio,
            descuento=descuento,
            impuesto=CalculadoraCostos.IMPUESTO_GENERAL
        )