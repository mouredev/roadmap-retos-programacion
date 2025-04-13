#Funciones

def sin_parametro_ni_retorno():
    print("Funcion sin Parametros ni Retorno")

sin_parametro_ni_retorno()

def con_parametros(nombre):
    print(f"Mi nombre es {nombre}")

mi_nombre = "Fabian"

con_parametros(mi_nombre)

def con_retorno(nombre, apellido):
    return f"Mi nombre completo es {nombre} {apellido}"

mi_apellido = "Petit"

print(con_retorno(mi_nombre, mi_apellido))


#Funcion dentro de una funcion

def funcion_externa():
    print("Esta es la funcion externa")

    def funcion_interna():
        print("Esta es la funcion Interna")

    funcion_interna()


funcion_externa()

# Funciones lambda (anonimas)

cuadrado = lambda x: x**2

print(cuadrado(4))

# Variables locales y globales

variable_global = "Esta es una variable Global"

def var_locales_globales():
    local = "Esta es una variable local"
    print(local)

var_locales_globales()

print(variable_global)
# print(variable_local) No existe fuera de la funcion



# Ejercicio:

def mi_funcion(string1, string2):

    contador = 0

    for number in range(101):


        if(number % 3 == 0 and number % 5 == 0):
            print(string1 + " " + string2)

        elif(number % 3 == 0):
            print(string1)
        
        elif(number % 5 == 0):
            print(string2)

        else:
            print(number)
            contador += 1

    return contador


str1 = "Primer Texto"
str2 = "Segundo Texto"
        
contador = mi_funcion(str1, str2)


print(f"El numero se ha impreso {contador} veces")

