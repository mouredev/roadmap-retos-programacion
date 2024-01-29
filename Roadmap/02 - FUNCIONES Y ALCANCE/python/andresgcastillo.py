# Variable global
variable_global = "Soy una variable global"

def funcion_sin_parametros_ni_retorno():
    print("Función sin parámetros ni retorno")

def funcion_con_parametros(a, b):
    print("Función con parámetros:", a, b)

def funcion_con_retorno(a, b):
    return a + b

def funcion_con_funcion_dentro(a, b):
    def suma(x, y):
        return x + y
    return suma(a, b)

def funcion_con_variable_local():
    variable_local = "Soy una variable local"
    print(variable_local)

def funcion_con_variable_global():
    global variable_global
    variable_global = "He modificado la variable global"
    print(variable_global)

# Llamada a las funciones
funcion_sin_parametros_ni_retorno()
funcion_con_parametros(5, 3)
print("Función con retorno:", funcion_con_retorno(5, 3))
print("Función con función dentro:", funcion_con_funcion_dentro(5, 3))
funcion_con_variable_local()
funcion_con_variable_global()
print(variable_global)

#Dificultad Extra
def funcion(cadena1, cadena2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            contador += 1
    return contador

# Llamada a la función
print("Número de veces que se ha impreso el número:", funcion("Ludwig", "Mozart"))