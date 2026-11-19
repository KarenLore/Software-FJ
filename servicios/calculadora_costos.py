
class CalculadoraCostos:
    """
    Clase encargada de realizar los cálculos económicos de los servicios.

    Permite calcular valores totales aplicando descuentos e impuestos,
    sin necesidad de crear objetos de esta clase.
    """

    # Porcentaje general de impuesto aplicado a los servicios (19 %).
    IMPUESTO_GENERAL = 0.19

    @staticmethod
    def calcular_total(servicio, descuento=0.0, impuesto=0.19):
        """
        Calcula el costo total de un servicio aplicando descuento e impuesto.

        Args:
            servicio: Objeto de una clase especializada de Servicio.
            descuento: Porcentaje de descuento expresado como decimal.
            impuesto: Porcentaje de impuesto expresado como decimal.

        Returns:
            El valor total del servicio redondeado a dos decimales.

        Raises:
            ValueError: Si el descuento o el impuesto están fuera del rango
            permitido entre 0 y 1.
        """

        # Verifica que el descuento esté dentro del rango permitido.
        if not 0 <= descuento <= 1:
            raise ValueError("El descuento debe estar entre 0 y 1.")

        # Verifica que el impuesto esté dentro del rango permitido.
        if not 0 <= impuesto <= 1:
            raise ValueError("El impuesto debe estar entre 0 y 1.")

        # Obtiene el costo inicial utilizando el método del servicio.
        subtotal = servicio.calcular_costo()

        # Calcula el valor correspondiente al descuento.
        valor_descuento = subtotal * descuento

        # Resta el descuento al subtotal.
        subtotal_con_descuento = subtotal - valor_descuento

        # Calcula el impuesto sobre el subtotal descontado.
        valor_impuesto = subtotal_con_descuento * impuesto

        # Suma el subtotal descontado y el impuesto.
        total = subtotal_con_descuento + valor_impuesto

        # Retorna el resultado con dos cifras decimales.
        return round(total, 2)

    @staticmethod
    def calcular_sin_impuesto(servicio, descuento=0.0):
        """
        Calcula el costo del servicio sin aplicar impuestos.

        Permite aplicar opcionalmente un descuento.
        """
        return CalculadoraCostos.calcular_total(
            servicio, descuento, impuesto=0
        )

    @staticmethod
    def calcular_con_impuesto(servicio):
        """
        Calcula el costo del servicio aplicando el impuesto general del 19 %.
        """
        return CalculadoraCostos.calcular_total(
            servicio,
            descuento=0,
            impuesto=CalculadoraCostos.IMPUESTO_GENERAL
        )

    @staticmethod
    def calcular_con_descuento(servicio, descuento):
        """
        Calcula el costo del servicio aplicando un descuento y el impuesto general.
        """
        return CalculadoraCostos.calcular_total(
            servicio,
            descuento=descuento,
            impuesto=CalculadoraCostos.IMPUESTO_GENERAL
        )