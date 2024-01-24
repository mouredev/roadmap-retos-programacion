
# ╔══════════════════════════════════════╗
# ║ Autor: Kenys Alvarado                ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 - Python                        ║
# ╚══════════════════════════════════════╝
print(f"""
1. Imprimir ejemplos utilizando todos los tipos 
de operadores de tu lenguaje:
-----------------------------------------------
Operadores aritmeticos:
********************************
- Suma:              10 + 5 = {10 + 5}
- Resta:             10 - 5 = {10 - 5}
- Multiplicacion:    10 * 5 = {10 * 5}
- Division:          10 / 5 = {10 / 5}
- Division Entera:   17// 4 = {17// 4}
- Residuo:           20 % 7 = {20 % 7}
- Potenciacion:      2 ** 3 = {2 ** 3}
- Combined: (4 + 2) * 3 / 2 = {(4 + 2) * 3 / 2}

Operadores de Comparación:
**************************
- igual a       5 == 5 -> {5 == 5}
- Diferente de  5 != 5 -> {5 != 5}
- Menor que     4 < 5  -> {4 <  5}
- Mayor que     4 > 5  -> {4 >  5}
- Menor o igual 4 <= 5 -> {4 <= 5}
- Mayor o igual 4 >= 5 -> {4 >= 5}

Operadores de Asignación:
*************************""")
n = 10; print(f"- asigna:          n = 10  = {n}")
n += 2; print(f"- suma:            n += 2  = {n}")
n -= 2; print(f"- resta:           n -= 2  = {n}")
n *= 2; print(f"- multiplica:      n *= 2  = {n}")
n /= 2; print(f"- división:        n /= 2  = {n}")
n **=2; print(f"- exponenciación:  n **= 2 = {n}")
n //=2; print(f"- división entera: n //= 2 = {n}")
n %= 2; print(f"- modulo:          n %= 2  = {n}")

print(f"""
Operadores Lógicos:
*******************
and: 5 == 5 and 6 != 5 -> {5 == 5 and 6 != 5}
or:  5 == 5 or 6 != 5  -> {5 == 5 or 6 != 5 }
not: not 5 == 6        -> {not 5 == 6}

Operadores de Identidad:
************************
is:     (6 > 5) is True     -> {(6 > 5) is True}
is not: (6 > 5) is not True -> {(6 > 5) is not True}

Operadores de Pertenencia:
**************************
in:     "c" in "abcde"     -> {"c" in "abcde"}
not in: "f" not in "abcde" -> {"f" not in "abcde"}""")
a = 0b1100
b = 0b1010
print(f"""
#Operadores Bit a Bit:
**********************
and:       bin(a & b)  -> {bin(a & b)}
or:        bin(a | b   -> {bin(a | b)}    
xor:       bin(a ^ b)  -> {bin(a ^ b)}
not_a:     bin(~a)     -> {bin(~a)}
izquierda: bin(a << 2) -> {bin(a << 2)}
derecha:   bin(a >> 1) -> {bin(a >> 1)}

2. Estructuras de control:
--------------------------
# condicinal:
*************""")
if 5 == 5:
    print("Si 5 == 5")
# si de lo contrario
elif suma == 2:
    print("Si 2 == 2")
else:
    print("Ninguna")

print("""
Operador ternario:""")
my_bool = True if 15 == 15 else False
print("si es igual" if my_bool else "no es igual")

print("""
match:""")
def operacion(operador):
    match operador:
        case 'suma': return "Realizando suma"
        case 'resta': return "Realizando resta"
        case 'multiplica':return "Realizando multiplicación"
        case 'divide': return "Realizando división"
        case _: return None
print(operacion('resta'))

print("""
Bucle for
zip: combina dos o más iterables creando una secuencia de tuplas.
enumerate: agrega un contador a un iterable.
range: iterar sobre una secuencia de números.""")
cadena = "abcd"
for i in range(2):
    print(cadena)
# de y hasta.
for i in range(3, 5):
    print(i)

print("con objeto_iterable")
for elemento in cadena:
    print(elemento)

print("Bucle while")
n = 3
while True:
    print(n) # 3, 2, 1
    n -= 1
    if n == 0:
        print("Llego a 0.")
        break # salir del bucle

print("while con condicional")
n = 3
while n > 0:
    print(n) # 3, 2, 1
    n -= 1
else:
    print("Llego a 0.")

print("Bucles anidados")
elementos = ["a", "b", "c"]
n = 1
while n < 4:
    print(n)
    n += 1
    for e in elementos:
        print(e)

print("*continue* en for o while")
for i in range(1, 4):
    if i == 2:
        continue
    print(i) 
    # 1, 3
print("""
Control de Excepciones:
***********************""")
try:
    print(5 / 0)
except Exception as e:
    print(f"{type(e).__name__}: {str(e)}")
finally:
    # Se produce o no se produce error.
    print("finalizado")

print("""
# Context Managers:
# Se utiliza para asegurar que ciertos recursos 
# se adquieran y liberen correctamente.
with open('ejemplo.txt', 'w') as archivo:
     archivo.write('hola')

3. Ejercicio:
-------------
Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.""")
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)