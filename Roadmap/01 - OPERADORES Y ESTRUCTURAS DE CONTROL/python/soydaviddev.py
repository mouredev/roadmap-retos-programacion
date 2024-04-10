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
num1 = 10
num2 = 3

# Aritméticos
print(num1 + num2) # Suma
print(num1 - num2) # Resta
print(num1 * num2) # Multiplicación
print(num1 / num2) # División
print(num1 % num2) # Módulo
print(num1 // num2) # División Entera
print(num1 ** num2) # Exponente

# Lógicos
logic1 = True
logic2 = False

resultado = logic1 and logic2
print(resultado)
resultado = logic1 or logic2
print(resultado)
resultado = not logic1
print(resultado)

# Comparación
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# Asignación
num1 = 20
print(num1)
num1 += 2
print(num1)
num1 -= 2
print(num1)
num2 *= 2
print(num2)
num2 /= 2
print(num2)
num2 %= 2
print(num2)
num1 //=2
print(num1)
num1 **=3
print(num1)

# Identidad
mi_lista = list()
mi_lista = [1 , 2, 3]
mi_other_lista = [1 , 2, 3]
print(mi_lista is mi_other_lista)

print(mi_lista is not mi_other_lista)

# Pertenencia
mi_saludo = "Hola, Mundo!"
print("M" in mi_saludo)

print("s" not in mi_saludo)

# Condicionales

if num1 > num2:
    print("El primero es mayor que el segundo")
elif num1 == num2:
    print("Son iguales")
else:
    print("El segundo es mayor que el primero")

# Iterativas

lenguajes = ["Python", "Java", "JavaScript", "Php"]

for lenguaje in lenguajes:
    print(f"Me gusta mucho aprender sobre {lenguaje}")

num1 = 10
num2 = 0
while num1 > num2:
    print(num2)
    num2+=2

#Excepciones
try:
    num_user = input("Dime un número")
    resultado = num1 / int(num_user)
    print(resultado)
except Exception:
    print("Entrada no válida, intenta que no sea 0 y no introducir texto.")
finally:
    print("El programa ha finalizado")


"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */
"""
num1 = 55
num2 = 10

while num2 < num1:
    if num2 % 2 == 0 and num2 !=16 and num2 % 3 != 0:
        print(num2)
    num2 += 2
    



    
