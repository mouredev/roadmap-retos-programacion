#Operadores y estructuras de control
"""
Crer ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritmeticos, logicos, comparacion, asgignacion, identidad, pertenencia y bit a bit.
"""
#Operadores Aritmeticos
a = 10
b = 5

print(a+b) #Suma
print(a-b) #Resta
print(a*b) #Multiplicacion
print(a/b) #Division
{a%b} #Modulo
print(a**b) #Exponente
print(a//b) #Division entera

#Operadores de comparacion
x = 10
y = 20
print(x == y) #Igual a
print(x != y) #Diferente a
print(x > y) #Mayor que
print(x < y) #Menor que
print(x >= y) #Mayor o igual que
print(x <= y) #Menor o igual que

#Operadores logicos
edad = 25
tiene_id = True
print(edad >= 18 and tiene_id) #AND
print(edad < 18 or tiene_id) #OR
print(not tiene_id) #NOT

#Operadores de asignacion
num = 10
num += 5 #Suma y asigna
print(num) #15 
num -= 3 #Resta y asigna
print(num) #12
num *= 2 #Multiplica y asigna   
print(num) #24
num /= 4 #Divide y asigna
print(num) #6.0

#Operadores de identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 is lista2) #False
print(lista1 is lista3) #True   
print(lista1 is not lista2) #True

#Operadores de pertenencia
frutas = ["manzana", "banana", "naranja"]
print("manzana" in frutas) #True
print("pera" in frutas) #False
print("pera" not in frutas) #True

#Operadores bit a bit
a = 5 #En binario: 0101
b = 3 #En binario: 0011

print(a & b) #AND bit a bit: 0001 (1 en decimal)
print(a | b) #OR bit a bit: 0111 (7 en decimal)
print(a ^ b) #XOR bit a bit: 0110 (6 en decimal)
print(~a) #NOT bit a bit: 1010 (-6 en decimal)
print(a << 1) #Desplazamiento a la izquierda: 1010 (10 en decimal)
print(a >> 1) #Desplazamiento a la derecha: 0010 (2 en decimal)

"""
Utilizaando las estructuras de control que tu quieras, 
crea ejemplos que representen todos los tipos de estructuras que existen en tu lenguaje: 
secuenciales, condicionales, iterativas.

"""
#secuenciales
nombre = input("Nombre: ")
edad = int(input("Edad: "))
#condicionales
if edad >= 18:
 print("acceso permitido")
#iterativas
for i in range(3):
    print("Bienvenido ",nombre)
else:
    print("acceso denegado")