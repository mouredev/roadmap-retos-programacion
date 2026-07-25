# Operadores aritméticos
x = 5; y = 10
print(f"Dado los valores: x = {x}; y = {y}")
print(f"Suma: x + y = {x + y}")
print(f"Resta: x - y = {x - y}")
print(f"Multiplicación: x * y = {x * y}")
print(f"División: x / y = {x / y}")
print(f"Módulo: y % x = {y % x}")
print(f"Exponenciación: y ** x = {y ** x}")
print(f"Cociente: x // y = {x // y}")

# Operadores relacionales o de comparación - Devuelven True o False
print("")
print(f"Igual: x == y = {x == y}")         # False
print(f"Distinto: x != y = {x != y}")      # True
print(f"Mayor: x > y = {x > y}")           # False
print(f"Menor: x < y = {x < y}")           # True
print(f"Mayor o igual: x >= y = {x >= y}") # False
print(f"Menor o igual: x <= y = {x <= y}") # True

# Operadores lógicos
x = True; y = False
print("")
print(f"Dado los valores: x = {x}; y = {y}")
print(f"and - y lógico: x and y = {x and y}") # False
print(f"or - o lógico: x or y = {x or y}")    # True
print(f"not - negación: not x = {not x}")     # False
print(f"not - negación: not y = {not y}")     # True

# Operadores bitwise - a nivel de bit
a = 0b1101   # 13
b = 0b1011   # 11
print("")
print(f"Dados dos numeros: a = {a} y b = {b}")
print(f"And a nivel de bits: a & b = {a & b}")       # 1001 = 9
print(f"Or a nivel de bits: a | b = {a | b}")        # 1111 = 15
print(f"Not a nivel de bits: ~a = {~a} y ~b = {~b}") # -14 y -12 => ~a = -a - 1
print(f"XOR bit a bit: a ^ b = {a ^ b}")             # 0110 = 6  => Es 1 para 1, 0 o 0, 1
print(f"Desplazamiento a la derecha: 10 >> 1 = {10 >> 1}")   # 1010 => 0101 = 5
print(f"Desplazamiento a la izquierda: 10 << 1 = {10 << 1}") # 1010 => 10100 = 20

# Operadores de asignación
a=7; b=2
print("")
print("Operadores de asignación")
print(f"Dado los valores a = {a}, b = {b} y x = {a}")
x=a; x+=b;  print("x += ", x)  # 9
x=a; x-=b;  print("x -= ", x)  # 5
x=a; x*=b;  print("x *= ", x)  # 14
x=a; x/=b;  print("x /= ", x)  # 3.5
x=a; x%=b;  print("x %= ", x)  # 1
x=a; x//=b; print("x //= ", x) # 3
x=a; x**=b; print("x **= ", x) # 49
x=a; x&=b;  print("x &= ", x)  # 2  
x=a; x|=b;  print("x |= ", x)  # 7   
x=a; x^=b; print("x ^= ", x)   # 5  
x=a; x>>=b; print("x >>= ", x) # 1
x=a; x<<=b; print("x <<= ", x) # 28    

# Operadores de identidad
x = 10; y = 10; z = 5
print("")
print(f"Dado los valores x = {x}; y = {y}")
print(f"x y y son el mismo objeto = {x is y}")  # is comprueba si dos variables hacen referencia a el mismo objeto.
print(f"x y y no son el mismo objeto = {x is not y}") # False

# Operadores de pertenencia o de membresía
print("")
print(f"La letra a esta en murciélago = {'a' in 'murciélago'}")
print(f"El número 3 no esta en la lista [1, 2, 4, 5] = {3 not in [1, 2, 4, 5]}")
print("")

# Estructuras de Control

# Condicionales 

# Uso de if - else - elif
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")

# Operador ternario
a = 10
b = 5
c = a / b if b != 0 else -1
print(c)                     # Imprime 2.0

# Bucle for
for i in range(0, 5):
    print(i)
# Salida:
# 0
# 1
# 2
# 3
# 4

for i in "Python":
    print(i)
# Salida:
# P
# y
# t
# h
# o
# n

# Bucle while
x = 5
while x > 0:
    x -= 1
    print(x)
# Salida: 4,3,2,1,0

# Sucesión de Fibonacci
print("Sucesión de Fibonacci")
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b
#1, 1, 2, 3, 5, 8, 13, 21

# Match - En python es similar al switch
hora = 8
match hora:
    case 8:
        print("Desayuno")
    case 14:
        print("Comida")
    case 21:
        print("Cena")
    case _:                       # _ caso por defecto
        print("No toca comer")
# Desayuno


print("")
print("Reto Extra")
print("")

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

print("Usando List comprehensions")
print([i for i in range(10, 56) if i % 2 == 0 and i != 16 and i % 3 != 0])
