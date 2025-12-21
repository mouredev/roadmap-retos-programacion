# EJERCICIO:
# Explora el concepto de callback en tu lenguaje creando un ejemplo
# simple (a tu elección) que muestre su funcionamiento.
import random
import threading
import time

def funcion_principal(num1: int, num2: int, callback):
    print(f"Suma de {num1} y {num2}")
    callback(num1 + num2)


def callback_resultado(resultado: int) -> None:
    print(f"El resultado de la suma es: {resultado}")


funcion_principal(5, 3, callback_resultado)

#
# DIFICULTAD EXTRA (opcional):
# Crea un simulador de pedidos de un restaurante utilizando callbacks.
# Estará formado por una función que procesa pedidos.
# Debe aceptar el nombre del plato, una callback de confirmación, una
# de listo y otra de entrega.
# - Debe imprimir un confirmación cuando empiece el procesamiento.
# - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#   procesos.
# - Debe invocar a cada callback siguiendo un orden de procesado.
# - Debe notificar que el plato está listo o ha sido entregado.




def procesar_pedido(
    pedido: str,
    callback_confirmacion,
    callback_listo,
    callback_entrega,
) -> None:
    def process():
        print(f"Procesando pedido: {pedido}")
        tiempo = random.randint(1, 10)
        callback_confirmacion(pedido, tiempo)
        tiempo = random.randint(1, 10)
        callback_listo(pedido, tiempo)
        tiempo = random.randint(1, 10)
        callback_entrega(pedido, tiempo)

    threading.Thread(target=process).start()


# definicion de callbacks
def callback_confirmacion(pedido: str, tiempo: int) -> None:
    time.sleep(tiempo)
    print(f"Pedido {pedido} confirmado después de {tiempo} segundos")


def callback_listo(pedido: str, tiempo: int) -> None:
    time.sleep(tiempo)
    print(f"Pedido {pedido} listo después de {tiempo} segundos")


def callback_entrega(pedido: str, tiempo: int) -> None:
    time.sleep(tiempo)
    print(f"Pedido {pedido} entregado después de {tiempo} segundos")


# ejemplo de uso

if __name__ == "__main__":
    print("=" * 50)
    print("Simulador de pedidos de un restaurante")
    print("=" * 50)
    plato = input("Ingrese el nombre del plato: ")
    if plato:
        procesar_pedido(plato, callback_confirmacion, callback_listo, callback_entrega)
    else:
        pedidos = [
            "Pizza de pepperoni",
            "Hamburguesa con queso",
            "Ensalada",
            "Sopa de fideos",
            "Flan",
        ]
        for i, pedido in enumerate(pedidos):
            tiempo = random.randint(1, 5)
            time.sleep(tiempo)
            print(f"Pedido {i + 1} de {len(pedidos)}")
            procesar_pedido(
                pedido, callback_confirmacion, callback_listo, callback_entrega
            )
