# Operadores de aritméticos
print('Operadores de aritméticos')
num_one = 34
num_two = 6
print(f'{num_one} + {num_two} = {num_one + num_two}')
print(f'{num_one} - {num_two} = {num_one - num_two}')
print(f'{num_one} * {num_two} = {num_one * num_two}')
print(f'{num_one} ** {num_two} = {num_one ** num_two}')
print(f'{num_one} / {num_two} = {num_one / num_two}')
print(f'{num_one} // {num_two} = {num_one // num_two}')
print(f'{num_one} % {num_two} = {num_one % num_two}')

# Operadores lógicos
print('Operadores lógicos')
bool_one = True
bool_two = False
print(f'{bool_one} and {bool_two} = {bool_one and bool_two}')
print(f'{bool_one} or {bool_two} = {bool_one or bool_two}')
print(f'not {bool_one} = {not bool_one}')
print(f'not {bool_two} = {not bool_two}')

# Operadores relacionales
print('Operadores relacionales')
print(f'{num_one} equal {num_two} = {num_one == num_two}')
print(f'{num_one} not equal {num_two} = {num_one != num_two}')
print(f'{num_one} more than {num_two} = {num_one > num_two}')
print(f'{num_one} less than {num_two} = {num_one < num_two}')
print(f'{num_one} more or equal than {num_two} = {num_one >= num_two}')
print(f'{num_one} less or equial than {num_two} = {num_one <= num_two}')

# Operadores de asignación
print('Operadores de asignación')
num_a=7; num_b=2
print(f"Operadores de asignación para x={num_a} y {num_b}")
num_x=num_a; num_x+=num_b; print("x+=", num_x)  # 9
num_x=num_a; num_x-=num_b; print("x-=", num_x)  # 5
num_x=num_a; num_x*=num_b; print("x*=", num_x)  # 14
num_x=num_a; num_x/=num_b; print("x/=", num_x)  # 3.5
num_x=num_a; num_x%=num_b; print("x%=", num_x)  # 1
num_x=num_a; num_x//=num_b;print("x//=", num_x) # 3
num_x=num_a; num_x**=num_b;print("x**=", num_x) # 49
num_x=num_a; num_x&=num_b; print("x&=", num_x);  print("x&=", bin(num_x))# 2
num_x=num_a; num_x|=num_b; print("x|=", num_x); print("x|=", bin(num_x))  # 7
num_x=num_a; num_x^=num_b;print("x^=", num_x); print("x^=", bin(num_x))   # 5
num_x=num_a; num_x>>=num_b;print("x>>=", num_x); print("x>>=", bin(num_x)) # 1
num_x=num_a; num_x<<=num_b;print("x<<=", num_x); print("x<<=", bin(num_x)) # 28

# Operadores bitwise
print('Operadores bitwise')
bit_a = 0b1101; bit_b = 0b1011;
print(f'AND: {bit_a} & {bit_b} = {bin(bit_a & bit_b)}') # 0b1001
print(f'OR: {bit_a} | {bit_b} = {bin(bit_a | bit_b)}') # 0b1111
print(f'XOR {bit_a} ^ {bit_b} = {bin(bit_a ^ bit_b)}')
num_a = 40; print(f'NOT {num_a}: {~num_a}'); print(bin(num_a),bin(~num_a))
bit_a=0b1000; print(bin(bit_a>>2)) # 0b10
bit_a=0b0001; print(bin(bit_a<<3)) # 0b1000

# Operadores de Identidad comparan los valores en memoria
print('Operadores de Identidad')
id_a = 10; id_b = 10; print(f'{id_a} is {id_b} = {id_a is id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')
id_a = 10; id_b = 10.0; print(f'{id_a} is {id_b} = {id_a is id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')
id_a = "perro"; id_b = 'perro'; print(f'{id_a} is {id_b} = {id_a is id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')
id_a = "perro"; id_b = 'Perro'; print(f'{id_a} is {id_b} = {id_a is id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')
id_a = "perro"; id_b = 'gato'; print(f'{id_a} is {id_b} = {id_a is id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')
id_a = [1, 2, 3]; id_b = [1, 2, 3]; print(f'{id_a} == {id_b}: {id_a == id_b}'); print(f'{id_a} is {id_b}: {id_a is id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')
id_a = [1, 2, 3]; id_b = [1, 2, 3]; print(f'{id_a} != {id_b}: {id_a != id_b}'); print(f'{id_a} is not {id_b}: {id_a is not id_b}'); print(f'El id del objeto es: {id(id_a)}'); print(f'El id del objeto es: {id(id_b)}')

# Operadores de membresía o pertnencia
print('Operadores de membresía o pertnencia')
memb_phrase = "El perro de San Roque ya no tiene rabo, porque Ramon Ramirez se lo ha cortado"
memb_a = 'perro'; print(f'Is "{memb_a}" in "{memb_phrase}": {memb_a in memb_phrase}')
memb_a = 'Perro'; print(f'Is "{memb_a}" in "{memb_phrase}": {memb_a in memb_phrase}')
memb_a = 'Ramon'; print(f'Is "{memb_a}" in "{memb_phrase}": {memb_a in memb_phrase}')
memb_a = 'gato'; print(f'Is "{memb_a}" in "{memb_phrase}": {memb_a in memb_phrase}')
memb_a = 'perro'; print(f'Is not "{memb_a}" in "{memb_phrase}": {memb_a not in memb_phrase}')
memb_a = 'Perro'; print(f'Is not "{memb_a}" in "{memb_phrase}": {memb_a not in memb_phrase}')
memb_a = 'ramon'; print(f'Is not "{memb_a}" in "{memb_phrase}": {memb_a not in memb_phrase}')
memb_a = 'gato'; print(f'Is not "{memb_a}" in "{memb_phrase}": {memb_a not in memb_phrase}')

# Operador Walrus
print('Operador Walrus')
x = "Python"
print(x)
print(type(x))
print(x := ascii(x))
print(type(x))

print('Utilizando las operaciones')
list_numeros = []
for num_d in range(25,0,-1):
    if num_d - 13 == 0:
        continue
    elif num_d - 13 < -2:
        break
    else:
        list_numeros.append(25 // (num_d - 13))
        list_numeros.append(25 % (num_d - 13))
print(list_numeros)

list_numeros.clear()
num_c = 1
while num_c <= 65:
    list_numeros.append(num_c)
    num_c *=3
print(list_numeros)

list_animals=['cat','dog','fish','mamut',num_c,'fly','butterfly','pikachu']
for animal in list_animals:
    try:
        print(animal.capitalize())
    except Exception as error:
        print(f'El valor que ha fallado ha sido {animal} por fallo {error}')

# Calculadora subred y broadcast
num_mask = 248
num_check = 121
subred = num_mask&num_check
broadcast = subred + (255-num_mask)
print(f'La subred es :{subred}')
print(f'La IP de broadcast es :{broadcast}')

# DIFICULTAD EXTRA (opcional):
print(list(num_z for num_z in range(10,56) if (num_z % 2) == 0 and num_z != 16 and (num_z % 3) != 0 ))