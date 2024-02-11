import random;

# --------------------------  TIPOS DE OPERADORES EN PYTHON -------------------------- 

num1 = random.randint(1, 99);
num2 = random.randint(1, 99);

# Operadores aritméticos:

print("-----------------OPERADORES ARITMÉTICOS-----------------" + "\n");
# Suma: +
print(f"SUMA: {num1} + {num2} = {num1 + num2}" + "\n");

# Resta: -
print(f"RESTA: {num1} - {num2} = {num1 - num2}" + "\n");

# Multiplicación: *
print(f"MULTIPLICACION: {num1} * {num2} = {num1 * num2}" + "\n");

# División: /
print(f"DIVISION: {num1} / {num2} = {float(num1 / num2):.2f}" + "\n");

# Módulo: %
print(f"MODULO: {num1} % {num2} = {num1 % num2}" + "\n");

# Potencia: **
print(f"POTENCIA: {num1} ** {num2} = {num1 ** num2}" + "\n");

# División entera: //
print(f"DIVISION ENTERA: {num1} // {num2} = {num1 // num2}" + "\n");

# Operadores de comparación:
print("-----------------OPERADORES DE COMPARACIÓN-----------------" + "\n");
# Igual: ==
print(f"IGUAL: {num1} == {num2} = {num1 == num2}" + "\n");

# Diferente: !=
print(f"DIFERENTE: {num1} != {num2} = {num1 != num2}" + "\n");

# Mayor que: >
print(f"MAYOR QUE: {num1} > {num2} = {num1 > num2}" + "\n");

# Menor que: <
print(f"MENOR QUE: {num1} < {num2} = {num1 < num2}" + "\n");

# Mayor o igual que: >=
print(f"MAYOR O IGUAL QUE: {num1} >= {num2} = {num1 >= num2}" + "\n");

# Menor o igual que: <=
print(f"MENOR O IGUAL QUE: {num1} <= {num2} = {num1 <= num2}" + "\n");

# Operadores de asignación:
print("-----------------OPERADORES DE ASIGNACIÓN-----------------" + "\n");
# =
num3 = num1;
print(f"NUM3 = NUM1: {num3} = {num1}" + "\n");

# Operadores de identidad:
print("-----------------OPERADORES DE IDENTIDAD-----------------" + "\n");
# is
print(f"IDENTIDAD: {num1} is {num2} = {num1 is num2}" + "\n");

# is not
print(f"IDENTIDAD: {num1} is not {num2} = {num1 is not num2}" + "\n");

# Operadores de pertenencia:
print("-----------------OPERADORES DE PERTENENCIA-----------------" + "\n");

# in
Vector = [random.randint(1, 99) for i in range(10)]
print(f"PERTENECE: {num1} in {Vector} = {num1 in Vector}" + "\n");

# not in
print(f"NO PERTENECE: {num1} not in {Vector} = {num1 not in Vector} " + "\n");

# Operadores de bits:
print("-----------------OPERADORES DE BITS-----------------" + "\n");
# &
print(f"&: {num1} & {num2} = {num1 & num2}" + "\n");

# |
print(f"|: {num1} | {num2} = {num1 | num2}" + "\n");

# ^
print(f"^: {num1} ^ {num2} = {num1 ^ num2}" + "\n");

# ~
print(f"~: {num1} ~ {num2} = {~num1}" + "\n");

# <<
print(f"<<: {num1} << {num2} = {num1 << num2}" + "\n");

# >>
print(f">>: {num1} >> {num2} = {num1 >> num2}" + "\n");

# Operadores lógicos:
print("-----------------OPERADORES LÓGICOS-----------------" + "\n");

boolean1 = bool(random.randint(0, 1));
boolean2 = bool(random.randint(0, 1));

# and
print(f"AND: {boolean1} and {boolean2} = {boolean1 and boolean2}" + "\n");

# or
print(f"OR: {boolean1} or {boolean2} = {boolean1 or boolean2}" + "\n");

# not
print(f"NOT: {boolean1} not = {not boolean1}" + "\n");


# --------------------------  TIPOS DE ESTRUCTURAS DE CONTROL -------------------------- 

# Ciclos, Condicionales y Exepciones:
print("-----------------ESTRUCTURAS DE CONTROL-----------------");
try:
    print(Vector[10])
except:

    # For

    print ("\n" + "For:" + "\n")
    x = 0
    for i in (Vector):
        x += 1
        print(f"{x} = {i}"); 

    # While con Condicionales

    print ("\n" + "While con Condicionales:" + "\n")
    while x > 0:
        
        if x in Vector:
            print(f"{x} Somos iguales {x}");
        elif x not in Vector:
            print(f"{x} No encontré un elemento parecido");
        else :
            print(f"{x} No es un número {x}");
        x -= 1;


# EXTRA:

print("\n" + "-----------------EJERCICIO EXTRA-----------------" + "\n");

for i in range(10, 56):
    if (i == 16 or not i%2==0 or i%3==0):
        continue
    print(i)