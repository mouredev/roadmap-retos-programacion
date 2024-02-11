#funciones basicas 
def suma_sin_parametros_retorno(): 
    print("funcion solo imprime en consola sin parametros")

def suma_con_parametros_retorno(num1, num2): 
    print("funcion solo imprime en consola con parametros", num1,"y", num2)

def suma_sin_parametros():
    return 3 + 4

def suma_con_parametros(num1, num2):
    return num1 + num2

#funcion upper creada en el lenguaje
def string_upper(word):
    new_string = str(word).upper() #upper convierte la cadena en mayuscula
    print(new_string)

#funciones dentro de funciones
def my_function1():
    def my_function2():
        print("estudiando con mouredev")    
    my_function2()    
    print("y pyhton")

#variable GLOBAL
my_variable_global = 20
def funcion_variable_global_local():
    my_variable_local = 10 # variable local
    return my_variable_global + my_variable_local

# ejemplo opcional
def devolver_numero_del_string(my_string, my_other_string):
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print(f"las cadenas se concatenan {my_string} {my_other_string}")
        elif index % 3 == 0:
            print(f"la primera cadena es: {my_string}")
        elif index % 5 == 0:
            print(f"la segunda cadena es: {my_other_string}")


suma_sin_parametros_retorno()
suma_con_parametros_retorno(2, 4)
print(suma_sin_parametros())
print(suma_con_parametros(8, 7))
string_upper("alan Ramirez")
my_function1()
print(funcion_variable_global_local())
print(devolver_numero_del_string("alan", "ramirez"))
