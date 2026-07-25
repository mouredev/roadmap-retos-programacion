#funciones basicas

#simples
def saludar():
    print("Hola Python")

saludar()

#retorno
def funcion_de_retorno():
    return "retorno de funcion"

print(funcion_de_retorno())

#con argumento
 
def saludo_de_cumpleaños(años, nombre):
    print(f"felicidades por tus {años} años {nombre}")

saludo_de_cumpleaños(33, "mateo")


#con un argumento predeterminado
def saludo_de_cumpleaños_predeterminado(años, nombre="crack!"):
    print(f"felicidades por tus {años} años {nombre}")

saludo_de_cumpleaños_predeterminado(33)


#con retorno de varios valores

def retorno_multiple():
    return "Hola","Maxi"

saludo, nombre = retorno_multiple()
print(saludo)
print(nombre)

#funciones con numero variable de argumentos

def argumentos_multiples_variables(*names):
    for name in names:
        print(f"Hola, {name}!")
    

argumentos_multiples_variables("Nicolás", "Maxi", "Pepe", "Lorena", "Melani")


#con numero variable de argumentos con palabra clave

def argumentos_multiples_variables(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")
    

argumentos_multiples_variables(
    name = "Nicolás",
    edad = 32,
    idioma = "español",
    nacionalidad = "uruguayo",
    )





#FUNCIONES DENTRO DE FUNCIONES

def funcion_contenedora():
    def funcion_contenida():
        print("soy una funcion interna")
    funcion_contenida()

funcion_contenedora()


#FUNCIONES YA CREADAS EN PYTHON

print(len("Nicolás Heguaburu"))
print(type(32))
print("nico".upper())


# Variables locales y globales

global_var = "python"

print(global_var)

def hola_python():
    local_var = "hola" #solo la puedo llamar en la funcion hola_python()
    print(f"Hola {global_var}")

hola_python()



#EJERCICIO EXTRA

def mi_funcion (str1, str2):
    num = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{str1} y {str2}")
        elif i % 3 == 0:
            print(str1)
        elif i % 5 == 0:
            print(str2)
        else:
            print(i)
            num += 1
    return num
        


print(mi_funcion("soy multiplo de 3", "soy multiplo de 5"))

