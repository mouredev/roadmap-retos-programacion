# Funciones y Alcaneces
# Autor: byTiagoGhost

# Funciones
# Funcion sin parametros y sin retorno
def my_function():
  print("Hola desde una funcion")

my_function()
print("")

# Funcion con parametros o argumento y sin retorno
def my_function(nombre):
    print("Hola " + nombre)

my_function("Tiago")
my_function("Ghost")
my_function("Santiago")
print("")

# Funcion con mas de un parametro o argumento y sin retorno
def my_function(nombre, programa):
    print("Hola " + nombre + " y este es tu programa que esta practicando " + programa)

my_function("Tiago", "Python")
my_function("Ghost", "Python")
my_function("Santiago", "Python")    
# Recordatorio o el envio de parametros solo se puede enviar los necesarios o los que se requieran
# Si no sabes cuantos parametros se enviaran puedes usar *args
def my_function(*nombres):
   print("El nombre es " + nombres[2])

my_function("Tiago", "Ghost", "Santiago")  
# Tabiem puedes enviar parametros con un valor por defecto
def my_function(nombre1, nombre2, nombre3):
    print("Hola ni nombre es: " + nombre3)

my_function(nombre1 = "Tiago", nombre2 = "Ghost", nombre3 = "Santiago")
# Si no sabes cuantas palabras claves hay en el argumento puedes usar **kwargs 
def my_function(**nombres):
    print("El nombre comprimido es " + nombres["nombre1"])

my_function(nombre1 = "Tiago", nombre2 = "Ghost", nombre3 = "Santiago")
# Puedes enviar hasta una lista como parametro
def my_function(comida):
    for x in comida:
        print(x)

comida = ["Manzana", "Banana", "Fresa"]
my_function(comida)
print("")

# Funcion con retorno
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print("")
# Si se puede crear una funcion dentro de otra funcion, pero eso si tienes que tener mucho cuidado
# de como funciona, o si tienes claro de como funciona
def my_function(x):
    def my_function2(y):
        return y * x
    return my_function2

mydoubler = my_function(2)
mytripler = my_function(3)
print(mydoubler(11))
print(mytripler(11))
print("")

# Funciones de la propia libreria 
# abs() Retorna el valor absoluto de un numero
x = abs(-7.25)
print(x)
print("")
# all() Retorna True si todos los elementos de un iterable son verdaderos
x = all([True, True, True])
print(x)
print("")
# any() Retorna True si algun elemento de un iterable es verdadero
x = any([True, False, True])
print(x)
print("")
# ascii() Retorna una version legible de un objeto
x = ascii("Mi nombre es Ståle")
print(x)
print("")
# bin() Convierte un numero en binario
x = bin(36)
print(x)
print("")
# bool() Retorna el valor booleano de un objeto
x = bool(0)
print(x)
print("")
# bytearray() Retorna un arreglo de bytes
x = bytearray(5)
print(x)
print("")
# bytes() Retorna un objeto de bytes
x = bytes(5)
print(x)
print("")
# chr() Retorna un caracter representado por el numero
x = chr(97)
print(x)
print("")
# max() Retorna el elemento mas grande de un iterable
x = max(5, 10, 25)
print(x)
print("")
# min() Retorna el elemento mas pequeño de un iterable
x = min(5, 10, 25)
print(x)
print("")
# pow() Retorna el valor de x elevado a la potencia de y
x = pow(4, 3)
print(x)
print("")
# round() Redondea un numero
x = round(5.76543, 2)
print(x)
print("")

# Alcances
# Global
x = "Global"
def myfunc():
    print("Python es " + x)

myfunc()
print("Python es " + x)
print("")
# Local
def myfunc():
    x = "Local"
    print("Python es " + x)

myfunc()
print("Python es " + x)
print("")
# Global Keyword
def myfunc():
    global x
    x = "Global"
    print("Python es " + x)

myfunc()
print("Python es " + x)
print("")

# Ehercicios Practicos
primerParametro = "Hola"
segundoParametro = "Mundo"
global Cont
def numerosEnTexto(primerParametro, segundoParametro):
    Cont = 0
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0: # x % 3 == 0
            print(primerParametro + " " +segundoParametro)
            Cont += 1
            continue
        elif x % 3 == 0: # x % 5 == 0
            print(primerParametro)
            Cont += 1
            continue
        elif x % 5 == 0: # x % 3 == 0 and x % 5 == 0
            print(segundoParametro)
            Cont += 1
            continue
        else:
            print(x)
    return Cont

numeroDeVeces=numerosEnTexto(primerParametro, segundoParametro)
print("Este fue el numero de veces que se imprimio los dos textos:", numeroDeVeces)