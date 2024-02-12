# Operadores de asignación.
x = 10
y = 2
z = x + y
verdadero = True
falso = False
lista = [10, 2]

operadores_aritmeticos = [('+', "Suma"), ('-', "Resta"), ("*", "Multiplicación"), ('/', "División"), ('**', "Exponenciación"), ('%', "Módulo"), ('//', "División entera")]

print("Operadores aritméticos.\n")
for operador in operadores_aritmeticos:
    resultado = eval(f'{x} {operador[0]} {y}')
    print(f'{x} {operador[0]} {y} = {resultado} - {operador[1]}')

print("\nOperadores lógicos.\n")
print(f"Verdadero y Falso: {verdadero and falso}")
print(f"Verdadero o Falso: {verdadero or falso}")
print(f"Verdadero y no Falso: {verdadero and not falso}")
print("\nOperadores de comparación.\n")
print(f"{x} es igual a {y}: {x == y}")   
print(f"{x} es diferente a {y}: {x != y}")   
print(f"{x} es mayor que {y}: {x > y}")    
print(f"{x} es menor que {y}: {x < y}")    
print(f"{x} es mayor o igual que {y}: {x >= y}")   
print(f"{x} es menor o igual que {y}: {x <= y}")   

print("\nOperadores de identidad. \n")
print(f"¿x es z?: {x is z}")
print(f"¿x no es z?: {x is not z}")

print("\nOperadores de pertenencia.\n")
print(f"¿x está en la lista?: {x in lista}")
print(f"¿y no está en la lista?: {y not in lista}")

print("\nOperadores de bits\n")
print(f"AND: {x & y}")
print(f"OR: {x | y}")
print(f"XOR: {x ^ y}")
print(f"Desplazamiento a la izquierda: {x << 1}")
print(f"Desplazamiento a la derecha: {y >> 1}")
print(f"Complemento a uno de {x}: {~x}")

# if
# elif 
# else
# while
# for
# break
# continue
# pass
# try
# excep
# finally

print("\nEstructura de control if")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("\nEstructura de control while")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

print("\nEstructura de control for con pass")
for i in range(5):
    if i == 3:
        pass 
    else:
        print(i)

print("\nEstructura de control else en bucle")
for i in range(3):
    print(f"Iteración {i}")
else:
    print("El bucle ha finalizado.")

print("\nEstructura de control if-else en una línea")
valor = 10
resultado = "Par" if valor % 2 == 0 else "Impar"
print(f"El número {valor} es {resultado}.")

print("\nEstructura de control break y continue")
for num in range(10):
    if num == 5:
        print("Encontré el número 5. Salgo del bucle.")
        break
    elif num % 2 == 0:
        print(f"Número par: {num}")
        continue
    print(f"Número impar: {num}")

print("\nEstructura de control try, except, finally")
try:
    print("Vamos a hacer una división.")
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    resultado = numerador / denominador
    print(f"Resultado de la división: {resultado}")
except ValueError:
    print("Error: Ingrese números enteros.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Este bloque siempre se ejecuta, independientemente de las excepciones.")

print("\nEjercicio EXTRA")
for _ in range(10, 56):
    if _ % 2 == 0 and _ != 16 and _ % 3 != 0:
        print(_)