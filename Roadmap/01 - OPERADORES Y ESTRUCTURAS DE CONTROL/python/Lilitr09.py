# Name: Liliana N. Torres Rignack

# EJERCICIO

# OPERADORES ARITMETICOS
print("--> OPERADORES ARITMETICOS <--")

my_sum = 10 + 9
print(my_sum)

my_rest = 10 - 9
print(my_rest)

my_multiplication = 79 * 45
print(my_multiplication)

my_division = 189 / 4
print(my_division)

modulo_operator = 20 % 2
print(modulo_operator)

my_floor_division = 256 // 3
print(my_floor_division)

my_exponent = 2**6
print(my_exponent)

# OPERADORES DE COMPARACION
print("--> OPERADORES DE ASIGNACION <--")
print(2 == 2)  # True
print("A" != "a") # True
print(25 > 30) # False
print(23456 < 23658) # True
print(10 >= 10) # True
print(5 <= 6) # True

# OPERADORES LOGICOS
print("--> OPERADORES LOGICOS <--")
print(f"False and False --> {False and False}") # False
print(f"True or False --> {True or False}") # True
print(f"not True --> {not True}") # False

# OPERADORES DE ASIGNACION
my_name = "Liliana" # Asignacion simple
my_num: int = 2
my_num += 4 # my_num = 6
my_num -= 1 # my_num = 5
my_num *= 5 # my_num = 25
my_num /= 5 # my_num = 5

# BITS
print("--> BITS <--")
x = 4
y = 5
print(f"AND bit a bit --> {x & y}")
print(f"OR bit a bit --> {x | y}")
print(f"XOR bit a bit --> {x ^ y}")
print(f"Complemento bit a bit --> {x} --> {~x}")
print(f"Desplazamiento a la izquierda {x << 1}")
print(f"Desplazamiento a la derecha {x >> 1}")

# OPERADORES DE IDENTIDAD
print("--> OPERADORES DE IDENTIDAD <--")
variable_1: str = "Variable"
variable_2: str = "variable"
print(variable_1 is variable_2) # False
print(variable_1 is not variable_2) # True

# OPERADORES DE PERTENENCIA
print("--> OPERADORES DE PERTENENCIA <--")
my_list = [10, 20, 30, 40, 50]
print(25 in my_list) # False
print(40 not in my_list) # False

# ESTRUCTURAS DE CONTROL

print("--> CONDICIONAL <--")
# Condicionales
var = 10
if var < 12:
    print("Less than 12")
elif var > 12:
    print("Greater than 12")
else:
    print("Equals to 12")

print("--> WHILE LOOP <--")    
# Bucles while
var = 1
while var <= 5:
    print(var)
    var += 1

print("--> FOR LOOP <--")    
# Bucles for
for _ in range(6):
    print("This is a for loop!")

print("--> TRY / EXCEPT <--")    
# Excepciones
try:
    print("Trying")
except ValueError:
    print("Cannot do this")

print("--> EXTRA <--")    
# DIFICULTAD EXTRA
def numbers(a, b):
    for number in range(a, b + 1, 2):
        if number is not 16 and number % 3 != 0:
            print(number)

numbers(10, 55)
        