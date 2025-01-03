# #21 CALLBACKS
"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""



def saludar(name):
    return (f"Hola {name}")

def ejecutar_saludo(saluda, name):
    return saluda(name)

print (ejecutar_saludo(saludar,"Fede"))
 
num = (8,7)

def multiplicar(num):
    return num[0]*num[1]

def multiplicados(mult,n):
    return mult(n)

print (multiplicados(multiplicar,num))


"""
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

import time
import random
import threading

def pedidos(plato,confirmado,listo,entregado):
    def ejecutar():
        confirmado(plato)
        time.sleep(random.randint(1,10))
        listo(plato)
        time.sleep(random.randint(1,10))
        entregado(plato)
    threading.Thread(target=ejecutar).start()
    

def confirmado(plato):
    print (f"El pedido de {plato} ha sido confirmado")

def listo(plato):
    print (f"El pedido de {plato} está listo")

def entregado(plato):
    print (f"El pedido de {plato} ha sido entregado")

pedidos ("Pizza",confirmado,listo,entregado)
pedidos ("Hamburguesa",confirmado,listo,entregado)
pedidos ("Empanadas",confirmado,listo,entregado)