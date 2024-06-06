# Reto #09 Herencia

"""

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 """
 
 # Herencia de clases

""" En la hrencia de clases una nueva clase hereda todos las propiedades y méetodos de otra clase (Clase Base)"""

class Animal():
    def __init__(self,name:str,race:str) -> None:
        self.name = name
        self.race =race

    def sounds(self):
        print (f"El sonido del {self.animal}  es {self.sound}")   

class Dog(Animal):
    def __init__(self,name,race) -> None:
        super().__init__(name,race)             # Toma los parámetros y métodos de la superclase Animal
        self.animal="perro"
        self.sound="Guau"
        
class Cat(Animal):
    def __init__(self,name,race):
        super().__init__(name,race)              # Toma los parámetros y métodos de la superclase Animal
        self.animal= "gato"
        self.sound="Miau"
        

dog1 = Dog ("Oliver","Dobrman")    
dog2 = Dog ("León","Ovejero")
cat1 = Cat("Peluchin","Siames")
print (f"El perro {dog2.name} es de raza {dog2.race}")
print (f"El perro {dog1.name} es de raza {dog1.race}")
dog1.sounds()
print (f"El gato {cat1.name} es de raza {cat1.race}")
cat1.sounds()

print ("\n"*3)

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
print ("-"*100)
print ("Empresa X")


class Empleados():
    def __init__(self,fname,id:int) -> None:
        self.fname = fname
        self.id = id


class Gerente(Empleados):
    def __init__(self, fname,id,emp_a_cargo) -> None:
        super().__init__(fname,id)
        self.emp_a_cargo = emp_a_cargo
    
    def mostrar_id(self):
        print (f"El gerente {self.fname} tiene id {self.id}")
    
    def list_pers_a_cargo(self):
        print (f"El gerente {self.fname} tiene a cargo a :")
        for i in range (0,len(self.emp_a_cargo)):
            print (self.emp_a_cargo[i])


class GerenteProyectos(Empleados):
    def __init__(self, fname,id: int,proy_a_cargo) -> None:
        super().__init__( fname, id)
        self.proy_a_cargo = proy_a_cargo
    
    def mostrar_id(self):
        print (f"El gerente de proyectos {self.fname} tiene id {self.id}")

    def list_proy_a_cargo(self):
        print (f"El gerente de proyectos {self.fname} tiene a cargo los proyectos:")

        for i in range (0,len(self.proy_a_cargo)):
            print (self.proy_a_cargo[i])


class Programadores(Empleados):
    def __init__(self, fname, id: int,programas) -> None:
        super().__init__(fname, id)
        self.programas = programas

    def mostrar_id(self):
        print (f"El Programador {self.fname} tiene id {self.id}")
    
    def list_program(self):
        print (f"El Programador {self.fname} conoce los siguientes lenguajes:")

        for i in range (0,len(self.programas)):
            print (self.programas[i])
   

e1 = Empleados("María",1)
e2 = Empleados("José",2)
e3 = Empleados("Pedro",3)
e4 = Empleados("Roberto",4)
e5 = Empleados("Pepe",5)
e6 = Empleados("Javier",6)

g1 = Gerente (e1.fname,e1.id,[e2.fname,e3.fname,e4.fname])
g2 = GerenteProyectos(e4.fname,e4.id, ["P1","P2","P3"])
prog1 = Programadores( e6.fname,e6.id, ["Python","R","Javascript"])

g1.mostrar_id()
g1.list_pers_a_cargo()
prog1.mostrar_id()
prog1.list_program()
g2.mostrar_id()
g2.list_proy_a_cargo()







"""


def cargar_emp(list_emp):
    
    id= len(list_emp)
    while True:
        fname = input ("Ingrese nombre:")
        sname = input ("Ingrese apellido: ")
        age = input ("Ingrese edad: ")
        id +=1
        
        puesto = input ("Ingrese puesto: ")

        list_emp.append (Empleados(fname, sname,age,id,puesto))
        continuar_carga = input ("Desea seguir cargando empleados S/N: ")

        if continuar_carga == "S":
            continue
        else: 
            break
    return list_emp

def listar_empleados(list_emp):
    for i in range (0,int(len(list_emp))):
        x=(list_emp[i])
        print (f"{x.id} --- {x.fname} --- {x.puesto}")

list_emp=[]

def main():
    print ("-"*60)
    while True:
        print ("1.Empleados  !  2.Cargar !  3.Salir")

        accion = (input("Ingrese una opción: "))
        match accion:
            case "1":
                listar_empleados(list_emp)
            case "2":
                cargar_emp(list_emp)
            case "3":
                print("Saliendo del programa")
                break
            
            case _:
                print ("Ingrese una opción válida")


                 
   
    
if __name__ == "__main__":
    main()

"""




        
       


        

    