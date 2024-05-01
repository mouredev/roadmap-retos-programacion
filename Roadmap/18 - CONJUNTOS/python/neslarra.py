"""
 EJERCICIO:
 Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 operaciones (debes utilizar una estructura que las soporte):
 - Añade un elemento al final.
 - Añade un elemento al principio.
 - Añade varios elementos en bloque al final.
 - Añade varios elementos en bloque en una posición concreta.
 - Elimina un elemento en una posición concreta.
 - Actualiza el valor de un elemento en una posición concreta.
 - Comprueba si un elemento está en un conjunto.
 - Elimina todo el contenido del conjunto.

 DIFICULTAD EXTRA (opcional):
 Muestra ejemplos de las siguientes operaciones con conjuntos:
 - Unión.
 - Intersección.
 - Diferencia.
 - Diferencia simétrica.
"""

print(f"##  Explicación  {'#' * 30}\n")

print(f"""Un conjunto es una colección no ordenada de objetos únicos => no tiene índice, ni primero ni último.
Se le pueden agregar elementos (método add), eliminar elementos (método remove) o eliminar TODOS los elementos (método clear).
Un conjunto es iterable.
Un conjunto vacío se puede crear con: "vacio = set()", PERO no con: "vacio = {{}}"  <= lo cual crea un diccionario vacío.
También se pueden crear asignando elementos directamente al conjunto: "numeros = {{1, 2, 3, 4, 5}}"
Si al conjunto le pasamos elementos "repetidos", se filtrarán las repeteciones: "numeros = {{1, 2, 3, 1, 3}}" => queda como: "numeros = {{1, 2, 3}}"
Tiene métodos para ejecutar operaciones de conjunto: intersection, union, issubset (incluído), issuperset (incluye), symmetric_difference (unión
excluyente), etc, las cuales se pueden explorar con la función "dir(set())"   
""")

cero = set()
primos = set()
no_primos = set()

cero.add(0)

primos.add(1)
primos.add(2)
primos.add(3)
primos.add(5)
primos.add(7)

no_primos.add(4)
no_primos.add(6)
no_primos.add(8)
no_primos.add(9)

digitos = cero.union(primos).union(no_primos)

print(f"Conjuntos:\n\tCero: {cero}\n\tPrimos: {primos}\n\tNo primos {no_primos}\n\tDígitos: {digitos}\n")
print(f"Elementos comunes por intersección: {cero.intersection(primos).intersection(no_primos).__len__()}\n")

digitos = digitos.union({2, 4, 5, 7, 11, 14, 15})
print(f"Agrego más números a digitos {digitos}\n")
print("Subconjuntos:")
print(f"\tPrimos está incluído en dígitos: {primos.issubset(digitos)}\n\tDígitos incluye no primos: {digitos.issuperset(no_primos)}")
print("También podemos usar operadores:")
print(f"\tPrimos está incluído en dígitos: {primos < digitos}\n\tDígitos incluye no primos: {no_primos < digitos}\n")
print(f"Se puede crear un conjunto por comprehensión:")
pares_mayores = set(x for x in digitos if (x > 9) and (x % 2 == 0))
impares_mayores = {x for x in digitos if (x > 9) and (x % 2 == 1)}
print(f"\tPares mayores: {pares_mayores}\n\tImpares mayores: {impares_mayores}\n")
print("Se puede itarar (recorro la union de los conjuntos pares e impoares mayores y los elimino de digitos):")
for n in pares_mayores.union(impares_mayores):
    digitos.remove(n)
print(f"\t{digitos}")
print("\nElimino TODOS los elementos de pares e impares mayores:")
pares_mayores = pares_mayores.clear()
impares_mayores = impares_mayores.clear()
print(f"\tpares_mayore = {pares_mayores}")
print(f"\timpares_mayores = {impares_mayores}\n")
print("Un conjunto puede ser inmutable: digitos = frozenset(digitos)")
digitos = frozenset(digitos)
try:
    digitos.add(10)
except Exception as e:
    print(f"\t{e.__str__()}\n")
print(f"Teniendo digitos = {digitos}, primos = {primos} y no_primos = {no_primos}")
print(f"Intersección:\n\t{digitos.intersection(primos)}")
print(f"Unión:\n\t{digitos.union(no_primos)}")
print(f"Diferencia:\n\t{digitos.difference(primos)}")
print(f"Unión exclusiva:\n\t{digitos.symmetric_difference(no_primos)}")


print(f"\n##  Dificultad extra  {'#' * 30}\nIncluída en la explicación!!!")
