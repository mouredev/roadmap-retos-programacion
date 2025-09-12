class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("General Animal")
    def get_name(self):
        return self.name    
class Perro(Animal):
    def sound(self):
        print("Guau")
class Gato(Animal):
    def sound(self):
        print("Miau") 

my_gato = Gato("Misifu")
my_gato.sound()   
print(my_gato.get_name())                
my_perro = Perro("Luna")
my_perro.sound()
print(my_perro.get_name())

#Extra exercise

class Empleado:
    def __init__(self,id,full_name):
        self.id = id
        self.full_name = full_name
    def get_id(self):
        return self.id
    def get_name(self):
        return self.full_name

class Gerente(Empleado):
    subordinates = []
    def addSubordinate(self,empleado:Empleado):
        self.subordinates.append(empleado)
    def get_subordinates(self):
        for item in self.subordinates:
            print(item.get_name())

class GerenteProyecto(Empleado): 
    projects = []
    def addProject(self,project_name):
        self.projects.append(project_name)
    def deleteProject(self,project_name):
        self.projects.remove(project_name)
    def get_projects(self):
        return self.projects        

class Programador(Empleado):

    def drink_cofee(self):
        print("Drinking cofee")
    def code(self):
        print("Coding in python")            

boos = Gerente(1,"Raul Garcia")
project_manager = GerenteProyecto(2,"Juan Perez")
boos.addSubordinate(project_manager)
project_manager.addProject("App1")
project_manager.addProject("App2")
project_manager.addProject("App 3")
project_manager.deleteProject("App 3")
programador1 = Programador(3,"Mike smith")
programador1.code()
boos.addSubordinate(programador1)
programador2 = Programador(4,"Maria aguilera")
programador2.code()
boos.addSubordinate(programador2)
print(boos.get_name()+" 's subordinates ")
boos.get_subordinates()
print("Projects for "+project_manager.get_name())
print(project_manager.get_projects())