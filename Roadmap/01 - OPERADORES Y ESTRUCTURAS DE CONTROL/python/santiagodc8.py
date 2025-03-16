# Operadores

# Operadores Aritmeticos
print(f'Suma: 10 + 3 = {10 + 3}')
print(f'Resta: 10 - 3 = {10 - 3}')
print(f'Multiplicacion: 10 * 3 = {10 * 3}')
print(f'Division: 10 / 3 = {10 / 3}')
print(f'Modulo: 10 % 3 = {10 % 3}')
print(f'Suma: 10 + 3 = {10 + 3}')
print(f'Exponente: 10 ** 3 = {10 ** 3}')
print(f'Division Entera: 10 // 3 = {10 // 3}')

# Operadores de Comparacion
print(f"Igualdad: 10 == 3 es: {10 == 3}")
print(f"Desigualdad: 10 != 3 es: {10 != 3}")
print(f"Mayor que: 10 > 3 es: {10 > 3}")
print(f"Menor que: 10 < 3 es: {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es: {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es: {10 <= 3}")

# Operadores Logicos
print(f"AND &&: 10 + 3 == 13 AND 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 AND 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de Asignacion
my_number = 11 # asignacion
print(my_number)
my_number += 1 # suma y asignacion
print(my_number)
my_number -= 1 # resta y asignacion
print(my_number)
my_number *= 2 # multiplicacion y asignacion
print(my_number)
my_number /= 2 # division y asignacion
print(my_number)
my_number %= 2 # modulo y asignacion
print(my_number)
my_number **= 1 # exponente y asignacion
print(my_number)
my_number //= 1 # division entera y asignacion

# Operadores de Identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de Pertenencia 
print(f"'u' in 'santiago' = {'u' in 'santiago'}")
print(f"'g' not in 'santiago' = {'u' not in 'santiago'}")

# Operadores de Bit
a = 10 # 1010 bits
b = 3  # 0011 bits
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR:  10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # 1001
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

'''
Estructuras de Control
'''

# if y else

my_string = "duran"

if my_string == "Santiago xd":
    print("my_string es: Santiago xd")
elif my_string == "Duran":
    print("my_string es: Duran")
else: 
    print("my_string no es 'Santiago xd' ni 'Duran'")
    
    
# Iterativas
for i in range(11):
    print(i)
    

i = 0

while i <= 10:
    print(i)
    i += 1
    
# Manejo de Excepciones
try:
    print(10 / 0)
except:
    print("No se puede dividir por 0")
finally:
    print("Se ha finalizado el manejo de excepciones")
    
    
'''
Extra
'''

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)