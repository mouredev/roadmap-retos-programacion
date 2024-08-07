#Reto 01

#Ejemplos con todos los tipos de operadores:
    # Operadores aritméticos
a = 10
b = 4
#Suma
sum = a + b
print(sum)
#Resta
rest = a - b
print(rest)
#División
div = a / b
print(div)
#Multiplicación
multi = a * b
print(multi)
#Modulo entre operandos (obtiene el resto de la división)
modulo = a % b
print(modulo)
#Potencia de operandos
pot = a ** b
print(pot)
#División con resultado de número entero
divent = a // b
print(divent)

    #Operadores de comparación (devuelven valor booleano)
#Mayor que
mayorque = a > b
print(mayorque)
#Menor que
menorque = a < b
print(menorque)
#Igual
igual = a == b
print(igual)
#Mayor o igual que
moique = a >= b
print(moique)
#Menor o igual que
meoique = a <= b
print(meoique)
#Diferente
dif = a != b
print(dif)

    #Operadores Bit a bit
c = 2
d = 3
e = 2
# & Realiza bit a bit la operación AND en los operandos: c & d = 2 (binario = 10 & 11 = 10)
bitand = c & d
print(bitand)
# | Realiza bit a bit la operación OR en los operandos: c | d = 3  (binario = 10 | 11 = 11)
bitor = c | d
print(bitor)
# ^ Realiza bit a bit la operación XOR en los operandos: c ^ d = 2  (binario = 10 ^ 11 = 01)
bitxor = c ^ d
print(bitxor)
# ~ Realiza bit a bit la operación NOT. Invierte cada bit en el operando: ~e = -3 (Binario: ~(00000010) = (11111101))
bitnot = ~e 
print(bitnot)
# >> Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha: c >> d = 0 (Binario: 00000010 >> 00000011 = 0)
bitdespder = c >> d
print(bitdespder)
# << Desplaza los bits del operador de la izquierda a la izquierda tantos bits como indica el operador de la derecha: c << d = 16 (Binario: 00000010 << 00000011 = 00001000)
bitdespizq = c << d 
print(bitdespizq)

    #Operadores de asignación
""" Se utilizan para asignar valores a una variable, generalmente se combina con otros poeradores
donde la operación se realiza en los operandos y el resultado se asigna al operando irquierdo.  
"""

a = 18 # = asigna el valor a la variable
print(a)
a += 10 # += es equivalente a a = a + 10
print(a)
a -= 5 # -= es equivalente a a = a - 5
print(a)
a *= 3 # *= es equivalente a a = a * 3
print(a)
a /= 3 # /= es equivalente a a = a / 3
print(a)
a %= 3 # %= es equivalente a a = a % 3
print(a)
a **= 3 # **= es equivalente a a = a ** 3
print(a)
a //= 3 # //= es equivalente a a = a // 3
print(a)
a &= 5 # &= es equivalente a a = a & 3
a |= 3 # |= es equivalente a a = a | 3
a ^= 3 # ^= es equivalente a a = a ^ 3
a >>= 3 # >>= es equivalente a a = a >> 3
a <<= 3 # <<= es equivalente a a = a << 3

    #Operadores lógicos
""" Se utilizan para tomar una decisión basada en múltiples condiciones
"""
g = True
h = True
i = False
# AND - Devuelve True si ambos operandos son True
land = g and h
# OR - Devuelve True si alguno de los operandos es True
lor = g or i
# NOT - Devuelve True si alguno de los operandos es False
lnot = not h

    #Operadores de pertenencia
""" Se emplean para identificar pertenencia en alguna secuencia (listas, strings, tuplas)
"""
lista = [1,2,3,4,5]

# in devuelve True si el valor especificado se encuentra en la secuencia, en caso contrario devuelve False.
print(4 in lista)

# not in devuelve True si el valor especificado no se encuentra en la secuencia, en caso contrario devuelve False.
print(6 not in lista)

    #Operadores de identidad
""" Se utilizan para comprobar si dos variables son, o no, el mismo objeto
"""
x = 4
y = 2
lista2 = [1, 5]
# is devuelve True si ambos operandos hacen referencia al mismo objeto, False en caso contrario
# is not devuelve True si ambos operandos no hacen referencia al mismo objeto, False en caso contrario
print(x is 4)
print(x is y)
print(x is not lista2)

# Ejemplos de estructura condicional
edadlegal = 18
fechaactual = 2024
fechanacimiento = input("Introduce tu año de nacimiento:")
fechanacimiento = int(fechanacimiento)

# IF - elif - else
if fechaactual - fechanacimiento < edadlegal:
    print("No tienes acceso, eres menor de edad")
elif fechaactual - fechanacimiento == edadlegal:
    print("Acceso autorizado, felicidades por tus 18")
else:
    print("Acceso autorizado")

# While
hora = 0
horadescuento = 12

while hora < horadescuento:
    print("Aun no es la hora feliz! Faltan ",horadescuento - hora," horas")
    hora = input("¿Que hora es?")
    hora = int(hora)
    
# For 
for numero in range(1, 10):
    print(numero)

# OPCIONAL - programa que imprime los números comprendidos entre 10 y 55, pares, que no sean 16 ni múltiplos de 3.
    
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:         
        print(numero)
