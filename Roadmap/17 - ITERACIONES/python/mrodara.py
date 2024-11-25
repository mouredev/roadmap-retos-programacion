##################################  ITERACIONES  ###################################################

# EJERCICIO 3 MANERAS DIFERENTES DE IMPRIMIR SECUENCIA 1 AL 10

# 1. Usando un for

for i in range(1,11):
    print(i," ", end="")
    
# 2. Recorriendo un lista wildcard
lista = [1,2,3,4,5,6,7,8,9,10]

print(lista[:])

# También podemos crear la lista por comprenhension
print (* [i for i in range(1,11)])

# 3. Usando un bucle While
number = 1

while number <= 10:
    print(number, " ", end="")
    number += 1


##################################  EXTRA ITERACIONES  ###################################################

# Podemos usar recursividad para iterar números

def recursive_iteration(i: int = 1):
    if i <= 10:
        print(i, " ", end="")
        recursive_iteration(i + 1)

recursive_iteration()

# Antes hemos usado listas pero también son iterables las tuplas y los diccionarios

tupla = (1,2,3,4,5,6,7,8,9,10)

for num in tupla:
    print(num, " ", end="")
    
my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

# En el caso de los diccionarios podemos iterar las claves, los valores u ambos a la vez

for key in my_dict.keys():
    print(key, " ", end="")
    
for value in my_dict.values():
    print(value, " ", end="")

for key,value in my_dict.items():
    print(f'Clave: {key}, Valor: {value}')
    
# Cadenas de caracteres también son iterables.

my_str = "Lleva la tarara un vestido blanco lleno de cascabeles"

for char in my_str:
    print(char, " ", end="")
    
# De la misma cadena también podemos iterar por las palabras que la conforman
for word in my_str.split():
    if word != " ":
        print(word, " ", end="")

# En listas, tuplas y cadenas de caracteres podemos iterar en orden inverso

print(tupla[::-1])
print(my_str[::-1])
print(my_str.split()[::-1])

##################################  FIN EXTRA ITERACIONES  ###################################################

##################################  FIN ITERACIONES  ###################################################