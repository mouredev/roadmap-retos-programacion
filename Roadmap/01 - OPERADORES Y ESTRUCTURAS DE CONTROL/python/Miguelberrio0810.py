# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa otro numero: "))

def condicionales(n1, n2):
    if (n1 > n2):
        print(f"numero 1 : {n1}, es mayor que numero {n2}")
    else:
        print(f"numero 2: {n2}, es mayor que numero 1: {n1}")

def iteraciones(n):
    for i in range(n, 21):
        print(n)
        n += 1
        break

def Suma(n1, n2):
    return n1 + n2

def Resta(n1, n2):
    return n1 - n2

def Division(n1, n2):
    return n1 / n2

def Multiplicacion(n1, n2):
    return n1 * n2

def Exponeciacion(n1, n2):
    return n1 ** n2

def imprimir_numeros(n1, n2):
    for i in range(10, 56):  # Rango de 10 a 55, 56 no está incluido
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)


print(condicionales(n1, n2))
print(iteraciones(8))
print(Suma(n1, n2))
print(Resta(n1, n2))
print(Division(n1, n2))
print(Multiplicacion(n1, n2))
print(Exponeciacion(n1, n2))
print(imprimir_numeros(n1, n2))

print("Fin del Juego, Gracias!")