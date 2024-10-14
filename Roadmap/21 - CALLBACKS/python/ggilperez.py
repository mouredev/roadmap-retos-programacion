# 21 Callbacks
import random
import time


def long_process(callback):
    print("Starting process")
    time.sleep(2)
    callback()


def process_completed():
    print("Process completed")


long_process(process_completed)


# Extra

def process_order(dish, confirm_callback, ready_callback, deliver_callback):
    print(f"Processing {dish}")
    confirm_callback(dish)
    time.sleep(random.randint(1, 10))
    ready_callback(dish)
    time.sleep(random.randint(1, 10))
    deliver_callback(dish)


def confirm(dish):
    print(f"{dish} confirmed")


def ready(dish):
    print(f"{dish} ready")


def deliver(dish):
    print(f"{dish} delivered")

process_order("Fish and chips", confirm, ready, deliver)