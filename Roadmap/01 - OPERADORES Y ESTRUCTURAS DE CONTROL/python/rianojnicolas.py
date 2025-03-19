# Operadores Aritmeticos

a = 1
b = -2
print("OPERADORES ARITMETICOS")
suma = a + b 
print(f'La suma entre {a} y {b} es igual a {suma}')
resta = a - b
print(f'La resta entre {a} y {b} es igual a {resta}')
division = a/b
print(f'La division entre {a} y {b} es igual a {division}')
producto = a*b
print(f'La multiplicacion entre {a} y {b} es igual a {producto}')
potencia = a**b
print(f'El numero {a} elevado a la potencia {b} es igual a {potencia}')
modulo = a%b
print(f'El resto de la division entre {a} y {b} es igual a {modulo}')
print("")

# Operadores Relacionales
print("OPERADORES RELACIONALES")
igualdad = a == b
print(f'¿ Son iguales {a} y {b} ? RTA -> {igualdad}')
diferencia = a != b
print(f'¿ Son diferentes {a} y {b} ? RTA -> {diferencia}')
mayor = a > b
print(f'¿ {a} es mayor a {b} ? RTA -> {mayor}')
menor = a < b
print(f'¿ {a} es menor a {b} ? RTA -> {menor}')
menorIgual = a <= b
print(f'¿ {a} es menor e igual a {b} ? RTA -> {menorIgual}')
mayorIgual = a >= b
print(f'¿ {a} es mayor e igual a {b} ? RTA -> {mayorIgual}')
print("")

# Operadores de Asignacion
print("OPERADORES DE ASIGNACION")
print("""
Asignación""")
x = 2
print(f'A la variable *x* le asiganmos el valor {x}, con la siguiente sintaxis x = 1 \n')

print("CONTADOR DE SUMA")
x += 1
print(f'La operacion (x += 1), es equivalente x = x + 1, que da como resultado {x} \n')

print("CONTADOR DE RESTA")
x -= 2
print(f'La operacion (x -= 2), es equivalente x = x - 2, que da como resultado {x} \n')

print("CONTADOR DE PRODUCTO")
x *=5
print(f'La operacion (x *= 5), es equivalente x = x * 5, que da como resultado {x} \n')

print("CONTADOR DE DIVISION")
x /= 5
print(f'La operacion (x /= 5), es equivalente x = x / 5, que da como resultado {x} \n')

print("CONTADOR DE MODULO")
print(f'La operacion (x %= 0.5), es equivalente al residuo de la división entre {x} / 0.5')
x %= 2
print(f'Esta operacion da como resultado {x} \n')

print("CONTADOR DE POTENCIACION")
x **= 2
print(f'La operacion (x **= 2), es equivalente x = x^2, que da como resultado {x} \n')


# Operadores Logicos
A = True
B = False
print("OPERADORES LOGICOS")
# AND
print(f'{A} and {B} = {A and B}')
print(f'{B} and {A} = {B and A}')
print(f'{A} and {A} = {A and A}')

# OR
print(f'{B} or {A} = {B or A}')
print(f'{A} or {B} = {A or B}')
print(f'{A} or {A} = {A or A}')
print(f'{B} or {B} = {B or B}')

# NOT
print(f'not({A}) = {not A}')
print(f'not({B}) = {not B}')
print("")

# Operadores de Pertenencia
print("OPERADORES DE PERTENCIA")
my_list = [1, 10, 4, 5, 100]
print(my_list, "\n")
element = 2
print(f'¿{element} esta en la lista? RTA->{element in my_list}')
print(f'¿{element} no esta en la lista? RTA->{element not in my_list} \n')

# Operadores de Identidad
print("OPERADORES DE IDENTIDAD")
print(f'¿{element} es {my_list[element]}? RTA->{element is my_list[element]}')
print(f'¿{element} no es {my_list[element]}? RTA->{element is not my_list[element]}\n')

# Estructuras de Control
mode = input("Ingresa modo de juego 1 o 2:")

# Ciclo while
print("Ciclo while - Iterativa \n")
while (mode != "1" and mode != "2"):
    print("Please enter the correct input")
    mode = input("Enter the mode: ")

# Ciclo IF
print("\nCiclo IF - Condicional")
if (mode == "2"):
    print("Elegiste modo de juego 2")
else:
    print("Elegiste modo de juego 1")

# Ciclo for
print("\nCiclo for - Iterativa")
for i in range(0,5):
    if (i%2==0):
        print(f'{i} es un numero par')
    else:
        print(f'{i} es un numero impar')

# Excepciones
print("\nExcepciones")
try:
    dividendo = int(input("Ingresa el dividendo de la división: "))
    divisor = int(input("Ingresa el divisor de la división: "))
    division = dividendo/divisor
except Exception as e:
    print("Error !!!!", e)

print("\n")
# Dificultad Extra
for i in range(9,56):
    if (i == 16):
        continue
    elif (i%3 == 0):
        continue
    else:
        print(i)