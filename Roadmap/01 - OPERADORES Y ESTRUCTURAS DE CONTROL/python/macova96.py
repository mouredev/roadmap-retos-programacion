"""
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
"""
a = 5
b = 7
t=True
f=False

print("\n_________________________________________________")

print("OPERADORES ARITMETICOS")
print(f"Variable A= {a}")
print(f"Variable B= {b}")

print(f"\nA + B = {a+b:10} <--Suma")
print(f"A - B = {a-b:10} <--Resta")
print(f"A * B = {a*b:10} <--Multiplicación")
print(f"A / B = {a/b:10.2f} <--División")
print(f"A % B = {a%b:10} <--Módulo")
print(f"A ** B = {a**b:10} <--Exponenciación")
print(f"A // B = {a//b:10} <--Cociente")
print("\n_________________________________________________")

print("\nOPERADORES LÓGICOS")
print(f"Variable T= {t}")
print(f"Variable F= {f}")

print(f"\nT and F = {t and f:10} <--AND")
print(f"T or F = {t or f:10} <--OR")
print(f"not T = {not t:10} <--NOT")
print("\n_________________________________________________")

print("\nOPERADORES DE COMPARACION")
print(f"Variable A= {a}")
print(f"Variable B= {b}")

print(f"\nA == B = {a==b:10} <--Igualdad")
print(f"A != B = {a!=b:10} <--Desigualdad")
print(f"A < B = {a<b:10} <--Menor que")
print(f"A > B = {a>b:10} <--Mayor que")
print(f"A <= B = {a>=b:10} <--Menor o igual que")
print(f"A >= B = {a>=b:10} <--Mayor o igual que")
print("\n_________________________________________________")

print("\nOPERADORES DE ASIGNACIÓN")
x = 0
print(f"Variable x= {x}")
a = 5
print(f"\nA = 5 --> {a:10} <--Asignacion simple")
a += 3
print(f"A += 3 --> {a:10} <--Suma y asigna")
a -= 4
print(f"A -= 4 --> {a:10} <--Resta y asigna")
a *= 5
print(f"A *= 5 --> {a:10} <--Multiplica y asigna")
a /= 6
print(f"A /= 6 --> {a:10.2f} <--Divide y asiga")
a //= 7
print(f"A //= 7 --> {a:10} <--División entera y asigna")
a //= 7
print(f"A %= 8 --> {a:10} <--Módulo y asigna")
a //= 7
print(f"A **= 7 --> {a:10} <--Exponenciación y asigna")
a //= 7
print(f"A //= 7 --> {a:10} <--Divición entera y asigna")
print("\n_________________________________________________")

print("\nOPERADORES BIT A BIT")

# Definimos dos números enteros (representando valores binarios)
a_bin = 5  # En binario: 0101
b_bin = 3  # En binario: 0011

print(f"Variable A= {a_bin}")
print(f"Variable B= {b_bin}")

# Operadores bit a bit
print(f"\nA & B = {a_bin & b_bin:10} <--AND bit a bit")
print(f"A | B = {a_bin | b_bin:10} <--OR bit a bit")
print(f"A ^ B = {a_bin ^ b_bin:10} <--XOR bit a bit")
print(f"~A = {~a_bin:10} <--NOT bit a bit")
print("\n_________________________________________________")


print("\nOPERADORES DE IDENTIDAD")
"""
Compara sin dos objetos apuntan a la misma ubicacion en memoria
Esto es diferente de comparar si dos objetos tiene el mismo valor
"""
a_list = [1, 2, 3]
b_list = [1, 2, 3]
c_list = a_list

print(f"Lista A= {a_list}")
print(f"Lista B= {b_list}")
print(f"Lista C= {c_list} <-- c_list = a_list")

print(f"\nA is B = {a_list is b_list} <--Devuelve true si son el mismo objeto")
print(f"A is not B = {a_list is not b_list} <--Devuelve true si diferentes objetos")
print(f"A is C = {a_list is c_list} ")
print("\n_________________________________________________")

print("\nOPERADORES DE PERTENENCIA")
"""
Validad si un valor se encuentra dentro de una lista
"""
frutas = ["manzana", "pera", "banano"]
print(f"Lista de frutas = {frutas}")

print(f"\npera in frutas {"pera" in frutas} <--Develve true si el valor esta dentro de la lista")
print(f"zapote in frutas {"zapote" in frutas} <--Develve true si el valor NO esta dentro de la lista")

print("\n_________________________________________________")

print("\nESTRUCTURAS DE CONTROL - ITERATIVAS - EXCEPCIONES")
print("\nIF - ELIF - ELSE --> (EJEMPLO CALIFICACIONES)")

try:
    calificacion = int(input("Ingrese su calificación de 1 a 10\n"))

    if calificacion >= 9 :
        print("\nExcelente")
    elif calificacion >= 8 :
        print("\nMuy Bien")
    elif calificacion >= 7 :
        print("\nBien")
    elif calificacion >= 6 :
        print("\nRegualar")
    else:
        print("\nMal")

except ValueError:
    print("Error: debe ingresar un numero valido ")
