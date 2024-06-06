
# Variables asignadas por valor
'''
Las variables por valor se asignan a tipos primitivos cuando se le da el valor a una variable se guarda
en un punto de la memoria que se puede obtener con la funcion "id" lo podemos conocer. Por  eso una vez
que hemos asignado el valor de "a" a "b" aunque cambiemos el valor de "a" el de "b" no cambia pues su
lugar en la memoria no cambia
'''

print("\n\n=========================\n\n")

a = 5
print(a, id(a))        # 140731962418088
b = a
print(b, id(b))        # 140731962418088
a = 10

print(a, id(a))     # 10    140731962418248
print(b, id(b))     # 5     140731962418088

print("\n\n=========================\n\n")

# Variables asignadas por referencia
'''
Las variables asignadas por referencia es a tipos compuestos(listas, tuplas, set o diccionarios)
Aqui­ al igualar las variables lo que hacemos es dar el mismo punto de memoria a las dos por lo 
al cambiar el valor de "list_b" lo cambiamos en la memoria que comparten "list_a" y "list_b"
'''

list_a = [5, 10]
print(list_a, id(list_a))   # [5, 10] 1711738540608
list_b = list_a
print(list_b, id(list_b))   # [5, 10] 1711738540608
list_b.append(15)

print(list_a, id(list_a))   # [5, 10, 15] 2834210902592
print(list_b, id(list_b))   # [5, 10, 15] 2834210902592


# Funcion con asignacion por valor
num = 5

def valor(n):
  n = 10
  print(n)
  
valor(num)
print(num)

# Funcion con asignacion por referencia
list_a = [5, 10]

def referencia(lis):
  lis.append(15)
  print(lis)

referencia(list_a)
print(list_a)  



print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


# Asignacion por valor

a = 5
b = 10

def intercambio_valor(num1, num2):
  num3 = num1
  num1 = num2
  num2 = num3
  return num1, num2


(c, d) = (intercambio_valor(a, b))

intercambio_valor(a, b)
print(a, b)
print(c, d)

print("\n\n=========================\n\n")

# Asignacion por referencia

list_a = [10, 20]
list_b = [30, 40]

def intercambio_ref(lis1, lis2):
  lis3 = lis1
  lis1 = lis2
  lis2 = lis3
  return lis1, lis2


(list_c, list_d) = (intercambio_ref(list_a, list_b))

intercambio_ref(list_a, list_b)
print(list_a, list_b)
print(list_c, list_d)


