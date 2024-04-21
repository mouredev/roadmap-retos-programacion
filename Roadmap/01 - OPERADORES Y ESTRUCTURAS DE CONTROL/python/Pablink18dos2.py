'''
Operadores'''

#Operadores aritméticos

#Suma
print(2+3)
print(f"suma: 10 + 3 = {10+3}")

def suma(a,b):
    return a+b

print(suma(10,5))

#Resta
print(2-3)
#Multiplicación
print(2*3)
#División
print(2/3)
#Módulo
print(2%3)
#Exponente
print(2**3)
#División entera
print(2//3)


#Operadores de comparación

#Igual
print(f"10 es igual a 3, respuesta: {10==3}")

#Diferente
print(f"10 es diferente a 3, respuesta: {10!=3}")

#Mayor que
print(f"10 es mayor que 3, respuesta: {10>3}")

#Menor que
print(f"10 es menor que 3, respuesta: {10<3}")

#Operadores lógicos

#And
print(f"10 es mayor que 3 y 11 es mayor que 10, respuesta:{10>3 and 11>10}")

#Or
print(f"10 es mayor que 3 o 11 es mayor que 10, respuesta: {10>3 or 11>10}")

#Not
print(f"10 es mayor que 3, respuesta: {not 10>3}")

#Operadores de asignación

#Asignación
a = 10
print(a)

#Suma y asignación

a += 3
print(a)
a += 3
print(a)

a-=3
print(a)

a*=3
print(a)

a/=2
print(a)

a%=3 # a = a % 3 devuelve el residuo de la división
print(a)

a**=3
print(a)

a//=3
print(a)


#Operadores de identidad, intentan verificar si los valores son iguales en la memoria. esto quiere decir que si se asigna una variable a otra, ambas variables apuntan a la misma dirección de memoria

#igualdad entre dos objetos, variables
my_new_number = a

print(f"my_new_number es igual a a, respuesta: {my_new_number is a}")

#Diferencia entre dos objetos, variables

print(f"my_new_number es diferente a a, respuesta: {my_new_number is not a}")


#Operadores de membresía, intentan verificar si un valor se encuentra en una secuencia

#In
print(f" 'u' está dentro de 'moure', respuesta:{'u'in 'moure'}")

#Not in
print(f" 'u' no está dentro de 'moure', respuesta:{'u'not in 'moure'}")

#Operadores de bits
a = 3 # 0011
b = 11 # 1011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # 0101
print(f"Desplazamiento a la izquierda: 10 << 3 = {10 << 3}") # 10000
print(f"Desplazamiento a la derecha: 10 >> 3 = {10 >> 3}") # 0

'''
Estructuras de control
'''

#Condicionales

my_string = "Pablo"

if my_string == "Pablo":
    print("Hola Pablo")
elif my_string == "Juan":
    print("Hola Juan")
else:
    print("No eres Nadie")

#Ciclos o bucles

for i in range(10):
    i=i*2
    print(i)

# bucle en el que duplique es el valor de  bucle en el que amuente de dos en dos el valor de i 10 veces y lo imprima
for i in range(0,20,2):
    print(i)

i = 0
while i <= 10:
    print(i)
    i+=1

# manejo de excepciones

try:
    print(10/1)
except:
    print("No se puede dividir por 0")
finally: # se ejecuta siempre, haya o no haya excepción
    print("Se ha ejecutado el bloque try para el manejo de excepciones")



'''
Extra
'''

a = 10

while a <= 55:
    if a % 2 == 0 and a % 3 != 0 and a != 16: 
        print(a)

    a+=1






