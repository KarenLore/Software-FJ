"""
Módulo de utilidades para el formato y presentación de información
del Sistema Integral de Gestión de Clientes, Servicios y Reservas
de la empresa Software FJ.

Contiene funciones para:
- Formatear fechas y horas.
- Presentar valores monetarios.
- Mostrar títulos organizados en la consola.
"""

# Importa datetime para obtener y trabajar con fechas y horas.
from datetime import datetime


def formatear_fecha(fecha=None):
    """
    Convierte una fecha y hora al formato día/mes/año.

    Si no se proporciona una fecha, utiliza la fecha y hora
    actual del sistema.

    Parámetro:
        fecha: Fecha que se desea convertir. Es opcional.

    Retorna:
        Una cadena de texto con el formato DD/MM/AAAA HH:MM:SS.
    """

    # Comprueba si no se recibió una fecha como argumento.
    if fecha is None:

        # Obtiene la fecha y hora actual del sistema.
        fecha = datetime.now()

    # Convierte la fecha al formato establecido y retorna el resultado.
    return fecha.strftime("%d/%m/%Y %H:%M:%S")


def formatear_moneda(valor):
    """
    Convierte un valor numérico a una representación monetaria.

    Parámetro:
        valor: Cantidad numérica que se desea presentar.

    Retorna:
        Una cadena de texto con el símbolo $,
        separadores de miles y dos decimales.
    """

    # Utiliza el formato de cadena para mostrar el valor
    # con separadores de miles y dos cifras decimales.
    return f"${valor:,.2f}"


def mostrar_titulo(titulo):
    """
    Muestra un título centrado en la consola.

    Presenta una línea superior y otra inferior para
    organizar visualmente las secciones del sistema.

    Parámetro:
        titulo: Texto que se desea mostrar como encabezado.
    """

    # Imprime una línea de separación de 50 caracteres.
    print("\n" + "=" * 50)

    # Centra el título dentro de un espacio de 50 caracteres.
    print(titulo.center(50))

    # Imprime la línea inferior para cerrar el encabezado.
    print("=" * 50)