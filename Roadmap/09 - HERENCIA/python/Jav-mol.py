# --- 09 HERENCIA Y POLIMORFISMO ---
# --- Javer Molina ---

# SuperClase
class Animal: 
    def __init__(self, name: str) -> None:
        self.name = name


# SubClases
class Gato(Animal):    
    def sonido(self):
        print('<MIAU>')
        
        
class Perro(Animal):
    def sonido(self):
        print('<GUAU>')
        
gato = Gato('gato')
gato.sonido()

perro = Perro('perro')
perro.sonido()

print()

# --- Dificultad Extra ---

class Empleado: #SuperClase
    def __init__(self,id: int, name: str, cargo: str) -> None:
        self.id = id
        self.name = name
        self.cargo = cargo
    
    def description():
        pass
    
    def __str__(self) -> str:
        return f'[Id: {self.id} - Nombre: {self.name} - Cargo: {self.cargo}]'


class Gerente(Empleado): #SubClase
    def __init__(self, id: int, name: str, cargo: str, empleados: list[Empleado]) -> None:
        super().__init__(id, name, cargo)
        self.empleados = [empleado.name for empleado in empleados]
        
    def description(self):
        return f'{self.cargo}: Tiene una jerarquia mas elevada, lidera los demas empleados'
    
    def empleados_a_cargo(self):
        return f'Empleados: {self.empleados}'
    
    
class GerenteDeProyecto(Empleado): #SubClase
    def __init__(self, id: int, name: str, cargo: str, empleados: list[Empleado]) -> None:
        super().__init__(id, name, cargo)
        self.empleados = [empleado.name for empleado in empleados]
    
    def description(self):
        return f'{self.cargo}: Tiene una jerarquia intermedia, lidera los proyectos bajo su cargo'

    def empleados_a_cargo(self):
        return f'Empleados a cargo: {self.empleados}'
    
    
class Programador(Empleado): #SubClase
    def __init__(self, id: int, name: str, cargo: str) -> None:
        super().__init__(id, name, cargo)

    def description(self):
        return f'{self.cargo}: Tiene una jerarquia baja, puede diriguir los demas programadores a su cargo'

    
desarrollador_1 = Programador(1,'Javi','Software Developer')
desarrollador_2 = Programador(2,'Camila','Software Developer')
desarrollador_3 = Programador(3,'Nico','Software Developer')
desarrollador_4 = Programador(4,'Sofia','Software Developer')

gerente_de_proyecto_1 = GerenteDeProyecto(
    id = 5,
    name = 'Pedro',
    cargo = 'Gerente de Proyecto', 
    empleados = [desarrollador_1,desarrollador_2]
)

gerente_de_proyecto_2 = GerenteDeProyecto(
    id = 6,
    name = 'Martin',
    cargo = 'Gerente de Proyecto', 
    empleados = [desarrollador_3,desarrollador_4]
)

gerente_1 = Gerente(
    id = 7,
    name = 'Alvaro',
    cargo = 'Gerente', 
    empleados = [gerente_de_proyecto_1,gerente_de_proyecto_2]
)

# Desarrolladores
print(desarrollador_1)
print(desarrollador_2.description())
print()

# Gerente De Proyectos
print(gerente_de_proyecto_1)
print(gerente_de_proyecto_1.description())
print(gerente_de_proyecto_1.empleados_a_cargo())
print()

# Gerente
print(gerente_1)
print(gerente_1.description())
print(gerente_1.empleados_a_cargo())
