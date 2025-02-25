print("***Python Operators***\n")

a,b = 3,5

#Arithmetic Operators

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a**b
division_entera = a//b

print(f"""Python Arithmetic Operators
    suma(+): {suma}
    resta(-): {resta}
    multiplicacion(*): {multiplicacion}
    division(/): {division}
    modulo(%): {modulo}
    potencia(**): {potencia}
    division_entera(//): {division_entera}\n
""")


#Python Assignment Operators

a+=1
a-=1
a&=1

print(f"""Python Assignment Operators
    los operadores de asignacion son usados para asignar valores a las variables.
    Se realizan con el simbolo =, puedes hacer uso de los operadores aritmeticos
    y los operadores a nivel de Bit (Bitwise)
    {a}\n
""")

#Python Comparison Operators

igual = a==b
no_igual = a!= b
mayor_que = a>b
menor_que = a<b
mayor_igual = a>=b
menor_igual = a<=b

print(f"""Python Comparison Operators
    igual que(==): {igual}
    diferente(!=): {no_igual}
    mayor que(>): {mayor_que}
    mayor o igual(>=): {mayor_igual}
    menor que(<): {menor_que}
    menor o igual(<=): {menor_igual}\n
""")

#Python Logical Operators

cond_and = (a>6 and b<1)
cond_or = (a<3 and b==5)
cond_not = not(a!=b)

print(f"""Python Logical Operators
    AND: {cond_and} (solo si ambas condiciones son verdaderas retorna un True)
    OR: {cond_or} (si una de las condiciones es verdadera retorna True)
    NOT: {cond_not} (revierte el resultado, si la condicion es True lo revierte a False)\n
""")

#Python Identity Operators

operator_is = a is b
operator_is_not = a is not b

print(f"""Python Identity Operators
    is; retorna True si las variables son el mismo objeto, {operator_is}
    is not; retorna False si ambas variables no son el mismo objeto, {operator_is_not}\n
""")


#Python Membership Operators

fruits = ["manzana", "tomate"]

print("Python Membership Operator")
print("banana" in fruits)
print("banana" not in fruits)

#Python Bitwise Operators

bit_and = a&b
bit_or = a|b
bit_not = ~b
bit_xor = a^b

print(f"""\nPython Bitwise Operators
    AND(&): Compara cada bit de dos números y devuelve
    1 solo si ambos bits son 1. {bit_and}

    OR(|): Compara cada bit y devuelve 1 si uno de ellos
    es 1. {bit_or}

    NOT(~): Invierte los bits de un numero {bit_not}

    XOR(^): Compara cada bit si al menos uno de los bits
    es 1 (no ambos) {bit_xor}\n
""")

#Estructuras de Control

#Condicionales"
if a > b:
    print("el mayor el a")
elif a < b:
    print("el mayor es b")
else:
    print("ambas variables son iguales")

nota_aprobatoria = 5.0

match nota_aprobatoria:
    case 5.0:
        print("puntaje alto")
    case 4.0:
        print("puntaje aceptable")
    case 3.0:
        print("puntaje promedio")
    case 2.0:
        print("puntaje bajo")
    case 1.0:
        print("reprobado")

#Bucles

#for
for i in range(1,10):
    print(f"iteracion N°{i}")

#while
i = 0
while i<6:
    print(f"bucle N°{i}")
    i+=1

#Extra

for i in range(10,56):
    if i%2==0 and i!=16 and i%3!=0:
        print(i)