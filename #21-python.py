frase ='''
Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu elección) que muestre su funcionamiento.

Crea una función procesar_numeros(numeros, callback).
Dentro, quédate solo con los números pares.
Cuando termine, llama a callback y pásale la lista resultante.
Define otra función, por ejemplo mostrar_resultado(pares), que imprima los números.
Llama a procesar_numeros([1, 2, 3, 4, 5, 6], mostrar_resultado).
Resultado esperado: Números pares: [2, 4, 6]

La idea clave es que procesar_numeros no decide qué hacer con el resultado: recibe una función y la ejecuta al finalizar.
'''
print(frase)
 
def procesar_numeros(numeros, retorno):
    pares = [numero for numero in numeros if numero % 2 == 0]
    impares = [numero for numero in numeros if numero % 2 != 0]
    retorno(pares)
    retorno(impares)  #También vamos a mostrar los impares

def mostrar_resultado(lista):
    print(f"Números: {lista}")

procesar_numeros([1, 2, 3, 4, 5, 6], mostrar_resultado)




'''
* DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
* Estará formado por una función que procesa pedidos.
* Debe aceptar el nombre del plato, una callback de confirmación, una
* de listo y otra de entrega.
* - Debe imprimir un confirmación cuando empiece el procesamiento.
* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
*   procesos.
* - Debe invocar a cada callback siguiendo un orden de procesado.
* - Debe notificar que el plato está listo o ha sido entregado.
'''
import random
import time
import threading



def simulador_pedidos(plato:str, retorno1, retorno2, retorno3):
    def procesar():
        retorno1(plato)
        time.sleep(random.randint(1, 10))
        retorno2(plato)
        time.sleep(random.randint(1, 10))
        retorno3(plato)

    threading.Thread(target=procesar).start()

def confirmacion(dish:str):
    print (f"Se ha hecho el pedido de {dish}")
def listo(dish:str):
    print (f"{dish} está listo")
def entregado(dish:str):
    print (f"{dish} está entregado")    

simulador_pedidos("Berenjenas",confirmacion,listo,entregado)    
simulador_pedidos("Patatas",confirmacion,listo,entregado)    
simulador_pedidos("Tomates",confirmacion,listo,entregado)    