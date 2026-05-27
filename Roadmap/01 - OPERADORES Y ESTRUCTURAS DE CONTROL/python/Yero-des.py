# Operador de asignacion
n1 = 10
n2 = 20

# Operadores aritmeticos
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)

# Asignacion
age = 21
age -= 4
print(f"Mi edad es: {age}")

# Bits
print(f"Movimiento de 2 bits: {50 >> 2}")
print(f"Movimiento de 1 bit: {50 >> 1}")

# Condicionales
if age < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

number_list = range(1,10)

# Identidad
print(f"Tipo de objecto: {type(number_list)}")

# Pertenencia
print(1 in number_list)

# Iteracion
for i in number_list:
    print(f"Numero iterado: {i}")
    
# Excepcion
try:
    number_list[11]
except Exception as e:
    print(f"Ha ocurrido una excepcion: {e}")
    
    
# Desafio Extra
numbers_range = range(10,56)

for i in numbers_range:
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)