#FUNCIONES Y ALCANCE
''''
las funciones definidas por el usuario en python son objetos que se pueden instasear en 
cualquiera parte del codigoestas pueden recibir unos paraemtros y tambien pueden retornar un parametro 
'''


numero = 10

#01-funcion simple
def saludar():
    print("hola!") #esta funcion retorna un saludo


#02-funcion con argumentos de entrada sin retorno
def suma(a): 
     x = a+2
     print(x) #esta funcion recibe un numero y le suma 2 y lo imprime


#03- funcion con mas de un parametro

def sumar(a,b):
    print(a+b)


#04-funcion con returno
def obtener_pi():
    return 3.1416


#05-funcion con parametro y returno
def cuadrado(a):
    result = a ** 2
    return result



#06-funcion con varios parametros y returno
def calculator(number_one, number_tow):
    calculator_result = number_one * number_tow
    return calculator_result


#07-funcion con parapemtros predefinidos
def suma_iva(precio,iva=0.19):
    result = precio *(1+iva)
    return result

#08-funcion con parametros infedinidos
def sumar_todos(*numeros):
    return sum(numeros)


#09-funcion con mas de un return
def saludo_adios(saldu="hola",despedida="adios"):
    return saldu,despedida

hello, goodbye = saludo_adios("adios","hola")



#funciones dentro de funciones

def nombre(nombre):
    def saludar():
        return "hola" + nombre
    return saludar()


#ejemplo de funciones ya creadas en el lenguaje

print(len("hola como estas"))   #aca hay dos funciones, print y len 

#una variable global es aquella que se declara fuera de una funcion y se tiene
#acceso en todo el codigo pero las variables declaradas dentro de una funcion
#solo se tiene acceso dentro de esa funcion

contador = 1

def contador():
    contador += 1
    return contador


#solucion de reto con funcion de argumentos predeterminados
def reto(string_one="es multiplo de 3",string_tow="es multiplo de 5"):

    contador = 0
    for i in range(100):
        if i % 3 == 0  and   i % 5 ==0:
            print(string_one, " y ",string_tow )
        elif i % 3 == 0:
            print(string_one)
        elif i % 5 == 0:
            print(string_tow)
        else:
            print(i)
            contador +=1
    return contador

saludar()

suma(10)

sumar(10,10)

obtener_pi()

cuadrado(2)

calculator(2,5)

suma_iva(10000)

sumar_todos(1,2,6,4,5,7)

saludo_adios()

nombre("daniel")

print(contador)
reto()