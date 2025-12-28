"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

print("========== Operadores Aritméticos ==========")
# Declaramos dos variables
a = 10
b = 3
print("a = 10, b = 3")

# * Suma: Junta dos valores
suma = a + b
print("a + b:", suma)

# * Resta: Quita el segundo valor al primero
resta = a - b 
print("a - b:", resta)

# * Multiplicación: Repite el valor varias veces
multiplicacion = a * b
print("a * b:", multiplicacion)

# * División: Divide y devuelve un float (valor decimal)
division = a / b 
print("a / b:", division)

# * División entera: Divide y descarta los decimales
division_entera = a // b 
print("a // b:", division_entera)

# * Modulo: Devuelve lo que sobra de una división
modulo = a % b 
print("a % b:", modulo)

# * Potencia: Eleva el primer número al exponente del segundo
potencia = a ** b
print("a ** b:", potencia)


print("========== Operadores de Comparación ==========")
# Declaramos dos variables
a = 10
b = 3
print("a = 10, b = 3")

# * ¿Son iguales estos dos valores?
print(f"Igualdad: a == b es {a == b}") 

# * ¿Son distintos estos dos valores?
print(f"Desigualdad: a != b es {a != b}")

# * ¿El de la izquierda es mayor?
print(f"Mayor_que: a > b es {a > b}")

# * ¿El de la izquierda es menor?
print(f"Menor_que: a < b es {a < b}")

# * ¿Es mayor o exactamente igual?
print(f"Mayor_igual_que: a >= b es {a >= b}")

# * ¿Es menor o exactamente igual?
print(f"Menor_igual_que: a <= b es {a <= b}")

print("========== Operadores Lógicos ==========")
# Declaramos variables
edad = 18
tiene_id = True
permiso = False

print("Edad: 18, Tiene id")

# * Usamos "and" para decidir, recordamos que en "and" ambos datos deben ser verdaderos.
if edad >= 18 and tiene_id:
    print("Tiene acceso")
else:
    print("No tienes acceso")

# * Usamos "or" para decidir, recordamos que en "or" al menos uno de los datos debe ser verdadero. 
if edad >= 18 and (tiene_id or permiso):
    print("Tienes acceso")
else:
    print("No tienes acceso")

autorizacion = False

# * Aquí usamos "not", en este caso la autorización por defecto es negada.
if not autorizacion:
    print("No tienes acceso")
else:
    print("Tienes acceso")

print("========== Operadores de Asignación ==========")
# * "x" guarda "10"
x = 10
print(x)

# * Suma y guarda
x += 10 #! x = x + 10
print(x)

# * Resta y guarda
x -= 10 #! x = x - 10
print(x)

# * Multiplica y guarda
x *= 10 #! x = x * 10
print(x)

# * Divide y guarda
x /= 10 #! x = x /10
print(x)

# * Divide entero y guarda
x //= 10 
print(x)

# * Quedate con lo que sobra y guarda
x %= 10
print(x)

print("========== Operadores de Identidad ==========")
# Declaramos dos listas
a = [1, 2, 3]
b = [1, 2, 3]

print("a = [1, 2, 3]")
print("b = [1, 2, 3]")

print("lista a == lista b:", a == b) #* True: mismo contenido
print("lista a is lista b:", a is b) #* False: NO son el mismo objeto 

print("========== Operadores de Pertenencia ==========")
# Declaramos una lista
frutas = ["pera", "manzana", "piña"]

print("frutas =", frutas)

#* in revisa si un elemento está dentro de la lista
print("pera in frutas:", "pera" in frutas)

#* not in revisa si un elemento NO está dentro de la lista
print("piña not in frutas:", "piña" not in frutas)

print("=" * 44)
print("========== Estructuras de control ==========")
print("=" * 44)

print("========== Condicionales ==========")
# Declaramos variable
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")

print("========== Iterativas ==========")
print("== for ==")

for num in range (1, 11): 
    print(num) #* “Para cada número del 1 al 10, imprímelo”
#* Se cuantas veces repetir "for"

print("== while ==")

contador = 1

while contador <= 5:
    print(contador)
    contador += 1
#* Depende de una condición "while"

print("=" * 43)
print("========== Manejo de excepciones ==========")
print("=" * 43)

try:
    resultado = 10 / 0
except:
    print("Ocurrió un error")

#* Manejo con 'else'
try:
    numero = int("5")
except ValueError:
    print("Error")
else:
    print("Conversión exitosa:", numero) #* 'else' solo corre si no hubo excepción

#* 'finally'
try:
    numero = int("5")
except ValueError:
    print("Error")
finally:
    print("Esto siempre se ejecuta")

#* try:
    # código riesgoso
#* except TipoDeError:
    # qué hacer si falla
#* else:
    # qué hacer si todo salió bien
#* finally:
    # siempre se ejecuta

# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print("=" * 27)
print("========== EXTRA ==========")
print("=" * 27)

for num in range (10, 56):
    if num % 2 == 0 and num != 16 and num % 3: #* % pregunta: ¿que sobra? si sobra 0 = division exacta, != 0 hay residuo
        print(num)

