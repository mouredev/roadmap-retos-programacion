
numero1 = 10
numero2 = 5
# Operadores Aritmeticos

print(numero1 + numero2) # Suma
print(numero1 - numero2) # Resta
print(numero1 * numero2) # Multiplicacion
print(numero1 / numero2) # Division
print(numero1 % numero2) # Modulo
print(numero1 ** numero2) # Potencia
print(numero1 // numero2) # Division entera

# Operadores relacionales

print(numero1 == numero2) # Igualdad
print(numero1 != numero2) # Diferente
print(numero1 > numero2) # Mayor que 
print(numero1 < numero2) # Menor que  
print(numero1 >= numero2) # Mayor o igual que
print(numero1 <= numero2) # Menor o igual que

# Operadors Bit a Bit

print(numero1 & numero2) # AND
print(numero1 | numero2) # OR
print(numero1 ^ numero2) # XOR
print(~numero1) # NOT
print(numero1 << 2) # Desplazamiento a la izquierda
print(numero1 >> 2) # Desplazamiento a la derecha

# Operadores de Asignacion

a = 5
a += 5 # a = a + 5
print(a)
a -= 5 # a = a - 5
print(a)
a *= 5 # a = a * 5
print(a)
a /= 5 # a = a / 5
print(a)
a %= 5 # a = a % 5
print(a)
a **= 5 # a = a ** 5
print(a)
a //= 5 # a = a // 5
print(a)
a //= 5 # a = a // 5
print(a)

# Operadores Logicos

if numero1 > 5 and numero2 < 10:
    print("Se cumple la condicion")

if numero1 > 5 or numero2 < 10:
    print("Se cumple la condicion")

if not numero2 > 5:
    print("Se cumple la condicion")

#Operadores de Pertenencia

my_list = [1, 2, 3, 4, 5, 6]


if 1 in my_list:
    print('True')

if 10 not in my_list:
    print('True')


# Operadores de Identidad

x = 7
y = 7
z = 3

print(x is y)
print(x is not y)
print(x is not z)


# Estructura de control condicinal

my_variable1 = 4

if my_variable1 > 10:
    print("La variable es mayor a 10")
elif my_variable1 < 10:
    print("La variable es menor a 10")
else:
    print("La variable es igual a 10")

# Estructura de control iterativa

for i in 'Esternoclidomastoideo':
    print(i)

while my_variable1 < 10:
    print(my_variable1)
    my_variable1 += 1


# Estructura de control de excepciones

try:
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Se termino la ejecucion")



# Ejercicio dificultad extra

def numeros():
    for i in range(10, 56):
       if i % 2 == 0 and i != 16 and i % 3 != 0:
              print(i)

        

numeros()
