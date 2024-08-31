# funcion sin parametro ni retorno
def hola():
    print("Hola ¿Como estas?")

hola()


# funcion con parametro sin retorno
def saludo(nombre):
    print(f"Hola {nombre}, mucho gusto")
    
saludo("Hyromy")


# funcion sin parametro con retorno
def ping():
    return "Pong"

funcion_ping = ping()
print(funcion_ping)


# funcion con parametro y retorno
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
funcion_es_par = es_par(9)
print(funcion_es_par)


# funcion con varios parametros
def funcion(texto, repetir, mayuscula):
    if mayuscula:
        texto = str.upper(texto)
        
    for i in range(0, repetir):
        print(texto)
        
funcion("hola", 4, True)


# funcion con n cantidad de parametros
def suma(*n):
    print(f"Parametros ingresados: {len(n)}")
    print(f"Resultado de la suma {sum(n)}")
    
suma(1, 2, 3, 4)
suma(10, 20, 30, 40 , 50 , 60 , 70, 80 , 90, 100)


# funcion que retorna mas de un valor
def min_max(*numeros):
    return min(numeros), max(numeros)
# desempaquetado
minimo, maximo = min_max(23, 54, 23, 987, 3, 321)
print(f"Minimo: {minimo}, Maximo: {maximo}")


# funciones dentro de funciones
def funcion_A():
    print("Esta es la funcion A")
    
def funcion_B():
    funcion_A()
    
    print("Esta es la funcion B")
    
funcion_B()


# funciones del lenguaje
print() # imprime texto en consola
variable = input("Este es un input, escribe algo para guardarlo en una variable => ")
print(type(variable)) # devuelve que tipo de dato es la variable
print(len([0, 1, 2, 3, 4])) # devuelve la cantidad de elementos que posee
print(range(5)) # genera una secuencia ascendente de numeros naturales (incluyendo el 0)
print(str(42)) # convierte a texto
print(int("12")) # convierte a entero
print(float("54.32")) # convierte a decimal
print(sorted([1,3,5,8,2,9,0,4,7,6])) # ordena los elementos de una lista


# variables globales y locales
variable_global = 3.14159

def prueba():
    variable_local = "Cat"
    
    print(f"Global: {variable_global}")
    print(f"Local: {variable_local}")
prueba()    

print(f"Global: {variable_global}")
# variable no definida
#print(f"Local. {variable_local}")


# ---- DIFICULTAD EXTRA ----

def extra(texto_1, texto_2):
    x = 0
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            x += 1
            print(texto_1 + texto_2)
        elif i % 3 == 0:
            x += 1
            print(texto_1)
        elif i % 5 == 0:
            x += 1
            print(texto_2)
    else:
        return x

numero = extra("algo", "seguro fue joel")
print(numero)