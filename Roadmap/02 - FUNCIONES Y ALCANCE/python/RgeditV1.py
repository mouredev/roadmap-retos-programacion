from math import sqrt as raiz

def sumar(): #Funcion sin parametros
    num1 = 5
    num2 = 6
    return num1 + num2 
#--------------------------------------------------
def restar(num1,num2): #funcion con parametros
    resultado = num1 - num2
    return resultado
#---------------------------------------------------
def dividir(num1=5,num2=2): #funcion con argumentos y sin return
    print(num1/num2)

"""Funcion sin parametros../ejecutara la funcion por si sola sin necesidad de que el usuario le pase algun dato
    amenos que en la propia funcion se encuentren algoritmos que lo pida
"""
print(sumar()) #llamada a la funcion sumar y la muestra en pantalla


#-------------------------------------------------------------------------------------

#Funcion con parametros../los digitos que ingresemos se pasara como argumento de los parametros en la funcion
num = int(input("Introduce digito: "))
num2 = int(input("Introduce digito 2: "))
resultado = restar(num,num2)
print(resultado)#llamada a la funcion restar, pero los parametros reciben su argumento de las var num y num2

#---------------------------------------------------------------------------------------------
#Funciones sin retorno

dividir()#Llamara a la funcion dividir que no tiene return pero si un print

#----------------------------------------------------------------------------------------------
#Funciones Decoradoras / son funciones que se utilizan para añadir nuevas funcionalidades a otra funcion
#-----------------------------------------------------------------------------------------------

def corrector(func): #esta funcion tomara como parametro la funcion Div que esta mas abajo
    def corregir(*args): #en esta funcion se corregira y añadira algunas cosas
        if func(*args) != 'NO SE DIVIDE ENTRE CERO': # si el retorno de la funcion div es diferente a "NO SE DIVIDE ENTRE CERO"
            print('Este esta es la division') #Entonces imprimira esto
        return func(*args)# y retornara el valor de la funcion div
    return corregir
        

@corrector #Decorador/esta funcion es la que se le pasara como parametro a la funcion corrector
def div(a, b):
    if b == 0: #si la division es entre cero entonces retornara...
        return 'NO SE DIVIDE ENTRE CERO'
    else:
        return a/b #Encambio si es una division comun retornara el valor

print(div(5,2))


#-----------------------------------------------------------------------------------------------
#Ejemplo de funciones nativa del lenguaje

"""la funcion sqrt renombrada a raiz, devuelve la raiz cuadrada de un numero 
    y lo guardara en la variable raiz_cuadrada
"""
raiz_cuadrada = raiz(5)

print(round(raiz_cuadrada,2)) #con la funcion round limitas el numero de decimales que quieres

#----------------------------------------------------------------------------------------------
"""Variables locales son las variables que solo se pueden usar dentro de una funcion, clase etc...
    Mientra que con una variable global puedes llamarla(por asi decirlo) desde cualquier parte del codigo
"""

#var_global
nombre = "Angel" #Esta variable puedo invocarla desde cualquier parte del codigo


def var_local():
    #var_local
    hola = "Hola, " #Esta variable no la podre invocar fuera de la funcion
    print(hola,nombre)

print(nombre) #estoy invocando la variable global desde la funcion y fuera de la funcion

#---------------------------------------------------------------------------------------------
#continuare en otro momento la dificultad opcional
#--------------------------------------------------------------------------------------------