"""
* EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
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
"""
import random
import time
import threading # Se usa para trabajar con hilos

def saludo(nombre:str):
    print('Ejecutando el proceso de saludar')
    print(f'Hola {nombre}!!')
    
def saludar(nombre:str, callback): # Callback, función que recibe como parámetro otra función
    print('Llamando al proceso de saludar')
    callback(nombre)
    
saludar('Luis',saludo) # Se llama a la función saludar, que recibe el callback

# EXTRA
def procesarPedido(comida:str, confirmar_callback, listo_callback, entregado_callback):
    def procesar(): # Creamos esta función recursiva para ejecutar el hilo. Ejecución multihilo
        print(f'Comenzando el proceso de preparación de {comida}')    
        time.sleep(random.randint(1, 10)) # Paramos entre 1 y 10 segundos la ejecución
        confirmar_callback(comida)
        time.sleep(random.randint(1, 10)) 
        listo_callback(comida)
        time.sleep(random.randint(1, 10)) 
        entregado_callback(comida)
    threading.Thread(target=procesar).start() #Ejecutamos el hilo

def confirmarPedido(comida:str):
    print(f'Pedido {comida} confirmado!!!')

def listoPedido(comida:str):
    print(f'Pedido {comida} listo para enviar!!!')
    
def entregadoPedido(comida:str):
    print(f'Pedido {comida} ha sido entregado!!!')

procesarPedido('Churrasco', confirmarPedido, listoPedido, entregadoPedido)
procesarPedido('Callos', confirmarPedido, listoPedido, entregadoPedido)
procesarPedido('Carne asada', confirmarPedido, listoPedido, entregadoPedido)
procesarPedido('Tortilla de patatas con cebolla', confirmarPedido, listoPedido, entregadoPedido)