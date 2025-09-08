# OPERADORES ARITMÉTICOS (cálculos matemáticos)
# + (suma)
edad = 25
años_extra = 5
nueva_edad = edad + años_extra  
puntos = 1000
# - (resta)
nueva_edad_1 = edad- años_extra
# / (división)
puntos_mitad = puntos / 2   
# * (multiplicación)
puntos_doble = puntos * 2  
# % (módulo - resto de división)
puntos_restantes = puntos % 30
# ** (exponente - potencia)
puntos_potencia = puntos ** 2
# // (división entera - parte entera de la división)
puntos_div_entera = puntos // 3

print(f"Operadores aritméticos: {nueva_edad}, {nueva_edad_1}, {puntos_mitad}, {puntos_doble}, {puntos_restantes}, {puntos_potencia}, {puntos_div_entera}")

# OPERADORES DE COMPARACIÓN (comparan valores)
es_mayor = edad > 18            # > (mayor que)
es_menor = edad < 30           # < (menor que)
es_mayor_igual = edad >= 18    # >= (mayor o igual que)
es_menor_igual = edad <= 30     # <= (menor o igual que)    
es_igual = edad == 25           # == (igual a)
es_diferente = edad != 30       # != (diferente de)
print(f"¿Mayor de edad? {es_mayor}, ¿Menor de edad? {es_menor}, ¿Mayor o igual que 18? {es_mayor_igual}, ¿Menor o igual que 30? {es_menor_igual}, ¿Edad 25? {es_igual},es diferente de 30? {es_diferente}")

# OPERADORES LÓGICOS (combinan condiciones)
tiene_permiso = True
tiene_credito = False

puede_acceder = tiene_permiso and edad >= 18  # AND (ambas deben ser True)
puede_comprar = tiene_permiso or tiene_credito # OR (al menos una True)
no_tiene_credito = not tiene_credito           # NOT (invierte el valor)
print(f"¿Puede acceder? {puede_acceder}, ¿Puede comprar? {puede_comprar}")

# OPERADORES DE ASIGNACIÓN (asignan valores)
contador = 10
contador += 5  # += (suma y asigna) → contador = 15
print(f"Contador: {contador}")
contador -= 3  # -= (resta y asigna) → contador = 12
print(f"Contador: {contador}")
contador *= 2  # *= (multiplica y asigna) → contador = 24
print(f"Contador: {contador}")
contador /= 4  # /= (divide y asigna) → contador = 6.0
print(f"Contador: {contador}")
contador %= 4  # %= (módulo y asigna) → contador = 2.0
print(f"Contador: {contador}")
contador **= 3 # **= (exponente y asigna) → contador = 8.0
print(f"Contador: {contador}")
contador //= 3 # //= (división entera y asigna) → contador = 2.0
print(f"Contador: {contador}")

# OPERADORES DE IDENTIDAD (verifican si es el mismo objeto)
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

mismo_objeto = lista1 is lista2      # is (False - no son el mismo objeto)
misma_referencia = lista1 is lista3  # is (True - misma referencia)
print(f"¿Mismo objeto? {mismo_objeto}, ¿Misma referencia? {misma_referencia}")

# OPERADORES DE PERTENENCIA (verifican si existe en secuencia)
frutas = ["manzana", "banano", "naranja"]
tiene_manzana = "manzana" in frutas       # in (True - existe)
no_tiene_uva = "uva" not in frutas        # not in (True - no existe)
print(f"¿Tiene manzana? {tiene_manzana}, ¿No tiene uva? {no_tiene_uva}")

# OPERADORES DE BITS (manipulación binaria)
a = 5  # 0101 en binario
b = 3  # 0011 en binario

and_bits = a & b   # AND bits: 0101 & 0011 = 0001 (1)
or_bits = a | b    # OR bits: 0101 | 0011 = 0111 (7)
xor_bits = a ^ b   # XOR bits: 0101 ^ 0011 = 0110 (6)
not_bits = ~a  # NOT bits: ~0101 = 1010 (-6 en complemento a dos)
desplazamiento_izq = a << 1  # Desplazamiento a la izquierda: 0101 << 1 = 1010 (10)
desplazamiento_der = a >> 1  # Desplazamiento a la derecha: 0101 >> 1 = 0010 (2)
print(f"AND bits: {and_bits}, OR bits: {or_bits}, XOR bits: {xor_bits}, NOT bits: {not_bits}, Desplazamiento Izquierda: {desplazamiento_izq}, Desplazamiento Derecha: {desplazamiento_der}")

"""
Estructuras de control:
1. Condicionales (if, elif, else)
2. Iterativas (for, while)
3. Manejo de excepciones (try, except)
"""
# condicionales
mi_nombre = "giovanni"
if mi_nombre == "willian":
    print("Hola, Willian!")
elif mi_nombre == "giovanni":
    print("mi nombre es Giovanni!")
else:
    print("mi nombre no es Willian ni Giovanni!")

# iterativas
for i in range(8):
    print(f"Iteración {i}")

contador = 0
while contador < 8:
    print(f"Contador {contador}")
    contador += 1

# manejo de excepciones (try, except)
try:
    resultado = 22 / 0# Esto generará un error (división por cero)
except:
    print("se ha producido un error, no se puede dividir por cero")
finally:
    print("ha finalizado el manejo de excepciones")

try:
    resultado = 22 / 2 # Esto no generará un error (división por dos)
except:
    print("se ha producido un error, no se puede dividir por cero")
finally:
    print("ha finalizado el manejo de excepciones")

"""
ejercicio extra:
programa que imprime por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)