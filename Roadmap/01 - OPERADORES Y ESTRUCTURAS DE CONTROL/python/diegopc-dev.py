#Operadores y estructuras de control

#->Operadores ariméticos
print(f"Suma: 12 + 3 = {12 + 3}")
print(f"Resta: 12 - 3 = {12 - 3}")
print(f"Multiplicación: 12 * 3 = {12 * 3}")
print(f"División: 12 / 3 = {12 / 3}")
print(f"División entera: 12 // 3 = {12 // 3}")
print(f"Exponencial: 12 ** 3 = {12 ** 3}")
print(f"Módulo: 12 % 3 = {12 % 3}")

#->Operadores de comparación
print(f"Comparacion igualdad: 12 == 3 -> {12 == 3}")
print(f"Comparacion no es igual: 12 != 3 -> {12 != 3}")
print(f"Comparacion mayor que: 12 > 3 -> {12 > 3}")
print(f"Comparacion menor que: 12 < 3 -> {12 < 3}")
print(f"Comparacion mayor igual que: 12 >= 3 -> {12 >= 3}")
print(f"Comparacion menor igual que: 12 <= 3 -> {12 <= 3}")

#->Operadores lógicos
print(f"AND: Verdadero && verdadero -> {True and True}")
print(f"OR: Verdadero || falso -> {True or False} ")
print(f"NOT: !Falso -> {not False}")

#->Operadores de asignación
n = 10
print(f"Asignación: n = {n}")
n += 1
print(f"Suma con asignación: n += 1 -> {n}")
n -= 1
print(f"Resta con asignación: n -= 1 -> {n}")
n *= 2
print(f"Multiplicacion con asignación: n *= 2 -> {n}")
n /= 2
print(f"División con asignación: n /= 2 -> {n}")
n //= 2
print(f"Division entera con asignación: n //= 2 -> {n}")
n %= 2
print(f"Modulo con asignación: n %= 2 -> {n}")
n **= 2
print(f"Exponente con asignación: n **= 2 -> {n}")

#->Operadores de identidad
a = "hola"
b = "hola"
print(f"a esta en b {a is b}")
print(f"a no esta en b {a is not b}")

#->Operadores de pertenencia
print(f"'o' esta en 'hola' -> {'o' in 'hola'}")
print(f"'x' no esta en 'hola' -> {'x' not in 'hola'}")

#->Operadores de bit
a = 10  # 1010
b = 7  # 0111
print(f"AND: 10(1010) & 7(0111) = {a & b}")  # 0010
print(f"OR: 10(1010) | 7(0111) = {a | b}")  # 1111
print(f"XOR: 10(1010) ^ 7(0111) = {a ^ b}")  # 1101
print(f"NOT: ~10(1010) = {~10}")
print(f"Desplazamiento a la derecha: 8(1000) >> 2 = {8 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 1(0001) << 3 = {1 << 3}")  # 0100

#->Estructuras de control condicionales
hambre = True
frigo = "vacío"
if hambre:
    print("Necesito comer algo")
elif frigo == "vacío":
    print("Necesito hacer la compra antes")
else:
    print("A seguir escribiendo código")

#->Estructuras de control iterativas
nombre = "Diego"

for i in nombre:
    print(i)

i=0
while i <= 4:
    print(nombre[i])
    i+=1

#->Estructuras de control de excepciones
try:
    i=0
    while i <= 5:
        print(nombre[i])
        i+=1
except:
    print("Ocurrió un error")
finally:
    print("Se puede continuar con la ejecución despues del error")

#Extra
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)