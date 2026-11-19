import re


def validar_texto(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"El campo {campo} no puede estar vacío.")
    return valor.strip()


def validar_documento(documento):
    documento = validar_texto(documento, "documento")

    if not re.fullmatch(r"[A-Za-z0-9-]{5,20}", documento):
        raise ValueError("El documento debe tener entre 5 y 20 caracteres.")

    return documento


def validar_correo(correo):
    correo = validar_texto(correo, "correo")

    patron = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(patron, correo):
        raise ValueError("El correo electrónico no es válido.")

    return correo


def validar_telefono(telefono):
    telefono = validar_texto(telefono, "teléfono")

    if not re.fullmatch(r"\+?[0-9]{7,15}", telefono):
        raise ValueError("El teléfono debe contener entre 7 y 15 dígitos.")

    return telefono