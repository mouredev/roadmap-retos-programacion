import random
var1 = "Hola soy una variable"
var2 = "Hola soy otra variable"
var3 = "Somos 3 variables"
var4 = "Somos 4 variables"
lista = ["manzana", "mandarina", "durazno", "sandia"]
#Funciones

#No recibe parametros
def funcion_sin_parametros():
    print("no uso parametros")

funcion_sin_parametros()

#Recibe un parametro
def funcion_con_un_parametro(var1):
    print(var1)

funcion_con_un_parametro(var1)

#recibe 2 o mas parametros, se conoce la cantidad exacta de parametros que recibe
def funcion_con_dos_parametros(var1, var2):
    print(var1)
    print(var2)

funcion_con_dos_parametros(var1, var2)

#se envian varios parametros, no se conoce la cantidad exacta de estos
def funcion_con_muchos_parametros(*nombres):
    for i in range(0, len(nombres)):
        print(f"Hola: {nombres[i]}")

funcion_con_muchos_parametros("Lucas", "Pedro", "Alejandro", "Mauro")

#se envian varios parametros, no se conoce la cantidad exacta de estos, se puede agregar ademas otros argumentos
def funcion_con_muchos_parametros(variable1, variable2, *nombres):
    for i in range(0, len(nombres)):
        print(f"Adios: {nombres[i]}")
    print(variable1)
    print(variable2)

funcion_con_muchos_parametros( var1, var2, "Lucas", "Pedro", "Alejandro", "Mauro")

#Variables creadas en los argumentos de las funciones

def funcion_con_var_propia(apellido1):
    print(f"El apellido es: {apellido1}")

funcion_con_var_propia(apellido1 = "Blanco")

#no se conocen los argumentos, del tipo variable, que se reciviran como parametros
def funcion_con_muchas_variables(**vars):
    print(vars["var9"])

funcion_con_muchas_variables(var7 = "hola", var8 = "Como", var9 = "Estas", var0 = "Adios")

#Parametro por defecto

def arg_por_defecto(pais = "Argentina"):
    print(f"Soy de: {pais}")

arg_por_defecto("España")
arg_por_defecto("Chile")
arg_por_defecto()
arg_por_defecto("Mexico")

#Pasar una lista como parametro

def comer_frutas(frutas):
    for i in range(len(frutas)):
        print(f"Comiste un/a: {frutas[i]}")

comer_frutas(lista)

#funcion que devuelve un resultado

def retorno():
    return 3+4

var4 = retorno()
print(var4)

#Si nesesitas dejar una funcion vacia

def vacia():
    pass

#crear funcion dentro de funcion 

def funcion_afuera():
    def funcion_adentro():
        return "hola"    
    print(funcion_adentro())

funcion_afuera()

#Funciones de Python

print(f"len(var3): {len(var3)}")
print(f"numero random= {random.randint(0,100)}")

#Variables Locales y Globales

var_global = "Soy una variable global"

def variables():
    var_local = "Solo me puedo imprimir en esta funcion"
    print(f"var_global= {var_global},||| var local= {var_local}")

variables()

#Extra

def extra(texto1, texto2):
    contador = 0

    for i in range(1, 101):
        if(i % 3 == 0 and i % 5 == 0):
            print(f"{texto1} {texto2}")
        elif(i % 3 == 0):
            print(texto1)
        elif(i % 5 == 0):
            print(texto2)
        else:
            print(i)
            contador += 1
    
    print(contador)

extra("hola", "chau")
