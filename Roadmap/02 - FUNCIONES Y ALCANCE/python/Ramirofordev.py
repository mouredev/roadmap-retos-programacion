# Funciones

# Funcion sin parametro ni retorno
def hello_python():
    print("Hola a todos, este es mi codigo en Python!")

hello_python()

# Funcion con parametros pero sin retorno
def area_circulo(ra, pi):
    print(f"El de tu circulo es {pi * ra**2}")

area_circulo(2, 3.1416)

# Funcion con parametros y retorno
def say_hello_to_user(user, times):
    n = 0
    for i in range(times):
        print(f"Hello {user}!")
        n += 1

    return n

count = say_hello_to_user("nacho", 8)
print(f"Se le dijo hola al usuario {count}")

# Funciones dentro de funciones

def show_pair_numbers(): 
    def get_pair_numbers():
        numbers = [1, 2, 3, 4, 5, 6]
        pair_numbers = []
        for i in numbers:
            if i % 2 == 0:
                pair_numbers.append(i)
            
        return pair_numbers
    
    pair_numbers = get_pair_numbers() 
    print(pair_numbers)
    
show_pair_numbers()

# Funciones ya creadas por python
print(sum(5 + 2))

# Variables locales y globales

global pi 

def pi_plus_everything(): 
    pi = 3.1416
    print(pi)
    ultimo_resultado = 0
    for i in range(100):
        print(f"Pi * {i} es = {pi * i}")
        ultimo_resultado = {pi * i}
    print(ultimo_resultado)

# print(ultima_operacion) dara error porque solo se puede usar en el scope de la funcion mientras que pi se puede usar en cualquier parte del codigo

pi = "pi"

print(pi)

# Ejercicio opcional

def opc_exercise(text1, text2):
    # La funcion imprime todos los numeros del 1 al 100
    counts_numbers = 0
    for i in range(100):
        if i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        elif i % 3 == 0 and i % 5 == 0:
            print(text1 , " " , text2)
        else:
            print(i)
            counts_numbers += 1
    return counts_numbers

cantidad = opc_exercise("Pablo", "queso")
print(cantidad)