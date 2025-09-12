"""EJERCICIO
"""
class Animal():
    """Clase para establecer características comunes
    de los animales en este ejercicio
    """
    def __init__(self, paws, condition):
        self.paws = paws
        self.condition = condition

    def __str__(self):
        return f"Este animal tiene {self.paws} patas, es {self.condition}"

class Perro(Animal):
    """Clase que establece alguna característica particular
    de un perro

    Args:
        Animal (class): clase padre
    """
    def sound(self):
        """Método que indica qué sonido hace el perro
        """
        return "Guau"

    def __str__(self):
        return f"{super().__str__()} y el sonido que hace es '{self.sound()}'"

class Gato(Animal):
    """Clase que establece alguna característica particular
    de un gato

    Args:
        Animal (class): clase padre
    """
    def sound(self):
        """Método que indica qué sonido hace el perro
        """
        return "Miau"

    def __str__(self):
        return f"{super().__str__()} y el sonido que hace es '{self.sound()}'"

# --------------- COMPROBACIONES DEL EJERCICIO --------------

pia = Perro(4, "doméstico")
rufus = Gato(4, "salvaje")

print(pia)
print(rufus)

# --------------------- DIFICULTAD EXTRA --------------------
class Employee():
    """Clase que establece los datos comunes de todos los
    empleados de la empresa
    """
    def __init__(self, name, identify):
        self.name = name
        self.id = identify

    total = int()
    organigram = {"Gerente": [], "Gerente de Proyecto": [], "Desarrollador": []}

    """Vamos a ver cómo integramos un método para conocer la cantidad de
    empleados que hay en la empresa"""
    @classmethod
    def add_employee(cls, name, category):
        """Método de clase para añadir el empleado a la empresa cuando se crea
        la instancia
        """
        cls.total += 1
        cls.organigram[category].append(name)

    @classmethod
    def functions(cls, t):
        """Método para mostrar las funciones del empleado

        Args:
            t (tuple): tupla con todas las funciones que realiza el empleado
        """
        for item in t:
            print(f"- {item}")

    @classmethod
    def advntg(cls, pros):
        """Método (propiedad) que muestra los pros de esta categoría
        """
        for key, value in pros.items():
            print(f"- {key}: {value}")

class Manager(Employee):
    """Clase que establece las propiedades y características de los 
    gerentes de la empresa

    Args:
        Employee (class): clase padre
    """
    def __init__(self, name, identify):
        self.category = "Gerente"
        super().__init__(name, identify)
        Employee.add_employee(name, self.category)

    dicc = {"Salario": 3000, "Coche de empresa": "Sí", "Dietas": "Sí", "Pagas": 14,
            "Dividendos": "Sí", "Vacaciones": 28, "Asuntos propios": 10}
    tpl = ("Organizar y planificar", "Controlar plazos", "Estimular la productividad",
           "Ser un líder", "Motivar a su grupo de trabajo", "Resolución de problemas")

    @classmethod
    def pros(cls):
        """Método (propiedad) que muestra los pros de esta categoría
        
        Returns:
            Las ventajas línea a línea
        """
        super().advntg(cls.dicc)

    @classmethod
    def function(cls):
        """Método que muestra las funciones del gerente

        Returns:
            Las funciones línea a línea
        """
        super().functions(cls.tpl)

    @classmethod
    def components(cls):
        """Método de clase para saber los empleados de esta categoría
        """
        print("\nGERENTES:")
        for i in range(len(Employee.organigram["Gerente"])):
            print(f"- {Employee.organigram["Gerente"][i]}")

class ProjectManager(Employee):
    """Clase que establece las propiedades y características de los 
    Gerentes de proyectos de la empresa

    Args:
        Employee (class): clase padre
    """
    def __init__(self, name, identify):
        self.category = "Gerente de Proyecto"
        super().__init__(name, identify)
        Employee.add_employee(name, self.category)

    dicc = {"Salario": 2200, "Coche de empresa": "No", "Dietas": "Sí", "Pagas": 14,
            "Dividendos": "No", "Vacaciones": 26, "Asuntos propios": 8}
    tpl = ("Realizar estudios de mercado", "Controlar plazos y calidades", "Estimar recursos",
           "Establecer plan de progreso", "Gestión de proveedores",
           "Monitorizar el progreso del proyecto")

    @classmethod
    def pros(cls):
        """Método (propiedad) que muestra los pros de esta categoría
        
        Returns:
            Las ventajas línea a línea
        """
        super().advntg(cls.dicc)

    @classmethod
    def function(cls):
        """Método que muestra las funciones del gerente

        Returns:
            Las funciones línea a línea
        """
        super().functions(cls.tpl)

    @classmethod
    def components(cls):
        """Método de clase para saber los empleados de esta categoría
        """
        print("\nGERENTES DE PROYECTO:")
        for i in range(len(Employee.organigram["Gerente de Proyecto"])):
            print(f"- {Employee.organigram["Gerente de Proyecto"][i]}")

class Developer(Employee):
    """Clase que establece las propiedades y características de los 
    Desarrolladores

    Args:
        Employee (class): clase padre
    """
    def __init__(self, name, identify):
        self.category = "Desarrollador"
        super().__init__(name, identify)
        Employee.add_employee(name, self.category)

    dicc = {"Salario": 1700, "Coche de empresa": "No", "Dietas": "No", "Pagas": 14,
            "Dividendos": "No", "Vacaciones": 24, "Asuntos propios": 8}
    tpl = ("Crear programas y sistemas eficientes", "Reparar o mejorar software existente",
           "Realizar pruebas", "Códigos eficientes y escalables", "Trabajar de forma colaborativa")

    @classmethod
    def pros(cls):
        """Método (propiedad) que muestra los pros de esta categoría
        
        Returns:
            Las ventajas línea a línea
        """
        super().advntg(cls.dicc)

    @classmethod
    def function(cls):
        """Método que muestra las funciones del gerente

        Returns:
            Las funciones línea a línea
        """
        super().functions(cls.tpl)

    @classmethod
    def components(cls):
        """Método de clase para saber los empleados de esta categoría
        """
        print("\nGERENTES DE PROYECTO:")
        for i in range(len(Employee.organigram["Desarrollador"])):
            print(f"- {Employee.organigram["Desarrollador"][i]}")

# -------------- COMPROBACIONES DIFICULTAD EXTRA -------------

emp1 = Manager("Raúl", "001")
emp2 = ProjectManager("Malena", "002")
emp3 = ProjectManager("Jose", "003")
emp4 = ProjectManager("Miriam", "004")
emp5 = Developer("Mario", "005")
emp6 = Developer("Rita", "006")
emp7 = Developer("Emilio", "007")
emp8 = Developer("Macarena", "008")
print(f"\nTOTAL DE EMPLEADOS: {Employee.total}")

# Gerente
Manager.components()
print("\nFUNCIONES:")
Manager.function()
print("\nCONDICIONES:")
Manager.pros()
print()

# Gerentes de Proyecto
ProjectManager.components()
print("\nFUNCIONES:")
ProjectManager.function()
print("\nCONDICIONES:")
ProjectManager.pros()
print()

# Desarrolladores
Developer.components()
print("\nFUNCIONES:")
Developer.function()
print("\nCONDICIONES:")
Developer.pros()
print()
