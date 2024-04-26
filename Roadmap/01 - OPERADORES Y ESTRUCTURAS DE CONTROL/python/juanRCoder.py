# Operadores Aritméticos
print(f"Suma: {3 + 1}")
print(f"Resta: {10 - 2}")
print(f"Multiplicacion: {2 * 5}")
print(f"Potencia: {3 ** 2}")
print(f"Dividir: {27 / 9}")             #-> devuelve un valor flotante
print(f"Division_baja: {27 // 9}")      #-> devuelve un valor entero
print(f"Resto: {12 % 2}")

print()
# Operadores logicos
print(True and False)    #-> devuelve True porque ambos son True
print(True or False)     #-> devuelve True porque al menos hay un True
print(not False)         #-> devuelve siempre lo contrario, True

print()
# Operadores de asignacion
print(10 > 5)   #-> 10 mayor que 5?, True
print(10 < 5)   #-> 10 es menor que 5?, False
print(5 >= 6)   #-> 5 es mayor igual que 6?, False
print(16 <= 3)  #-> 16 es menor igual que 3?, False
print(5 == 5)   #-> 5 es igual a 5?, True
print(9 != 4)   #-> 9 es diferente que 4?, True


print()
# Operadores de identidad
x = [4, 5, 6]
y = [4, 5, 6]
z = x
print(x is y)       #-> False, x y y no apuntan a lo mismo en memoria.
print(x is not y)   #-> True, x y y ahora si no apuntan a lo mismo en memoria.
print(x is z)       #-> True, x y z apuntan al mismo objetivo en memoria. 

print()
# Operadores de pertenencia
lista = ['maria', 'manzana', 24, True]
print('maria' in lista) #-> True, 'maria' esta presente en la lista
print(6 not in lista)   #-> True, 6 no esta presente en la lista

print()
# Operadores a nivel de bit
a = 5
b = 3
print(f"AND: {a & b}")  #-> 1, en binario 001
'''
   101   (5 en binario)
 & 011   (3 en binario)
 ------
   001   (Resultado en binario)
'''

print(f"OR: {a | b}")   #-> 7, en binario es 111
'''
   101   (5 en binario)
 | 011   (3 en binario)
 ------
   111   (Resultado en binario)
'''

print(f"XOR: {a ^ b}")  #-> True, 6 en binario es 110
'''
   101   (5 en binario)
 ^ 011   (3 en binario)
 ------
   110   (Resultado en binario)
'''

print(f"NOT: {~a}")     #-> -5, en binario es -0b101
                        #-> prefijo negativo en binario -> -0b

print(f"Desplzamiento a la izquierda: {a << 1}")    #-> 10, es decimal es 1010
# 010 << 1 = 1010

print(f"Desplzamiento a la derecha: {a >> 1}")      #-> 2, es decimal es 0010
# 010 >> 1 = 0010

# CONDICINAL ELSE IF:
# Condicionales, bloques de codigo que se cumplen si la condicion es verdadera
lista = [1, 2, 'Maria']

# Si se cumple, se imprime True
if 2 in lista:
    print(True)

# Si en caso la primera es falsa y esta condicion es verdadera, se imprime False
elif lista[0] == lista[1]:
    print(False)
     
# Si ninguna condicion se cumple se imprime False 
else:
    print(False)

# BUCLES:
for x in range(10):
    if x == 9:
        print(x, end='')
    else:
        print(x, end=', ')
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

x = 0
while x < 10:
    print(x, end='')
    x += 1
# 0123456789

#  DIFICULTAD EXTRA (opcional):
for i in range(11,55+1):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i, end=' ')

# 14 20 22 26 28 32 34 38 40 44 46 50 52