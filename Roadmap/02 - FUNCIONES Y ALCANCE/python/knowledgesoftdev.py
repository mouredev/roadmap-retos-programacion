import random

def funcionSinRetornoSinParametros():
    print("Hola mundo")
funcionSinRetornoSinParametros()


def funcionConRetornoConParametros(a,b):
    return a+b
resultadoFuncion=funcionConRetornoConParametros(12,2)
print(resultadoFuncion)


def funcionPrueba():
    def funcionPruebaDos():
        print("Esta la funcion que esta dentro de una funcion")
    funcionPruebaDos()
    print("Esta funcion es padre")

funcionPrueba()

#funcion creada por el lenguaje
#devolver numeros aleatorios entre un rango colocado por parametros
numRandom=random.randint(1,10)
print("Numero escondido es",numRandom)

#varible LOCAL y GLOBAL
VARIABLE_GLOBAL="ES UNA VARIABLE GLOBAL"
def ejemploVariable():
    variable_local="soy una variable local"
    return VARIABLE_GLOBAL

#como con conclusion se sabe que la variable local dentro de una funcion no puede ser accesible
print(ejemploVariable())
#print(variable_local)


'''
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 *   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''
def funcion(param1="textoUNO",param2="textoDOS"):
    cont=0
    for i in range(1,101):
        if(i%3==0):
            print(param1)
        elif(i%5==0):
            print(param2)
        elif(i%3==0 and i%5==0):
           print(param1+param2)
        else:
            cont+=1
    
    return cont
        
print(funcion())