## Funciones integradas en Python

print("Hola, mundo")

lst = [1, 23, 4, 5, 6, 6]
print(len(lst))


name = input("Dime cual es tu nombre ")
print("Hola,", name)


for i in range(5):
    print(i)

number = 23
print(type(number))
number = str(number)
print(type(number))

lst = [1, 3, 9, 10, 21, 33]
print(max(lst))
print(min(lst))


## Funciones básicas definidas por el usuario


def greet():
    print("Hola desde python")


# greet()


## Funciones con parámetros
def greeting(name):
    print("Hola", name, "que tal!")


# greeting("Elkin")


def multiply(value1, value2):
    return value1 * value2


# print(multiply(4, 5))


def sum(a, b):
    return a + b


# print(sum(2, 5))
## Funciones con parámetros predefinidos
def subtraction(a=3, b=4):
    return a - b


# print(subtraction())


def power(a, b=2):
    return a**b


# print(power(5))
## Funcion lambda

square_area = lambda x: x**2
print(square_area(5))
## Funciones anidadas


def exterior(x):
    def interior(y):
        return y * 2  # Esta es la función anidada

    resultado_interior = interior(x)
    return resultado_interior + 5


# llamado a la función exterior
resultado_exterior = exterior(10)
print(resultado_exterior)

# variable global
variable_global = 10


def funcion():
    # variable local dentro de la función
    variable_local = 3
    print("Variable local dentro de la función:", variable_local)

    # acceso a la variable global dentro de la función
    print("Variable global dentro de la función:", variable_global)


funcion()


def extra(param1, param2) -> int:
    count = 1
    numbers = []
    while count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print(f"{count} {param1} y {param2}")
        elif count % 3 == 0:
            print(f"{count} {param1}")
        elif count % 5 == 0:
            print(f"{count} {param2}")
        else:
            numbers.append(count)
        count += 1
    return f"{len(numbers)} Incidencias"

print(extra("Múltiplo de 3", "Múltiplo de 5"))
