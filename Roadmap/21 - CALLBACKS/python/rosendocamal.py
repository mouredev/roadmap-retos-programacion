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

def greeting_process(name: str, callback):
    callback(name)

def greet_callback(name: str):
    print(f"Hola, {name}.")

greeting_process("Spinoza", greet_callback)


#### EXTRA ####

from time import sleep as haraganear
from random import randint as hacer_perder_tiempo_al_cliente

def Confirmación_Pedido(platillo: str) -> str:
    return f"Se ordena el platillo {platillo}."

def Finalizar_Pedido(platillo: str) -> str:
    return f"El platillo {platillo} ya está listo para entregar."

def Entrega_Pedido(platillo: str) -> str:
    return f"El platillo {platillo} ha sido entregado."

def Notificar(txt: str, callback) -> None:
    print(callback(txt))

def Esperar():
    haraganear(hacer_perder_tiempo_al_cliente(1, 10))

class Platillo():
    SOPA: str = "sopa"
    LENTEJAS: str = "lentejas"
    FRIJOL: str = "frijol"
    HABAS: str = "habas"

class SimulaciónPedido():
    def __init__(self):
        pass

    def proceso_pedido(self, nombre_platillo: str):
        Notificar(nombre_platillo, Confirmación_Pedido)
        Esperar()
        Notificar(nombre_platillo, Finalizar_Pedido)
        Esperar()
        Notificar(nombre_platillo, Entrega_Pedido)

pedido1 = SimulaciónPedido()
pedido2 = SimulaciónPedido()
pedido3 = SimulaciónPedido()
pedido4 = SimulaciónPedido()

pedido1.proceso_pedido(Platillo.SOPA)
pedido2.proceso_pedido(Platillo.LENTEJAS)
pedido3.proceso_pedido(Platillo.FRIJOL)
pedido4.proceso_pedido(Platillo.HABAS)
