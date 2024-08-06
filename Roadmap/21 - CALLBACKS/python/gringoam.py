import random
import time
import threading
"""
Ejercicio
"""

def proceso_prin(nom: str, fun_prin):
    fun_prin(nom)

def imp_nom(nom:str):
    print(nom)

proceso_prin("Diego", imp_nom)

"""
Extra
"""

def procesa_pedidos(plato, conf_pedido, conf_listo, conf_entregado ):
    def proceso():

        conf_pedido(plato)
        time.sleep(random.randint(1,10))
        conf_listo(plato)
        time.sleep(random.randint(1,10))
        conf_entregado(plato)
    threading.Thread(target=proceso).start()

def confirmar_pedido(producto:str):
    print(f"El pedido de {producto} fue confirmado")

def pedido_listo(producto:str):
    print(f"El pedido de {producto} ya está listo")

def pedido_entregado(producto:str):
    print(f"El pedido de {producto} fue esntregado")


procesa_pedidos("Ravioles", confirmar_pedido, pedido_listo, pedido_entregado)
procesa_pedidos("Milanesa", confirmar_pedido, pedido_listo, pedido_entregado)
procesa_pedidos("Pizza", confirmar_pedido, pedido_listo, pedido_entregado)
    




