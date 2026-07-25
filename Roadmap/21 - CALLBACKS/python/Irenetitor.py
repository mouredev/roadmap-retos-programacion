import random
import time
import threading

#Exercise
def call_twice(callback):
    print("About to call the callback...")
    callback()
    callback()
    print("Done!")


def greeting():
    print("Hello!")

call_twice(greeting)

#Extra Exercise

def order_process(dish_name: str, confirm_order, order_ready, order_delivered):
    def orders():
        confirm_order(dish_name)
        time.sleep(random.randint(1, 10))
        order_ready(dish_name)
        time.sleep(random.randint(1, 10))
        order_delivered(dish_name)

    threading.Thread(target=orders).start()

def confirm_order(dish_name: str):
    print(f"Your {dish_name} order has been received and is being prepared.")

def order_ready(dish_name: str):
    print(f"Your {dish_name} is cooked and ready for delivery")

def order_delivered(dish_name: str):
    print(f"Your {dish_name} has been delivered. Enjoy your meal! :)")


order_process("Spicy Chicken wings", confirm_order, order_ready, order_delivered)
order_process("Chicken tenders", confirm_order, order_ready, order_delivered)
order_process("French fries", confirm_order, order_ready, order_delivered)
order_process("Caesar salad", confirm_order, order_ready, order_delivered)