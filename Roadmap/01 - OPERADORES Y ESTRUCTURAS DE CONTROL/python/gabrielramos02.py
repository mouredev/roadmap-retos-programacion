## 01 - OPERADORES Y ESTRUCTURA DE CONTROL

# Operadores aritmeticos
print(2 + 3)  # Suma
print(2 - 3)  # Resta
print(1 / 2)  # Division
print(1 * 2)  # Multiplicacion
print(13 // 2)  # Division Entera
print(13 % 2)  # Resto de la division
print(12**2)  # Exponenciacion

# Operadores de Comparacion
print(2 < 3)  # Menor que
print(2 <= 3)  # Menor o igual que
print(2 > 3)  # Mayor que
print(2 >= 3)  # Mayor o igual que
print(2 == 3)  # Igual a
print(2 != 3)  # Distinto de

# Operadores Logicos
print(True and True)  # Operador and
print(True or False)  # Operador or
print(not False)  # Operador not

# Condicionales
print("Condicionales")
#############################
if True:
    print("Condicional 'if'")
#############################
if False:
    pass
elif True:
    print("Condicional 'elif'")
#############################
if False:
    pass
elif False:
    pass
else:
    print("Condicional 'else'")

# Estructuras Repetitivas
for i in range(5):
    print("Esto es un 'for'")
#############################
j = 0
while j < 5:
    print("Esto es un 'while'")
    j += 1

# Excepciones
    try:
        division = 10 / 0
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print("Division realizada")
    finally:
        print("Bloque ejecutado al finalizar")

    
