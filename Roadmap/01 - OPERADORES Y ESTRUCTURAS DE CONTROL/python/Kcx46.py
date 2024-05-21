#Operadores y estructuras de control#

#operadores aritmeticos
suma = 5 + 5
resta = 5 - 5
multiplicacion = 5 * 5
division = 5 / 5
division_entera = 5 // 5
modulo = 5 % 5
potencia = 5 ** 5
#operadores logicos
and_op = True and False
or_op = True or False
also_or_op = True | False
not_op = not True
#operadores de comparacion
igual = 5 == 5
diferente = 5 != 5
mayor_que = 5 > 5
menor_que = 5 < 5
mayor_o_igual_que = 5 >= 5
menor_o_igual_que = 5 <= 5
#printeos
print(f"5 + 5 = {suma}", "\n")
print(f"5 - 5 = {resta}", "\n")
print(f"5 * 5 = {multiplicacion}", "\n")
print(f"5 / 5 = {division}", "\n")
print(f"5 // 5 = {division_entera}", "\n")
print(f"5 % 5 = {modulo}", "\n")
print(f"5 ** 5 = {potencia}", "\n")
print(f"True and False = {and_op}", "\n")
print(f"True or False = {or_op}", "\n")
print(f"True | False = {also_or_op}", "\n")
print(f"not True = {not_op}", "\n")
print(f"5 == 5 es {igual}", "\n")
print(f"5 != 5 es {diferente}", "\n")
print(f"5 > 5 es {mayor_que}", "\n")
print(f"5 < 5 es {menor_que}", "\n")
print(f"5 >= 5 es {mayor_o_igual_que}", "\n")
print(f"5 <= 5 es {menor_o_igual_que}", "\n")
print("*"*50)
#estructuras de control
print("**ESTRUCTURAS DE CONTROL**")
print("if sum == 10 print sum \n")
if suma == 10:
    print("La suma es igual a 10")
else:
    print("La suma no es igual a 10")
if resta == 0:
    print("La resta es igual a 0")
elif resta < 0:
    print("La resta es menor a 0")
else:
    print("La resta es mayor a 0")
print("\n")

list_for_for = [1, 2, 3, 4, 5]
print("**FOR**")
for i in list_for_for:
    print(i)
print("\n")
print("**WHILE**")
while suma < 20:
    print(suma)
    suma += 1
print("\n")
print("*"*50)
print("***EJERCICIO EXTRA***")
#Dificultad extra
'''
Este imprime por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
for i in range(10, 57):
    if i % 2 == 0 and i != 16 and 1 % 3 != 0:
        print(i)
