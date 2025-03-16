# Tipos de operadores

# Operadores aritméticos
number1 = 10
number2 = 2

suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2
division = number1 / number2
division_entera = number1 // number2
modulo = number1 % number2
potenciacion = number1 ** number2

# Operadores de asignación
number1 += number2
number1 -= number2
number1 *= number2
number1 /= number2
number1 %= number2
number1 **= number2

# Operadores de comparación
igual = (number1 == number2)
no_igual = (number1 != number2)
mayor = (number1 > number2)
mayor_igual = (number1 >= number2)
menor = (number1 < number2)
menor_igual = (number1 <= number2)

# Operadores logicos
y = True
x = False
print(y and x)
print(y or x)
print(not x)

# Operadores de pertenencia
string = "hola"
print("h" in string)
print("h" not in string)

# Operadores de identidad
lista_de_numeros = [1, 2, 3]
tupla_de_numeros = (1, 2, 3)
una_lista = lista_de_numeros

print(una_lista is lista_de_numeros)
print(una_lista is not tupla_de_numeros)
print(lista_de_numeros is tupla_de_numeros)

# Tipos de estructuras de control

# Condicionales
if number1 > number2:
    print("number1 es mayor que number2")
elif number1 < number2:
    print("number1 es menor que number2")
else :
    print("number1 es igual que number2")

# while
number3 = 5
while number3 > 0:
    print(number3)
    number3 -= 1

# for in
for number4 in lista_de_numeros:
    print(number4)
    
# for range
for number5 in range(10, 20, 2):
    print(number5)
    
# break
for number6 in range(10, 20, 2):
    print(number6)
    if number6 == 16:
        break
    
# continue
for number7 in range(10, 20, 2):
    if number7 == 16:
        continue
    print(number7)
    
# excepciones
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        
division(5, 0)
    
# Extra
excluir_numero = 16
for i in range(10, 55, 2):
    if i == excluir_numero or i % 3 == 0:
        continue
    print(i)

    

