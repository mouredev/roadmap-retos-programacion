"""
Operadores
"""

# Operadores Aritméticos
sum = 10 + 5
print(f"Suma: 10 + 3 = {10 + 3}")
print(sum)
print(f"Resta: 20 - 8 = {20 - 8}")
print(f"Multiplicación: 6 * 6 = {6 * 6}")
print(f"División: 20 / 7 = {20 / 7}")
print(f"Módulo: 20 % 7 = {20 % 7}")
print(f"Exponente: 2 ** 4 = {2 ** 4}")
print(f"División Entera: 20 // 7 = {20 // 7}")

# Operadores de comparación // devuelve un valor True o False
print(f"Igual a: 10 == 3 es {10 == 3}")
print(f"No es igual: 10 != 3 es {10 != 3}")
print(f"Es mayor que: 10 > 3 es {10 > 3}")
print(f"Es menor que: 10 < 3 es {10 < 3}")
print(f"Es mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Es menor o igual que: 10 <= 8 es {10 <= 8}")

# Operadores lógicos
print(f"AND: 10 + 3 == 13 and 5 -1 == 4 es: {10 + 3 == 13 and 5 -1 == 4}")
print(f"OR: 10 + 9 == 16 and 5 -1 == 4 es: {10 + 9 == 16 or 5 -1 == 4}")
print(f"NOT: 20 + 7 == 24 es: {not 20 + 7 == 24}")

# Operadores de asigmación
mi_numero = 12 # = asignación
print(f"Mi número es: {mi_numero}")
mi_numero += 5 # + suma y asignación
print(mi_numero)
mi_numero -= 5 # - resta y asignación
print(mi_numero)
mi_numero *= 5 # * multiplicación y asignación
print(mi_numero)
mi_numero /= 4 # / división y asignación
print(mi_numero)
mi_numero %= 2 # % módulo y asignación
print(mi_numero)
mi_numero **= 8 # ** exponente y asignación
print(mi_numero)
mi_numero //= 12 # división exacta y asignación 
print(mi_numero)

# Operadores de identidad
mi_nuevo_numero = 0.0 # mismo valor numérico, distinta posición en memoria
print(f"mi_numero is mi_nuevo_numero es: {mi_numero is mi_nuevo_numero}")
mi_nuevo_numero = mi_numero # misma posición en memoria
print(f"mi_numero is mi_nuevo_numero es: {mi_numero is mi_nuevo_numero}")
print(f"mi_numero is not mi_nuevo_numero es: {mi_numero is not mi_nuevo_numero}")

# Operadores de pertenencia
print(f" 'a' está en 'mendoza' = 'a' in 'mendoza' = {'a' in 'mendoza'}")
print(f" 'b' no está en 'mendoza' = 'a' not in 'mendoza' = {'b' not in 'mendoza'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 & 3 = {10 | 3}") # 1011
print(f"XOR: 10 & 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10  = {~10}") # 1001 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

"""
Estrucuras de Control
"""

# Condicionales

mi_cadena = "AndresMendoza"
if mi_cadena == "AndresMendoza":
    print("mi_cadena es 'AndresMendoza'")
elif mi_cadena == "Figueroa":
    print("mi_cadena es 'Figueroa'")
else:
    print("mi_cadena no es ni 'AndresMendoza' ni tampoco 'Figueroa'")

# Iterativas

for i in range(11):
    print(i) #imprimirá de 0 a 10

x = 0

while x <= 10:
    print(x)
    x += 1 #imprimirá de 0 a 10

# Manejo de excepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el control de excepciones")

"""
Ejercicio extra
"""

for i in range(10,56):
    if i%2 == 0 and i != 16 and i%3 != 0:
        print(i, end= '-')