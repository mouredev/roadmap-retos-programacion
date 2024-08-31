# -> Operadores Aritmeticos
a = 1
b = 3

suma = a + b  # Este es un operador para sumas
resta = b - a  # Este operador es para restas
multi = a * b  # Este operador es para multiplicación
div = b / a  # Este operador es para Dividir

# -> Operadores Logicos
#       Exiten 3 tipos de operadores logicos -> and, or y not


# Operador and (evalua si ambas condiciones son ciertas para devolver un TRUE)
print("---------- Operador and -----------")
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Operador or (Devuelve TRUE cuando almenos alguno de los valores es TRUE)
print("---------- Operador or -----------")
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Operador not (Simplemente invierte el valor True por False y False por True)
print("---------- Operador not -----------")
print(not True)  # False
print(not False)  # True
print(not not not not True)  # True

# -> Operadores de Comparación
#       Se usan para saber la relación que existe entre dos variables.
#       El valor que devuelven es TRUE o FALSE.

# Operador == (Compara si las variables son iguales)
print("---------- Operador == -----------")
print(4 == 4)          # True
print(4 == 5)          # False
print(4 == 4.0)        # True
print(0 == False)      # True

# Operador != (Devuelve TRUE si los elementos a comparar son iguales y FALSE si son distintos)
print("---------- Operador != -----------")
print(4 != 4)          # False
print(4 != 5)          # True
print(4 != 4.0)        # False
print(0 != False)      # False

# Operador > (Devuelve TRUE si el primer valor es mayor que el segundo y FALSE de lo contrario)
print("---------- Operador > -----------")
print(5 > 3)  # True
print(5 > 5)  # False

# Operador < (Devuelve TRUE si el primer elemento es menor que el segundo)
print("---------- Operador < -----------")
print(5 < 3)  # False
print(3 < 5)  # True

# Operador >= (Permite comparar si el elemento es mayor o igual)
print("---------- Operador >= -----------")
print(3 >= 3)           # True
print([3, 4] >= [3, 5])  # False

# Operador <= (Devuelve TRUE si el primer elemento es menor o igual que el segundo)
print("---------- Operador <= -----------")
print(3 <= 2.99999999999999999)  # False

# -> Operadores de Asignación
#       Nos permiten realizar una operacion y almacenar el resultado en la variable inicial

# Operador =
print("---------- Operador = -----------")
x = 2       # Uso correcto del operador =
print(x)  # 2
# 3=5      # Daría error, 3 no es una variable

# Operador +=
print("---------- Operador += -----------")
x = 5      # Ejemplo de como incrementar
x += 1     # en una unidad x
print(x)  # 6

# Operador -=
print("---------- Operador -= -----------")
i = 5
i -= 1
print(i)  # 4

# Operador *=
print("---------- Operador *= -----------")
a = 10
b = 2  # Inicializamos a 10 y 20
a *= b      # Usando dos variables
print(a)  # 20

# Operador /=
print("---------- Operador /= -----------")
x = 10
print(type(x))  # <class 'int'>
x /= 3
print(type(x))  # <class 'float'>

# Operador %=
print("---------- Operador %= -----------")
x = 3
x %= 2
print(x)  # 1

# Operador //=
print("---------- Operador //= -----------")
x = 5      # El resultado es el cociente
x //= 3    # de la división
print(x)  # 1

# Operador **=
print("---------- Operador **= -----------")
x = 5      # Eleva el número al cuadrado
x **= 2    # y guarda el resultado en la misma
print(x)  # 25

# Operador &= (Realiza una comparación & bit a bit entre dos variables y almacena el resultado en la primera)
print("---------- Operador &= -----------")
a = 0b101010
a &= 0b111111
print(bin(a))  # 0b101010

# Operador |
print("---------- Operador |= -----------")
a = 0b101010
a |= 0b111111
print(bin(a))  # 0b111111

# Operador ^=
print("---------- Operador ^= -----------")
a = 0b101010
a ^= 0b111111
print(bin(a))  # 0b10101

# Operador >>=
print("---------- Operador >>= -----------")
x = 10
x >>= 1
print(x)  # 5

# Operador <<=
print("---------- Operador <<= -----------")
x = 10     # Inicializamos a 10
x <<= 1    # Desplazamos 1 a la izquierda
print(x)  # 20

# -> Operadores de Identidad
#       Nos indica si dos variables hacen referencia al mismo objeto

# Operador is
print("---------- Operador is -----------")
a = 10
b = 10
print(a is b)  # True

# Operador is not
print("---------- Operador is not -----------")
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # True


# -> Reto Opcional
print("----------- Opcional -------------------------")
for x in range(10, 56):
    if x % 2 == 0 and x != 16 and x % 3 != 0:
        print(x)
