"""
Exercise
"""
import time
import random


def data_processing(callback):
    print("Processing data...")
    time.sleep(2)  # Simula una tarea que toma 2 segundos
    print("Data processed.")
    callback()  # Llama al callback


def results_notify():
    print("The process has ended.")


"""
Extra
"""


def process_order(dish, confirmation_callback, ready_callback, delivery_callback):
    print(f"Order received: {dish}")
    confirmation_callback(dish)

    # Simulate processing time
    processing_time = random.randint(1, 10)
    time.sleep(processing_time)

    ready_callback(dish)

    # Simulate delivery time
    delivery_time = random.randint(1, 10)
    time.sleep(delivery_time)

    delivery_callback(dish)


def confirmation(dish):
    print(f"Confirmation: The order for {dish} is being processed.")


def ready(dish):
    print(f"Ready: The dish {dish} is ready for delivery.")


def delivery(dish):
    print(f"Delivery: The dish {dish} has been delivered to the customer.")


if __name__ == "__main__":
    print("Exercise")
    print("Starting processing...")
    data_processing(results_notify)

    print("Extra")
    process_order("Pizza Margherita", confirmation, ready, delivery)
