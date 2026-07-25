print("ARITHMETIC OPERATORS:")

a = 4
b = 2

print(f"""
adition: 4 + 2 = {a + b}\n
substraction: 4 - 2 = {a - b}\n
multiplication: 4 * 2 = {a * b}\n
division: 4 / 2 = {a / b}\n
modulus: 4 % 2 = {a % b}\n
exponentiation: 4 ** 2 {a**b}\n
floor division: 4 // 2 {a // b}
""")

print("ASSIGMENT OPERATORS:\n")

my_number = 7
print(f"assigment = {my_number}")
my_number += 1
print(f"sum assigment = {my_number}")
my_number -= 1
print(f"substraction assigment = {my_number}")
my_number *= 2
print(f"multiplication assigment = {my_number}")
my_number /= 2
print(f"division assigment = {my_number}")
my_number %= 4
print(f"modulus assigment = {my_number}")
my_number **= 2
print(f"exponentiation assigment = {my_number}")
my_number //= 4
print(f"floor division assigment = {my_number}\n")

print("IDENTITY OPERATORS:\n")

my_new_number = my_number
print(f"my_number is my_new_number: {my_number is my_new_number}")
print(f"my_number is not my_new_number: {my_number is not my_new_number}\n")

print("MEMBERSHIP OPERATORS\n")

print(f"'i' in 'Martin' = {'i' in 'Martin'}")
print(f"'i' not in 'Martin' = {'i' not in 'Martin'}\n")

print("BIT OPERATORS:\n")

print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")

print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}\n")  # 101000

print("CONTROL ESTRUCTURES:\n")
print("Conditional:\n")

my_string = "Martin"

if my_string == "Martin":
    print(f"my string is {my_string}\n")
elif my_string == "Melo":
    print(f"my_string is {my_string}\n")
else:
    print(f"my_string is not {my_string}\n")

print("loop for:\n")
hash = "#"
for i in range(10):
    print(hash)
    hash += "#"

print("loop while:\n")

i = 0

while i <= 10:
    print(i)
    i += 1

print("\nException Handling:\n")

try:
    print(10 / 0)
except:
    print("Esta no es una diciosión válida, divides entre 0")
finally:
    print("Ha finalizado el manejo de excepciones\n")

print("EXTRA\n")

for i in range(10, 56):
    num_par = i % 2 == 0
    not_multiple_of_3 = i % 3 != 0

    if num_par and i != 16 and not_multiple_of_3:
        print(i)
