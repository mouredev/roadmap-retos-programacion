'''
Operadores
'''
# Operadores Aritméticos

print(f'suma: 19 + 8 ={19 + 8}')
print(f'resta: 24 - 10 ={24 - 10}')
print(f'multiplicación: 8 * 12 ={8 * 12}')
print(f'división: 14 / 3 ={14 / 3}')
print(f'módulo: 14 % 3 ={14 % 3}')
print(f'exponenciación: 2 ** 3 ={2 ** 3}')
print(f'división entera: 14 // 3 ={14 // 3}')

# Operadores de comparación

print(f'igual a: 5 == 3 : {5 == 3}')
print(f'desigualdad a: 5 != 3: {5 != 3}')
print(f'mayor que: 10 > 5: {10 > 5}')
print(f'menor que: 5 < 10: {5 < 10}')
print(f'mayor o igual que: 5 >= 5: {5 >= 5}')
print(f'menor o igual que: 5 <= 10: {5 <= 10}')

# Operadores lógicos
print(f'AND: 10 > 5 AND 5 <10: {10 > 5 and 5 < 10}')
print(f'or: 10 > 11 or 5 <10: {11 > 11 or 5 < 10}')
print(f'NOT: NOT 10 > 11: {not 10 > 11}')

# Operadores de asignación

My_number = 12
print(My_number)
My_number += 6 # operador de suma asignación
print(My_number)
My_number -= 9 # operador de resta asignación
print(My_number)
My_number *= 8 # operador de multiplicación asignación
print(My_number)
My_number /= 3 # operador de división asignación
print(My_number)
My_number **= 2 # operador de exponenciación asignación
print(My_number)
My_number //= 5 # operador de división entera asignación
print(My_number)
My_number %= 4  # operador de módulo asignación
print(My_number)

#operadores de identidad
my_new_number = My_number
print(f'my_number is my new_number es: {My_number is my_new_number}')
print(f'my_number is not my new_number es: {My_number is not my_new_number}')

#operadores de pertenencia
print(f"'a' in 'ariel martinez': {'a' in 'ariel martinez'}")
print(f"'o' not in 'ariel martinez': {'o' not in 'ariel martinez'}")

#operadores de bits
a: 11 # en binario: 1011
b: 5 # en binario: 101
print(f'AND 5 & 11: {5 & 11}') # resultado: 1 (en binario: 001)
print(f'OR 5 | 11: {5 | 11}') # resultado: 15 (en binario: 1111)
print(f'XOR 5 ^ 11: {5 ^ 11}') # resultado: 14 (en binario: 1110)
print(f'NOT ~5: {~5}') # resultado: -6 (en binario: -110)
print(f'Left Shift 5 << 1: {5 << 1}') # resultado: 10 (en binario: 1010)
print(f'Right Shift 5 >> 1: {5 >> 1}') # resultado: 2 (en binario: 10)

'''Estructuras de Control
'''

#Condicionales

my_string = "Ariel"

if my_string == "ArielDEV":
    print("my_string es 'ArielDEV'") 

elif my_string == 'Ariel':
    
 print("my_string es 'Ariel'")
    
else:print("my_string no es 'ArielDEV'")

#Iterativas

for i in range(10):
    print(i)

i = 0

while i <= 10:
   print(i)
   i += 1


#Manejo de excepciones
   try:
      print(11 / 1)
   except:
      print("Error: División por cero no permitida")
   finally:
        print("Se ha completado el manejo de excepciones")

#extra

for number in range(1, 56):
   if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)        
