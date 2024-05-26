# funciones simoples


def saludo():
    print ("hola python")


saludo()

# funcion con retorno

def return_saludo():
    return "hola, python"



print (return_saludo())


# funcion con argumento, argumentos, argumentos predeterminado

def return_argumento( nombre):
    print (f"hola, {nombre}")


return_argumento("simon")


def return_argumento(saludo, nombre):
    print (f"{saludo}, {nombre}")


return_argumento("hi", "simon")

def default_return_argumento(nombre="python"):
    print (f"hola,{nombre}!")


default_return_argumento("simon")
default_return_argumento()

# funcion con retorno de varios valores

def multiple_return_arguments():
    return "hola", "python"

saludo, nombre = multiple_return_arguments()
print(saludo)
print(nombre)

# funciones con numero variable de argumento

def variable_arg_saludo(*nombres):
    for nombre in nombres:
        print(f"hola, {nombre}")

variable_arg_saludo("python","simon","storbett")


# funcion con numero variable de argumento con palabra clave

def variable_key_arg_saludo(**nombres):
    for key, valor in nombres.items():
        print(f"hola, {valor} ({key})")

variable_key_arg_saludo(
    lenguaje= "python",
    nombre = "simon",
    alias = "storbett",
    edad = 33
)



