#FUNCIONES

#Funcion de suma
"""
Las funciones pueden no recibir ningun parametro o pueden recibir varios parametros
Pueden tener un valor de retorno (return) que se devuelve al invocar la funcion
"""
def Sumar(a, b): 
    c = a + b
    return c #Funcion con retorno

print("El resultado de la funcion sumar de 3 + 2 es: " + str(Sumar(3,2)))

#Funcion de resta
def Resta(a,b):
    c = a - b
    #Funcion dentro de funcion
    print("Primera funcion Resta")
    def SegundaResta():
       print ("Segunda funcion Resta")
       #Funcion sin retorno
    #LLamada a funcion dentro de una funcion
    SegundaResta()
    return c

print("El resultado de la funcion resta de 3 - 2 es: " + str(Resta(3,2)))

def Resultados():
    #Llamadas a funciones fuera de funciones
    print("El resultado de la funcion sumar de 3 + 2 es: " + str(Sumar(3,2)))
    print("El resultado de la funcion resta de 3 - 2 es: " + str(Resta(3,2)))

print("Los resultados de las funciones: " )
Resultados()

#Funciones predefinidas de phyton

print(divmod(10,2)) # El primer numero nos indica el resultado de la division, el segundo el resto
print(chr(363)) # Traduce el numero al codigo Unicode

# Variables

def AccesoVariables():
    a = 0 # Variable Local (Solo existe dentro de la funcion)
    return a

a = 1 # Variable Global (Accesible en todo el programa)

print("Accedemos a la variable local a con valor : "+ str(AccesoVariables()))
print("Comprobamos la variable global a : "+str(a))

"""
 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def X (a, b) :
    contador = 0
    for i in range (1,100) :
        if i%5==0 and i%3==0 :
            print(a+" y tambien "+b)
        elif i%3==0 : 
            print(a)
        elif i%5==0 :
            print (b)
        else :
            print(i)
            contador += 1
    return contador

print("Se ha impreso un numero: " + str(X("Soy multiplo de 3","Soy multiplo de 5"))+" veces")
