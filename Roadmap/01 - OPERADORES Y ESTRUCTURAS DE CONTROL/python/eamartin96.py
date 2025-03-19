def Aritmeticos():
    print("Operadores aritmeticos")
    a = 5
    b = 2

    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicacion: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Modulo: {a} % {b} = {a % b}")
    print(f"Potencia: {a} ^ {b} = {a ** b}")

def Logicos():
    print("\nOperadores logicos")
    a = True
    b = False

    print(f"AND: {a} AND {b} = {a and b}")
    print(f"OR: {a} OR {b} = {a or b}")
    print(f"NOT: NOT {a} = {not a}")

def Comparacion():
    print("\nOperadores de comparacion")
    a = 5
    b = 2

    print(f"{a} > {b} = {a > b}")
    print(f"{a} >= {b} = {a >= b}")
    print(f"{a} < {b} = {a < b}")
    print(f"{a} <= {b} = {a <= b}")
    print(f"{a} == {b} = {a == b}")
    print(f"{a} != {b} = {a != b}")

def Identidad():
    print("\nOperadores de identidad")
    a = 1
    b = 2

    print(f"{a} is {b} = {a is b}")
    print(f"{a} is {b} = {a is b}")

def Bits():
    print("\nOperadores de Bits")
    a = 5
    b = 3

    print(f"AND: {a} & {b} = {a & b}")
    print(f"OR: {a} | {b} = {a | b}")
    print(f"XOR: {a} ^ {b} = {a ^ b}")
    print(f"Left shift: {a} << 3 = {a << 3}")
    print(f"Right shift: {a} >> 3 = {a >> 3}")
    print(f"NOT: !{a} = {~a}")

def Pertenencia():
    print("\nOperadores de Pertenencia")
    a = 4
    lista = [1, 2, 3, 4 , 5]

    print("Lista:", *lista)
    print(f"{a} is in Lista = {a in lista}")
    print(f"{a} is not in Lista = {a not in lista}")

def Condicionales():
    a = 5
    print(f"a = {a}")
    if a == 5:
        print("if: a == 1")

    if a != 5:
        print("if")
    else:
        print("else: a != 1")

    if a < 4:
        print("if")
    elif a > 4:
        print("elif: a > 4")
    else:
        print("else")

def Iterativas():
    for i in range(1,6):
        print("for")

    i = 5
    while(i < 5):
        print("while")

def Exceptions():
    while True:
        try:
            x = int(input("Enter a number: "))
            break
        except ValueError:
            print("Opps! That was no valid number. Try again...")

def ExtraDificult():
    for number in range(10, 56):
        if number % 2 == 0 and number != 16 and number % 3 != 0:
            print(number)

def main():
# Operadores
    Aritmeticos()
    Logicos()
    Comparacion()
    Identidad()
    Bits ()
    Pertenencia()

# Operaciones
    Condicionales()
    Iterativas()
    Exceptions()

# Dificultad Extra
    ExtraDificult()
if __name__ == "__main__":
    main()
