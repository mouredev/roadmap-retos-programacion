#Operadores aritméticos
num1 = 4
num2 = 3
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2
division_entero = num1 // num2
resto = num1 % num2
potencia = num1 ** num2

print(f"Suma: {suma}, Resta: {resta}, Producto: {producto}, División: {division}, División entero: {division_entero}, Resto: {resto}, Potencia: {potencia}")

#Operadores relacionales
mayor_que = num1 > num2
menor_que = num1 < num2
igual_a = num1 == num2
mayor_o_igual = num1 >= num2
menor_o_igual = num1 <= num2
diferente_de = num1 != num2

print(f"Mayor que: {mayor_que}, Menor que: {menor_que}, Igual a: {igual_a}, Mayor o igual que: {mayor_o_igual}, Menor o igual que: {menor_o_igual}, Diferente de: {diferente_de}")

#Operadores de asignación
num3 = 4
num3 += 8   #Equivalencia: num1 = num1 + 8
print(num3)
num3 -= 8   #Equivalencia: num1 = num1 - 8
print(num3)
num3 *= 8   #Equivalencia: num1 = num1 * 8
print(num3)
num3 **= 8   #Equivalencia: num1 = num1 ** 8
print(num3)
num3 /= 8   #Equivalencia: num1 = num1 / 8
print(num3)
num3 //= 8   #Equivalencia: num1 = num1 // 8
print(num3)
num3 %= 8   #Equivalencia: num1 = num1 % 8
print(num3)

#Operadores lógicos
print(f"5 < 8 and 8 > 3 es: {5 < 8 and 8 > 3}")
print(f"4 > 3 or 2 > 9 es: {4 > 3 or 2 > 9}")
print(f"5 > 6 es: {not 5 > 6}")

#Operadores de pertenencia
print(f"in: 'a' in 'hola' es {'a' in 'hola'}") #True
print(f"not in: 'a' not in 'hola' es {'a' not in 'hola'}") #False

#Operadores de identidad
mi_variable = 10 
print(id(mi_variable)) #4372070928
tu_variable = 10
print(id(tu_variable)) #4372070928

print(f"is: mi_variable is tu_variable es {mi_variable is tu_variable}") #True
print(f"is not: mi_variable is not tu_variable es {mi_variable is not tu_variable}") #False

#Operador nivel de Bit
  ##operador and &: comparamos todos los bits uno a uno, y, si están los dos a 1, entonces sería 1; si alguno de los dos valores está a 0, sería 0.
numero = 20
numero_bin = 0b10100

numero_dos = 22
numero_dos_bin = 0b10110

print(bin(numero & numero_dos)) ## 0b10100

  #operador or |: comparamos todos los bits uno a uno, y, si está alguno de los dos a 1, entonces sería 1; y si no está ninguno, es 0.

print(bin(numero | numero_dos)) ## 0b10110

  #operador not ~ invierte cada bit en el operando. El bit que tiene como valor 1 lo pone a 0, y al contrario.

print(bin(~numero)) ## -ob10101

  #operador xor ^ devuelve los bits que estén a 1 no comunes en los dos operandos.

print(bin(numero ^ numero_dos)) ##^0b10

  #operador shift >> ó << se utiliza para mover bits hacia la derecha ó izquierda. Hacen falta dos parámetros para indicarle primero qué vamos a desplazar y después el número de posiciones que lo desplazaremos.

print(bin(numero >> 2)) ##ob101
print(bin(numero << 2)) ##ob1010000

## Estructuras de control

  # if  =>  condicional
color = "azul"

if color == "azul":
  print("Hace frio en la calle")
elif color == "rojo":
  print("Hace calor en la calle")
else:
  print("No hace ni frío ni calor")

  # for => iterativa

cadena = 'Sevilla'

for i in cadena:
  print(i)

  # while => iterativa

numero = 1
while numero < 6:
  print('hola mundo')
  numero = numero + 1

  # Manejo de excepciones
try:
  print('No hay error')
except TypeError:
  print(f'Encontré este error: {TypeError}')
finally:
  print('Siempre se ejecuta')

### EXTRA ###

for a in range(10, 56):
  if a % 2 == 0 and a != 16 and a % 3 != 0:
    print(a)

