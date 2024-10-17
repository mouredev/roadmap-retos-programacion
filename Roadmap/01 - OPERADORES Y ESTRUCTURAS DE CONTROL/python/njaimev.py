
# Primero tenemos los operadores aritmeticos para realizar operaciones matematicas

a = 6
b = 15

print(a + b)
print(a - b)
print(a * b)
print(b / a)
print(b % a)
print(a ** b)
print(b // a)

# // sería una división entera sin decimales

# Luego tenemos los operadores de asignación que se usan para asignar valores a variables

asign_suma = 3 #suma y asigna
asign_suma += 4 
print(asign_suma)

asign_resta = 6 #resta y asigna
asign_resta -= 2 
print(asign_resta)

asign_mult = 2 #multiplica y asigna
asign_mult *= 2 
print(asign_mult)

asign_div = 12 #divide y asigna
asign_div /= 10 
print(asign_div)

asign_mod = 12 #modulo y asigna
asign_mod %= 18 
print(asign_mod)

asign_exp = 2 #exponenciacion y asigna
asign_exp **= 2 
print(asign_exp)

asign_div_e = 4 #division entera y asigna
asign_div_e //= 3 
print(asign_div_e)

# Tambien estan los operadores de comparacion
# Usando las variable ya definidas a y b

print(a == b)
print(a != b)
print(a < b)
print(a > b)            # Esto dara como resultado un booleano
print(a <= b)
print(a >= b)

# Operadores logicos para realizar operaciones logicas entre booleanos

a = False
b = True

print(a and b)  #True si ambos son true
print(a or b)   #True si alguno es true
print(not b)  #Devuelve lo contrario (False)

# Los operadores de identidad comprueban si dos objetos son el mismo (en memoria)

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_a is list_b) #True, el mismo contenido en la "misma" memoria
print(list_c is list_a) #False, los datos son los mismos pero ocupan memoria distinta

# Operadores de pertenencia comprueban si un valor esta en una secuencia

list_x = [1, 2, 3, 4, 5, 6]

print(5 in list_x) #True
print(9 not in list_x) #True

# Operadores de bits realizan operaciones logicas a nivel de bits

num_1 = 3 #0011
num_2 = 8 #1000

print(num_1 & num_2)
print(num_1 | num_2)
print(num_1 ^ num_2)
print(~num_2)
print(num_1 << num_2)
print(num_1 >> num_2)

# If, if else, else

nota = 4

if nota > 4:
    print("Apruebas")
elif nota < 4: 
    print("REPRUEBAS!")
else:
    print("nota morada uf")

# Bucle, para repetir un bloque de codigo hasta que se cumpla la condición

# FOR

nombres = ["Ana", "Luis", "Carlos"]
for nombre in nombres:
    print(f"Hola, {nombre}!")

# WHILE

numero = 0
while numero <= 3:
    print(numero)
    numero += 1


# EJERCICIO EXTRA 

for num in range(10, 56):  # Recorre números del 10 al 55
    if num % 2 == 0 and num != 16 and num % 3 != 0: #al dividir por 2 el num da 0 Y el numero es distinto a 16
        print(num)                                  # Y el restante al dividir por 3 es distinto a 0
