

#  su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  *      *******(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)*******
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

     # variable x pasa por valor 5 y no por valor numero(10). 
def punto(x):
    x = 10
    print(x)  #imprime 10
x = 5
punto(x)
print(x)  # imprime: 5




   #variable por referencia 

def modific(lista):
    lista.append(4)  #la funcion es agregar el 4 a una lista no conocida
    lista=[5, 6, 7, 8] 
    print(lista)   #no se agregó el "4"  [5, 6, 7, 8]
mi_lista = [5, 6, 7, 8]
modific(mi_lista)  #aqui se agrega el 4 a mi_lista,la funcion viene de la definicion 
print(mi_lista) # se gregó 4 [5, 6, 7, 8, 4]
lista=mi_lista
print(lista)  # se imprime lista modificada

    ####esituacion donde se aplican variables por valor y por referencia


def negocio(compra="Casa"):
    print(f"buscando,{compra} sin dinero")
    negocio=10
    print(negocio)   #Imprime 10
negocio()    # imprime "buscando,Casa sin dinero"
negocio("Carro")  # imprime "buscando,Carro sin dinero"
negocio("nada de nada")  #imprime "buscando,nada de nada sin dinero"

