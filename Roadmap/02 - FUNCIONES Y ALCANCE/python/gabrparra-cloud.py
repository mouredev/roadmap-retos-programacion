
#Funcion sin parametros y retorno
def saludar():
    nombre = "Gabrparra"
    
saludar()

#Funcion sin parametros y retorno
def saludar2():
    nombre = "Gabrparra"
    print("Función Saludar 02 " + nombre)
saludar()

#funcion con parametros y retorno
def saludar3(nombre):
    print("Función Saludar 03 " + nombre)
saludar3("Gabrparra")

#funcion con parametros y retorno
def saludar4(nombre):
    return "Función Saludar 04 " + nombre
print(saludar4("Gabrparra"))

def saludar5(nombre, apellido):
    return "Función Saludar 05 " + nombre + " " + apellido
print(saludar5("Gabrparra", "Parra"))
print(saludar5(nombre="Nombre", apellido="Apellido"))

def suma_varios_numeros(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(suma_varios_numeros(1, 2, 3, 4, 5))

Nombre = "Gabrparra"
print("Hola " + Nombre + ". Nombre es una variable global")

def saludar6():
    Apellido = "Parra"
    print("Hola " + Nombre + " " + Apellido + ". Apellido es una variable local")
saludar6()

#print("Hola " + Nombre + " " + Apellido + ". Apellido es una variable local") Y NO SE PUEDE USAR PORQUE ES UNA VARIABLE LOCAL Y NO SE PUEDE ACCEDER FUERA DE LA FUNCION

def outer_function():
    def inner_function():
        print("Hola python. Esta es una función interna")
    inner_function()

outer_function()

print(len("Hola python. Esta es una función del leguaje"))
print(type("Hola python. Esta es una función del leguaje"))
print(type(2))
print(type("2"))

def funcion_extra(parametro01,parametro02):
    numero_impresos = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(parametro01 + " " + parametro02)
        elif i % 3 == 0:
            print(parametro01)
        elif i % 5 == 0:
            print(parametro02)
        else:
            print(i)
            numero_impresos += 1

    print(f"Se impresaron {numero_impresos} números.")

funcion_extra("Parametro 01", "Parametro 02")

