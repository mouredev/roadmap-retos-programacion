#!/usr/bin/python3 

==================== FUNCION SIN ARGUMENTOS Y SIN RETORNO ====================

def hola_mundo():
    print("Hola mundo!!")

hola_mundo() 

==================== FUNCION CON 1 ARGUMENT0 SIN RETORNO ====================

def hola_lenguaje(lenguaje):
    print(f"Hola mundo!! mi lenguaje de programación favorito es {lenguaje}")

hola_lenguaje("Python") 

==================== FUNCION CON 2 ARGUMENTOS SIN RETORNO ====================

def presentacion(nick, lenguaje):
    print(f"Hola mundo!! soy {nick} y mi lenguaje de programación favorito es {lenguaje}")

presentacion("rantamplan", "Python") 

==================== FUNCION CON 2 ARGUMENTOS Y CON RETORNO ====================

def publicacion(año, lenguaje):
    edad = 2024 - año
    print(f"El lenguaje {lenguaje} se publicó en {año}")
    if edad >= 18:
        return print(f"El lenguaje {lenguaje} es adulto, tiene {edad} años")
    else:
        return print(f"El lenguaje {lenguaje} es aún muy reciente, tiene {edad} años")

publicacion(1991, "Python") 

==================== FUNCION DENTRO DE FUNCION ====================

my_list = [1, 2, 3, 4]
n=5

def base(my_list):
    def exponente(n):
        for i in my_list:
            print(i**n)
    exponente(n)
base(my_list)        

==================== FUNCION PROPIA DE PYTHON ====================

my_text = "La primera función contará los caracteres de esta frase y la segunda los pondrá en mayúsculas"

def contar_caracter():
    print(len(my_text))
    print(my_text.upper())

contar_caracter()

==================== VARIABLES GLOBALES Y LOCALES ====================

# Variable global, está fuera de las funciones y puede ser llamada por cualquier
# parte del código
# La variable local está dentro de la función y solo puede usarse dentro de ella

n = 5  # Variable global

def multiplicar(numero):
    b = 3  # Variable local
    return numero * b

print(multiplicar(4))
print(n)
# print(b) Esto nos daría error como variable no definida

==================== EJERCICIO EXTRA ====================

text1 = "multiplo de 3"
text2 = "multiplo de 5"

def num_impress(text1, text2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"Es {text1} y {text2}") 
        elif i % 3 == 0:
            print(f"Es {text1}")
        elif i % 5 == 0:
            print(f"Es {text2}")
        else:
            contador +=1
            print(i)

    print(f"Hay {contador} números que no son {text1} ni {text2}")

num_impress(text1, text2)
