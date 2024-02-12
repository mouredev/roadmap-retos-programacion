#Función sin parámetros y sin retorno
def funcion_sin_parametros():
    print("Función sin parámetros")

funcion_sin_parametros()

#Función con parámetros y sin retorno
def funcion_con_parametros_sin_retorno(param1, param2):
    print(f"El primer parámetro es: {param1}, el segundo parámetro es: {param2}")

funcion_con_parametros_sin_retorno("Hola", 4)

#Función con parámetros y retorno
def funcion_con_parametros_y_retorno(a, b):
    return a - b

print(funcion_con_parametros_y_retorno(5, 3))

#Función con parámetros por defecto y retorno de varios parámetros
def funcion_con_parametro_por_defecto(nombre, apellido, alias = "Anonimo"):
    return nombre, apellido, alias

print(funcion_con_parametro_por_defecto("Mario", "Velasco"))
print(funcion_con_parametro_por_defecto("Mario", "Velasco", "mariovelascodev"))

#Función dentro de función
def funcion_1():
    def funcion_2(arg):
        return arg
    print(f"Hola", funcion_2("mundo"))

funcion_1()

#Funciones creadas en el lenguaje
print(f"len() que nos calcula la longitud del string: Hola mundo tiene una longitud de -> {len('Hola mundo')}")
print(f"pow() nos eleva el primer número a la potencia del segundo: 4**2 = {pow(4,2)}")

#Variable LOCAL y GLOBAL
variable_global = "Contenido de la variable global"

def funcion_variable_local():
    variable_local = "Contenido de la variable local"
    print(variable_local)

print(variable_global)
funcion_variable_local()
variable_local = 5 # el contenido de la variable no cambia dentro de la función ya que tiene ambito local

print(variable_local)
funcion_variable_local()

#EXTRA
def print_number(arg1, arg2):
    parametro_1 = str(arg1)
    parametro_2 = str(arg2)
    contador = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{parametro_1} {parametro_2}")
        elif i % 3 == 0:
            print(parametro_1)
        elif i % 5 == 0:
            print(parametro_2)
        else:
            print(i)
            contador+=1
        
    return f"Número de veces que se ha impreso el número en lugar de textos: {contador} veces"

print(print_number("Hola", "Mundo"))