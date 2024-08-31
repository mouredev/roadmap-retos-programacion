# Operadores aritmeticos
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
potencia = a ** b
division = a / b
division_entera = a // b
modulo = a % b
print("*-*-*-Operadores aritmeticos-*-*-*")
print(f"Suma de {a} y {b} = {suma}")
print(f"Resta de {a} y {b} = {resta}")
print(f"Multiplicacion de {a} y {b} = {multiplicacion}")
print(f"Potencia de {a} y {b} = {potencia}")
print(f"Division de {a} y {b} = {division}")
print(f"Division entera de {a} y {b} = {division_entera}")
print(f"Modulo de {a} y {b} = {modulo}")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Operadores logicos
x = 15
y = 0
caso1 = x or y
caso2 = x and y
caso3 = not x
caso4 = not y
print("*-*-*-Operadores Logicos-*-*-*")
print(f"{x} or {y} = {caso1}")
print(f"{x} and {y} = {caso2}")
print(f"not {x} = {caso3}")
print(f"not {y} = {caso4}")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Operadores de comparacion
igualdad = a == b
diferente = a != b
a_mayor_que_b = a > b
a_menor_que_b = a < b
a_menor_igual_que_b = a <= b
a_mayor_igual_que_b = a >= b
print("*-*-*-Operadores de comparacion-*-*-*")
print(f"{a} es igual a {b} : {igualdad}")
print(f"{a} es diferente a {b} : {diferente}")
print(f"{a} es igual a {b} : {a_mayor_que_b}")
print(f"{a} es igual a {b} : {a_menor_que_b}")
print(f"{a} es igual a {b} : {a_mayor_igual_que_b}")
print(f"{a} es igual a {b} : {a_menor_igual_que_b}\n")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
# Operadores de identidad
z = 4
k = 2
lista_identidad = [2, 4]
operador_is = z is lista_identidad
operador_is1 = z is k
print("*-*-*-Operadores de identidad-*-*-*")
print(f"z esta en la lista_identidad : {operador_is}")
print(f"z esta en k : {operador_is1}\n")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Operadores de pertenencia
lista_pertenencia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
in_lista = 4 in lista_pertenencia
not_in_lista = 4 not in lista_pertenencia
print("*-*-*-Operadores de pertenencia-*-*-*")
print(f"4 esta en la lista_pertenencia: {in_lista}")
print(f"4 no esta en la lista_pertenencia: {not_in_lista}\n")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Operadores de bits
b = 1
n = 0
# Esta informacion la obtuve de la pagina web: https://j2logo.com/python/tutorial/operadores-en-python/
print("*-*-*-Operadores de bits-*-*-*")
print("Operacion OR a nivel de bits: ", b | n)
print("Operación XOR a nivel de bits: ", b ^ n)
print("Operación AND a nivel de bits: ", b & n)
print("Se desplaza n bits a la izquierda: ", b << 1)
print("Se desplaza n bits a la derecha: ", b >> 1)
print("Obtiene los bits invertidos: ", ~b)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Condicionales
print("*-*-*-Condicionales-*-*-*")
nombre = "julio"

if nombre == "julio":
    print("Nombre registrado")
elif nombre == "carmen":
    print("Nombre registrado")
else:
    print("Nombre no registrado")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

print("*-*-*-Operador match-*-*-*")


def verificador_colores(color):
    match color:
        case "verde":
            return "color verde"
        case "rojo":
            return "color rojo"
        case "marron":
            return "color marron"
        case _:
            return "No añadiste ningun color registrado"


print(f"Operador match: {verificador_colores('rojo')}")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Iterativas
print("*-*-*-Bucle for-*-*-*")
for i in range(1, 10):
    print(i)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

print("*-*-*-Bucle while-*-*-*")
while True:
    print(i)
    if i == 9:
        break
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# Excepciones
print("*-*-*-Excepciones-*-*-*")
try:
    a = 1
    b = 0
    division = a/b
except Exception as e:
    print(f'Excepcion: {e}')
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

print("*-*-*-Programa extra-*-*-*")


def filter_numbers():
    for i in range(10, 56):
        if i % 2 == 0 and i % 3 != 0 and i != 16:
            print(i)


filter_numbers()
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
