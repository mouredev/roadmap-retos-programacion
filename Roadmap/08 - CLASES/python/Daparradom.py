### 08-CLASES ###

class animal :
    def __init__(self,name : str ,grupo : str):  
        self.name = name
        self.grupo = grupo 

    def presentacion (self) :
        print(f"Mi animal es un {self.name} y es un {self.grupo}")



my_animal = animal("Leon", "Mamifero")

my_animal.presentacion()

my_second_animal = animal ("Sapo" , "Anfibio")

my_second_animal.presentacion()


class cola :
    def __init__(self):
        self.elementos = []
    
    def vacio (self) :
        if len(self.elementos) == 0 :
            return True
        else:
            return False
    def añadir (self, elemento) :
        self.elementos.append(elemento)
    def eliminar (self) :
        if self.vacio() == False :
            self.elementos.pop(0)
        else:
            print("El conjunto de elementos de la cola esta vacio")
    def show (self) :
        for item in self.elementos:
            print(item)

mi_cola = cola()

mi_cola.añadir("Hola")
mi_cola.añadir("python")
mi_cola.añadir("te saluda")
mi_cola.añadir("David")

mi_cola.show()

mi_cola.eliminar()

mi_cola.show()

mi_cola.eliminar()

mi_cola.show()


print("*******************************************\n")
class pila :
    def __init__(self):
        self.elementos = []
    
    def vacio (self) :
        if len(self.elementos) == 0 :
            return True
        else:
            return False
    def añadir (self, elemento) :
        self.elementos.append(elemento)
    def eliminar (self) :
        if self.vacio() == False :
            self.elementos.pop()
        else:
            print("El conjunto de elementos de la pila esta vacio")
    def show (self) :
        for item in reversed(self.elementos):
            print(item)


mi_pila = pila()

mi_pila.añadir("Hola")
mi_pila.añadir("python")
mi_pila.añadir("te saluda")
mi_pila.añadir("David")

mi_pila.show()

mi_pila.eliminar()

mi_pila.show()

mi_pila.eliminar()

mi_pila.show()