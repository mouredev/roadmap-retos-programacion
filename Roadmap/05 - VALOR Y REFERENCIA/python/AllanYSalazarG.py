""" #05 VALOR Y REFERENCIA """

# Modulos importados
""" import copy

# ---------- Asignación de variable por valor ----------

print("---------- Asignación de variables por valor ----------")
string = "Hola"
anotherString = string
anotherString = "mundo"
number = 1
anotherNumber = number
anotherNumber = 2
floatNumber = 1.5
anotherFloatNumber = floatNumber
anotherFloatNumber = 3.4
print(string, anotherString, anotherNumber, anotherFloatNumber)

# Cuando se asigna por valor, pasa que en caso de anotherString = string,
# anotherString guarda una copia de string, por lo que si modificamos anotherString,
# string no se ve afectada.
# Esto aplica para los numeros (enteros y flotantes), caracteres, cadenas y tuplas.

# ---------- Asignación de variable por referencia ----------

print("---------- Asignación de variables por referencia ----------")
aList = [1, 2, 3]
anotherList = aList
anotherList.append(4)
aDicc = {"id": 1,
         "Name": "Allan",
         "LastName": "Salazar"}
anotherDicc = aDicc
# Con update tambien podemos agregar claves y valores al diccionario
anotherDicc["age"] = 29
newSet = {1, 2, 3, 4, 5, 6}
anotherSet = newSet
anotherSet.add(7)
print(aList, anotherList, aDicc, anotherDicc, newSet, anotherSet)

# Las listas, diccionarios y conjuntos (sets) se asignan por referencia
# pasa que la nueva variable hace referencia a la anterior.
# Por ejemplo, en anotherList = aList, significa que podemos acceder al mismo espacio
# de memoria tanto como anotherList como con aList, por lo que se ve reflejado
# el cambio en ambas variables

# ---------- Copia de variables por referencia ----------

# Si queremos hacer que los datos de listas, diccionaros y conjuntos no se cambien,
# o que funcionen como las variables asignadas por valor, necesitamos
# el metodo copy o importar el modulo copy (al inicio del doc)

# Usando el metodo copy

print("---------- Copiando variables asignadas por referencia ----------")
print("---------- Usando el metodo copy() ----------")
newList = [7, 8, 9, 10]
anotherNewList = newList.copy()
anotherNewList.append(11)
print(newList, anotherNewList)

# Usando el modulo copy

print("---------- Usando el modulo copy y su metodo deepcopy() ----------")
newList = [[1, 2], [3, 4]]
anotherNewList = copy.deepcopy(newList)
anotherNewList.append([5, 6])
print(newList, anotherNewList) """

# ---------- EJERCICIO ----------


print("---------- EJERCICIO ----------")

firstParamValue = 1
secondParamValue = "hola"
firstParamReference = [1, 2, 3]
secondParamReference = {4, 5, 6}

print(firstParamValue, secondParamValue)
print(firstParamReference, secondParamReference)


def functionPerValue(firstParamValue, secondParamValue):
    tempVar = firstParamValue
    firstParamValue = secondParamValue
    secondParamValue = tempVar
    return firstParamValue, secondParamValue


def functionPerReference(firstParamReference, secondParamReference):
    firstParamReference = secondParamReference
    secondParamReference = firstParamReference
    return firstParamReference, secondParamReference


newFirstParamValue, newSecondParamValue = functionPerValue(firstParamValue,
                                                           secondParamValue)
newFirstParamReference, newSecondParamReference = functionPerReference(firstParamReference,
                                                                       secondParamReference)
print(firstParamValue, secondParamValue)
print(firstParamReference, secondParamReference)
print(newFirstParamValue, newSecondParamValue)
print(newFirstParamReference, newSecondParamReference)
