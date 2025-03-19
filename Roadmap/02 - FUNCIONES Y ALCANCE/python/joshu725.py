# Funciones #

# Simples
def jump():
    print("Salto")

jump()

# Con retorno

def collect():
    return "Objeto"

print(collect())

# Con argumentos

def attack(damage, name):
    return f"Has realizado {damage} de daño al enemigo llamado {name}"

print(attack(20, "Paco"))
print(attack(name="Paco", damage=20))

# Con argumentos predeterminados

def salute(name="a todos"):
    return f"¡Hola {name}!"

print(salute())
print(salute("Juan"))

# Retorno de varios valores

def eat():
    return "Manzana", "Platano"

food1, food2 = eat()

print(food1)
print(food2)

# Con un numero NO especificado de argumentos

def sum(*number):
    total = 0
    for n in number:
        total += n
    return total

print(sum(2, 3, 4, 5))

# Funcion dentro de una funcion #

def a():
    def b():
        print("Test")
    b()

a()

# Funciones de Python #
print(len("Prueba"))
print(type(22))
print(int(23.52))
print("PRUEBA".lower())
print("PRUEBA".capitalize())

# Variables locales y globales #

# Variable global
var = 8  # Las variables declaradas fuera de una función se consideran globales

def test():
    # Variable local
    local = 3

    print(var)

test()
# print(local) # Da error porque estamos intentando acceder a una variable local, es decir, fue declarada dentro de una función

# Extra #

def count(str1, str2):
    n = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str1 + str2)
        elif i % 3 == 0:
            print(str1)
        elif i % 5 == 0:
            print(str2)
        else:
            print(i)
            n += 1

    return n

print(count("Primero", "Segundo"))
