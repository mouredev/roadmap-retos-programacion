###################################
# Dev: rianojnicolas              #
###################################

# 1. Asignacion de variables por valor y referencia

## 1.1 Variables por valor
##      Generalmente en python, los valores que se pueden asignar por valor son los tipos de datos primitivos
##      Por ejemplo: Int, float, string y booleanos
##      Se puede decir que se puede hacer una copia del valor de una variable
myIntA = 10
myIntB = myIntA
#myIntB = 20
myIntA = 50
print(myIntA)
print(myIntB)


## 1.2 Variables por referencia
##      Generalmente en python, los valores que se pueden asignar por referencia son los tipos de datos que no son primiticos
##      Por ejemplo: Listas, tuplas, diccionarios, set, etc
##      Se traduce a que estos valores por referencia heredan la posición de memoria, parece como si fueran los punteros de C++

my_setA = {10, 20}
#my_setB = {30, 40}
my_setB = my_setA
my_setB.add(30)
print(my_setA)
print(my_setB)


# 2. Ejemplos de funciones por valor y por referencia

## 2.1 Funciones con datos por valor

def fillCoupValue(fill):
    fill = 99
    print(fill)
    return fill

my_fill = 50
fillCoupValue(my_fill)
print(my_fill)

## 2.2 Funciones con datos por referencia
def fillCoupHistory(fill):
    fill.append(25)
    
    fill_a = fill
    fill_a.append(45)

    print(fill)
    print(fill_a)
    return fill

my_fill_history = [0, 10, 5, 50, 20]
fillCoupHistory(my_fill_history)
print(my_fill_history)

# Dificultad Extra
# Caso 1: Parametros por valor
def byValue(a, b):
    c = a
    a = b
    b = c
    return a, b


# Caso 2: Parametros por referencia
def byRefer(a, b):
    c = a
    a = b
    b = c
    return a, b


def run():
    # Caso 1: Parametros por valor
    my_val_1 = 10
    my_val_2 = 20
    print("Los valores inciales son: ")
    print(my_val_1)
    print(my_val_2)
    my_val_3, my_val_4 = byValue(my_val_1, my_val_2)
    print("Los valores retornados son: ")
    print(my_val_3)
    print(my_val_4)
    print("Los valores originales son: ")
    print(my_val_1)
    print(my_val_2)

    # Caso 2: Parametros por referencia
    my_ref_1 = [10, 30, 50]
    my_ref_2 = [20, 40, 60]
    print("Los valores inciales son: ")
    print(my_ref_1)
    print(my_ref_2)
    my_ref_3, my_ref_4 = byValue(my_ref_1, my_ref_2)
    print("Los valores retornados son: ")
    print(my_ref_3)
    print(my_ref_4)
    print("Los valores originales son: ")
    print(my_ref_1)
    print(my_ref_2)


if __name__ == '__main__':
    run()