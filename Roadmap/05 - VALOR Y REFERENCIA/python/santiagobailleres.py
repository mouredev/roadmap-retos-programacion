'''EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.'''

# Asignación de variables por valor
a = 5 # Asignación por valor
b = a # Asignación por valor
a = 10 # Modificación de a
print(a) # a vale 10
print(b) # b sigue valiendo 5
b = 15 # Modificación de b
print(b) # b vale 15

# Asignación de variables por referencia
lista1 = [1, 2, 3] # Asignación por referencia
lista2 = lista1 # Asignación por referencia
lista2.append(4) # Modificación de lista2
print(lista1) # lista1 vale [1, 2, 3, 4]
print(lista2) # lista2 vale [1, 2, 3, 4]
lista1.append(5) # Modificación de lista1
print(lista1) # lista1 vale [1, 2, 3, 4, 5]
print(lista2) # lista2 vale [1, 2, 3, 4, 5]

# Funciones con variables por valor
def int_func(var_int:int):
    var_int = 10
    return var_int

c = 2
print(int_func(c)) # Imprime 10
print(c) # Imprime 2

# Funciones con variables por referencia
def list_func(var_list:list):
    var_list.append(4)
    lista = var_list
    lista.append(5)
    print(var_list) # Imprime [1, 2, 3, 4, 5]
    print(lista) # Imprime [1, 2, 3, 4, 5]

var_lista = [1, 2, 3]
list_func(var_lista)
print(var_lista) # Imprime [1, 2, 3, 4, 5]

# EXTRA
'''Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.'''

# Por valor
def value(value1:int, value2:int):
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2

value3 = 5
value4 = 10
value5, value6 = value(value3, value4)

print(f'{value3}, {value4}') # Imprime 5, 10
print(f'{value5}, {value6}') # Imprime 10, 5

# Por referencia
def reference(ref1:list, ref2:list):
    temp = ref1
    ref1 = ref2
    ref2 = temp
    return ref1, ref2

ref3 = [1, 2, 3]
ref4 = [4, 5, 6]
ref5, ref6 = reference(ref3, ref4)

print(f'{ref3}, {ref4}') # Imprime [1, 2, 3], [4, 5, 6]
print(f'{ref5}, {ref6}') # Imprime [4, 5, 6], [1, 2, 3]