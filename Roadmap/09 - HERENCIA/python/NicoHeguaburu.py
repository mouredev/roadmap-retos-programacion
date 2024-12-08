# Herencia


class Animal:

    def __init__(self, name: str):
        self.name = name
        
    def sound(self):
        pass
    


class Dog(Animal):

    def sound(self):
        print("Guau!")

class Cat(Animal):

    def sound(self):
        print("Miau!")


def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal("Animal")
my_animal.sound()

my_dog = Dog("Dog")
my_dog.sound()

my_cat = Cat("Cat")
my_cat.sound()


print_sound(my_cat)




#Dificultad Extra
planilla = []

class Empleado:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.id = len(planilla) + 1
        self.puesto = self.definir_puesto()
        perfil_empleado = {}
        perfil_empleado["Nombre"] = nombre
        perfil_empleado["ID"] = self.id
        perfil_empleado["Puesto"] = self.puesto
        planilla.append(perfil_empleado)
    
class Gerente(Empleado):
    def definir_puesto(self):
        return "Gerente"
    
    def desarolladores_a_cargo(self):
        desarolladores = []
        for i in planilla:
            if i["Puesto"] == "Desarollador":
                desarolladores.append(i["Nombre"])
        print(desarolladores)
        
        
    def pms_a_cargo(self):
        pms = []
        for i in planilla:
            if i["Puesto"] == "PM":
                pms.append(i["Nombre"])
        print(pms)
        

    
class Pm(Empleado):
    def definir_puesto(self):
        return "PM"
    
    def desarolladores_a_cargo(self):
        desarolladores = []
        for i in planilla:
            if i["Puesto"] == "Desarollador":
                desarolladores.append(i["Nombre"])
        print(desarolladores)


class Desarollador(Empleado):
    def definir_puesto(self):
        return "Desarollador"


empleado1 = Gerente("Jorge")
empleado2 = Pm("Nicolás")
empleado3 = Desarollador("Sofia")
empleado4 = Gerente("Matias")
empleado5 = Pm("Lorenzo")
empleado6 = Desarollador("Julio")
empleado7 = Gerente("Marcos")
empleado8 = Pm("Maria")
empleado9 = Desarollador("Sebastian")





print(planilla)

empleado1.desarolladores_a_cargo()
empleado1.pms_a_cargo()
empleado2.desarolladores_a_cargo()