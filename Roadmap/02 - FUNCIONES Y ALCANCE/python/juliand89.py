#funciones 


# sin parametro

def saludo():
    print("Esta es una funcion sin parametros")
saludo()    

# con 1 parametro

def nombre(name):
    print(f"Hola {name} esta es una funcion con 1 parametro")
nombre("Julian")


# con 2 parametros

def mostrar_mayores(lista,n):
    for i in lista:
        if i > n:
            print(i)
mostrar_mayores([1, 2, 3, 4, 5], 2)   

# con retorno

def suma(a,b):
    return a + b
print(suma(89,2))

# con valores por defecto

def resta(a=0,b=0,c=0):
    print(a+b+c)
resta(10, 5, 2)
resta(3)  

# anotacion en funcion 
def multiplica_por_3(numero: int):
    return numero*3
print(multiplica_por_3(6)) # 18
  

# Con un número variable de argumentos
def sume(*numeros): 
    total = 0
    for n in numeros:
        total += n
    return total
sume(1, 3, 5, 4) # 13

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)   


#funcion dentro de funcion 
def nombres(nom):
    def apellidos(ape):
        print(f"su nombre es {nom} {ape}" )
    apellidos("salamanca")
nombres("Julian")  


# Funciones del lenguaje (built-in)

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

# Variables locales y global

global_1 = "Python"
print(global_1)

def hello_python():
    local_1 = "Hola"
    print(f"{local_1} {global_1}")
print(global_1)
#print(local_1) da error porque esta definida de forma local en la funcion    
hello_python()

#Ejercicio

def extra(cadena1,cadena2):
    count = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            count += 1
    return count            

print(extra("Fizz", "Buzz"))        