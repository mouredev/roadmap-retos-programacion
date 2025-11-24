# Operadores

# Operadores aritmeticos 

print(f"La suma de 5 + 2 es {5 + 2}")
print(f"La resta de 10 - 10 es {10 - 20}")
print(f"La multiplicacion de 100 * 20 es {100 * 20}")
print(f"La division de 70 / 18 es {70 / 18}")
print(f"El modulo de 5 % 2 es {5 % 2}")
print(f"Dos al cuadrado es {2**2}")
print(f"La division por piso de 5 // 10 es {5 // 10}")

# Operaciones de comparacion

print(3 > 2)
print(2 < 3)
print(10 >= 100)
print(56 <= 10)
print("hola" == "hola")
print(2 != 3)

# Operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 5 * 2 == 10 or 5 / 2 == 1 es {5 * 2 == 10 or 5 / 2 == 1}")
print(f"NOT !: not 10 + 15 == 25 es {not 10 + 15 == 25}")

# Operaciones de asignacion
a = 5
print(a)
a += 10
print(a)
a -= 9
print(a)
a *= 2
print(a)
a /= 3
print(a)
a %= 4
print(a)
a **= 8
print(a)
a //= 5
print(a)

# Operadores de identidad
new_number = a
print(f"new_number is a es {new_number is a}")
print(f"new_number is a es {new_number is not a}")

# Operadores de pertenencia 
numbers = [1, 2, 3, 4, 5]
print(f"IN: 3 in numbers es {3 in numbers}")
print(f"NOT IN: 3 not in numbers es {3 not in numbers}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 es {10 & 3}") # 0010
print(f"OR: 10 | 3 es {10 | 3}") #  1011
print(f"XOR: 10 ^ 3 es {10 ^ 3}") # 1001
print(f"NOT: ~10 es {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 es {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 es {10 << 2}")

# Estructuras de control

# Condicionales

age = 18
if age >= 18: 
    print("Felicidades eres mayor de edad.")
elif age >= 80:
    print("Felicidades entraste a la etapa final de tu vida")
else:
    print("Eres menor de edad. Felicidades sigues siendo un chaval.")

# Iterativas

for i in range(3):
    print("Hola Python!")

while True:
    r = input("Bienvenidos a mi menu: \n" \
    "1. Decir hola." \
    "2. Salir")
    if r == 1:
        print("Hola")
    else:
        break

# Manejo de excepciones

try:
    print(10 / 0)
except:
    print("No se puede dividir entre 0")
finally:
    print("Gracias por ejecutarme")

# Ejercicio opcional

for i in range(10, 56):
    if i % 3 != 0 and i != 16 and i % 2 == 0:
        print(i)