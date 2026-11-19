
import re


def validar_texto(valor, campo):
    """
    Comprueba que un dato sea una cadena de texto y no esté vacío.

    Args:
        valor: Dato que se desea validar.
        campo: Nombre del campo que se está verificando.

    Returns:
        El texto sin espacios al inicio ni al final.

    Raises:
        ValueError: Si el valor no es texto o está vacío.
    """

    # Verifica que el dato sea texto y contenga información.
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"El campo {campo} no puede estar vacío.")

    return valor.strip()


def validar_documento(documento):
    """
    Valida el formato del documento de identificación.

    Permite letras, números y guiones, con una longitud
    entre 5 y 20 caracteres.
    """

    # Comprueba primero que el documento sea un texto válido.
    documento = validar_texto(documento, "documento")

    # Verifica los caracteres permitidos y la longitud.
    if not re.fullmatch(r"[A-Za-z0-9-]{5,20}", documento):
        raise ValueError("El documento debe tener entre 5 y 20 caracteres.")

    return documento


def validar_correo(correo):
    """
    Comprueba que el correo electrónico tenga un formato válido.

    Verifica que exista un nombre de usuario, el símbolo @,
    un dominio y una extensión de al menos dos letras.
    """

    # Comprueba que el correo no esté vacío.
    correo = validar_texto(correo, "correo")

    # Define el patrón de validación del correo electrónico.
    patron = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

    # Comprueba que el correo cumpla con el patrón establecido.
    if not re.fullmatch(patron, correo):
        raise ValueError("El correo electrónico no es válido.")

    return correo


def validar_telefono(telefono):
    """
    Valida el número telefónico del cliente.

    Permite un signo + opcional al inicio y entre 7 y 15 dígitos.
    """

    # Comprueba que el teléfono sea un texto válido.
    telefono = validar_texto(telefono, "teléfono")

    # Verifica que el número tenga el formato permitido.
    if not re.fullmatch(r"\+?[0-9]{7,15}", telefono):
        raise ValueError("El teléfono debe contener entre 7 y 15 dígitos.")

    return telefono