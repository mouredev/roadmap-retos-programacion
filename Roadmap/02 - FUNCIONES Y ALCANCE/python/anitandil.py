#FUNCIONES BASICAS
#sin parametros sin retorno
def hola_mundo():
    print("Hola Mundo")

#con parametros sin retorno
def sum(numero1, numero2):
    print(numero1 + numero2)

#sin parametros y con retorno
def pedir_nombre():
    return(input("Ingrese su nombre: "))

#con parametros y retorno
def triplicar(numero):
    return(numero*3)

#funciones dentro de funciones
    """
    en Python es posible declarar una función dentro de otra función. Sin embargo, la vida de esa función 
    pertenece al ámbito de la función donde es definida. Va a ser creada de nuevo cada vez que se llame 
    a la función donde es creada y dejará de existir cuando esta retorne  
    Esto implica que no podrá ser llamada desde fuera de la función donde es definida en principio.
    Por eso, son pocos los casos en los que esto es útil, principalmente en clausuras y factory-functions 
    """
def sumar_mas(numero1,numero2):
    def sumar_diez(valor):
        return(valor +10) 
    
    total = numero1 + numero2
    if  total < 10:
        total=sumar_diez(total)
    
    return total 

#FUNCIONES LAMBDA
potenciacion_lambda = lambda base, exponente: base ** exponente

#funciones ya creadas en Python
#pueden ser llamadas si importamos el modulo donde fueron creadas, por ejemplo funciones matematicas
import math

print(math.sqrt(16))

#variables locales y variables globales
def circunsferencia():
    PI = 3.1416 #variable local
    return PI*(radio**2)

hola_mundo()
sum(2,5)
print(pedir_nombre())
print(triplicar(3))
print(sumar_mas(1,2))
print(potenciacion_lambda(3, 4))
radio = 5 #variable global
print(circunsferencia())


"""
     DIFICULTAD EXTRA (opcional):
     Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
       - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
       - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
       - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
       - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
def imprimir_numeros(cadena1:str, cadena2:str)->int:
    contador = 0
    for num in range(1,101):
        if num%3==0 and num%5==0:
            print(str(num)+cadena1+cadena2)
        elif num%3==0:
            print(str(num)+cadena1)
        elif num%5==0:
            print(str(num)+cadena2)
        else:
            print(num)
            contador+=1
    return contador

cantidad = imprimir_numeros("divisor de 3","divisor de 5")
print(f"La cantidad de numero entre 1 y 100 que no son multiplos ni de 3 ni de 5 son:  {cantidad}") 
