class Animal:
    def __init__ (self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        print(self.nombre + "hace ruido...")
        
class Perro(Animal):
    def sonido(self):
        print("El perro de nombre " + self.nombre + " ladra haciendo 'Guau, guau'...")
        
class Gato(Animal):
    def sonido(self):
        print("El gato de nombre " + self.nombre + " maulla haciendo 'Miau, miau'...")
        
perro = Perro("Milu")
perro.sonido()

gato = Gato("Garfield")
gato.sonido()

class Empleado():
    def __init__(self, id ,nombre):
        self.id = id
        self.nombre = nombre        
        
class Gerente(Empleado):
    def __init__(self, id, nombre, personas_a_cargo):
        super().__init__(id, nombre)
        self.personal = personas_a_cargo
    
    def mostrar(self):
        print("Gerente: ", self.nombre, " con ", self.personal, " personas a cargo")
        
    def convocar(self):
        print("Reunión con el personal")
        for a in self.personal:
            print(a)

class GerenteP(Empleado):
    def __init__(self, id, nombre, personas_a_cargo):
        super().__init__(id, nombre)
        self.personal = personas_a_cargo
    
    def mostrar(self):
        print("Gerente: ", self.nombre, " con ", self.personal, " programadores a cargo")
        
    def convocar(self):
        print("Reunión con el programador")
        for a in self.personal:
            print(a)
class Programador(Empleado):
    def __init__(self, id, nombre, lenguajes):
        super().__init__(id, nombre)
        self.lenguajes = lenguajes
    
    def mostrar(self):
        print("Programador: ", self.nombre, " maneja los lenguajes ", self.lenguajes)
        
    def programar(self):
        print(self.nombre + " programara hoy en: ")
        for a in self.lenguajes:
            print(a)

gerente1 = Gerente(1, "Juan", ["Pedro", "Luis", "Ana"])
gerente1.mostrar()
gerente1.convocar()

gerente2 = Gerente(2, "Migue", ["Jose", "Rafa", "Maria"])
gerente2.mostrar()
gerente2.convocar()    

jefe1 = GerenteP(3, "Pedro", ["Alberto", "Pepa", "Josefa"])   
jefe1.mostrar()
jefe1.convocar()

jefe2 = GerenteP(4, "Luis", ["Rafael", "Miguel", "María"])
jefe2.mostrar()
jefe2.convocar()

programador1 = Programador(5, "Alberto", ["Python", "Java", "C++"]) 
programador2 = Programador(6, "Pepa", ["Pascal", "Javascript", "C", "Python"])

programador1.mostrar()
programador1.programar()

programador2.mostrar()
programador2.programar()

            