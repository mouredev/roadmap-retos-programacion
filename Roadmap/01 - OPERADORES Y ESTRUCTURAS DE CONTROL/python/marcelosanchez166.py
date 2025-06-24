"""EJERCICIO:
  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...

  - Debes hacer print por consola del resultado de todos los ejemplos.
  DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo."""


# 1. Operadores Aritmeticos

suma = 1 + 2
resta = 2 - 1
multiplicacion = 3 * 4
division = 25 / 5
division_entera = 15 // 4
modulo = 4 % 2
exponente = 3 ** 2

# 2. Operadores de Comparación:

igualdad = 5 == 5
menor_que = 5 < 6
mayor_que = 7 > 3
menor_igual_que = 4 <= 5
mayor_igual_que = 5 >= 2
diferente_de = 7 != 6

is_ = suma is resta
is_not = resta is not multiplicacion
print(is_, is_not)

# 3. Operadores Lógicos:

and_ = igualdad and menor_que
or_ = mayor_igual_que or menor_igual_que
not_ = not igualdad

print(and_, or_, not_)


# 4. Operadores de asignacion

# asignando el entero 5 a la variable x
x = 5
# Suma y asigna.
x += 3
# Resta y asigna
x -= 2
# Multiplica y asigna
x *= 4
# Divide y asigna
x /= 10
# Módulo y asigna
x %= 3


# Operaciones con operadores:  Condicionales, iterativas, excepciones...
if suma:
    print(suma)

valor = 5
for i in range(1, valor+1):
    if i == 5:
        print("soy igual que el valor de la variable")
    else:
        print(i)


for i in range(10, 0, -2):
    if i >= 3:
        print("numero es mayor o igual a 3")
    else:
        print(i)

frutas = ['manzana', 'banana', 'uva']

for fruta in frutas:
    if "tomate" not in frutas:
        print("No esta en la lista")

nombres = ['Ana', 'Luis', 'Mario']

for i, nombre in enumerate(nombres):
    if "Ana" == nombre:
        print("El nombre Ana si existe en la lista")
    else:
        print(f"{i}: {nombre}")

persona = {'nombre': 'Juan', 'edad': 30}

for clave in persona:
    print(clave)


for clave, valor in persona.items():
    print(f"{clave}: {valor}")


for letra in "Hola":
    print(letra)

contador = 0
while contador < 5:
    print(contador)
    contador += 1


numero = 0
while numero <= 0:
    try:
        numero = int(input("Ingrese un número positivo: "))
        if numero <= 0:
            print("El número debe ser positivo.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")
print("Número válido ingresado:", numero)

while True:
    entrada = input("Ingrese 'salir' para terminar: ")
    if entrada.lower() == "salir":
        break
    print("Entrada:", entrada)


numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Salta el resto del código en esta iteración si es par
    print(numero)


