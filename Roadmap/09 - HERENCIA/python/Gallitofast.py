"""Herencia y polimorfismo"""
'''Heredacion de metodos, atributos, etc.'''
class Animal:
    def __init__(self,name: str):
        self.name = name 
    def sound(self):
        pass
    
class Dog(Animal):
    
    def sound(self):
        print("WOOF WOOF")
 

class Cat(Animal):
        def sound(self):
            print("MIAW MIAW")
 

perrito= Dog("Panchito")
perrito.sound()
gatito= Cat("Alpaccino")
gatito.sound()


class Employee():
     def __init__(self,name,id:int)-> None:
          self.name = name
          self.id = id 

class Manager(Employee):
     def __init__(self,name,id:int,designations)-> None:
          self.name = name
          self.id = id
          self.designations = designations
     def show_id(self):
        print (f"The manager {self.name} has this id {self.id}")
    
     def list_designations(self):
        print (f"The manager {self.name} has in charge :")
        for i in range (0,len(self.designations)):
            print (self.designations[i])

class Project_Manager(Employee):
     def __init__(self,name,id:int,project_designations) -> None:
          self.name= name
          self.id= id
          self.project_designations = project_designations
     def show_id(self):
        print (f"The project manager {self.name} has this id {self.id}")
     def list_projects(self):
         print (f"The manager {self.name} has in charge the following projects:")

         for i in range (0,len(self.project_designations)):
             print (self.project_designations[i])

class Programmer(Employee):
     def __init__(self, name, id: int,programs) -> None:
        super().__init__(name, id)
        self.programs = programs

     def show_id(self):
        print (f"The programmer {self.name} has this id {self.id}")
    
     def list_program(self):
        print (f"This programmer {self.name} knows the following languages:")

        for i in range (0,len(self.programs)):
            print (self.programs[i])


e1 = Employee("María",1)
e2 = Employee("José",2)
e3 = Employee("Pedro",3)
e4 = Employee("Roberto",4)
e5 = Employee("Pepe",5)
e6 = Employee("Javier",6)

g1 = Manager (e1.name,e1.id,[e2.name,e3.name,e4.name])
g2 = Project_Manager(e4.name,e4.id, ["P1","P2","P3"])
prog1 = Programmer( e6.name, e6.id, ["Python","R","Javascript"])

g1.show_id()
g1.list_designations()
prog1.show_id()
prog1.list_program()
g2.show_id()
g2.list_projects()