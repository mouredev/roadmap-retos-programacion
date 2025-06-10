#02 - FUNCIONES Y ALCANCE
#EJERCICIO:
#- Crea ejemplos de funciones basicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parametros ni retorno, con uno o varios parametros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algun ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer mas o menos posibilidades)

''' Definidas por el usuario'''

#Sin retorno
def funcion():
    print("Hola")

funcion()

#Con retorno
def funcion_ret():
    return "Hola"

print(funcion_ret())

#Con un argumento
def funcion_arg(arg1):
    print(f"arg1: {arg1}")

funcion_arg("argumento1")

#Con varios argumentos
def funcion_arg_multiple(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")

funcion_arg_multiple("argumento1",2)
funcion_arg_multiple(arg1=2, arg2="argumento2")

#Con argumento predeterminado
def funcion_arg_default(arg1="argumento1"):
    print(f"arg1: {arg1}")

funcion_arg_default("arg1")
funcion_arg_default()

#Con argumentos y return 
def funcion_arg_return(arg1, arg2):
    return f"arg1: {arg1} arg2: {arg2}"

print(funcion_arg_return("arg1",2))

#Con return multiple
def funcion_mult_return():
    return "arg1",2

arg1, arg2 = funcion_mult_return()
print(f"arg1: {arg1}")
print(f"arg2: {arg2}")

#Con numero variable de argumentos
def funcion_arg_variable(*args):
    for arg in args:
        print(f"arg: {arg}")
    
funcion_arg_variable("arg1",2,"arg3",'4')

#Con numero variable de argumentos con palabra clave
def funcion_arg_variable_key(**args):
    for key,value in args.items():
        print(f"{key}, {value}")

funcion_arg_variable_key(
    arg1="argumento1",
    arg2=2, 
    arg3='3'
)

'''
Funciones dentro de funciones.
'''
def funcion_ext():
    def funcion_int():
        print("Funcion interna dentro de funcion externa")
    funcion_int()

funcion_ext()

'''
Funciones del lenguaje
'''
print(len("string"))
print(type("string"))
print(type(3))
print("string".upper())

'''
variables locales y globales
'''

global_var = "Global"

def funcion_local_global():
    local_var = "Local"
    print(f"Global= {global_var} Local={local_var}")

funcion_local_global()

"""
Extra
"""
def funcion(parametro1, parametro2) -> int:
    count = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0: 
            print (parametro1 + parametro2)
        elif i % 3 == 0:
            print (parametro1)
        elif i % 5 == 0:
            print (parametro2)
        else:
            print(i)
            count += 1
    
    return count

print (funcion("parametro1","parametro2"))