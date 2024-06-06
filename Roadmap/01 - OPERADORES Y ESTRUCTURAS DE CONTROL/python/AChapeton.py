# Operadores Aritmeticos
suma = 2 + 3
resta = 9 - 5
producto = 5 * 5
division = 21 / 7
modulo = 16 % 3
potencia = 8 ** 3
division_entera = 16 // 5
print('Suma: ', suma)
print('Resta: ', resta)
print('Producto: ' , producto)
print('Division: ', division)
print('Modulo: ', modulo)
print('Potencia: ', potencia)
print('Division con enteros: ', division_entera) 


# Operadores Relacionales
mayor_que = 3 > 5
menor_que = 5 < 8
igualdad = 7 == 7
mayor_igual = 5 >=5
menor_igual = 7 <= 4
desigualdad = 8 != 6
print('Mayor que: ', mayor_que)
print('Menor que: ', menor_que)
print('Igualdad: ', igualdad)
print('Mayor o igual que: ', mayor_igual)
print('Menor o igual que: ', menor_igual)
print('Desigualdad: ', desigualdad)


# Operadores Bit a Bit
print('AND', 10 & 12)
print('OR', 10 | 12)
print('XOR', 10 ^ 12)
print('NOT', ~12)
print('Desplazamiento a la derecha', 10 >> 12)
print('Desplazamiento a la izquierda', 10 << 12)


# Operadores de Asignacion
# Estos operadores son una forma mas rapida de utilizar los operadores Aritmeticos

# Asignacion
x =  0 
print(x)
# Suma
x +=  5
print(x)
# Resta
x -= 5
print(x)
# Producto
x *= 5
print(x)
# Division
x /= 5
print(x)
# Modulo
x %= 5
print(x)
# Potencia
x **= 5
print(x)
# Division Entera
x //= 5
print(x)


# Operadores Logicos
true_value = True
false_value = False
# and - Devuelve true si ambos son True
print('and: ', true_value and false_value)
# or - Devuelve Truse si alguno es False
print('or: ', true_value or false_value)
# not - Devuelve True si alguno es False
print('not: ', not false_value)


# Operadores de Pertenencia
list = [1, 2, 3, 4, 5]
hello = 'Hello World'
# in - Devuelve True si el elemento se encuentra en la lista
print('In list: ', 3 in list)
print('In Hello: ', 'World' in list)
# not in - Devuelve Truse si el elemento NO se encuentra en la lista
print('Not in list: ', 7 not in list)
print('Not in Hello: ', 'Hello' not in list)


# Operadores de Identidad
# is - Devuelve True si los operandos se refieren al mismo objeto
# is not - Devuelve True si los operandos NO se refieren al mismo objeto
aa = 3
bb = 3  
cc = 4
print('AA es BB', aa is bb) # muestra True
print('AA no es BB',aa is not bb) # muestra False
print('AA no es CC', aa is not cc) # muestra True

# Condicionales

# If
edad = 18
if edad < 18:
  print("Menor de edad")
elif edad >= 18:
  print('Mayor de edad')
else:
  print('No se va a ejecutar')


# For
lenguajes = ['Python', 'JavaScript', 'Dart']
for lenguaje in lenguajes:
  print(lenguaje)

# While
contador = 0
while contador < 3:
  print("Dentro del bucle", contador)
  contador += 1



# DIFICULTAD EXTRA

for i in range(10, 56):
  if i % 2 == 0:
    if i != 16 and i % 3 != 0:
      print(i)

