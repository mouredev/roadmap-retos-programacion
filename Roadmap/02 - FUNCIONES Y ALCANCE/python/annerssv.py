# FUNCIONES

####FUNCION QUE NO ESPERA PARAMETROS####
def mi_primera_funcion():
    print("Hola! esta es mi primera funcion")

mi_primera_funcion()

#####FUNCION CON RETORNO####

def funcion_retorno():
    return "Hola!, esta es una función de retorno"

print(funcion_retorno())

#####FUNCION CON 1 PARAMETRO#####

def funcion_un_arg(name):
    print(f'Hola {name}!')

funcion_un_arg("Jhan")

#####FUNCION CON MAS DE UN PARAMETRO#####

def fun_mas_arg(saludo, name):
    print(f"{saludo}, {name}!")

fun_mas_arg("Hola", "Jhan")

#####FUNCION CON VALOR POR DEFECTO####

def valor_por_defecto(name="Mundo"):
    print(f"Hola {name}")

valor_por_defecto("Pier")
valor_por_defecto()

#####FUNCION CON MULTIPLES ARGUMENTOS *args ####

def suma_args(*args): #Los parametros recibidos seran converidos en una tupla 
    total = 0
    for n in args: 
        total += n
    return print(total)

suma_args(1,2,3)


####FUNCION CON MULTIPLES ARGUMENTOS KEY/VALUE####

def resta_kwargs(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        print (f"{key} = {value}")
        suma += value
    return print(suma)

resta_kwargs(a=20, b=10, c= 5)


#####FUNCIONES DENTRO DE FUNCIONES####

def calculadora():

    def suma(n1=0, n2=0):
        return n1 + n2
    print(suma(2,3))

    def resta(n1=0, n2=0):
        return n1 - n2
    print(resta(4,5))

    def multiplicacion(n1=0, n2=0):
        return n1 * n2
    print(multiplicacion(5,6))

    def division(n1=0, n2=0):
        return n1 / n2
    print(division(7,8))

calculadora()


###FUNCIONES DEL LENGUAJE###

#-----Funciones de cadenas

#--IMPRESION
print("Este texto fue impreso con la funcion print()")

#--CADENAS
minuscula = "ESTE TEXTO FUE CONVERTIDO EN MINUSCULAS CON LA FUNCION lower()"
print(minuscula.lower())
mayuscula = "este texto fue convertido a mayusculas con la funcion upper()"
print(mayuscula.upper())

#----FUNCION PARA TIPO DE DATOS

mi_arreglo = [1,2,3,4,5]
print(type(mi_arreglo))

####CONCEPTO DE VARIABLE LOCAL Y GLOBAL####

#VARIABLE GLOBAL
mi_variable_local = "Hola soy una variable local"

def funcion_local():
    print(mi_variable_local)

funcion_local()

#VARIABLE LOCAL

def funcion_local1():
    variable = "Hola soy una variable local"
    return print(variable)
funcion_local1()

print("En esta linea no puedo acceder la variable de la funcion1")



#EJERCICIO EXTRA

def extra(texto1, texto2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            contador +=1

    return contador

print(extra("Fizz", "Buzz"))


