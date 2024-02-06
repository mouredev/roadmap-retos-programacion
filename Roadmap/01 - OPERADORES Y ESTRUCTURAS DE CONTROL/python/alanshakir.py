#operadores aritmeticos
print("suma", 5 + 3)
print("resta", 5 - 3)
print("multiplicacion", 5 * 3)
print("division", 5 / 3)
print("division exacta", 5 // 3)
print("modulo", 5 % 3)
print("exponente", 5 ** 3)

#operadores logicos
print("operador AND:", 8 + 5 == 13 and 9 + 4 == 13)
print("operador OR:", 8 + 5 == 13 or 9 + 4 == 13)
print("operador NOT:", not 8 + 5 == 14)

#operadores de comparacion
print("igualdad: ", 15 == 5)
print("distinto: ", 15 != 5)
print("mayor que: ", 15  > 5)
print("menor que: ", 15  < 5)
print("mayor o igual que: ", 15  >= 5)
print("menor o igual que: ", 15  <= 5)

#estructuras de control
#condicionales
my_variable = 8
if my_variable == 10:
    print("mi variable es: ", my_variable)
elif my_variable > 10:
    print("mi variable es mayor que 10")
else:
    print("mi variable es menor que  10")

#iterativas
index = 0
while index < 7:
    print(index)
    index+=1

for index in range(7):
    print(index)

#excepciones
try:
    print(7/0)
except:
    print("division entre cero no es posible")
finally:
    print("cambiar numero divisor")

#ejercicio opcional
for index in range(10, 56):
    if index % 2 == 0 and index % 3 != 0:
        if index != 16:
            print(index)
    if index == 55:
         print(index)
