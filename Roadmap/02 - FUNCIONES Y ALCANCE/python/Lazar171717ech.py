## 1. FUNCIONES BÁSICAS ##

def PrintHola(): # Definimos una función simple con def + [nombre de la función] + () + :
    print("¡Hola!") # Código que se ejecuta

PrintHola() # Llamamos a la función con [nombre de la función] + ()

def PrintTexto(texto): # Definimos una función con argumentos poniendo los mismos dentro de los paréntesis
    print(texto) # Código que se ejecuta. Cuando usamos "texto" hace referencia al argumento que hayamos metido

PrintTexto("¡Adiós!") # Llamamos a la función con argumenos añadiendo estos dentro de los parentesis

def ReturnTexto(texto): # Cuando usamos return en una función, cuando se llame a esta...
    return texto*2 #  ...no solo se ejecutará el codigo sino que haremos también referencia al valor que returnemos.

print(ReturnTexto("Ventana")) # En este caso cuando llamemos a la función ReturnTexto() hacemos referencia al argumento dos veces (el return)

## 2. FUNCIONES DENTRO DE FUNCIONES ##

def Funcion1(): # Definimos la primera función.
    print("Ejecución 1")

    def Funcion2(): # Definimos la segunda función dentro de la primera.
        print("Ejecución 2")

    Funcion2() # Solo se puede llamar a la función2 dentro de la función1

Funcion1() 

## 3. FUNCIONES DENTRO DEL LENGUAJE ##

print("¡Hola Mundo!") # print Escribe en consola el argumento o argumentos que metamos
print(len("¡Hola Mundo!")) # len Mira la cantidad de caracteres o elementos de un string o lista, tupla ...
print(type("¡Hola Mundo!")) # type Devuelve el tipo de dato que damos como argumento
print(bool("¡Hola Mundo!")) # bool, int ... Intenta transformar el dato dado como argumento a otro tipo de dato

## 4. VARIABLES LOCALES Y GLOBALES ##

variable_global = 5

def func(numero):
    variable_local = 7
    return numero * variable_local

print(variable_global)
#print(variable_local) No se puede acceder a la variable local porque está definida dentro de una función

print(func(2)) # Accedemos a esa variable solo si entramos a la función

contador = 0

def masuno():
    contador += 1 # Si la variable aparece descolorida es porque dentro de la función esta no se puede acceder
    print(contador) # El lenguaje crea una variable local igual a la variable global.

#Si queremos usarla sería de la siguiente manera
def masuno2():
    global contador # Al hacer esto le estamos diciendo a Python que estamos tratando con la variable global
    contador += 1
    print(contador) 

masuno2()
masuno2()

## 5. DIFICULTAD EXTRA ##

def funcion(string1, string2):
    counter = 0
    for index in range(1, 101):
        if index%5 == 0 and index%3 == 0:
            print(string1 + string2)
        elif index%3 == 0:
            print(string1)
        elif index%5 == 0:
            print(string2)
        else:
            counter += 1
            print(index)
    return(counter)

print(funcion("Hola", "Brais"))
