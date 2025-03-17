#FUNCIONES Y ALCANCE
''''
las funciones definidas por el usuario en python son objetos que se pueden instasear en 
cualquiera parte del codigoestas pueden recibir unos paraemtros y tambien pueden retornar un parametro 
'''


numero = 10

#funcion simbre
def saludar():
    print("hola!") #esta funcion retorna un saludo


#funcion con argumentos de entrada
def suma(a): 
     x = a+2
     print(x) #esta funcion recibe un numero y le suma 2 y lo imprime


#funcion con return
def resta():
    resultado = 12-1
    return resultado


#funcion con argumneto y return
def calculator(number_one, number_tow):
    calculator_result = number_one * number_tow
    return calculator_result


#funcion con mas de un return
def saludo_adios(saldu="hola",despedida="adios"):
    return saldu,despedida

hello, goodbye = saludo_adios("adios","hola")



# Con un número variable de argumentos es decir que recibe una lista o una tupla como argumento



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

print(hello,goodbye)