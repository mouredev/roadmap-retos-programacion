"""
* EJERCICIO:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* números del 1 al 10 mediante iteración.
"""

def imprimir_numeros_1() -> None:
    for i in range(1, 11):
        print(i)
imprimir_numeros_1()
print("\n")

def imprimir_numeros_2(lista_numeros: list) -> None:
    for numero in lista_numeros:
        print(numero)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
imprimir_numeros_2(lista)
print("\n")

def imprimir_numeros_3() -> None:
    parar = False
    numero = 1
    while not parar:
        print(numero)
        numero += 1
        if numero > 10:
            parar = True
imprimir_numeros_3()
print("\n")

def imprimir_numeros_4(i: int) -> None:
    print(i)
    if i >= 10:
        return
    imprimir_numeros_4(i + 1)
imprimir_numeros_4(1)
print("\n")

"""
* DIFICULTAD EXTRA (opcional):
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

for e in {1, 2, 3, 4, 4}:
    print(e)
print("\n")

for e in {1 : "q", 2 : "w", 3 : "e", 4 : "r", 5 : "t", 6 : "y"}:
    print(e)
print("\n")

for e in {1 : "q", 2 : "w", 3 : "e", 4 : "r", 5 : "t", 6 : "y"}.items():
    print(e)
    print(type(e))
print("\n")

for e in {1 : "q", 2 : "w", 3 : "e", 4 : "r", 5 : "t", 6 : "y"}.values():
    print(e)
    print(type(e))
print("\n")

print(*[i for i in range(1, 11)], sep = "\n")
print("\n")

for indice, c in enumerate(sorted(["M", "a", "r", "c", "o", "s"])):
    print(f"Este es la posición {indice}, y este el valor {c}.")