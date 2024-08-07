from collections import namedtuple, defaultdict, Counter
import copy
#Permite crear tuplas con nombre
#Counter permite el conteo de elementos en una lista, y tambien contar elementos 
#úncos y repetitivos en coleccion de datos

# ESTRUCTURAS DE DATOS 

## lISTA -> colección de elementos ordenados y modificables

lista = [27, 13, 14, 66, 21]
lista[2] = 54
print(lista)

lista.append(9)
lista.insert(2, 33)
lista.count(13)
print(lista.remove(21))
print(lista.pop(2))
print(lista.sort())
print(lista.reverse())
print(lista.clear())
print(lista)
lista.append(9)
hola = lista.copy()
print(hola)

#Copia superficial:
## Afectará la lista original si se modifica la copia

lista4 = [1,2,3, [3,4,5]]
copia_superficial = lista4.copy()

copia_superficial[3][0] = 100
print(lista4, " La lista original se modifica")

#Copia profunda:
## Necesario importar copy, y esta copia no afectará la lista original

copia_profunda = copy.deepcopy(lista4)
copia_profunda[3][0] = 234
print(lista4, " La lista original no se modifica\n",copia_profunda, "Mientras que la copia cambia" )





## TUPLAS -> colección de elementos ordenados e inmutables
#No podemos agregar ni eliminar elementos
#Usadas para datos no modificables
tupla = (5,12,34, "hola")
tupla1 = (1,2,3,4,5,6,7,8,9,10)
print(tupla.count(12))
print(tupla.index(34))
print(min(tupla1))
print(max(tupla1))
resultado = sum(tupla1)
print("La suma es ", resultado)

# Para ordenar una tupla la convertimos en lista
lista_tupla = list(tupla1)
lista_tupla.sort()
print(lista_tupla)
tupla1 = tuple(lista_tupla)

### TUPLAS CON NOMBRES -> NAMEDTUPLE
#No podemos modificar los datos

Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad']) #Nombre de la tupla y los elementos
persona = Persona('Katherinne', 18, 'Bogotá')

print(f"Nombre: {persona.nombre} \nEdad: {persona.edad} \nCiudad {persona.ciudad}")


#Para iterar
def reture(tupla1):
    tupla_iterada = []
    for i in tupla1:
        tupla_iterada.append(i)
    return "ok", tupla_iterada
        
print(reture(tupla1))





## DICCIONARIOS -> colección de elementos no ordenados, modificables e indexados
## Almacenar y7 acceder a datos con claves
## Contar frencuencias de un elemento


diccionario = {'nombre': 'Katherinne', 'edad' : 18, 'curso': 'Python'}
diccionario1 = diccionario.copy()
print(diccionario1.items())
print(diccionario1.keys())
print(diccionario1.pop("nombre"))
print(diccionario1.setdefault("ciudad", "Bogotá")) #setdefault da un valor por defecto

camisa ={'marca': 'Adidas'}
print(diccionario1.update(camisa))
key = {'Pais natal', 'País de trabajo'}
value = "Colombia"
pais_ciudad = dict.fromkeys(key, value)
print(pais_ciudad)
print(len(diccionario1))
print(diccionario1.clear())
#del(diccionario)
#print(diccionario)

diccionario['edad'] = 19
print(diccionario['curso'], diccionario['edad'])


#get(clave, valor por defecto) -> Permite obtener un valor de una clave
print(diccionario.get('nombre', 'No existe'))


def letter_frequency_normal(sentence):
  frequencies = {}  # Diccionario normal
  for letter in sentence:
    frequency = frequencies.setdefault(letter, 0)  # Verifica si la clave existe
    frequencies[letter] = frequency + 1
  return frequencies

def letter_frequency_default(sentence):
  frequencies = defaultdict(int)  # defaultdict con valor por defecto int(0)
  for letter in sentence:
    frequencies[letter] += 1
  return frequencies # defaultdict se puede indexar igual que un diccionario normal

if __name__ == '__main__':
  print(letter_frequency_normal("hola mundo"))
  print(letter_frequency_default("hola mundo")) 
  
##Creditos a Felipe 



## CONJUNTOS -> colección de elementos no ordenados y sin elementos duplicados


# Permite eliminar duplicados, hacer operaciones de conjuntos
# Permite hacer pruebas de pertenencia in not in más rapidas que listas
### Borra automaticameto los duplicados
lista_conjunto = [1,2,3,4,5,5,5,4,3,4,320]
conjunto = set(lista_conjunto)
conjunto1 = {3,432,4,5634,12,5,1,42,7,2}

#Operacion de conjuntos -> UNIÓN
union = conjunto | conjunto1
print("union ",union)

#Operación de conjuntos -> INTERSECCIÓN
interseccion = conjunto & conjunto1
print("Intersección ", interseccion)

#Operación de conjuntos -> DIFERENCIA
diferencia = conjunto - conjunto1
print("Diferencia ", diferencia)

diferencia = conjunto1 - conjunto
print("Diferencia 2", diferencia)

#Operación de conjuntos  -> issubset(otro_conjunto)
##Permite saber si los elementos del primer conjutno estan en otro

print("Elementos conjunto estan en el segundo ", conjunto.issubset(conjunto1))
print("Elementos del segundo conjunto están en el primero ", conjunto.issuperset(conjunto1))

#Operación de conjuntos -> DIFERENCIA SIMESTRICA
#Diferencia de ambos conjuntos
diferencia_simetrica = conjunto ^ conjunto1
print("Diferencia simetrica ", diferencia_simetrica)


conjunto.add(11)
print(conjunto)

conjunto.remove(2) #Con error si no está en el set
conjunto.discard(328193) #No error si no está en el set
conjunto.pop() #Borra algo aleatorio

print(32432 in conjunto)
print("Longitud ", len(conjunto))
print("Maximo ", max(conjunto))
print("Minima ", min(conjunto))
print(sorted(conjunto))

suma1 = sum(conjunto)
print("Suma ", suma1)
