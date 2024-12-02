# T I P O S   D E   O P E R A D O R E S
print('======================')
print('A R I T M E T I C O S')
print('======================')
# 1. Adición ( + )
print(f'800 + 88 = {800 + 88}')

# 2. Substracción ( - )
print(f'900 - 12 = {900 - 12}')

# 3. Multiplicación ( * )
print(f'444 * 2 = {444 * 2}')

# 4. División ( / )
print(f'8880 / 10 = {8880 / 10}')

# 5. Módulo ( % )
print(f'1788 % 900 = {1788 % 900}')

# 6. Potencia ( ** )
print(f'8 ** 2 = {8 ** 2}')

# 7. División entera
print(f'18 // 5 = {18 // 15}')
print('======================')


print('R E L A C I O N A L E S')
print('======================')
# 1. Mayor que ( > )
print(f'10 > 5 = {10 > 5}')

# 2. Menor que ( < )
print(f'10 < 5 = {10 < 5}')

# 3. Igual que ( == )
print(f'10 == 10 = {10 == 10}')

# 4. Mayor o igual que ( >= )
print(f'8 >= 8 = {8 >= 8}')

# 5. Menor o igual que ( <= )
print(f'6 <= 3 = {6 <= 3}')

# 6. Diferente que ( != )
print(f'10 != 5 = {10 != 5}')
print('======================')

print('B I T  A  B I T')
print('======================')
a = 2 # 10 en binario
b = 3 # 11 en binario

# 1. AND ( & )
print(f'a & b = {a & b}')

# 2. OR ( | )
print(f'a | b = {a | b} ')

# 3. XOR ( ^ )
print(f'a ^ b = {a ^ b}')

# 4. NOT ( ~ )
print(f'~a = {~a}')

# 5. Desplazamiento a la derecha ( >> )
print(f'5 >> 1 = {5 >> 1}')

# 6. Desplazamiento a la izquierda ( << )
print(f'5 << 1 = {5 << 1}')
print('======================')

print('D E  A S I G N A C I Ó N')
print('======================')
# 1. Asignación ( = )
a = 5
print(f'a = {a}')  # a = 5

# 2. Asignación de adición ( += )
a += 1
print(f'a += 1 = {a}') 

# 3. Asignación de substracción ( -= )
a -= 1
print(f'a -= 1 = {a}')  

# 4. Asignación de multiplicación ( *= )
a *= 2
print(f'a *= 2 = {a}')  

# 5. Asignación de división ( /= )
a /= 2
print(f'a /= 2 = {a}')  

# 6. Asignación de módulo ( %= )
a = 10
a %= 2
print(f'a (10) %= 2 = {a}') 

# 7. Asignación de potencia ( **= )
a = 8
a **= 2
print(f'a (8) **= 2 = {a}')  

# 8. Asignación de división entera ( //= )
a //= 2
print(f'a //= 2 = {a}')
print('======================')

print('L Ó G I C O S')
print('======================')
# 1. and
a = 10
b = 5
print(f'a == 10 and b == 5 --> {a == 10 and b == 5}')

# 2. or 
print(f'a == 10 or b == 15 --> {a == 10 or b == 15}')

# 3. not
a = True
print(f'not a = {not a}')
print('======================')

print('D E  P E R T E N E N C I A')
print('======================')
# 1. in
lista_numeros = [1, 2, 3, 4, 5]
print(lista_numeros)
print(f'¿Se encuentra en la lista el número "3"? --> {3 in lista_numeros}')
print('======================')

# 2. not in
lista_lenguajes = ['Python', 'JavaScript', 'C#', 'PHP']
print(lista_lenguajes)
print(f'¿No se encuentra en la lista el lenguaje "Java"? --> {'Java' not in lista_lenguajes}')
print('======================')

print('D E   I D E N T I D A D')
print('======================')
# 1. is
a = 888
print(f'a = 888')
print(f'¿a is 888? --> {a is 888}')

# 2. is not
print(f'¿a is not 999? --> {a is not 999}')

print('======================')

print('E S T R U C T U R A S   D E   C O N T R O L')
print('======================')
print('1. I F')
num = 8
if num > 0:
	print(f'{num} es un número positivo.')
print('======================')

print('1.1. I F - E L S E')
if num < 0:
	print(f'{num} es un número negativo.')
else:
	print(f'{num} es un número positivo.')
print('======================')

print('1.2. I F - E L I F - E L S E')
num = 0
if num > 0:
	print(f'{num} es un número positivo.')
elif num < 0:
	print(f'{num} es un número negativo.')
else:
	print('El número es cero.')
print('======================')

print('1.3. O P E R A D O R  T E R N A R I O ')
num = 8
print('Es positivo.') if num > 0 else print('Es negativo.')
print('======================')

print('2. F O R')
lista_nombres = ['Iván','Gera', 'Joaquín']
for nombre in lista_nombres:
	print(nombre)
print('======================')

print('2.1. F O R  E N U M E R A T E')
lista_nombres = ['Iván', 'Gera', 'Joaquín']
for indice, valor in enumerate(lista_nombres):
	print(indice, valor)
print('======================')

print('2.2. F O R  R A N G E')
for _ in range(4):
	print('Python')
print('======================')
	
print('3. W H I L E ')
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
print('======================')

print('4. T R Y ')
a = 10
try:
	resultado = a / 0
except ZeroDivisionError:
	print('No se puede dividir entre cero.')
print('======================')

print(' E X T R A ')
for i in range(10, 56): 
    if i % 2 == 0 and i != 16 and i % 3 != 0:  
        print(i)

