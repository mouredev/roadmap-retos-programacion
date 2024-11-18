
"ejercicio"


class Pila:
    
    def __init__(self):
        self.var= []
        


    def añadir(self, elmento):
        self.var.append(elmento)
        print(f"Elemento añadido {elmento} a la lista")

    def eliminar(self):
        ele_list= self.var[len(self.var)-1]
        del self.var[len(self.var)-1]
        print(f"Elemento {ele_list} eliminadao de la lista")


    def ir_a(self,elemnto):
        
        ele_list= self.var.index(f"{elemnto}")
        
        print(f"estamos en el el elemento {ele_list} de la lista")

mi_pila=Pila()

mi_pila.añadir("A")
mi_pila.añadir("B")
mi_pila.añadir("C")
mi_pila.añadir("D")

mi_pila.ir_a("C")

mi_pila.eliminar()
mi_pila.eliminar()
mi_pila.eliminar()
mi_pila.eliminar()




class Cola:

    def __init__(self) :
        self.cola=[]

    def añadir(self,elmento):
        self.cola.append(elmento)
        print(f"Elemento {elmento}  añadidoa la lista")

    def eliminar(self):
        ele_list= self.cola[0]
        self.cola.pop(0)
        print(f"Elemento {ele_list} eliminadao de la lista")

    def contar(self):
        print(f"hay {len(self.cola)} elementos") 


mi_cola=Cola()

mi_cola.añadir("a")
mi_cola.añadir("b")
mi_cola.añadir("c")
mi_cola.añadir("d")
mi_cola.añadir("e")

mi_cola.contar()

mi_cola.eliminar()
mi_cola.eliminar()
mi_cola.eliminar()