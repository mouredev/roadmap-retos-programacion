# fUNCIONES

#### Suma

def suma(num1, num2):
    print("Suma: ", num1, "+", num2, "=", num1 + num2)

suma(3, 2)

print()
#### Suma de strings

def full_name(name, surname):
    print("Nombre completo:", name, surname)

full_name("Juan", "Pérez")

print()
#### Funcion llama a otro funcion

def if_less (number):
    if int(number) > 4:
        print (f"{number} es mayor que 4")
    elif int(number) == 4:
        print (f"El numero es igual a 4")
    else:
        print (f"El numero es menor a 4")


def sum_if(num1, num2):
    mi_suma = num1 + num2
    print(f"Suma: {mi_suma}")
    if_less(mi_suma)

n1 = input("Ingrese un numero entero: ")
n2 = input("ingrese otro numero entero: ")

sum_if(int(n1), int(n2))

print()

#### Funcion sencilla con return

def suma_str (str1, str2):
    resultado = str1 + str2
    return resultado

print (suma_str("Saludos a ", "todos ustedes"))

#### Funciones incorporadas en Python

print()

a = 1234
b = str(a)
print(len(b), "es el largo de la variable a = 1234, que previamente debe pasarse a string con otra funcion de Python como str()")

print()


#### FUNCION SIMPLE Y EJEMPLO DE VARIABLE GLOBAL Y LOCAL

my_global_variable ="Soy una variable global, llamame desde cualquier funcion"

def saludo():
    my_local_variable = "Soy una variable local, no me llames desde fuera de esta funcion"
    print("Hola, soy una funcion!")
    print(my_global_variable)
    print(my_local_variable)


saludo()

#### Extra

def extra_02 (text1, text2):

    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
           print(f"{index}: {text1} {text2} Es múltiplo de 3 y 5")
        elif index % 3 == 0:
           print(f"{index}: {text1} Es múltiplo de 3")
        elif index % 5 == 0:
            print(f"{index}: {text2} Es múltiplo de 5")
        else:
            print (index)

    return index


print(f"El numero se imprimió {extra_02("Texto 1", "Texto 2")} veces")

# THE END. TO BE CONTINUED...




