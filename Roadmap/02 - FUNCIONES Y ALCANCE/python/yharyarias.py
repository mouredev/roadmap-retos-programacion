# Funciones básicas que representen las diferentes posibilidades del lenguajee
def hello_world():
    print("¡Hello world!")
hello_world()

def greeting(name):
    print(f"Hello {name}")
greeting('Yhary')

def addition(num1, num2):
    result = num1 + num2
    print(f"El resultado de la suma de los números {num1} y {num2} es {result}")
addition(4, 6)

def get_number():
    return 42
reult = get_number()
print(f"The number obtained is: {reult}")

def square(num):
    return num ** 2
result = square(5)
print(f"The square of 5 is: {result}")

def multiply(a, b):
    return a * b
result = multiply(4, 6)
print(f"El resultado de la multiplicación es: {result}")

# -------------------------------------------------------------
# Funciones dentro de funciones
def operators(a, b):
    def addition():
        return a + b

    def subtraction():
        return a - b

    def multiplication():
        return a * b

    def division():
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero."

    result_addition = addition()
    result_subtraction = subtraction()
    result_multiplication = multiplication()
    result_division = division()

    print(f"Addition: {result_addition}")
    print(f"Subtraction: {result_subtraction}")
    print(f"Multiplication: {result_multiplication}")
    print(f"Division: {result_division}")
operators(10, 5)

# -------------------------------------------------------------
# Funciones del lenguaje
# sorted()
print("Ordered list:", sorted([4, 1, 8, 3, 7]))
# len()
print("List size:", len([4, 1, 8, 3, 7]))
#sum()
print("Sum of the elements of the list:", sum([4, 1, 8, 3, 7]))
# type()
num = 3
print("Data type:", type(num))
# max()
print("Largest item in the list:", max([4, 1, 8, 3, 7]))
# min()
print("Smallest item in the list:", min([4, 1, 8, 3, 7]))
# str()
print("Number as string:", str(num))
# list()
my_tuple = (1, 2, 3, 4, 5)
print("Tuple as list:", list(my_tuple))

# -------------------------------------------------------------
# DIFICULTAD EXTRA (opcional):
def function(a: str, b: str) -> int:
    counter = 0
    for i in range(1, 101):
        if i % 3 == 0:
            print(a)
        elif i % 5 == 0:
            print(b)
        elif i % 3 == 0 and i % 5 == 0:
            print(a, b)
        else:
            counter += 1

    return print(f"{counter} numbers are not multiplies of 3 and 5")

function("Multiplo of 3", "Multiplo of 5")
