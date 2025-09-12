"""
 EJERCICIO:
 Explora el concepto de callback en tu lenguaje creando un ejemplo
 simple (a tu elección) que muestre su funcionamiento.

 DIFICULTAD EXTRA (opcional):
 Crea un simulador de pedidos de un restaurante utilizando callbacks.
 Estará formado por una función que procesa pedidos.
 Debe aceptar el nombre del plato, una callback de confirmación, una
 de listo y otra de entrega.
 - Debe imprimir un confirmación cuando empiece el procesamiento.
 - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
   procesos.
 - Debe invocar a cada callback siguiendo un orden de procesado.
 - Debe notificar que el plato está listo o ha sido entregado.
"""
from random import randint

print(f"##  Explicación  {'#' * 30}")
print(r"""
Un "callback" es una función que puede ser llamada como argumento de otra función. Por ejemplo, tengo una función operar cuyos argumentos son
la operación a ejecutar (que es el nombre de la función que hará la operación "real") más el resto de argumentos necesarios para que la 
operación pueda ejecutarse. 

def sumar(num1, num2):
    return num1 + num2


def multiplicar(num1, num2):
    return num1 * num2


def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)


def operar(operacion, *args):
    return operacion(*args)


print(f"Suma: {operar(sumar, 3, 2)}")
print(f"Multiplicación: {operar(multiplicar, 2, 3)}")
print(f"Factorial: {operar(factorial, 4)}")
print(f"Factorial de la multiplicación: {operar(factorial, operar(multiplicar, 2, 3))}")

Suma: 5
Multiplicación: 6
Factorial: 24
Factorial de la multiplicación: 720

""")

print(f"##  Dificultad extra  {'#' * 30}\n")


def seconds_in_wait(init: int, end: int) -> int:
    return randint(init, end)


def process_order(callback_func, *args):
    from time import sleep
    sleep(seconds_in_wait(1, 10))
    return callback_func(*args)


def order_number():
    valor = 100
    while valor <= 1000:
        yield valor
        valor += 1


def create_order(*args) -> int:
    global orders
    global order_gen
    order_num = next(order_gen)
    orders[order_num] = {"meal": args[0], "state": "ordered"}
    return order_num


def confirm_order(*args):
    global orders
    if args[0] == "Y":
        state = "confirmed"
    else:
        state = "cancelled"
    orders[args[1]]["state"] = state


def order_ready(*args) -> int:
    global orders
    doing = randint(0, 5)
    if not doing:
        orders[args[0]]["state"] = "ready"
    return doing


def order_delivered(*args) -> int:
    global orders
    delivering = randint(0, 3)
    if not delivering:
        orders[args[0]]["state"] = "delivered"
    return delivering


def order_process(meal: str):
    order = process_order(create_order, meal)
    print(f"New order: order {order} {orders[order]}")
    process_order(confirm_order, "Y", order)
    print(f"Confirmation: order {order} {orders[order]}")
    print(f"Preparation: order {order} .", end="")
    while process_order(order_ready, order):
        print(".", end="")
    print(f" {orders[order]}")
    print(f"Delivering: order {order} .", end="")
    while process_order(order_delivered, order):
        print(".", end="")
    print(f" {orders[order]}")


order_gen = order_number()
orders = {}

order_process("milanesa")
order_process("locro")
order_process("pizza")
