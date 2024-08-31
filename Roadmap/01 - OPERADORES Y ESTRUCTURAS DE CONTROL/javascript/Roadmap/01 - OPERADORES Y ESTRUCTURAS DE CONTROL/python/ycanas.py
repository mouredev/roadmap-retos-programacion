# --------- Operadores

# --- I. Asignación

# 1. Asignar un valor

A = 10
print(f"A = {A}")

# 2. Asignar y realizar operación

""" Los operadores de asignación son herramientas que
permiten combinar operadores aritméticos y de bits
para asignar y operar valores de manera abreviada.
Estos operadores se presentan en formas como 

    +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=

donde se fusiona primero el operador aritmético con el
operador de asignación correspondiente. """

A += 10
print(f"A += 10 = {A}")


# --- II. Aritmeticos

# 1. Suma

""" Juan tenía 5 manzanas y su amigo le dio 3 manzanas más.
 ¿Cuántas manzanas tiene ahora en total? """

A = 5
B = 3

C = A + B
print(f"Juan tiene en total {C} manzanas.")

# 2. Resta

""" Si un DVD cuesta $10 y tienes $7,
¿cuánto falta para poder comprarlo? """

A = 10
B = 7

C = A - B
print(f"Faltan {C}$ para comprar el DVD.")

# 3. Multipliación

""" Una caja contiene 6 paquetes de galletas,
cada paquete tiene 12 galletas.
¿Cuántas galletas hay en total? """

A = 6
B = 12

C = A * B
print(f"En total hay {C} galletas.")

# 4. División

""" Tienes 18 dulces y quieres compartirlos
entre 6 amigos de manera equitativa.
¿Cuántos dulces le tocan a cada amigo? """

A = 18
B = 6

C = A / B
print(f"A cada amigo le tocan {C} dulces.")

# 5. División entera

""" Un pastel se corta en 8 porciones iguales.
Si quieres repartirlo entre 3 personas,
¿cuántas porciones enteras recibirá cada persona? """

A = 8
B = 3

C = A // B
print(f"Cada persona recibira {C} porciones enteras.")

# 6. Módulo

""" Si divides 25 entre 7, ¿cuál es el resto? """

A = 25
B = 7

C = 25 % 7
print(f"El resto de la división es {C}.")

# 7. Potencia

""" Si un cuadrado tiene un lado de longitud 5 cm, ¿cuál es su área? """

A = 5

B = 5 ** 2
print(f"El área del cuadrado es {B}.")


# --- III. Comparación

# 1. Igual

""" Comparar si los números 2 y 8 son iguales """

A = 2
B = 8

C = A == B
print(f"¿Los números {A} y {B} son iguales?: {C}")

# 2. Diferente

""" Comparar si los números 2 y 8 son diferentes """

C = A != B
print(f"¿Los números {A} y {B} son diferentes?: {C}")

# 3. Mayor

""" Comparar si el número 8 es mayor que el número 2 """

C = B > A
print(f"¿El número {B} es mayor que el número {A}?: {C}")

# 4. Menor

""" Comparar si el número 8 es menor que el número 2 """

C = B < A
print(f"¿El número {B} es menor que el número {A}?: {C}")

# 5. Mayor o igual

""" Comparar si el número 2 es mayor o igual que el número 8 """

C = A >= B
print(f"¿El número {A} es mayor o igual que el número {B}?: {C}")

# 6. Menor o igual

""" Comparar si el número 2 es menor o igual que el número 8 """

C = A <= B
print(f"¿El número {A} es menor o igual que el número {B}?: {C}")


# --- IV. Lógicos

# 1. and

""" Para asistir a un concierto, se requiere que el
individuo sea mayor de 18 años y tenga su boleto. 
Si cumple ambas condiciones, se le permite el acceso. """

A = 18
B = True

C = (A > 18) and B
print(f"¿Puede ingresar al concierto?: {C}.")

# 2. or

""" En una tienda, se ofrece un descuento del 10%
si el cliente compra más de 5 artículos o si el
total de la compra supera los $100. """

A = 4
B = 101

C = (A > 5) or (B > 100)
print(f"¿Aplica al descuento?: {C}.")

# 3. not

""" Para entrar a un laboratorio se requiere que 
la persona no tenga enfermedades """

A = True

B = not A
print(f"¿La persona puede entrar?: {B}.")


# --- V. Identidad

# 1. is

""" Verificar si la variable A es un dato nulo """

A = None

B = A is None
print(f"¿La variable A es un dato nulo?: {B}")

# 2. is not

""" Verificar si la variable A no es un dato nulo """

A = None

B = A is not None
print(f"¿La variable A no es un dato nulo?: {B}")

# --- VI. Pertenencia

# 1. in

""" Verificar si la letra 'n' esta en la palabra 'hola' """

A = 'n'
B = 'hola'

C = A in B
print(f"¿La letra {A} esta en la palabra {B}? {C}.")

# 2. not in

""" Verificar si la letra 'n' no esta en la palabra 'hola' """

A = 'n'
B = 'hola'

C = A not in B
print(f"¿La letra {A} no esta en la palabra {B}? {C}.")

# --- VII. Bits

# 1. and

A = 10
B = 5

C = A & B
print(f"{A} & {B} = {C}")

# 2. or

A = 10
B = 5

C = A | B
print(f"{A} | {B} = {C}")

# 3. xor

A = 10
B = 5

C = A ^ B
print(f"{A} ^ {B} = {C}")

# 4. not

A = 10

B = ~A
print(f"~{A} = {B}")

# 5. Dezplazamiento a la izquierda

A = 10
B = 5

C = A << B
print(f"{A} << {B} = {C}")

# 6. Dezplazamiento a la derecha

A = 10
B = 5

C = A >> B
print(f"{A} >> {B} = {C}")

print('-' * 100)


# --------- Estructuras de Control

# --- I. condicionales

# 1. if

A = 10
B = A

if A is B: print("A is B")

# 2. else
    
if A is B:
    print("A is B")
else:
    print("A not is B")

# 3. elif
    
A = 10
B = 7

if A == B:
    print("A == B")
elif A < B:
    print("A < B")
else:
    print("A > B")


# --- II. Bucles
    
# 1. for
    
numeros = [i for i in range(10)]

for numero in numeros:
    print(numero, end=' ')

print()

# 2. while

A = 100

while not A == 0:
    print(A, end=' ')
    A = A // 2

print()

# 3. break

A = 100

while True:
    A = A - 10

    if A < 50:
        break

# 4. continue
    
for i in range(6):
    if i == 0:
        continue

    print(i, end=' ')

print()

# 5. pass
    
def hola():
    pass

print("Esto no ejecuta nada")

# --- III. Excepciones

# 1. try

A = 5
B = '2'

try:
    C = A + B
except:
    print("Error.")

# 2. finally
    
try:
    C = A + B
except:
    print("Error.", end=' ')
finally:
    C = 0

print(C)

print('-' * 100)


# --------- Extra

for i in range(10, 56):
    if i == 16 or i % 3 == 0:
        continue

    if i % 2 == 0:
        print(i)
