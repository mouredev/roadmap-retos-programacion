# /*
#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  * 
#  */

class Pila_o_Cola:
    def __init__(self,init_value = None) -> None:
        if init_value == None:
            init_value = []
        self.__list_value = init_value

    def add(self):
        print(" A rellenar , entra un elemento : ")
        item = input()
        self.__list_value.append(item)

    def is_empty(self):
        return self.__list_value == []

    def items_count(self):
        if not self.is_empty():
            print(f"There are  {len(self.__list_value)} Items ")
            return  
        print("eEmpty List... Add first")
    
    def print_items(self):
        if not self.is_empty():
            print(" Mostrando elementos ... : ")
            print(self.__list_value)
            return
        print("eEmpty List... Add first")


    def delete_one_value(self, index=None):
        if not self.is_empty():
            if index == None :
                index = len (self.__list_value)-1
            return self.__list_value.pop(index)
        
        


class Pila(Pila_o_Cola):
    
    def delete_lifo(self):
        if not super().is_empty():
            print(" Deleting  LIFO  ... : ")
            print(f"Item {self.delete_one_value()} deleted succesfully ")
            return
        print("Empty List... Add first")
    
    
class Cola(Pila_o_Cola):
     
    def delete_fifo(self):
        if not super().is_empty():
            print(" Deleting  FIFO  ... : ")
            print(f"Item {self.delete_one_value(0)} deleted succesfully ")
            return
        print("Empty List... Add first")


pila = Pila()
cola = Cola()
poc = ""
while True:
    print("PIla (P)  o  COLA (C)  Quit (Q) ?")
    pc = input()
    if pc == "P":
        poc = "Pila"
    elif pc == "C":
            poc = "Cola"
    elif pc == "Q":
        break
    else :
        print("Enter only P, C or Q")
        continue

    while True:
    
        print(f" What do you want to do with {poc} : ")
        print("1 - ) ADD")
        print("2 - ) PRINT")
        print("3 - ) How many Items are there")
        print("4 - ) REMOVE")
        print("5 - ) EXIT")
        op = input()
        match op:
            case "1":
                
                pila.add() if pc == "P" else cola.add()
            case "2":
                pila.print_items()   if pc == "P" else cola.print_items()
            case "3":
                pila.items_count()  if pc == "P" else cola.items_count()
            case "4":
                pila.delete_lifo()  if pc == "P" else cola.delete_fifo()
            case "5":
                print("EXIT now.. ... ")
                break
            case _:
                print("Enter number between 1 and 5 , try again")         
                

    


    
    
    



