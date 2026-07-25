"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 """

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def printSound(self):
        print(f"El animal llamado {self.name} hace {self.sound}")
        
    
class Perro(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        
        
class Gato(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        

# DIFICULTAD EXTRA
class Empresa:
    def __init__(self, name, year_creation, employees = []):
        self.name = name
        self.year_creation = year_creation
        self.employees = []
        if employees is not None:
            for e in employees:
                self.employees.append(e)
    
    def showEmployees(self):
        if len(self.employees):
            print("--------LISTA DE EMPLEADOS--------")
            print('\n'.join(str(f"- {e}") for e in self.employees))
        else:
            print(f"La empresa {self.name} no tiene empleados")

class Empleado:
    def __init__(self, oid, name, category):
        self.oid = oid
        self.name = name
        self.category = category
    
    def __str__(self):
        return f"El empleado {self.name} tiene la categoría de {self.category}"

class Gerente(Empleado):
    def __init__(self, oid, name, employees = []):
        super().__init__(oid, name, "Gerente")
        self.employees = []
        if employees is not None:
            for e in employees:
                self.employees.append(e)
    
    def showEmployees(self):
        if len(self.employees):
            print("--------LISTA DE EMPLEADOS--------")
            print('\n'.join(str(f"- {e}") for e in self.employees))
        else:
            print(f"El empleado {self.name} no tiene empleados a su cargo")

class GetenteProyectos(Empleado):
    def __init__(self, oid, name, proyectos = []):
        super().__init__(oid, name, "Gerente de proyectos")
        self.proyectos = []
        if proyectos is not None:
            for p in proyectos:
                self.proyectos.append(p)
    
    def showProyects(self):
        print(f"El empleado {self.name} tiene los siguientes proyectos a su cargo:")
        print(self.proyectos)


class Programador(Empleado):
    def __init__(self, oid, name, len_prog):
        super().__init__(oid, name, "Programador")
        self.leng_prog = len_prog
    
    def coding(self):
        print(f"El empleado {super().name} ha empezado a picar código en {self.leng_prog}")
        

if __name__ == "__main__":

    print("----------------------CLASE----------------------------")
    miPerro = Perro("Kala", "guau")
    miGato = Gato("Michi", "miau")
    
    miPerro.printSound()
    miGato.printSound()
    
    # DIFICULTAD EXTRA
    developers = [GetenteProyectos(3, "Lucia Domingo Anaya", ["ERP", "Pagina Web"]), Programador(2, "Mario Garcia Arnaiz", "c#"), Programador(4, "Ana Gonzalez Diez", "python")]
    all_employees = [Gerente(1, "Juan Lopez Ramirez", developers)]
    all_employees.extend(developers)
    miEMpresa = Empresa("PEPITO S.L.", 2019, all_employees)
    miEMpresa.showEmployees()
    print(all_employees[0].showEmployees())
    print(all_employees[1].showProyects())

