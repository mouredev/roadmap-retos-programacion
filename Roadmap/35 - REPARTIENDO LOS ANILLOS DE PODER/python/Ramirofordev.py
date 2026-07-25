'''
Ejercicio:
Desarrolla un programa que se encargue de distribuir los anillos del poder.

Requisitos:
    1. Los elfos recibiran un numero impar.
    2. Los enanos un numero primo.
    3. Los hombres un numero par.
    4. Sauron siempre uno.

Acciones:
    1. Crea un programa que reciba el numero total de anillos y busque una posible combinacion para repartirlos.
    2. Muestra el reparto final o el error al realizarlo.
'''
print(2 % 30)

# Obtenemos la cantidad de anillos a repartir.
anillos = int(input("Inserte la cantidad de anillos a repartir: "))

if anillos <= 0:
    print("No se pueden repartir los anillos, porque no hay.")
    exit()

def es_impar(n):
    if n % 2 != 0:
        return True
    return False

def es_par(n):
    if n % 2 == 0:
        return True
    return False

def es_primo(n):
    if n <= 1:
        return False
    for numeros in range(2, n):
        if n % numeros == 0:
            return False
    return True

solucion = False

# Le damos un anillo a sauron 
resto = anillos - 1

for elfos in range(1 , resto + 1):
    if not es_impar(elfos): continue

    for enanos in range(1, resto - elfos + 1):
        if not es_primo(enanos): continue

        for hombres in range(1, resto - elfos - enanos + 1):
            if not es_par(hombres): continue

            if elfos + enanos + hombres == resto:
                print(f"Los anillos han sido repartidos! \n"\
                    f"Elfos: {elfos}\n"\
                    f"Enanos: {enanos}\n"\
                    f"Hombres: {hombres}\n"\
                    "Sauron: 1.")
                solucion = True

if not solucion:
    print("\nNo existe una combinacion valida para repartir los anillos.")