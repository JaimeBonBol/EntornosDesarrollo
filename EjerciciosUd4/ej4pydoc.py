def raiz_n_esima(x, n):
    """
    Calcula la n-ésima raíz de un número.

    Args:
        x (float): El número del cual calcular la raíz.
        n (int): El valor de la raíz (por ejemplo, 2 para la raíz cuadrada, 3 para la raíz cúbica).

    Returns:
        float: El resultado de la n-ésima raíz de x.
    """
    if x < 0 and n % 2 == 0:
        raise ValueError("No se puede calcular la raíz n-ésima de un número negativo con un exponente par.")
    
    return x ** (1 / n)

# Ejemplo de uso:
numero = 27
n = 3

resultado = raiz_n_esima(numero, n)
print(f"La {n}-ésima raíz de {numero} es {resultado}")
