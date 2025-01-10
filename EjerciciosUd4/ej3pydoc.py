# matematicas.py

def suma(a, b):
    """
    Realiza la suma de dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def resta(a, b):
    """
    Realiza la resta de dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la resta.
    """
    return a - b

def multiplicacion(a, b):
    """
    Realiza la multiplicación de dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b

def division(a, b):
    """
    Realiza la división de dos números. Si el divisor es cero, retorna un mensaje de error.

    Args:
        a (float): Numerador.
        b (float): Denominador.

    Returns:
        float: Resultado de la división o mensaje de error si b es cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b
