# OPERADORES  Y ESTRUCTURAS DE CONTROL

# Operadores aritméticos
suma = 10 + 5
resta = 18 - 4
multiplicacion = 8 * 11
division = 120 / 3

print(f"El resultado de la suma es {suma}")
print(f"El resultado de la resta es {resta}")
print(f"El resultado de la multiplicación es {multiplicacion}")
print(f"El resultado de la división es {division}")


# Operadores lógicos
verdadero = True
falso = False

resultado = verdadero and verdadero
print (f"Verdadero y Verdadero es igual a {resultado}")
resultado = verdadero or falso
print(f"Veradero o Falso es igual a {resultado}")
resultado = not verdadero
print(f"No verdadero es igual a {resultado}")


# Operadores de comparación
resultado = 7 > 8
print(f"7 es mayor que 8? {resultado}")
resultado = 10 < 20
print(f"10 es menor que 20? {resultado}")
resultado = 26 <= 29
print(f"26 es menor o igual que 29? {resultado}")
resultado = 34 >= 104
print (f"34 es mayor o igual que 104? {resultado}")
resultado = 56 == 56
print(f"56 es igual a 56? {resultado}")
resultado = 77 != 77
print(f"77 es distinto de 77? {resultado}")


# Operadores de asignación
numero = 17

numero+=2
print(f"El valor actual de la variable número es {numero}")
numero-=2
print(f"El valor actual de la variable número es {numero}")
numero*=2
print(f"El valor actual de la variable número es {numero}")
numero/=2
print(f"El valor actual de la variable número es {numero}")


# Operadores de identidad
objeto1 = 10
objeto2 = [12, 14]

print(f"Objeto1 es Objeto2? {objeto1 is objeto2}")
print(f"Objeto1 no es Objeto2? {objeto1 is not objeto2}")


# Operadores de pertenencia
print(f"17 está en [1, 14, 17, 34]? {17 in [1, 14, 17, 34]}")
print(f"17 no está en [1, 14, 17, 34]? {17 not in [1, 14, 17, 34]}")


# Operadores binarios
numero1 = 16
numero2 = 128

print(f"El binario de numero1 y numero2 es {bin(numero1 & numero2)}")
print(f"El binario de numero1 o numero2 es {bin(numero1 | numero2)}")
print(f"El binario de not numero1 es {bin(~numero1)}")
print(f"El binario de numero1 xor numero2 es {bin(numero1 ^ numero2)}")


# Condicionales
n1 = 33
n2 = 46

if n1 == n2:
    print(f"El número {n1} es igual al número {n2}")
else:
    print(f"El número {n1} es distinto al número {n2}")


# For
lista = [0, 1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)


# While
repeticiones = 1

while repeticiones < 11:
    print(f"Ejecución del bucle while {repeticiones}")
    repeticiones += 1


# Ejercicio extra
for i in range(10, 56):
    if (i % 2 == 0) and (i != 16) and (i % 3 != 0):
        print(i)