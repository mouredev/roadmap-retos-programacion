""""
Operadores
"""
# Operadores artiméticos
op_sum = 2 + 5
print(op_sum)
op_res = 10 - 3
print(op_res)
op_div = 20/10
print(op_div)
op_multiply = 4*5
print(op_multiply)
op_module = 16 % 3
print(op_module)
op_pow = 3**3
print(op_pow)
op_div_int = 35//7
print(op_div_int)

#Operadores lógicos
a = 3
b = 4

op_and = b > a and b >=10
print(op_and)
op_or = a < b or b < 12
print(op_or)
op_not = not a > b
print(op_not)

#Operadores de comparación
b = 10
c = 30

op_equal = b == c
print(op_equal)
op_menor = c > b
print(op_menor)
op_mayor = b < 30
print(op_mayor)
op_minus_than = c <= b
print(op_minus_than)
op_mayor_than = b >= c
print(op_mayor_than)
op_distinct = b != c
print(op_distinct)

# Operadores de asignación
num = 35
num += 1 #suma y asiganación
print(num)
num -= 1 # resta y asiganación
print(num) 
num *= 3 # multiplicación y asiganación
print(num) 
num /= 5 # division y asiganación
print(num)
num %= 10 # modulo y asignación
print(num)
num **= 3 # potencia y asiganación
print(num)
num //= 6 # division entera y asiganación
print(num)

""""
Estrcuturas de control
"""

# Condicionales
numero = 7
if numero != 350:
    print("No es mi numero favorito")
elif numero * 50 == 350:
    print("Ese es mi numero favorito")
else:
    print("Prueba otro numero")

# Iterativas
for i in range(35):
    if i % 2 == 0:
        print("Es un número par")
    else:
        print("Es número impar")


i = 0
while(i<=35):
    i += 1
    print(i)

#Excepciones

try:
    print(20 / 0)
except:
    print("No se puede realizar esa operación")


"""
Extra
"""

for i in range(10,56):
    if i % 2 == 0 and i % 3 != 0 and i != 16:
        print(i)
