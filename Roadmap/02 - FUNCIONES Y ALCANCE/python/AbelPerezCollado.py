# Func sin parametros ni retorno
def sin_param_retorno():
    print('Funcion no devuelve nada ni tiene parametros')

# Func con varios parametros con retorno
def suma(num1:int , num2:int):
    return num1 + num2

# Funciones dentro de funciones
def fun_dentro(param1:int,param2:int):
    def suma(n1,n2):
        return n1 + n2
    return suma(param1,param2)

# Funcion con parametros por defecto
def fun_param_defecto(nombre = 'Abel', apellido = 'Perez'):
    return f'Bienvenido, {nombre} {apellido}' 

# Ejemplo de funciones ya creadas en el lenguaje
nombre ='Abel'
print(f'El numero de letras de {nombre} es de {len(nombre)}')


# Funcion Lambda
square = lambda num : num * num
print(square(3))

# Funcion recursiva

# función recursiva
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial(41))

# Concepto de variable Local y Global
var_global = 100

def devuelve_numero(num : int):
    var_local = num
    return var_local

 
# Dificultad extra

def funcion_dificultad_extra(cad1 : str, cad2:str):
    cont = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(f'{cad1}{cad2}')
        elif num % 3 == 0:
            print(cad1)
        elif num % 5 == 0:
            print(cad2)
        else:
            cont += 1
    return cont