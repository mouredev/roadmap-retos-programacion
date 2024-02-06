# Operadores Aritméticos

print(4 + 5) # adición
print(5 - 5) # resta
print(7 * 5) # multiplicación
print(9 / 4) # división
print(10 % 2) # módulo
print(4**2) # exponente
print(9 // 3) # división entera 

# Operadores de comparación

print(8 > 4) # Mayor qué
print(8 < 4) # Menor qué
print(8 <= 4) # Menor igual qué
print(8 >= 4) # Mayor igual qué
print(8 == 4) # Igualdad
print(8 != 4) # Desigualdad

# Operadores lógicos

print(8 > 4 and 4 != 2) #Operador and
print(8 < 4 or 2 == 2) #Operador or
print(not 4 == 2) #Operador not

# Operadores de asignación

var_num = 10 # asignación
print(var_num)
var_num += 3 #asignación y suma
print(var_num)
var_num -= 3 #asignación y resta
print(var_num)
var_num *= 2 #asignación y multiplicación
print(var_num)
var_num **= 2 #asignación y exponente
print(var_num)
var_num //= 2 #asignación y división entera
print(var_num)
var_num %= 2 #asignación y módulo
print(var_num)


# Operadores de identidad
print("2 is 2 =", 2 is 2)
print("4 is not 2 =", 4 is not 2)

# Operadores de pertenencia
print("8 in [1, 2, 3] =", 8 in [1, 2, 3])
print("8 not in [1, 2, 3] =", 8 not in [1, 2, 3])

# Operadores de bits
print("\nOperadores de bits:")
print("5 & 2 =", 5 & 2)
print("5 | 2 =", 5 | 2)
print("5 ^ 2 =", 5 ^ 2)
print("~5 =", ~5)
print("5 << 2 =", 5 << 2)
print("5 >> 2 =", 5 >> 2)

# Condicionales

var_cond_1 = 10
var_cond_2 = 20

if var_cond_1 > var_cond_2:
    print(f"{var_cond_1} es mayor")
elif var_cond_1 < var_cond_2:     
    print(f"{var_cond_2} es mayor")
else:
    print("Los números son iguales")

# Bucles
    
# While

i = 0

while (i < 5):
    print(i)
    i += 1

# for
    
    for i in range(10):
        print(i)

# Extra
        
for numero in range(10, 50):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)         
