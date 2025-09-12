# ===============================
# 1. ARITHMETIC OPERATORS
# ===============================
print("🔢 Arithmetic Operators")

a = 10
b = 3.2
c = 2
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print("always returns a floating-point number")
print(f"Floor Division: {a} // {b} = {a // b}")
print("return an integer result")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {c} = {a ** c}")
print("The equal sign (=) is used to assign a value to a variable")
print(f"There is full support for floating point; 
operators with mixed type operands convert the 
integer operand to floating point:")

# ===============================
# 2. COMPARISON OPERATORS
# ===============================
# Se usan para comparar valores y devuelven booleanos (True o False).

es_igual = a == b            # False
es_diferente = a != b        # True
mayor = a > b                # True
menor = a < b                # False
mayor_o_igual = a >= b       # True
menor_o_igual = a <= b       # False

print("\n🔍 Comparison Operators")
print(f"== : {es_igual}, != : {es_diferente}, > : {mayor}, < : {menor}")
print(f">= : {mayor_o_igual}, <= : {menor_o_igual}")

print(f"{a} == {b} ➜ {a == b}")
print(f"{a} != {b} ➜ {a != b}")
print(f"{a} > {b} ➜ {a > b}")
print(f"{a} < {b} ➜ {a < b}")
print(f"{a} >= {b} ➜ {a >= b}")
print(f"{a} <= {b} ➜ {a <= b}")

# ===============================
# 3. LOGICAL OPERATORS
# ===============================
# Se usan para combinar expresiones booleanas.

x = True
y = False

resultado_and = x and y  # False
resultado_or = x or y    # True
resultado_not = not x    # False

print("\n🔐 Logical Operators")
print(f"{x} and {y} ➜ {resultado_and}")
print(f"{x} or {y} ➜ {resultado_or}")
print(f"not {x} ➜ {resultado_not}")

# ===============================
# 4. ASSIGNMENT OPERATORS
# ===============================
# Se usan para asignar valores y modificarlos directamente.

z = 5
z += 3  # z = z + 3 → 8
z -= 2  # z = z - 2 → 6
z *= 2  # z = z * 2 → 12
z /= 3  # z = z / 3 → 4.0
z %= 2  # z = z % 2 → 0.0

print(f"z = {z}")
print(f"z += 3 ➜ {z}")
print(f"z -= 2 ➜ {z}")
print(f"z *= 2 ➜ {z}")
print(f"z /= 3 ➜ {z}")
print(f"z %= 2 ➜ {z}")

print("\n🖋 Assignment Operators")
print(f"Resultado final de z: {z}")

# ===============================
# 5. IDENTITY OPERATORS
# ===============================
# Comparan si dos variables apuntan al mismo objeto en memoria.

lista_1 = [1, 2, 3]
lista_2 = [1, 2, 3]
lista_3 = lista_1

misma_identidad = lista_1 is lista_3     # True
diferente_identidad = lista_1 is not lista_2  # True (aunque tengan el mismo contenido)

print("\n🪞 Identity Operators")
print(f"lista_1 is lista_3 ➜ {misma_identidad}")
print(f"lista_1 is not lista_2 ➜ {diferente_identidad}")

# ===============================
# 6. MEMBERSHIP OPERATORS
# ===============================
# Verifican si un valor está (o no está) presente en una secuencia.

frutas = ["manzana", "banana", "cereza"]

hay_manzana = "manzana" in frutas         # True
no_hay_uva = "uva" not in frutas          # True

print("\n📦 Membership Operators")
print(f"'manzana' in frutas ➜ {hay_manzana}")
print(f"'uva' not in frutas ➜ {no_hay_uva}")

lista = [1, 2, 3, 4, 5]
print(f"3 in lista ➜ {3 in lista}")
print(f"10 not in lista ➜ {10 not in lista}")


# ===============================
# 7. BITWISE OPERATORS
# ===============================
# Operan a nivel de bits. Son útiles en optimización o en programación de bajo nivel.

# Representaciones binaria:
# x = 5  → 0101
# y = 3  → 0011

x = 5
y = 3

bitwise_and = x & y     # 1 (0001)
bitwise_or = x | y      # 7 (0111)
bitwise_xor = x ^ y     # 6 (0110)
bitwise_not = ~x        # -6 (complemento a 2)
desplazar_izq = x << 1  # 10 (multiplica por 2)
desplazar_der = x >> 1  # 2 (divide entre 2)

print("\n💡 Bitwise Operators")
print(f"{x} & {y} = {bitwise_and}")
print(f"{x} | {y} = {bitwise_or}")
print(f"{x} ^ {y} = {bitwise_xor}")
print(f"~{x} = {bitwise_not}")
print(f"{x} << 1 = {desplazar_izq}")
print(f"{x} >> 1 = {desplazar_der}")

# ===============================
# 8. CONTROL STRUCTURES
# ===============================
print("\n🧠 Control Structures")

# --- Condicionales (if/elif/else)
edad = 17
if edad >= 18:
    mensaje = "Eres mayor de edad"
elif edad == 17:
    mensaje = "Tienes 17, casi adulto"
else:
    mensaje = "Eres menor de edad"
print(mensaje)

# --- Bucle for
print("\nBucle for:")
for numero in range(1, 4):  # Imprime 1, 2, 3
    cuadrado = numero ** 2
    print(f"{numero} al cuadrado es {cuadrado}")

# --- Bucle while
print("\nBucle while:")
contador = 0
while contador < 3:
    print(f"Contador = {contador}")
    contador += 1

# --- Try/Except (manejo de errores)
print("\nManejo de excepciones:")
try:
    division = 10 / 0
except ZeroDivisionError:
    print("❌ No puedes dividir entre cero.")
finally:
    print("Este bloque se ejecuta siempre.")

#Ejercicio Dificultad extra
for i in range(10,56):
  if i != 16 and i%3 != 0 and i%2 == 0:
    print(f"{i}", end " ")

  
