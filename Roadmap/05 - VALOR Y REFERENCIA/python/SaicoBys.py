# Asignación por valor (tipos de datos inmutables)
x = 5
y = x  # Se asigna una copia del valor de x a y

print("Antes de modificar y:", x, y)  # 5 5
y = 10

print("Después de modificar y:", x, y)  # 5 10 (x no cambia)

# Asignación por referencia (tipos de datos mutables)
lista1 = [1, 2, 3]
lista2 = lista1  # Se asigna una referencia a la misma lista

print("Antes de modificar lista2:", lista1, lista2)  # [1, 2, 3] [1, 2, 3]
lista2.append(4)

print("Después de modificar lista2:", lista1, lista2)  # [1, 2, 3, 4] [1, 2, 3, 4] (lista1 también cambia)

# Funciones y paso de parámetros
def modificar_por_valor(numero):
    """Modifica un número (paso por valor)."""
    numero = numero * 2  # Se modifica una copia local del número

def modificar_por_referencia(lista):
    """Modifica una lista (paso por referencia)."""
    lista.append(5)  # Se modifica la lista original

# Ejemplo de uso
a = 7
b = [6, 7, 8]

print("Antes de las funciones:", a, b)  # 7 [6, 7, 8]

modificar_por_valor(a)
modificar_por_referencia(b)

print("Después de las funciones:", a, b)  # 7 [6, 7, 8, 5] (a no cambia, b sí)

# Ejercicio

# Programa 1: Intercambio por valor (no funciona")
def intercambiar_por_valor(x, y):
    temp = x
    x = y
    y = temp

# Programa 2: Intercambio por referencia (funciona)
def intercambiar_por_referencia(lista):
    lista[0], lista[1] = lista[1], lista[0]

# Programa 1: Intercambio por valor (no funciona)
def intercambiar_por_valor(x, y):
    temp = x
    x = y
    y = temp

# Programa 2: Intercambio por referencia (funciona)
def intercambiar_por_referencia(lista):
    lista[0], lista[1] = lista[1], lista[0]

# Ejemplo de uso
a = 1
b = 2
c = [3, 4]

print("Antes:", a, b, c)  # 1 2 [3, 4]

intercambiar_por_valor(a, b)
intercambiar_por_referencia(c)

print("Después:", a, b, c)  # 1 2 [4, 3] (a y b no cambian, c sí)
