"""
Operadores
"""

def operadores_aritmeticos(a,b):
    print(f"Este es el operador de suma '+'\nmira el resultado de a y b de los dos numeros que proporcionaste: {a + b}")
    print(f"Este es el operador de resta '-'\nmira el resultado de a y b de los dos numeros que proporcionaste: {a - b}")
    print(f"Este es el operador de multiplicacion '*'\nmira el resultado de a y b de los dos numeros que proporcionaste: {a * b}")
    print(f"Este es el operador de division '/'\nmira el resultado de a y b de los dos numeros que proporcionaste: {a / b}")
    print(f"Este es el operador de potencia '**'\nmira el resultado de a y b de los dos numeros que proporcionaste: {a ** b}")
    print(f"Este es el operador llamado modulo '%'\nmira el resultado de a y b de los dos numeros que proporcionaste: {a % b}")
    print(f"Este es el operador de division entera '//' \nmira el resultado de a y b de los dos numeros que proporcionaste: {a // b}")
operadores_aritmeticos(20,80) # coloca dos numeros que quieras

# Operadores logicos: son and,or y not

def operadores_logicos(x,y):
    print(x==y and x > y)
    print(x >= y or x != y)
    print(not(x < y and x == y))

operadores_logicos(40,50)

#Operadores de comparacion:

def operadores_de_comparacion(a,b):
    print(f"IGUAL: a == b, seran iguales? {a==b}")
    print(f"DIFERENTE: a != b, seran distintos? {a != b} ")
    print(f"Mayor: a > b,es 'a' mayor que b? {a > b}")
    print(f"Menor: a < b es 'a' menor que b? {a < b}")
    print(f"Menor o igual: a <= b es 'a' menor o igual que 'b'? {a <= b}")
    print(f"Mayor o igual: a >= b es 'a' mayor o igual que 'b'? {a <= b}")

operadores_de_comparacion(90,50)

# Operadores de asignacion

a = 5
a += 3
print(f"Suma y asignación (a += 3): {a}")
a -= 2
print(f"Resta y asignación (a -= 2): {a}")
a *= 4
print(f"Multiplicación y asignación (a *= 4): {a}")
a /= 2
print(f"División y asignación (a /= 2): {a}")
a **= 2
print(f"Potencia y asignación (a **= 2): {a}")
a //= 3
print(f"División entera y asignación (a //= 3): {a}")
a %= 2
print(f"Módulo y asignación (a %= 2): {a}")

# Operadores de identidad: son is y is not,algo parecidos a los de comparacion

def operadores_de_identidad(a,b):
    print(f"'is' me devuelve true si estos son iguales,sera cierto que {a} is {b}? {a is b}")
    print(f"'is not' me devuelve true si estos son diferentes,sera cierto que {a} is not {b}? {a is not b}")
operadores_de_identidad('HOLA','HUESO')

# Operadores de pertenencia: in y not in

def operadores_de_pertenencia(a,b):
    print(f" '{a} in {b}' in devolvera True si '{a}' no esta en la frase {b}, veamos si es cierto {a in b}")
    print(f" '{a} not in {b}' not in devolvera True si '{a}' no esta en la frase {b}, veamos si es cierto {a not in b}")

operadores_de_pertenencia("a","barcelona")

def operadores_de_bit(a,b): # Parecidos a los operadores logicos
    print(f"AND: {a} & {b} = {a & b} ")
    print(f"OR: {a} | {b} = {a | b} ") #
    print(f"XOR: {a} ^ {b} = {a ^ b} ")
    print(f"NOT: ~{a} = {~a}")
    print(f"Desplazamiento a la derecha: {a} >> {b} = {a >> b} ")
    print(f"Desplazamiento a la izquierda: {a} << {b} = {a << b} ")

operadores_de_bit(10,3)

"""
Estructuras de control
"""

# Estructura de control condicional
def condicionales():
    prompt1 = input("escriba un numero: ")
    prompt2 = input("Escriba otro numero: ")
    if prompt1 < prompt2:
        print(f" Si {prompt1} es menor que {prompt2}")
    elif prompt1 > prompt2:
        print(f" en este caso {prompt1} es mayor que {prompt1}")
    else:
        print("los numeros son iguales")
condicionales()

# Iterativas
for i in range (6):
    print("Hola Brais,esto es un bucle for")

n = 20
while n != 3:
    print(n)
    n -= 1

# excepciones
try:
    print(0/0)
except:
    print("Hay un error")
finally:
    print("Como vas a dividr 0/0?")
"""
EXTRA
"""

for j in range(9,56):
    if j == 16:
        continue
    elif j % 3 == 0:
        print(j)
    else:
        continue

print("WALAAAAAAA!")