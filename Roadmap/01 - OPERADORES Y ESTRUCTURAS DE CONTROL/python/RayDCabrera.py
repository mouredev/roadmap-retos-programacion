n1 = 10
n2 = 20

#Operadores Aritméticos   
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
modulo = n1 % n2
potencia = n1 ** n2
division_entera = n1 // n2

print(suma, resta, multiplicacion, division, modulo, potencia, division_entera)
#Operadores Relacionales
n1 < n2 # mayor que
n1 > n2 # menor que
n1 == n2 # igual que
n1 >= n2 # mayor o igual
n1 <= n2 # menor o igual
n1 != n2 # distinto que

#Operadores Bit a Bit
#lo que hace el operador bit a bit (& and) es comparar, bit por bit y setea 1 en la posicion donde los dos bit comparados son 1 y pone 0 si no.

a = 6 # 0000000000000110
b = 3 # 0000000000000011

a & b # ----> 0000000000000010

'''
#6 = 0000000000000110
#3 = 0000000000000011
#--------------------
#2 = 0000000000000010
- en el caso del operador (| or) se setea 1 cuando uno de los dos numeros es 1 o los dos son 1 
- en el operador (^ xor) se setea 1 solo cuando 1 de los dos es 1 
- operador (- not) intercambia todos los bits
- el operador << inserta el numero especificado de 0 desde la derecha y elimina la misma cantidad de la izquierda
- el operador >> mueve cada bit el numero de veces especificado hacia la derecha y los espacios vacios a la izquierda se rellenan con 0.
'''

#Operadores de asignación
a = 5 # el valor 5 es asignado a la variable a  
a += 5 # => a = a + 5
a -= 5 # => a = a - 5
a *= 5 # => a = a * 5
a /= 5 # => a = a / 5

print(a)

#Operadores lógicos
a = 5
b = 5
c = 4
if a == 5 and b == 5:
    print ("a y b son iguales")
if a == 4 or b > c:
    print ('Entra por que se cumple uno de las dos condiciones')


#Operadores de pertenencia

a = [1,2,3,4,5]

print (3 in a) # True

print (12 in a) # True
#Lo mismo para strings

#Operadores de identidad

a = 3
b = 3
c = 4

print (a is b) # True
print (a is not b) # False
print (a is not c) # True


#programa
desde = 10
hasta = 55

for x in range(desde, hasta+ 1):
    if x % 2 == 0 and x != 16 and x % 3 != 0:
        print(x)
