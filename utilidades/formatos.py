from datetime import datetime


def formatear_fecha(fecha=None):
    if fecha is None:
        fecha = datetime.now()

    return fecha.strftime("%d/%m/%Y %H:%M:%S")


def formatear_moneda(valor):
    return f"${valor:,.2f}"


def mostrar_titulo(titulo):
    print("\n" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50)