"""
#funcion sin parametros ()
def saludar ():
    print("Hola Mundo")
saludar() #Aca se llama a la funcion, sin esta linea esta funcion no se ejecutaria

#funcion con retorno
def hola():
    return "Ay miguel"
retorno= hola()
print(retorno)

#Funcion con dos parametros y con retorno
def multiplicacion(a,b):
    return a*b
resultado = multiplicacion(5,6)
print(f"El resultado de la multiplicacion es: {resultado}")
 
 #Ejemplo funcion con libreria math con parametros y retorno
import math

def circulo(radio):
    return math.pi * (radio**2)
radio = float(input("Ingrese el radio del circulo para calcular el area: "))
print(f"El radio del circulo es: {circulo(radio)}")

#Ejemplo funcion con parametro y retorno
def temperatura(grados):
    return (grados * (9/5)) +32
grados = int(input("Ingrese los grados centigrados para obtener su valor en Fahrenhait: "))
print(f"!La cantidad de",grados,"centigrados, equivale a ",temperatura(grados) ,"fahrenheit!") 


#Ejmplo funcion con parametro y retorno
def par(numero):
    if numero % 2 ==0:
        return "Es par"
    else:
        return "No es par"

numero = int(input("Ingrese el numero para determinar si es o no es par: "))
print("El numero",numero,par(numero))

#Ejemplo de funciones anidadas
def kilometros(centimetros):
    def metros(centimetros):
        return centimetros /100
    metros = metros(centimetros)
    totalkm = metros/1000
    return totalkm
    
centimetros = float(input("Ingrese la cantidad de centimetros a convertir a metros y luego kilometros: "))
print("El valor de",centimetros,"equivale a",kilometros(centimetros),"kilometros")

#Ejmplo de funciones anidadas
def operacion(a,b):
    def suma():
        return a+b
    def multiplicacion():
        return a*b
    def division():
        return a/b
    sumar = suma()
    multi = multiplicacion()
    divi = division()
    return sumar,multi,divi
a = float(input("Ingrese el valor de a: "))    
b = float(input("Ingrese el valor de b: "))
sumar,multi,divi = operacion(a,b)
print("La suma de",a,"y",b,"es",sumar)    
print("La multiplicacion de",a,"por",b,"es",multi)    
print("La division de",a,"entre",b,"es",divi)    
"""
#Ejercicio Extra
def ejercicio(texto1,texto2)-> int:
    count = 0
    for i in range (1,101):
        if i % 3==0 and i % 5==0:
            print(texto1+texto2)
        elif i % 5 ==0:
            print(texto2)
        elif i % 3 == 0:
            print(texto1) 
        else:
            print(i)
            count +=1
            conteo = count
    return conteo
texto1="Ay"
texto2="Miguel"
print("La cantidad de veces que se han impreso numeros es: ",ejercicio(texto1,texto2),)
