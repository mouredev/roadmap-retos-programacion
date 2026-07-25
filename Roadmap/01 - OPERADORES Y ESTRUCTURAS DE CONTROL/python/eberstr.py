x = 9
y = 8

# Ejemplos operadores aritmeticos
print("operadores aritmeticos")
print(f'suma "x + y" {x + y}')
print(f'resta "x - y" {x - y}')
print(f'multiplicación "x * y" {x * y}')
print(f'división "x / y" {x / y}')
print(f'modulo "x % y" {x % y}')
print(f'Potencia "x ** y" {x ** y}')
print(f'División entera "x // y" {x // y}')

# Operadores lógicos
j= True
i = False
print("Operadores lógicos")
print(j)
print(i)
print(f'and "j and i" {j and i}')
print(f'or - "j or i" {j or i}')
print(f'not - "j not i" {j not i}')

# Operadores comparacion
print("Operadores comparacion")
print(f'Mayor que ">"; "x > y" {x > y}')
print(f'Mayor o igual que ">=" x > y" {x >= y}')
print(f'Menor que "<"; "x < y" {x < y}')
print(f'Menor o igual que "<="; "x <= y" {x <= y}')
print(f'igual que "=="; "x == y" {x == y}')
print(f'igual que "!="; "x != y" {x != y}')

# Operadores de asignación
a=0
print("Operadores de asignación")
print("Asignar a = 0")
a += 5
print(f"Suma 'a += 5' {a}")
a -= 5
print(f"Resta 'a -= 5' {a}")
a *= 5
print(f"Multiplicación 'a *= 5' {a}")
a /= 5
print(f"División 'a /= 5' {a}")
a %= 5
print(f"Modulo 'a %= 5' {a}")
a **= 5
print(f"Potencia 'a **= 5' {a}")
a // 5
print(f"Division entera 'a //= 5' {a}")

# Operadores de Identidad
print("Operadores de identidad")
print(f'is "x is y"  {x is y}')
print(f'is not "x is not y"  {x is not y}')

# Operadores de pertenencia
lista = [1, 3, 4]
print("Operadores de pertenencia")
print(f'in "x in lista" {x in lista}')
print(f'not in "x not in lista" {x not in lista}')

# Operadores de Bits
print("Operadores de Bits")
print(f"AND: 'x & y' {x & y}")
print(f"OR: 'x | y' {x | y}")
print(f"XOR: 'x ^ y' {x ^ y}")
print(f"NOT: '~10' {~x}")
print(f"Desplazamiento a la derecha: 'y >> x' {y>>y}")
print(f"Desplazamiento a la izquierda: 'y << x' {x<<y}")

# Estrucura de control if
a = 10
b = 30

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

# Estrucuta de control for
numeros = [18,50,90,-20,100,80,37]
for n in numeros:
    print(n)

# Estrucua de control while
x = 1
while x < 5:
    print(x)
    x += 1

# Estructura de control try/except
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

try:
    c = a / b 
except ZeroDivisionError:
    print("Estás intentando dividir por cero")


# Ejercicio extra
for i in range(10,56):
    if  i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

