# Función sin parámetros ni retorno
def greeting() -> None:
    print("Hello World!")


greeting()


# Función con parámetros sin retorno
def print_language(language) -> None:
    print(f"{language}")


print_language("Python")


# Función con parámetros y retorno
def is_pair(num1: int) -> bool:
    return num1 % 2 == 0


print(is_pair(4))


# Funciones anidadas
def parent():
    def nested():
        pass


ages = [25, 16, 19, 50, 34]

# Funciones de Python
print(f"Las edades ordenadas: {sorted(ages)}")
print(f"El edad mas alta es: {max(ages)}")
print(f"El valor ASCII de la letra 'a' es: {ord('a')}")


# Varaibles locales
def using_local_variables():
    notes = [100, 85.6, 79.4, 87, 94]  # variable local
    notes.append(60)

    def nested():  # Tiene acceso a las variables de la función padre
        print(f"Las notas son: {notes}")

    nested()


using_local_variables()


# Variables globales
global number
number = 5


def using_global():
    global number  # para usar la variable global
    number = 4  # modifica la variable global


using_global()
print(f"El valor actual de number es: {number}")


# EXTRA
def extra(str1: str, str2: str) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{str1 + str2}")
        elif i % 3 == 0:
            print(f"{str1}")
        elif i % 5 == 0:
            print(f"{str2}")
        else:
            print(i)
            count += 1
    return count


count = extra("Hello", "World")
print(f"Cantidad de números impresos: {count}")
