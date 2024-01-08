def operadores_aritmeticos():
    print("OPERADORES ARITMETICOS\n")
    a = 10
    b = 7
    suma = a + b
    print(f"Suma de {a} y {b} = {suma}")
    resta = a - b
    print(f"Resta de {a} y {b} = {resta}")
    multiplicacion = a * b
    print(f"Multiplicación de {a} y {b} = {multiplicacion}")
    division = a / b
    print(f"División de {a} y {b} = {division}")
    division_entera = a // b
    print(f"División entera de {a} y {b} = {division_entera}")
    modulo = a % b
    print(f"Módulo de {a} y {b} = {modulo}")
    exponente = a ** b
    print(f"Exponente de {a} y {b} = {exponente} \n ")

def operadores_logicos():
    print("OPERADORES LOGICOS\n")
    x = True
    y = False
    resultado_and = x and y
    print(f"{x} AND {y} = {resultado_and}")
    resultado_or = x or y
    print(f"{x} OR {y} = {resultado_or}")
    resultado_not = not x
    print(f"NOT {x} = {resultado_not}")
def operadores_comparacion():
    print("OPERADORES DE COMPARACION\n")
    a = 10
    b = 7
    c = 7
    igual = a == b
    print(f"{a} == {b}: {igual}")
    diferente = a != b
    print(f"{a} != {b}: {diferente}")
    mayor = a > b
    print(f"{a} > {b}: {mayor}")
    menor = a < b
    print(f"{a} < {b}: {menor}")
    menorIgual = b <= c
    print(f"{b} <= {c}: {menorIgual}")

def estructuras_control():
    print("ESTRUCTURAS CONDICIONALES\n")
    a = 5
    b = 10
    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} y {b} son iguales")

    # Iterativas - Bucle for
    for i in range(3):
        print(f"Repetición {i+1} con for")
    
    # Iterativas - Bucle while
    i = 0
    while i < 3:
        print(f"Repetición {i+1} con while")
        i += 1

    # Excepciones
    try:
        division = 10 / 0
    except ZeroDivisionError:
        print("División por cero no permitida.")

def dificultad_extra():
    print("Números entre 10 y 55, pares, y que no son ni 16 ni múltiplos de 3:")
    for i in range(10, 56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i, end=" ")
operadores_aritmeticos()
operadores_logicos()
operadores_comparacion()
estructuras_control()
dificultad_extra()