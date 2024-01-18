import os
os.system('clear') #MAC/LINUX
#os.system('cls') #WINDOWS

"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
"""

#FUNCIÓN SIN RETORNO NI PARÁMETROS
def imprime_hasta_10():
    for i in range (1,11):
        print(i, end=' ')

imprime_hasta_10()

#FUNCIÓN CON RETORNO
def introducir_datos()->str:
    mi_texto = input("Escriba su texto: ")
    return mi_texto

#FUNCIÓN SIN RETORNO CON UN PARÁMETRO RECIBIDO DE LA FUNCIÓN ANTERIOR 
def imprimir_datos(mi_texto):
    print(mi_texto)

imprimir_datos(introducir_datos())


#FUNCIÓN QUE RECIBE VARIOS PARÁMETROS
def calcular_media_valores (valor1, valor2, valor3,valor4,valor5):
    media = (valor1+valor2+valor3+valor4+valor5)/5
    print(media)

calcular_media_valores(1,3,5,7,9)

mi_lista = [1,3,5,7,9] #variable global
mi_otra_lista = [0,1,2,3,4,5,6,7,8,9] #variable global

#FUNCIÓN QUE RECIBE UNA LISTA COMO PARÁMETRO
def calcular_media_lista (mi_lista):
    print(sum(mi_lista)/len(mi_lista))

calcular_media_lista(mi_lista)


#FUNCIÓN LAMBDA (SÓLO PARA CÁLCULOS)
calcular_media_lambda = lambda valor1,valor2,valor3,valor4,valor5:(valor1+valor2+valor3+valor4+valor5)/5

print(calcular_media_lambda(1,3,5,7,9))



#FUNCIÓN LAMBDA CON FUNCIÓN DE LENGUAJE filter Y LLAMADA A OTRA FUNCIÓN ANTERIOR
impares = filter(lambda filtrado: filtrado % 2 != 0, mi_otra_lista)
calcular_media_lista(list(impares))

#FUNCIÓN QUE RECIBE LA VARIABLE GLOBAL mi_lista E IMPRIME SUS VALORES CON BUCLE FOR
def imprimir_numeros_lista_for(mi_lista):
    for i in (mi_lista):
     print (i)
imprimir_numeros_lista_for(mi_lista)

#FUNCIÓN QUE IMPRIME LOS VALORES DE LA VARIABLE LOCAL mi_lista_local SIN USAR BUCLE
def imprimir_numeros_lista_sin_bucle():
    mi_lista_local = [1,3,5,7,9] #variable local
    print (* mi_lista_local)
imprimir_numeros_lista_sin_bucle()


#FUNCIÓN QUE RECIBE VARIABLE GLOBAL E IMPRIME VALORES SIN BUCLE CON SEPARADOR DEFINIDO
def imprimir_numeros_con_separador(mi_lista):
    print (* mi_lista , sep = "-")
imprimir_numeros_con_separador(mi_lista)

#FUNCIÓN CON VARIABLE LOCAL QUE IMPRIME VALORES CON FUNCIÓN DE LENGUAJE join
def imprimir_numeros_con_funcion_join():
    mi_lista_str = ["1","3","5","7","9"]#la lista se debe definir con strings para usar join
    print('_'.join(mi_lista_str))
imprimir_numeros_con_funcion_join()


#FUNCIÓN IGUAL A LA ANTERIOR PERO RECIBE LISTA DE NÚMEROS Y LA CONVIERTE EN STRING
def imprimir_numeros_con_funcion_join_map(mi_lista):
    print('>'.join(map(str, mi_lista))) # con el método propio map se castea la lista de numérica a string
imprimir_numeros_con_funcion_join_map(mi_lista)


#FUNCIÓN DENTRO DE OTRA FUNCIÓN
def elimina_pares():
        def imprime_impares(mi_otra_lista):
            print(mi_otra_lista)# 4- La función interna imprime la lista de impares

        print(mi_otra_lista[0:len(mi_otra_lista)])# 1- Se imprime la lista completa
        for i in mi_otra_lista:
          if i % 2 == 0:
            mi_otra_lista.remove(i)# 2- Se quitan los números pares

        imprime_impares(mi_otra_lista)# 3- Llamamos la la función que imprime y le pasamos la lista de impares

elimina_pares()


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda."""

cadena1 = "Hola"
cadena2 = "Python"

def hola_python(cadena1,cadena2)->int:
    acumulado=0
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1, cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print (cadena2)
        else:
            print(i)
            acumulado +=1
    print(f"hay {acumulado} números que no son múltiplos de 3 ni de 5")

hola_python(cadena1,cadena2)