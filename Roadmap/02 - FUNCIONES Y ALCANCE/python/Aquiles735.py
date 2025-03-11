

#  EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.



# ejemplo de funciones 
def saludar(nombre):
    print(f"¡Hola, bienvenido {nombre}!")    #¡Hola, bienvenido juancho!
saludar("juancho")


#ejemplo de funcion con variable local (interna)
def calcfoza ():
    calcfoza=calcfoza  
c=100
b=20  
print(c*b)  #2000



 #variable glogal (externa)
num_a=10    
def opera():
    opera=opera
print(num_a*num_a)   #100
print(num_a/2*num_a) #50.0



                        


  
# funcion dentro de otra funcion 
def carros(m):
    carros=carros
    def cac(n):
        cac=cac
m=20
n=50
print(m*n)  #1000
print(m*m/(m+n)*n)    #285.7142857142857


    #imprime numeros del uno al 100

     
for x in range(1, 101):
            print("Imprime numeros:", x)

            if x== x in range(1, 99, 3):   #falta calibrar un poco mas
                print("Igual a 3")
           
            # else:
            #     print(x)
          
