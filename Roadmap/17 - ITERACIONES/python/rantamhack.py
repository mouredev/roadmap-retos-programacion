'''
* EJERCICIO:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* numeros del 1 al 10 mediante iteracion.
'''

print("\n\n=======================================EJERCICIO=======================================\n\n")

# Usando 'for'

for i in range(1, 11):
    print(f"El valor de la iteracion en 'bucle for' para 'i' es: {i}")

print("\n=====================\n")    
    
# Usando 'while'    
    
n = 1    
while n < 11:
    print(f"El valor de la iteracion en bucle 'while' para 'n' es: {n}")
    n += 1
    
print("\n=====================\n")

# Usando 'while do'

n = 1
while True:
    if n > 10:
        break
    print(f"El valor de la iteracion en bucle 'do while' para 'n' es: {n}")
    n += 1    


print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


'''
* DIFICULTAD EXTRA (opcional):
* Escribe el mayor numero de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

# Iterar Cadena de Texto

texto = "rantamplan"

for c in texto:
    print(c)
    
print("\n=====================\n")
    
# Iterar lista

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)
    
print("\n=====================\n")
    
# Iterar tupla

for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(i)
    
print("\n=====================\n")

# Iterar set

for i in {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}:
    print(i)
    
print("\n=====================\n")

# Iterar diccionario por clave

for i in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.keys():
    print(i)
    
print("\n=====================\n")

# Iterar diccionario por valor

for i in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.values():
    print(i)
    
print("\n=====================\n")

# Iterando lista al reves

for i in reversed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i)
    
print("\n=====================\n")

# Iterando mediante recursividad


def recursive(x = 1):
    if x < 11:    
        print(x)
        recursive(x+1)


recursive()
