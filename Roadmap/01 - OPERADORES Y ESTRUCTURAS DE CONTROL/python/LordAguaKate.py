#Reto 01 OPERADORES Y ESTRUCTURAS DE CONTROL

'''
Los operadores aritmeticos permiten realizar operaciones numericas
usando variables
'''
#Operadores Aritmeticos
suma = 3 + 3
resta = 10 - 5
multiplicacion = 5 * 5
division = 10 / 2        #Esta division se usa para decimales
modulo = 10 % 3
potencia = 5 ** 2
divisionEntera = 10 // 2 #Esta division se usa para numeros enteros

'''
Los operadores de asignacion funcionan para asignar valor a una variable
'''
# Operadores de Asignacion
valor = 10 #Asignacion
valor += 2 #Suma
valor -= 3 #Resta
valor *= 2 #Multiplicacion
valor /= 2 #Division
valor %= 3 #Modulo
valor **= 2 #Potencia
valor //= 2 #Division entera

#Operadores relacionales
ejem1 = 10
ejem2 = 5
print(ejem1 == ejem2) #Igualdad
print(ejem1 != ejem2) #Desigualdad
print(ejem1 < ejem2) #Menor que
print(ejem1 <= ejem2) #Menor igual que
print(ejem1 > ejem2) #Mayor que
print(ejem1 >= ejem2) #Mayor igual que

'''
Los operadores logicos se usan en combinacion con los operadores de 
comparacion cuando la expresion de la condicion lo requiere
'''
#Operadores logicos
x = 10
y = 5

print(x > 5 and y < 5)
print(x > 5 or y < 5)
print(not y == 5)

'''
Las estructuras de control son muy fundamentales para la ejecuccion de un codigo, permitiendo 
la ejecuccion continua de codigo hasta cumplir con la condicional
'''

'''
El uso de if, elif, else. se basa en si es verdadero o falso
'''
#Uso de if, elif, else.
dinero = 100

if dinero >= 100:
    print("Gasta lo que quieras")
elif dinero >= 50:
    print("No gastes mucho")
else:
    print("No gastes nada mejor")

#Bucle for
for i in range(10):
    print("Bucles", i)

#Ciclo while
numeros = 0
while numeros <= 10:
    print(numeros)
    numeros += 1





