#funcion sin parametro ni retorno



def hola_mundo():
    print("!Hola Mundo¡")

hola_mundo()


#con parametros y con retorno

def suma_numeros(num1,num2):
    return num1 + num2

print(suma_numeros(5,6))


#funcion dentro de una funcion

def funcion_de_afuera():
    def funcion_de_adentro():
        print("!Hola a todos desde la función de adentro¡")
    funcion_de_adentro()
    print("!Hola a todos desde la función de afuera¡")

funcion_de_afuera()


#Funciones lambda
funcion_lambda = lambda x,y: x * y

print(funcion_lambda(5,3))


#funciones del lenguaje

lista_numeros = [1,2,3,4,5]
#round
print(round(lista_numeros[2]/lista_numeros[4]))
#sum
print(sum(lista_numeros))
#pow
print(pow(lista_numeros[4],lista_numeros[1]))
#len
print(len(lista_numeros))
#list y map
print(list(map(lambda x:x +1,lista_numeros)))
#type
print(type(lista_numeros))


#variable global y variable local

variable_global = "!Hola¡"
def funcion_random():
    variable_local = "!Adios¡"
    print(f"{variable_global}, {variable_local}")
funcion_random()



"""
Dificultad extra
"""


def imprimir_numeros(texto1, texto2):
    contador = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"El número es {texto1}, el número es {texto2}")
        elif numero % 3 == 0:
            print(f"El número es {texto1}")
        elif numero% 5 == 0:
            print(f"El número es {texto2}")
        else:
            print(numero)
            contador +=1
    print(f"El número se imprimió {contador} veces")


imprimir_numeros("múltliplo del 3", "múltiplo del 5")
