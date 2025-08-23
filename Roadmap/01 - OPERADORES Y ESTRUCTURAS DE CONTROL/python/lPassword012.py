#Operadores 

# Declaracion y asignacion de variables:
a, b = 10, 3
c = 5
x, y = True, False
lista = [1, 2, 3, 4, 5]
w, z = 5, 3

# Aritméticos
print("Concepto operaciones\n")
print("Es posible trabajar con diversas operaciones en Python.\nSe agrupan en las siguientes categorias:\n")
print("-Aritmeticos\n-Comparacion\n-Asignacion\n-Logicos\n-Identidad\n-Pertenencia\n-Bits\n")

print("Operadores Aritmeticos:")
print(f"Suma: {a} + {b} = ", a + b)
print(f"Resta: {a} - {b} = ", a - b)
print(f"Multiplicacion: {a} * {b} = ", a * b)
print(f"Division con parte decimal: {a} / {b} = ", a / b)
print(f"Division con parte entera: {a} / {b} = ", a // b)
print(f"Módulo: {a} % {b} = ", a % b)
print(f"Potencia: {a} ** {b} = ", a ** b)

# Comparación
print("\nOperadores de comparacion:")
print("Igualdad:", a == b)
print("Desigualdad:", a != b)
print("Mayor:", a > b)
print("Menor o igual:", a <= b)

# Asignación
c += 2  # Equivalente a c = c + 2
print("\nAsignacion:", c)

# Lógicos
print("\nOperadores logicos:")
print("AND logico:", x and y)
print("OR logico:", x or y)
print("NOT logico:", not x)

# Identidad
print("\nOperadores de identidad:")
print("Es el mismo objeto:", a is b)
print("No es el mismo objeto:", a is not b)

# Pertenencia
print("\nOperadores de pertenencia:")
print(f"Lista de numeros naturales: {lista}")
print(f"El {lista[2]} existe en la lista:", 3 in lista)
print(f"El {lista[4]} no existe en la lista:", 5 not in lista)

# Operadores de bits
print("\nOperadores de bits:")
print("AND bit:", w & z)
print("OR bit:", w | z)
print("XOR bit:", w ^ z)
print("\nDesplazamiento izquierda:", w << 1)
print("Desplazamiento derecha:", w >> 1)

# Estructuras de control
print("\nEstructuras de control:\n")

# Condicionales
print("Bifurcacion:")
edad = 28
print(f"La edad del usuario es {edad}")
if edad >= 18:
    print("Eres mayor de edad\n")
else:
    print("Eres menor de edad\n")

# Bucle iterativo - for
print("Bucles:")
print("Iterar en un rango 0...5 iterable:")
for i in range(5):
    print(f"Iteración {i}")

# Bucle iterativo - while
contador = 0
print("\nIterar sobre una condicion:")
while contador < 3:
    print(f"Contador en {contador}")
    contador += 1

# Manejo de excepciones
print("\nManejo de excepciones:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Fin del manejo de excepciones")

# Ejercicio extra:
print("\n========================")
print("Ejercicio extra:")
print("\nCrea un script que imprima por consola todos los numeros comprendidos")
print("Entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni multiplos de 3.")

numeros_comprendidos=[]

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        numeros_comprendidos.append(numero)

print(f"\nLista de numeros comprendidos: {numeros_comprendidos}")
