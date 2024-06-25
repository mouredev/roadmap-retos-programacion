# Funciones

# Función simple

def say_hi():
    print("Hola!")


say_hi()


# Funcion con retorno

def alias_dev():
    alias = "DevsDav"
    return alias


name = alias_dev()
print(name)


# Funcion con un argumento

def triple_value(value):
    return value * 3


print(triple_value(3))


# Funcion con varios argumentos

def get_hypotenuse(cathetus_a, cathetus_b):
    hypotenuse = (cathetus_a**2 + cathetus_b**2)**(0.5)
    return hypotenuse


print(get_hypotenuse(3, 4))


# Funcion con argumento predeterminado

def mode_house(mode="default"):
    return mode


print(mode_house())
print(mode_house("Noche de juegos"))


# Funcion con retorno de varios valores

def get_subjects():
    return "lenguaje", "matemáticas", "íngles", "tecnología"


subject_1, subject_2, subject_3, subject_4 = get_subjects()

print(f"Asignaturas: {subject_1}, {subject_2}, {subject_3}, {subject_4}")


# Funciones propias del lenguaje

list_numbers = list(range(30))
print(len("DevsDav"))
print(type(1.2))
print(list_numbers)


# Variables locales y  globales

global_var = "Me puedes llamar de cualquier parte del código"


def example():
    local_var = ", a mi solo me puedes llamar dentro de mi función."
    print(global_var + local_var)


example()
print(global_var)
# print(local_var) # no se puede acceder


# Challenge Extra

def challenge_fun(first_string, second_string):
    number = 0
    for i in range(0, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(first_string + second_string)
        elif i % 3 == 0:
            print(first_string)
        elif i % 5 == 0:
            print(second_string)
        else:
            print(i)
            number += 1
    return number


print(challenge_fun("fizz", "buzz"))
