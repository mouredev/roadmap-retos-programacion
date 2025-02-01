# OPERADORES

#----OPERADORES ARITMETICOS----
# ---- SUMA ----
sum = 10 + 13
print(f'La suma de 10 + 13 = {sum}')
# ---- RESTA ----
resta = 10 - 13
print(f'La resta de 10 - 13 = {resta}')
# ---- MULTIPLICACION ----
multiplicacion = 10 * 13
print(f'La multiplicacion de 10 * 13 = {multiplicacion}')
# ---- DIVISION ----
division = 10 / 13  
print(f'La division de 10 / 13 = {division}')
# ---- DIVISION ENTERA ----
division_entera = 10 // 13  
print(f'La division entera de 10 // 13 = {division_entera}')    
# ---- MODULO ----
modulo = 10 % 13      
print(f'El modulo de 10 % 13 = {modulo}')
# ---- POTENCIA ----
potencia = 10 ** 3 
print(f'La potencia de 10 ** 3 = {potencia}')

#OPERADORES DE COMPARACION
# ---- IGUAL ----
print(f'Igualdad: 10 == 13 = {10 == 13}')
# ---- DISTINTO ----
print(f'Distinto: 10 != 13 = {10 != 13}')
# ---- MAYOR ----
print(f'Mayor: 10 > 13 = {10 > 13}')
#  ---- MENOR ----
print(f'Menor: 10 < 13 = {10 < 13}')
# ---- MAYOR O IGUAL ----
print(f'Mayor o igual: 10 >= 13 = {10 >= 13}')
# ---- MENOR O IGUAL ----
print(f'Menor o igual: 10 <= 13 = {10 <= 13}')

#OPERADORES LOGICOS
# ---- AND ----
print(f'AND &&: 10 + 3 == 12 and 5 - 4 == 1  = {10 + 3 == 12 and 5 - 4 == 1}')
# ---- OR ----
print(f'OR ||: 10 + 3 == 13 and 5 - 4 == 1 = {10 + 3 == 13 or 5 - 4 == 1}')
# ---- NOT ----
print(f'NOT !: not 10 + 3 == 14 = {not 10 + 3 == 14}')

# OPERADORES DE ASIGNACION
# ---- ASIGNACION ----
x = 10
print(f'Asignacion: x = 10 = {x}') 
# ---- ADICION DE VALORES DE UNA VARIABLE ----
x += 5
print(f'Adicion: x += 5 = {x}')
# ---- RESTA DE VALORES DE UNA VARIABLE----
x -= 5
print(f'Resta: x -= 5 = {x}')
# ---- MULTIPLICACION DE VALORES DE UNA VARIABLE----
x *= 5
print(f'Multiplicacion: x *= 5 = {x}')
# ---- DIVISION DE VALORES DE UNA VARIABLE----
x /= 5
print(f'Division: x /= 5 = {x}')
# ---- DIVISION ENTERA DE VALORES DE UNA VARIABLE----
x //= 5
print(f'Division entera: x //= 5 = {x}')
# ---- MODULO DE VALORES DE UNA VARIABLE----
x %= 5
print(f'Modulo: x %= 5 = {x}')
# ---- POTENCIA DE VALORES DE UNA VARIABLE----
x **= 5
print(f'Potencia: x **= 5 = {x}')

#  OPERADORES DE IDENTIDAD
new_x = x
# ---- IS ----
print(f'Is: x is new_x = {x is new_x}')
# ---- IS NOT ----
print(f'Is not: x is not new_x = {x is not new_x}')

# OPERADORES DE PERTENENCIA
# ---- IN ----
print(f'In: "a" in "Annerssv" = {"a" in "Annerssv"}')
print(f'In: "a" not in "Annerssv" = {"a" not in "Annerssv"}')

# OPERADORES DE BIT
a = 10 #1010 
b = 3 #0011

# ---- AND ----
print(f'AND: 10 & 13 = {10 & 13}') #0010
# ---- OR ----
print(f'OR: 10 | 13 = {10 | 13}') #1011
# ---- XOR ----
print(f'XOR: 10 ^ 13 = {10 ^ 13}') #1001
# ---- NOT ----
print(f'NOT: ~10 = {~10}')
# ---- DESPLAZAMIENTO A LA DERECHA ----
print(f'Desplazamiento a la derecha: 10 >> 13 = {10 >> 2}') #0010
# ---- DESPLAZAMIENTO A LA IZQUIERDA ----
print(f'Desplazamiento a la izquierda: 10 << 13 = {10 << 2}') #101000



#ESTRUCUTURAS DE CONTROL

#SENTENCIAS CONDICIONALES

mi_cadena = 'Annerssv'

if mi_cadena == 'Annerssv':
    print('Mi cadena es "Annerssv"')
elif mi_cadena == 'Pier':
    print('Mi cadena es "Pier"')
else:
    print('Mi cadena no es "Annerssv" ni "Pier"')


# BUCLES

# ---- FOR ----
for i in range(10):
    print(i)

# ---- WHILE ----
contador = 0

while contador < 10:
    print(contador)
    contador += 1   

# MANEJO DE EXCEPCIONES

try:
    print(10 / 0)

except:
    print('No se puede dividir entre 0')

finally:
    print('Se ha ejecutado el manejo de errores')


# RETO EXTRA

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
        
