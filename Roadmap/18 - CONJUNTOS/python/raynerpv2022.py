# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):

class MyConjunto:
    def __init__(self, conjunto=[]) -> None:
        self.conjunto = conjunto

#  * - Añade un elemento al final.
    def insert_at_end(self, items):
        self.conjunto.append(items)
         
    #  * - Añade un elemento al principio.
    def  insert_at_start(self, items):
        self.conjunto.insert(0,items)
         
    #  * - Añade varios elementos en bloque al final.
    def bloque_At_end(self, bloque):
        self.conjunto.extend(bloque)
         

    #  * - Añade varios elementos en bloque en una posición concreta.
    def insertBloque(self,pos, bloque):
        self.conjunto[pos:pos] = bloque
         

    #  * - Elimina un elemento en una posición concreta.
    def delete_at_index(self, index):
        
         print(f"se elimino el items {self.conjunto.pop(index)}")

    #  * - Actualiza el valor de un elemento en una posición concreta.
    def update_at_index(self, index, new_value):
            self.conjunto[index] = new_value

    #  * - Comprueba si un elemento está en un conjunto.
    def chek_value(self, items):
         print(f"Elemento {items} esta en {self.conjunto}? : {items in self.conjunto}")
        
              
     
    #  * - Elimina todo el contenido del conjunto.
    def remove_data(self):
         self.conjunto.clear()

    def print_data(self):
         print(self.conjunto)


conjunto = MyConjunto()
conjunto.print_data()
conjunto.insert_at_end(4)
conjunto.print_data()
conjunto.bloque_At_end([1,2,3,4,5,6])
conjunto.print_data()
conjunto.insert_at_start(0)
conjunto.print_data()
conjunto.insertBloque(3,[99,98,97])
conjunto.print_data()
conjunto.update_at_index(0,100)
conjunto.print_data()
conjunto.delete_at_index(4)
conjunto.print_data()
conjunto.chek_value(100)
conjunto.print_data()
conjunto.chek_value(123)
conjunto.print_data()
conjunto.print_data()
conjunto.remove_data()
conjunto.print_data()
                


    #  *






#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.
#  */

set1 = {2,4,6,8,10}
set2 = {1,2,3,4,5,7,9}

 
print(f"UNION {set1.union(set2)}")
print(f"INTERSECCION {set1.intersection(set2)}")
print(f"Diferencia {set1.difference(set2)}")
print(f"Diferencia {set2.difference(set1)}")
print(f"Diferencia Simetrica {set1.symmetric_difference(set2)}")

# usando lista
s1 = [2,4,6,8,10]
s2 = [1,2,3,4,5,7,9]

# Union

print("UNION", set(s1+s2))

