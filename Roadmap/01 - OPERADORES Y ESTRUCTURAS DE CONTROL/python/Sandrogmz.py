"Operadores"

# Operadores Aritméticos

print(f"Suma: 10 + 3 = {10 + 3}")  # SUMA
print(f"Resta: 10 - 3 ={10 - 3}")  # RESTA
print(f"Multi: 10 * 3 = {10 * 3}")  # MULTIPLICACIÓN
print(f"Div: 12 / 3 = {10 / 3}")  # DIVISION
print(f"Mod: 16 % 3 = {16 % 3} ")  # MÓDULO
print(f"Potencia: 12 ** 3 = {12 ** 3}")  # POTENCIA
print(f"DivInt: 18 // 5 = {18 // 5}")  # DIVISION NUMERO ENTERO

# Operadores Relacionales

# Devuelve True si el operador de la izquierda es mayor que el operador de la derecha
print(f"OpLftBigTru: 3 > 2 = {3 > 2}")
# Devuelve True si el operador de la derecha es mayor que el operador de la izquierda
print(f"OpRightBigTru: 2 < 3 = {2 < 3}")
# Devuelve True si ambos operandos son iguales
print(f"SameValuesTru: 10 == 10 {10 == 10}")
# Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
print(f"OpLftBigOrSameTrue: 10 >= 5 10 >= 10{10 >= 5}{10 >= 10}")
# Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda
print(f"OpRigBigOrSameTrue: 5 <= 10 10 <= 10{5 <= 10}{10 <= 10}")
# Devuelve True si ambos operandos no son iguales
print(f"DifOpTrue: 10 != 7{10 != 7}")

# Operadores de Bit

# Realiza bit a bit la operación AND en los operandos
print(f"OpBitAND: 10 & 3 = {10 & 3}")
# Realiza bit a bit la operación OR en los operandos
print(f"OpBiOR: 10 | 11 = {10 | 11}")
# Realiza bit a bit la operación XOR en los operandos
print(f"OpBitXOR: 10 ^ 11 = {10 ^ 11}")
# Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando
print(f"OpBitNOT: ~3 ={~3}")
# Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha
print(f"DespDer: 10 >> 2 = {10 >> 2}")
# Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha
print(f"DespIzq: 10 << 2 = {10 << 2}")

# Operadores de asignación

numero = 20  # Asignación
print(numero)
numero += 5  # Suma y Asignaciónn
print(numero)
numero -= 5  # Resta y Asignación
print(numero)
numero *= 30  # Multiplicacion y Asignación
print(numero)
numero /= 2  # Division y Asignación
print(numero)
numero %= 1  # Modulo y Asignación
print(numero)
numero **= 1  # Exponente y Asignación
print(numero)
numero //= 1  # Division entera y asignación
print(numero)

# Operadores lógicos

print(f"AND &&: True and True es {True and True}")
print(f"OR ||: True or True es {True or True}")
print(f"NOT !: not True == True es {not True == True}")

# Operadores de Pertenencia

print(f"'a' in 'sandro' = {'a' in 'sandro'}")
print(f"'s' not in 'sandro' = {'s' not in 'sandro'}")

"""in y not in son operadores de pertenencia.

in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.

not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False."""

# Operadores de identidad

MiNuevoNumero = numero
print(f"numero is MiNuevoNumero es {numero is MiNuevoNumero}")
print(f"numero is not MiNuevoNumero es {numero is not MiNuevoNumero}")

# Operadores Condicionales

my_string = "Gomez"

if my_string == "Sandro":
    print("my_string es 'Sandro'")
elif my_string == "Gomez":
    print("my_string es 'Gomez'")
else:
    print("my_string no es 'Sandro' ni 'Gomez'")

# Iteradores

number = 17
while number <= 17:
    print("Hola Python!")
    number += 2

for i in range(5):
    print(i)

    # Manejo de excepciones


def verificar_paridad():
    try:
        # Pedimos al usuario un número y convertimos la entrada a entero
        numero = int(input("Introduce un número entero: "))

        # Verificamos si el número es par o impar usando el operador módulo
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")

    except ValueError:
        # Capturamos el error cuando el usuario no introduce un número entero
        print("Error: Debes introducir un número entero válido.")

        "Extra"


for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)