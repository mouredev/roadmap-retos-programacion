"""
Ejercicio
"""
def apply_discount(prices, discount_function):
  """Aplica un descuento a cada precio en una lista.

  Args:
    prices: Una lista de precios.

    discount_function: Una función que calcula el descuento.
  """
  discounted_prices = []
  for price in prices:
    discounted_price = discount_function(price)
    discounted_prices.append(discounted_price)
  return discounted_prices

def ten_percent_off(price):
  return price * 0.9

def twenty_percent_off(price):
  return price * 0.8

prices = [100, 50, 25, 75]

discounted_prices_10 = apply_discount(prices, ten_percent_off)
discounted_prices_20 = apply_discount(prices, twenty_percent_off)

print("Original Prices:", prices)
print("10% Off:", discounted_prices_10)
print("20% Off:", discounted_prices_20)


"""
Dificultad extra
"""

import time
import random

def process_order(dish_name, confirmation_callback, ready_callback, delivery_callback):
  """Simula el procesamiento de un pedido de restaurante con callbacks.

  Args:
    dish_name: El nombre del plato ordenado.

    confirmation_callback: Función a llamar al confirmar el pedido.

    ready_callback: Función a llamar cuando el plato esté listo.

    delivery_callback: Función a llamar al entregar el pedido.
  """
  confirmation_callback(dish_name)  

  print(f"Preparing {dish_name}...")
  processing_time = random.randint(1, 10)  
  time.sleep(processing_time)

  ready_callback(dish_name) 

  print(f"Delivering {dish_name}...")
  time.sleep(random.randint(1, 10))  

  delivery_callback(dish_name) 

# Callback
def on_confirmation(dish):
  print(f"Order confirmed: {dish}")

def on_ready(dish):
  print(f"{dish} is ready!")

def on_delivery(dish):
  print(f"{dish} has been delivered. Enjoy!")

# Simula una orden
process_order(
    "Pizza",
    on_confirmation,
    on_ready,
    on_delivery
)