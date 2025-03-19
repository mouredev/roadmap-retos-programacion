#%% Operadores --------------------------------------------------
print("Operadores --------------------------------------------------")
#%% Aritméticos
print("Aritméticos")
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
exponente = a ** b
division_entera = a // b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Exponente:", exponente)
print("División Entera:", division_entera)

#%% Lógicos
print("Lógicos")
x = True
y = False

and_result = x and y
or_result = x or y
not_result = not x

print("AND:", and_result)
print("OR:", or_result)
print("NOT:", not_result)

#%% De comparación
print("De comparación")
c = 5
d = 10

igual = c == d
diferente = c != d
mayor = c > d
menor = c < d
mayor_igual = c >= d
menor_igual = c <= d

print("Igual:", igual)
print("Diferente:", diferente)
print("Mayor:", mayor)
print("Menor:", menor)
print("Mayor o Igual:", mayor_igual)
print("Menor o Igual:", menor_igual)

#%% Asignación
print("Asignación")
e = 5
e += 2  # Equivalente a: e = e + 2
print("Asignación con Suma:", e)

#%% Identidad
print("Identidad")
f = [1, 2, 3]
g = [1, 2, 3]
h = f

identidad1 = f is g
identidad2 = f is h
no_identidad = f is not g

print("Identidad 1:", identidad1)
print("Identidad 2:", identidad2)
print("No Identidad:", no_identidad)

#%% Pertenencia
print("Pertenencia")
lista = [1, 2, 3, 4, 5]

pertenencia1 = 3 in lista
pertenencia2 = 6 not in lista

print("Pertenencia 1:", pertenencia1)
print("Pertenencia 2:", pertenencia2)

#%% Bits
print("Bits")
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~a
bitwise_left_shift = a << 2
bitwise_right_shift = a >> 1

print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT:", bitwise_not)
print("Bitwise Left Shift:", bitwise_left_shift)
print("Bitwise Right Shift:", bitwise_right_shift)

#%% Estructuras de Control: -----------------------------------
print("Estructuras de Control: -----------------------------------")

#%% Condicionales
print("Condicionales")
numero = 15

if numero > 10:
    print("El número es mayor que 10")
elif numero < 10:
    print("El número es menor que 10")
else:
    print("El número es igual a 10")

#%% Iterativas
print("Iterativas")
for i in range(5):
    print(i)

while numero > 0:
    print(numero)
    numero -= 1

#%% Excepciones
print("Excepciones")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Este bloque siempre se ejecutará")

#%% Opcional --------------------------------------------------
print("Opcional --------------------------------------------------")
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
