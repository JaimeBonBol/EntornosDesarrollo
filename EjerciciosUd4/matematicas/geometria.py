# matematicas/geometria.py

import math

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    """
    Calcula el perímetro de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El perímetro del círculo.
    """
    return 2 * math.pi * radio
