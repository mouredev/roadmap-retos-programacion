
#  EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.    

import time
import random

def aviso_terminado():
    print("¡Descarga completada con éxito!")

def descargar_archivo(nombre, callback_al_terminar):
    print(f"Descargando {nombre}...")
    time.sleep(2)
    callback_al_terminar()

descargar_archivo("foto_vacaciones.jpg", aviso_terminado)


#  DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.

def order_confirm (platillo : str):
    print(f"El platillo {platillo} se ha aprobado")

def order_ready (platillo : str):
    print(f"Pedido listo. Su platillo {platillo} esta listo")

def order_delivered (platillo : str):
    print(f"Pedido enregado con exito {platillo}")

def order (platillo : str,function_confirm, function_ready, function_deliverd):
    function_confirm(platillo)
    print(f"El platillo {platillo} se esta cocinado por favor espere")
    time_waiting = random.randint(1,10)
    print(f"Tiempo de espera {time_waiting} segundos")
    time.sleep(time_waiting)
    function_ready(platillo)
    print("Su platillo se esta llevando a su lugar")
    time_waiting = random.randint(1,10)
    print(f"Tiempo de espera {time_waiting} segundos")
    time.sleep(time_waiting)
    function_deliverd(platillo)

order ("Milanesa de pollo",order_confirm, order_ready, order_delivered)