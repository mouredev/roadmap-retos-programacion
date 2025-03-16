'''/*
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
 */
```'''
import random
import time
def espera():
    return random.randint(1,10)
    
def pedido(plato):
    print(f"Pedido de {plato} Aceptado")

def preparacion(plato):
    print(f"{plato} listo para entrega")
def entrega(plato):
    print(f"Enviando {plato}...")

def proceso(plato, pedido, preparacion, entrega):
    pedido(plato)
    time.sleep(espera())
    preparacion(plato)
    time.sleep(espera())
    entrega(plato)

menu = [
    "Ensalada Caprese",
    "Bruschetta",
    "Sopa de Cebolla",
    "Tartar de Salmón",
    "Risotto de Setas",
    "Pollo al Curry",
    "Paella de Mariscos",
    "Lomo de Cerdo a la Mostaza",
    "Tarta de Chocolate",
    "Tiramisú",
    "Cheesecake de Frutos Rojos",
    "Helado Artesanal"
]
print("¿Que desea pedir?")
for i in enumerate(menu):   
    print(i)
num= int(input("introduza el numero del plato que desea pedir\n"))
plato = menu[num]
proceso(plato, pedido, preparacion, entrega)