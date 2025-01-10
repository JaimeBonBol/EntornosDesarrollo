import algebra
import geometria

"""
Este es el programa principal donde se importan los módulos algebra y geometria.
Se calculan el área de un círculo y la suma de dos números dentro de la función 'main()'.
"""

def main():
    """
    Función principal donde se realizan los cálculos.
    - Cálculo del área de un círculo con radio 10.
    - Cálculo de la suma de dos números.
    """
    
    # Cálculo del área de un círculo con radio 10 utilizando la función 'area_circulo' del módulo 'geometria'
    areaCirculo = geometria.area_circulo(10)
    print(f"Área del círculo con radio 10: {areaCirculo}")

    # Cálculo de la suma de dos números (8 y 2) utilizando la función 'suma' del módulo 'algebra'
    sumaNumeros = algebra.suma(8, 2)
    print(f"Suma de 8 y 2: {sumaNumeros}")

# Este bloque asegura que la función main() solo se ejecute cuando el script sea ejecutado directamente
if __name__ == "__main__":
    main()
