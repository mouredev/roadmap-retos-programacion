class animal:
    def caminar(self):
        print('camino en 4 patas')

class perro(animal):
    def sonido(self):
        print('hago guau guau')

class gato(animal):
    def sonido(self):
        print('hago miau')

#tobias = perro()
#tobias.caminar()
#tobias.sonido()

#matias = gato()
#matias.sonido()

### Dificultad Extra ###
        
class empleado:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class gerente(empleado):
    region = 'latam'
    salario = '15000 USD'

    def __init__(self, id, name) -> None:
        super().__init__(id, name)
        self.empleadosACargoGerente = []

    def firmar(self):
        print('Firmo los cheques del pago de los empleados')

    def nuevoEmpleadosCargo(self, nombre):
        self.empleadosACargoGerente.append(nombre)

class gerenteDeProyecto(empleado):
    region = 'Argentina'

    def __init__(self, id, name) -> None:
        super().__init__(id, name)
        self.empleadosACargoGerenteDeProyectos = []

    def gant(self):
        print('se hacer diagramas de gant')

    def nuevoEmpleadosCargo(self, nombre):
        self.empleadosACargoGerenteDeProyectos.append(nombre)

class programador(empleado):
    region = 'Colombia'
    def __init__(self, id, name, lenguage) -> None:
        super().__init__(id, name)
        self.lenguage = lenguage

    def programar(self):
        print(f'programo en {self.lenguage}')

jefe = gerente('1', 'Christian H')
print(f'El salario de {jefe.name} es {jefe.salario}')

segundo = gerenteDeProyecto('2','Joe V')
driver = programador('3','Max V','Python')

jefe.nuevoEmpleadosCargo('Joe V')
jefe.nuevoEmpleadosCargo('Max V')
segundo.nuevoEmpleadosCargo('Max V')

print(f'Los empleados a cargo de {jefe.name} son {jefe.empleadosACargoGerente[0]} y {jefe.empleadosACargoGerente[1]} ')




