#Python es un lenguaje con una amplia gama de estructuras de datos.

#Listas, son mutables y aceptan datos de cualquier tipo mezclados, están indexados y no poseen un tamañó fijo

lista = [1,  True, "hola"]

print(lista[0])

lista.append(2)

print(lista)

lista.pop(3)

print(lista)

lista.remove("hola")
print(lista)

lista.sort()
print(lista)

#Tuplas, son estructuras inmutables que no se pueden modificar una vez declaradas. Permiten mezclar datos de distinto tipo

tupla = (1,2,"hola")
print(tupla)

print(tupla.count(1))

print(tupla[1])

#Sets, son estructuras mutables y dinámicas que admiten distintos tipos de elemento. Su particularidad es que no están indexadas
#ni permiten duplicados. Lo que los hace útiles para ciertos programas.

sets = {1,2,3,4}

sets.add("hola")
sets.add("hola")

print(sets)

sets.remove(3)

print(sets)

#Diccionarios, estructuras dinámicas y mutables, aceptan todo tipo de datos y trabajan en parejas clave:valor 

diccionario = {1:"fasd", 2: 3, 3:"adfad"}

diccionario.pop(1)

print(diccionario)

diccionario[5]="fsdfaf"

print(diccionario)

#OPCIONAL

