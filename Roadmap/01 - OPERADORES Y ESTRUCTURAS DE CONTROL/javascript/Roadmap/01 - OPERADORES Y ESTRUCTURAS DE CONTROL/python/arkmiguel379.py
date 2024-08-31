#Operadores aritmericos

num1 = 5
num2 = 2

suma = num1 + num2 #Operacion de suma
resta = num1 - num2 #Operacion de resta
multiplicacion = num1 * num2 #Operacion de multiplicacion
division = num1 / num2 #Operacion de division
modulo = num1 % num2 #Operacion de residuo de una division
division_entera = num1 // num2 # El resultado de la division es un numero entero
potencia = num1 ** num2 #Potenciación

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(division_entera)
print(potencia)

print("\n")

#Operadores de comparacion

igual = num1 == num2 #Valor A igual que valor B
diferente = num1 != num2 #Valor A diferente de valor B
mayor = num1 > num2 #Valor A mayor que valor B
menor = num1 < num2 #Valor A menor que valor B
mayor_igual = num1 >= num2 #Valor A mayor o igual que valor B
menor_igual = num1<= num2 #Valor A menor o igual que valor B

print(igual)
print(diferente)
print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)

print("\n")

#Operadores logicos

op_and = (num1 == num2) and (num1 > num2) #Operador Y (Se tienen que cumplir las dos condiciones para que el valor sea true)
op_or = (num1 == num2) or (num1 > num2) #Operador O (Se tiene una de las dos condiciones para que el valor sea true)
op_not = not (num1 == num2) == (num1 > num2) #Operador NO (El valor es el contrario al que realmente es)

print(op_and)
print(op_or)
print(op_not)

print("\n")

# Operadores de asignacion

x = 10

x += 3 #El valor de x se suma con 3
print(x)

x -= 3 #El valor de x se resta con 3
print(x)

x *= 3 #El valor de x se multiplica con 3
print(x)

x /= 3 #El valor de x se divide con 3
print(x)

x //= 3 #El residuo de la division es un numero entero
print(x)

x %= 3 #El valor dado es el residuo de la division de x entre 3
print(x)

x **= 3 #El valor de x se potencia en 3
print(x)

print("\n")

# Operadores de pertenencia

nombre = "Miguel Angel Moreno"
print('o' in nombre) # Verifica si un valor está presente en una secuencia, como una lista, cadena, etc.
print('o' not in nombre) # Verifica si un valor no está presente en una secuencia.

# Operadores de identidad

my_number1 = 257
my_number2 = 379

if my_number1 is my_number2: # IS: Verifica si dos variables son la misma instancia de objeto
    print("Son el mismo numero")
else:
    print("No son el mismo numero")

if my_number1 is not my_number2: # IS NOT: Verifica si dos variables no son la misma instancia de objeto
    print("No son el mismo numero")
else:
    print("Son el mismo numero")

print("\n")

#Estructuras condicionales

if num1 == num2:
    print(f"{num1} es igual que {num2}")

elif num1 > num2:
    print(f"{num1} es mayor que {num2}")

elif num1 < num2:
    print(f"{num1} es menor que {num2}")

elif num1 != num2:
    print(f"{num1} es diferente de {num2}")

print("\n")

# Estructuras iterativas

while num1 > num2:
    print(f"Num2 ha aumentado su valor en 1, su valor ahora es {num2 + 1}")
    num2 += 1

print("\n")

contador = 0

while True:
    print("Codigo que se ejecuta el menos una vez")
    contador += 1

    if contador > 3:
        break

print("\n")

# Control de excepciones

try:
    print(65 + "Cadena")
except:
    print("Se ha producido un error")
finally:
    print("El control de excepciones ha finalizado")


# ======================== EXTRA ===========================

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

