
# Asignación por valor: 
# Se copia el valor directamente. 
# Esto ocurre con tipos de datos inmutables como números, cadenas y tuplas. 
# Cambiar el valor de una variable no afecta a las demás.

# Ejemplo
a = 10
b = a  # a y b son independientes
b = 20
print(a)  # a sigue siendo 10


# Asignación por referencia: 
# Se comparte la referencia al objeto en la memoria. 
# Esto sucede con tipos de datos mutables como listas y diccionarios. 
# Modificar un objeto afecta a todas las variables que hacen referencia a él.

#Ejemplo
list_1 = [1, 2, 3]
list_2 = list_1  # list_2 apunta al mismo objeto que list_1
list_2.append(4)
print(list_1)  # list_1 se ve afectada, [1, 2, 3, 4]

# En resumen: 
# Con asignación por valor, cada variable tiene su propio valor independiente. 
# Con asignación por referencia, varias variables pueden apuntar al mismo objeto mutable en la memoria.


# * DIFICULTAD EXTRA (opcional):
# * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
# *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
# *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
# *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
# *   Comprueba también que se ha conservado el valor original en las primeras.

def exchange_values(value_1, value_2):
    tmp = value_1
    value_1 = value_2
    value_2 = tmp
    return value_1, value_2

# Ejemplo de uso
original_value_1 = 'Hola'
original_value_2 = 'Mundo'

new_value_1, new_value_2 = exchange_values(original_value_1, original_value_2)

print(f"Original Values: {original_value_1}, {original_value_2}") # ---> Original Values: Hola, Mundo
print(f"New Values: {new_value_1}, {new_value_2}") # ---> New Values: Mundo, Hola


def exchange_references(list_1, list_2):
    list_1[0], list_2[0] = list_2[0], list_1[0]
    return list_1, list_2

# Ejemplo de uso
original_list_1 = ['Hola']
original_list_2 = ['Python']

new_list_1, new_list_2 = exchange_references(original_list_1, original_list_2)

print(f"Original Lists: [{original_list_1[0]}], [{original_list_2[0]}]") # ---> Original Lists: [Python], [Hola]
print(f"New Lists: [{new_list_1[0]}], [{new_list_2[0]}]")  # ---> New Lists: [Python], [Hola]
