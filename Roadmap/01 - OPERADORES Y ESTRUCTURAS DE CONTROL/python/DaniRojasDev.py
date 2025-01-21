'''
Operadores aritméticos
'''

a = 10
b = 3

print (f"10 + 4 = {a + b}") #suma
print (f"10 - 4 = {a - b}")#resta
print (f"10 x 4 = {a * b}") #multiplicación
print (f"10 / 4 = {a / b}") #división
print (f"10 % 4 = {a % b}")#módulo
print (f"10 ** 4 = {a ** b}") #exponente
print (f"10 // 4 = {a // b}") #cociente

'''
Operadores de comparación
'''
print (f"10 = 3 is {a==b}") # Igualdad
print (f"10 is diferent than 3 is {a!=b}") # Desigualdad
print (f"10 is greater than 3 is {a>b}") # Mayor que
print (f"10 is less than 3 is {a<b}") # Menor que
print (f"10 is greater or equal than 3 is {a>=b}") # Mayor o igual que
print (f"3 is less or equal than 10 is {b<=a}") # Menor o igual que

'''
Operadores lógicos
'''
# operador "and"
print (f"10+3 = 13 y 10-3 = 7 is {a+b==13 and a-b==7}") # Si ambas operaciones son verdad es true, si no false
print (f"10+3 = 13 y 10-3 = 7 is {a+b==12 and a-b==7}") # Si ambas operaciones son verdad es true, si no false

# operador "or"
print (f"10+3 = 13 y 10-3 = 7 is {a+b==13 or a-b==7}") # Si una de las operaciones es verdad es true, si no false
print (f"10+3 = 13 y 10-3 = 7 is {a+b==12 or a-b==7}") # Si una de las operaciones es verdad es true, si no false
print (f"10+3 = 13 y 10-3 = 7 is {a+b==12 or a-b==7}") # Si una de las operaciones es verdad es true, si no false

# operador "not"
print (f"10+3 = 13 is not {not a+b==13 }") # Si una de las operaciones es verdad es false, si no true (invierte true por false)









