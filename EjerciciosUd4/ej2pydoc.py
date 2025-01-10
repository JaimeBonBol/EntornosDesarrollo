class Empleado:
    """
    Clase que representa a un empleado dentro de una empresa.
    """
    def __init__(self, nombre, salario, puesto):
        """
        Inicializa los atributos básicos de un empleado.

        Args:
            nombre (str): Nombre del empleado.
            salario (float): Salario mensual del empleado.
            puesto (str): Puesto de trabajo del empleado.
        """
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto

    def obtener_nombre(self):
        """
        Retorna el nombre del empleado.

        Returns:
            str: Nombre del empleado.
        """
        return self.nombre

    def obtener_salario(self):
        """
        Retorna el salario del empleado.

        Returns:
            float: Salario mensual del empleado.
        """
        return self.salario

    def cambiar_puesto(self, nuevo_puesto):
        """
        Cambia el puesto del empleado.

        Args:
            nuevo_puesto (str): El nuevo puesto que el empleado ocupará.
        """
        self.puesto = nuevo_puesto

    def mostrar_informacion(self):
        """
        Muestra la información básica del empleado.

        Returns:
            str: Información del empleado.
        """
        return f"Empleado: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}"

    def aumento_salario(self, aumento):
        """
        Aumenta el salario del empleado.

        Args:
            aumento (float): El incremento en el salario del empleado.
        """
        self.salario += aumento


class Gerente(Empleado):
    """
    Clase que representa a un gerente, que es un tipo especializado de empleado.
    """
    def __init__(self, nombre, salario, puesto, departamento):
        """
        Inicializa los atributos de un gerente, incluyendo el departamento que supervisa.

        Args:
            nombre (str): Nombre del gerente.
            salario (float): Salario mensual del gerente.
            puesto (str): Puesto de trabajo del gerente.
            departamento (str): El departamento que el gerente supervisa.
        """
        super().__init__(nombre, salario, puesto)
        self.departamento = departamento
        self.empleados_bajo_cargo = []

    def obtener_departamento(self):
        """
        Retorna el departamento que supervisa el gerente.

        Returns:
            str: El departamento del gerente.
        """
        return self.departamento

    def agregar_empleado(self, empleado):
        """
        Agrega un empleado a la lista de empleados bajo su cargo.

        Args:
            empleado (Empleado): El empleado que será agregado.
        """
        if isinstance(empleado, Empleado):
            self.empleados_bajo_cargo.append(empleado)
        else:
            print("El objeto no es un empleado válido.")

    def mostrar_empleados(self):
        """
        Muestra los empleados bajo el cargo del gerente.

        Returns:
            str: Lista de empleados a cargo del gerente.
        """
        if self.empleados_bajo_cargo:
            return "\n".join([empleado.mostrar_informacion() for empleado in self.empleados_bajo_cargo])
        else:
            return "No hay empleados bajo su cargo."

    def mostrar_informacion(self):
        """
        Muestra la información básica del gerente, incluyendo su departamento.

        Returns:
            str: Información del gerente.
        """
        return f"Gerente: {self.nombre}, Puesto: {self.puesto}, Departamento: {self.departamento}, Salario: {self.salario}"


# Ejemplo de uso
empleado1 = Empleado("Juan Pérez", 2500, "Desarrollador")
empleado2 = Empleado("Ana Gómez", 2700, "Diseñadora")

gerente = Gerente("Carlos Ruiz", 5000, "Gerente de TI", "Tecnología")

# Agregar empleados al gerente
gerente.agregar_empleado(empleado1)
gerente.agregar_empleado(empleado2)

# Mostrar la información de empleados y gerente
print(empleado1.mostrar_informacion())
print(empleado2.mostrar_informacion())
print(gerente.mostrar_informacion())

# Mostrar los empleados bajo el cargo del gerente
print("\nEmpleados bajo el cargo de Carlos Ruiz:")
print(gerente.mostrar_empleados())

# Cambiar puesto y aumentar salario de un empleado
empleado1.cambiar_puesto("Líder de equipo")
empleado1.aumento_salario(500)

print("\nInformación actualizada de Juan Pérez:")
print(empleado1.mostrar_informacion())
