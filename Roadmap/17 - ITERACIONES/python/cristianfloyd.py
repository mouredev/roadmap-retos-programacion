# EJERCICIO:
# Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
# números del 1 al 10 mediante iteración.

def bucle_for():
    for i in range(1,11):
        print(f"Bucle FOR - numero: {i}")


def bucle_while():
    i: int = 1
    while i <= 10:
        print(f"Bucle while - numero: {i}")
        i += 1

# recursividad

def bucle_recursivo(i: int = 1):
    if i > 1:
        bucle_recursivo(i - 1)
    print(f"Funcion recursiva: {i}")


bucle_for()
bucle_while()
bucle_recursivo(10)


#
# DIFICULTAD EXTRA (opcional):
# Escribe el mayor número de mecanismos que posea tu lenguaje
# para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

print("=" * 80)
print("DIFICULTAD EXTRA (opcional):")
print("Escribe el mayor número de mecanismos que posea tu lenguaje")
print("para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?")
print("=" * 80)

# Mecanismos de iteracion

# 1. For con range
for i in range(1, 11):
    print(f"For con range - numero: {i}")

# 2. For con lista
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f"For con lista - numero: {i}")

# 3. For con tupla
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(f"For con tupla - numero: {i}")

# 4. For con set
for i in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
    print(f"For con set - numero: {i}")

# 5. For con diccionario
for i, value in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.items():
    print(f"For con diccionario - numero: {i} - valor: {value}")

# 6. For con string
for i in "Hello, World!":
    print(f"For con string - caracter: {i}")

# 7. For con enumerate
for i, value in enumerate("Hello, World!"):
    print(f"For con enumerate - numero: {i} - valor: {value}")

# 8. For con zip
for i, value in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]):
    print(f"For con zip - numero: {i} - valor: {value}")

# 9. For con reversed
for i in reversed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(f"For con reversed - numero: {i}")

# 10. For con sorted
for i in sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(f"For con sorted - numero: {i}")

# 11. For con generator
for i in (i for i in range(1, 11)):
    print(f"For con generator - numero: {i}")

# 12. For con iter
for i in iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(f"For con iter - numero: {i}")
