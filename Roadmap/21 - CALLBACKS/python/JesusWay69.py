import os, time, random
os.system('cls')



"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 """
def show_result(result):#Esta función callback imprime el resltado que ha devuelto la función de suma
    print("El resultado es: ",result)
    print()

def main_funtcion (fun, args,callback):#Creamos una función principal con los argumentos de:
        # otra función, los argumentos de esta y una o varias llamadas callback a otra/s funcion/es
    result = fun(*args)#Le indicamos que la función debe retornar un resultado a partir de sus argumentos
    callback(result)#Definimos la función callback a la que le pasamos ese resultado

def sum(a,b):
    return a + b
main_funtcion(sum, (5,7), callback=show_result)#Llamamos a la función principal pasando la de sum, 
        # sus argumentos y la llamada a la función callback

"""* DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado."""

def processing(state,args,callback1,callback2,callback3):
    result = state(args)
    if result == None:
        return
    callback1(result)#Las llamadas callback así como la función que lanza los pedidos  
    callback2(result)# se harán en el el orden establecido
    callback3(result)# aunque las funciones estén desordenadas como en este caso
    
def ready(food:str)->str:
    print(F"El plato de {food} está listo para servir")
    seconds = random.randint(1,10)
    time.sleep(seconds)
    return food

def delivery(food:str):
    print(F"El plato de {food} está servido")
    seconds = random.randint(1,10)
    time.sleep(seconds)
    print()

def orders(foods:list)->str:
    if len(foods)==0:
        return
    return foods.pop(0)#Esta función gestiona los pedidos por orden de llegada (FIFO)

def confirmation(food:str)->str:
    print(F"El plato de {food} se ha confirmado")
    seconds = random.randint(1,10)
    time.sleep(seconds)
    return food


           
foods = ["ensalada", "paella", "lentejas"]

while len(foods)>0:
    processing(orders,foods, callback1=confirmation, callback2=ready,callback3=delivery) 