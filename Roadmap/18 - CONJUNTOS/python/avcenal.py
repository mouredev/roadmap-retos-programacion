"""
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
"""

class MySet():
    def __init__(self,*elements): #el constructor debe comprobar que si le pasamos el mismo argumento solo lo añade una vez
        one_list = list(elements)
        if len(one_list) == 1:
            self.__custom_set = one_list.copy()
        else:
            for element in one_list:
                if one_list.count(element) > 1:
                    one_list.remove(element)
            self.__custom_set = one_list.copy()
        #self.__custom_set.append(element)

    def __to_list(self):
        return list(self.__custom_set)

    def add_last(self,element): #en cualquier método para añadir se ha de comprobar si el elemento existe o no en el conjunto
        for item in self.__custom_set:
            if item == element:
                break
        else:
            self.__custom_set.append(element)
        return self.__custom_set

    def add_first(self,element):
        for item in self.__custom_set:
            if item == element:
                break
        else:
            self.__custom_set = [element] + self.__custom_set
        return self.__custom_set
    
    def show_set(self):
        if len(self.__custom_set) == 0:
            print("El conjunto está vacío")
        else:
            print(self.__custom_set)

    def add_several_first(self,*elements): #lo mismo aquí, hay que comprobar que ningún elemento existe ya en el conjunto
        element_list = [*elements]
        for element in element_list:
            if element_list.count(element)>1:
                element_list.remove(element)
            elif element in self.__custom_set:
                element_list.remove(element)
        self.__custom_set = element_list + self.__custom_set
        return self.__custom_set
    
    def add_several_last(self,*elements):
        element_list = [*elements]
        for element in element_list:
            if element_list.count(element)>1:
                element_list.remove(element)
            elif element in self.__custom_set:
                element_list.remove(element)
        self.__custom_set = self.__custom_set + element_list
        return self.__custom_set
    
    def erase_element_at_position(self,position): #se ha de comprobar que el elemento existe en el conjunto
        try:                                      #y que no le pasamos un índice mayor que el máximo del conjunto
            del(self.__custom_set[position])
        except TypeError:
            print("Debes introducir un número entero como posición para borrar")
        except IndexError:
            print(f"Solo puedes elegir valores entre el 0 y {len(self.__custom_set)-1}")
        return self.__custom_set

    def update_value(self, position,value): #lo mismo que el método anterior
        try:
            self.__custom_set[position] = value
        except TypeError:
            print("Debes introducir un número entero como posición para actualizar el valor")
        except IndexError:
            print(f"Solo puedes elegir valores entre el 0 y {len(self.__custom_set)-1}")
        return self.__custom_set
    
    def check_element(self,element):
        try:
            self.__custom_set.index(element)
        except ValueError:
            print(f"El elemento {element} no está en el conjunto")
        else:
            print(f"El elemento {element} si está en el conjunto")

    def delete_set(self):
        return self.__custom_set.clear()
    
    def union (self,other_set): #se unen los dos conjuntos sin repetir elementos
        if type(other_set) != MySet:
            raise TypeError("El otro elemento no es un conjunto")
        else:
            my_new_set = MySet()
            other_set_list = my_other_set.__to_list()
            for element_a in self.__custom_set:
                for element_b in other_set_list:
                    if element_a == element_b:
                        other_set_list.remove(element_b)
                        break
                my_new_set.add_last(element_a)
            for element in other_set_list:
                my_new_set.add_last(element)
            return my_new_set
    
    def intersection (self,other_set): #nos da como resultado los elementos comunes a los conjuntos
        if type(other_set) != MySet:
            raise TypeError("El otro elemento no es un conjunto")
        else:
            my_new_set = MySet()
            other_set_list = my_other_set.__to_list()
            for element_a in self.__custom_set:
                for element_b in other_set_list:
                    if element_a == element_b:
                        my_new_set.add_last(element_a)
            return my_new_set
        
    def difference (self,other_set): #nos da como resultado los elementos que estan en el conjunto A pero no en el B
        if type(other_set) != MySet: #ha de funcionar A / B y B / A
            raise TypeError("El otro elemento no es un conjunto")
        else:
            my_new_set = MySet()
            temp_list = self.__custom_set.copy()
            other_set_list = other_set.__to_list()
            for element_a in self.__custom_set:
                for element_b in other_set_list:
                    if element_a == element_b:
                        temp_list.remove(element_a)
            for element in temp_list:
                my_new_set.add_last(element)
            return my_new_set
    
    def simmetric_difference(self,other_set): #nos da como resultado un conjunto que incluye las diferencias A/B y B/A
        if type(other_set) != MySet:
            raise TypeError("El otro elemento no es un conjunto")
        else:
            my_new_set = MySet()
            temp_list = self.__custom_set.copy()
            other_set_list = other_set.__to_list()
            for element_a in temp_list:
                for element_b in other_set_list:
                    if element_a == element_b:
                        temp_list.remove(element_a)
                        other_set_list.remove(element_b)
            for element in (temp_list + other_set_list):
                my_new_set.add_last(element)
            return my_new_set

    
my_set = MySet(3,"Alex","Alex","Alex") #se controla que no se guarden valores repetidos al crear el conjunto
my_set.show_set()
my_set.add_first("hola") #ni al añadir
my_set.add_first("hola")
my_set.show_set()
my_set.add_last(18.3)
my_set.add_last("Alex")
my_set.show_set()
my_set.add_several_first("que",5,"que","que")
my_set.show_set()
my_set.add_several_last("Cenalmor",11.3,"Cenalmor","Cenalmor")
my_set.show_set()
my_set.erase_element_at_position("a")
my_set.erase_element_at_position(0)
my_set.erase_element_at_position(7)
my_set.show_set()
my_set.update_value("a","hey")
my_set.update_value(5,"Valderrama")
my_set.update_value(9,"sssap")
my_set.show_set()
my_set.check_element("Alejandro")
my_set.check_element("Alex")
my_set.delete_set()
my_set.show_set()

"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""
my_set = MySet("Alex","Gonzalez",39)
my_other_set= MySet("Sole","Gonzalez",41)
print("\n")
print("CONJUNTOS")
my_set.show_set()
my_other_set.show_set()
print("\n")
print("UNION")
my_union_set = my_set.union(my_other_set)
my_union_set.show_set()
print("\n")
print("INTERSECCIÓN")
my_intersection_set = my_set.intersection(my_other_set)
my_intersection_set.show_set()
print("\n")
print("DIFERENCIAS")
my_difference_set = my_set.difference(my_other_set)
my_difference_set.show_set()
my_other_difference_set = my_other_set.difference(my_set)
my_other_difference_set.show_set()
print("\n")
print("DIFERENCIA SIMÉTRICA")
my_simmetric_diff_set = my_set.simmetric_difference(my_other_set)
my_simmetric_diff_set.show_set()
