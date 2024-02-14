# Funciones

# Sin parámetros ni retorno

def saludar():
    print("Hola, soy un saludo")

saludar()

# Con parámetros sin retorno

def suma(num1, num2):
    
    resultado = num1 + num2
    print(resultado)

suma(4, 5)


# Con parámetros y retorno


def suma_retorno(num1, num2):
    
    return num1 + num2

print(suma_retorno(4, 5))

# Con parámetros opcionales

def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

print(area_circulo(5))

# Con número variable de argumentos

def promedio(*args):
    return sum(args) / len(args)

print(promedio(10,44,5,6,7))

# Con retorno de varios valores

def varios_retornos():
    return "Paco", "Copa"

name, name2 = varios_retornos()
print(name)
print(name2)

# Funciones anidadas

def operacion(cantidad, balance, tipo="deposito"):
    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantida, balance):
        if cantidad < balance:
            return balance - cantidad
        else:
            return None
    
    if tipo == "deposito":
        return deposito(cantidad, balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)    

print(operacion(20, 40))

# Funciones del lenguaje

print(len("La vida es una moneda"))
print(type(True))
print("pcOSin".lower())

# Scope

animal = "gato" # variable global

persona = "Paco" # variable global

def print_animal():
    global persona # variable global
    persona = "Fernando" 
    animal = "perro" # variable local
    print(animal)
    print(persona)
    
print_animal()

print(animal)    

#EXTRA

def FixBux(str1, str2):
    count = 0
    for num in range(1,100):
        if num % 15 == 0:
            print(f"{str1}{str2}")
        elif num % 5 == 0:
            print(str2)
        elif num % 3 == 0:
            print(str1)
        else:
            print(num)
            count += 1
    return count                 
    
FixBux("Fix", "Bux")    