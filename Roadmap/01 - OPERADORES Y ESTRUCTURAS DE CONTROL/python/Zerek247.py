# -------------------- Tipos de operadores Aritméticos en python ------------------------
#Operador suma ( + )
print("Ahora vamos con la suma")
num1 = 20
num2 = 21
suma = num1 + num2
print(f'El resultado de sumar {num1} + {num2} es: {suma}')

#Operador resta ( - )
print("\nAhora vamos con la resta")
num1 = 40
num2 = 13
resta = num1 - num2
print(f'El resultado de restar {num1} - {num2} es: {resta}')

#Operador multiplicación ( * )
print("\nAhora vamos con la multiplicacion")
num1 = 23
num2 = 55
multiplicacion = num1 * num2
print(f'El resultado de multiplicar {num1} * {num2} es: {multiplicacion}')

#Operador división ( / )
print("\nAhora vamos con la división")
num1 = 10
num2 = 2
division = num1 / num2
print(f'El resultado de dividir {num1} / {num2} es: {division}')

#Operador división entera ( // )
print("\nAhora vamos con la división entera")
num1 = 70
num2 = 20
division_entera = num1 // num2
print(f'El resultado de la division entera {num1} // {num2} es: {division_entera}')

#Operador división entera ( // )
print("\nAhora vamos con la división entera")
num1 = 70
num2 = 20
division_entera = num1 // num2
print(f'El resultado de la division entera {num1} // {num2} es: {division_entera}')

#Operador Módulo (Resto de la división) ( % )
print("\nAhora vamos con el resto")
num1 = 86
num2 = 67
resto = num1 % num2
print(f'El resultado del módulo o resto {num1} % {num2} es: {resto}')

#Operador exponente (potencia)
print("\nAhora vamos con la potencia")
num1 = 4
num2 = 2
exponente = num1 ** num2
print(f'El resultado del numero {num1} elevado al {num2} es: {exponente}')


# ------------------- Tipos de operadores lógicos en python ---------------------------


#Operador  AND ( & ) Es true si ambas condiciones se cumplen
num1 = 50
num2 = 60
if num1 & num2 >40:
    print(True)   
else:
    print(False)
    
#operador OR ( | ) Es true si al menos una condicion se cumple
num1 = 50
num2 = 60
if num1 | num2 > 55:
    print(True)   
else:
    print(False)
    
#Operador NOT (  )
num1 = 50
num2 = 60
if not (num1 > num2):
    print("No es mayor")   
else:
    print("Es mayor")
    
# ------------------------ Tipos de operadores de comparación en python -------------------------

#Operador Igual a ( == )
tupla1 = (23,67,89,0)
tupla2 = (23,67,89,0)

if tupla1 == tupla2:
    print("Son iguales")
else:
    print("No son iguales")
    
#Operador No igual a ( != )
lista1 = [23,67,89,0]
lista2 = [23,6,89,0]

if lista1 != lista2:
    print("Son diferentes")
else:
    print("Son iguales")
    
#Operador Mayor que ( > )
num1 = 23.3
num2 = 23.1
if num1 > num2:
    print(f'Efectivamente {num1} es mayor a {num2}')
else:
    print(f'El numero {num1} no es mayor a {num2}')
    
#Operador Mayor o igual que ( >= )
num1 = 78
num2 = 78
if num1 >= num2:
    print(f"El numero {num1} es igual o mayor al numero {num2}")
else:
    print(f'El numero {num1} no es mayor o igual al numero {num2}')
    
#Operador Menor que ( < )
num1 = 23.3
num2 = 23.1
if num1 < num2:
    print(f'Efectivamente {num1} es menor a {num2}')
else:
    print(f'El numero {num1} no es menor a {num2}')
    
#Operador Menor o igual que ( <= )
num1 = 90
num2 = 78
if num1 <= num2:
    print(f"El numero {num1} es igual o menor al numero {num2}")
else:
    print(f'El numero {num1} no es menor o igual al numero {num2}')
    

# ---------------------  Tipos de operadores de asignacíon en python --------------------------------

#Asignación simple ( = )
a = 4
print(a)

#Suma y signación ( += )
c = 3
c += 6
print(c)

#Resta y asignación ( -= )
d = 90
d -= 70
print(d)

#Multiplicación y asignación
g = 4
g *=4
print(g)

#División y asignación ( /= )
h = 10
h /= 2
print(h)

#Módulo y asignación ( %= )
b = 8
b %= 5
print(b)

#División entera y asignación ( //= )
e = 34
e //= 4
print(e)

#Exponente y asignación ( **= )
f = 4
f **= 2
print(f)

# AND bit a bit y asignación ( &= )
''' 00000011  (3 en binario)
 &  00000111  (7 en binario)
-----------
    00000011  (resultado, que es 3 en decimal)
'''
i = 3
i &= 7
print(i)
#OR bit a bit y asignación ( |= )
''' 00000011  (3 en binario)
 |  00000111  (7 en binario)
-----------
    00000111  (resultado, que es 7 en decimal)
'''
j = 3
j |= 7
print(j)
#XOR bit a bit y asignacíon ( ^= )
''' 00000011  (3 en binario)
 ^  00000111  (7 en binario)
-----------
    00000100  (resultado, que es 7 en decimal)
'''
k = 3
k ^= 7
print(k)
#Desplazamiento a la derecha y asignación ( >>= )
'''  00110010  (50 en binario)
>>          3  (desplazamos 3 posiciones a la derecha)
--------------
     00000110  (resultado, que es 0 en decimal)
'''
l = 50
l >>= 3
print(l)
#Desplazamiento a la izquierda y asignación ( <<= )
'''  00101101  (50 en binario)
<<          3  (desplazamos 3 posiciones a la derecha)
--------------
     00000110  (resultado, que es 0 en decimal)
'''
m = 45
m <<= 3
print(m)


# ------------------- Operadores de identidad ( ís & is not) ---------------------
#Operador is
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, porque b es la misma referencia que a
print(a is c)  # False, porque c es una lista diferente, aunque tiene el mismo contenido
#Operador is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is not b)  # False, porque b es la misma referencia que a
print(a is not c)  # True, porque c es una lista diferente, aunque tiene el mismo contenido


# ----------------------Operadores de indentidad (in & not in) ----------------------------
#Operador in
# Ejemplo con una lista
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # True, porque 3 está en la lista
#Operador not
lista = [1, 2, 3, 4, 5]
print(6 not in lista)  # True, porque 6 no está en la lista



# programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for contador in range(10, 56):
    if contador != 16 and contador % 2 == 0 and contador % 3 != 0:
        print(contador)
        