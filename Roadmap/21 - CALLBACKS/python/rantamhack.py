import random
import time


'''
* EJERCICIO:
* Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu eleccion) que muestre su funcionamiento.
'''
print("\n\n=======================================EJERCICIO=======================================\n\n")



def called(num):
    return num[0] * num[1]

def caller(function, num):
    return function(num)

num = [7, 8]

result = caller(called, num)


print("El resultado de la multiplcacion es: ", result)



'''
* DIFICULTAD EXTRA (opcional):
* Crea un simulador de pedidos de un restaurante utilizando callbacks.
* Estara formado por una funcion que procesa pedidos.
* Debe aceptar el nombre del plato, una callback de confirmacion, una
* de listo y otra de entrega.
* - Debe imprimir un confirmacion cuando empiece el procesamiento.
* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
*   procesos.
* - Debe invocar a cada callback siguiendo un orden de procesado.
* - Debe notificar que el plato esta listo o ha sido entregado.
'''

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


exit_program = False
order = input("Que Pizza de la carta te apetece tomar?: ")

def place_order(order):

    global exit_program

    if order in menu:
        print(f"Ha elegido la pizza {order}, enviamos el pedido a cocina")
        waiting_time = random.uniform(1, 10)
        time.sleep(waiting_time)
        return
    else:
        print("La pizza elegida no esta en la carta.") 
        print("[!] Saliendo del programa .....")
        exit_program = True
        return

def order_received(func):
    if exit_program == False:
        print(f"Su pedido de pizza {order} ha llegado a cocina y esta en espera")
        waiting_time = random.uniform(1, 10)
        time.sleep(waiting_time)
        return   

def order_in_process(func):
    print(f"Su pizza {order} esta siendo procesada")
    waiting_time = random.uniform(1, 10)
    time.sleep(waiting_time)

def order_delivered(func):
    print(f"Su pizza {order} esta preparada para entregar")
    waiting_time = random.uniform(1, 10)
    time.sleep(waiting_time)
    print(f"La pizza {order} ha sido entregada")


menu = ("4 Quesos", "Margarita", "Tropical", "Carbonara", "Campesina", "Barbacoa")

order_received(place_order(order))

if not exit_program:
    order_delivered(order_in_process(order))
