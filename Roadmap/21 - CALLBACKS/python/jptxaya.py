# #21 CALLBACKS

## Ejercicio

# /*
#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.
#  */

lista = ["fgd","Fad","gfads","erd"]

print(sorted(lista))

print(sorted(lista,key=str.lower))


def multiplicar(num1, num2):
    return num1 * num2

def sumar(num1,num2):
    return num1 + num2

def operacion(callback,num1,num2):
    print(callback(num1,num2))

print("Callback sumar")
operacion(sumar,3,2)
print("Callback multiplicar")
operacion(multiplicar,3,2)

print("Dificultad Extra")

import random
import time

def confirmacion(plate):
    print(f"Plato {plate} confirmado")

def ready(plate):
    print(f"Plato {plate} listo")

def delivered(plate):
    print(f"Plato {plate} entregado")

def process_order(plate, on_confirmacion,on_ready,on_delivered):
    on_confirmacion(plate)
    time.sleep(random.randint(1,10))
    on_ready(plate)
    time.sleep(random.randint(1,10))
    on_delivered(plate)
    

process_order("Asado",confirmacion,ready,delivered)