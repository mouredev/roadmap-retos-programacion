import random
import threading
import time
from collections.abc import Callable

"""
    CALLBACKS
"""


def greeting_process(name: str, callback: Callable[[str], None]):
    print("Running the greeting process...")
    callback(name)


def greet_callback(name: str):
    print(f"Hello, {name}!")


greeting_process("Elhdrond", greet_callback)


"""
    EXTRA EXERCISE
"""


def order_process(
    drink_name: str,
    confirm_callback: Callable[[str], None],
    ready_callback: Callable[[str], None],
    delivered_callback: Callable[[str], None],
):
    def process():
        confirm_callback(drink_name)
        time.sleep(random.randint(1, 10))
        ready_callback(drink_name)
        time.sleep(random.randint(1, 10))
        delivered_callback(drink_name)

    # threading.Thread runs each order concurrently: without it, every time.sleep
    # would block the main thread and orders would be processed one at a time.
    threading.Thread(target=process).start()


def confirm_order(drink_name: str):
    print(f"Your order '{drink_name}' has been confirmed.")


def order_ready(drink_name: str):
    print(f"Your order '{drink_name}' is ready for collection.")


def order_delivered(drink_name: str):
    print(f"Your order '{drink_name}' has been delivered. Enjoy!")


order_process("Flat White", confirm_order, order_ready, order_delivered)
order_process("Matcha Latte", confirm_order, order_ready, order_delivered)
order_process("Espresso Tonic", confirm_order, order_ready, order_delivered)
order_process("Oat Milk Cappuccino", confirm_order, order_ready, order_delivered)
