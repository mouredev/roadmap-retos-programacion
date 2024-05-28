""" EJERCICIO
Explora el concepto de callback en tu lenguaje creando un ejemplo
simple (a tu elección) que muestre su funcionamiento."""

import asyncio
import requests
import random


async def async_function(callback):
    results = api_call()
    print('Async function started')
    print('loading 10%')
    await asyncio.sleep(0.5)
    print('loading 30%')
    await asyncio.sleep(1)
    print('loading 60%')
    await asyncio.sleep(0.5)
    print('loading 90%')
    await asyncio.sleep(1)
    print("Async operation completed")
    callback(results)


def api_call():
    response = requests.get('https://www.boredapi.com/api/activity')
    if response.status_code == 200:
        return dict(response.json())
    else:
        return 0


def my_callback(activity):
    if activity != 0:
        print('**** Bored API ****')
        print(f'Activity: {activity.get("activity")}')
        print(f'Type of activity: {activity.get("type")}')
        print(f'Participants: {activity.get("participants")}')
        print(f'Price: {activity.get("price")}')
    else:
        print('No activity to display')


async def main():
    await async_function(my_callback)


"""DIFICULTAD EXTRA (opcional):
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estará formado por una función que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmación, una
de listo y otra de entrega.
- Debe imprimir un confirmación cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre procesos.
- Debe invocar a cada callback siguiendo un orden de procesado.
- Debe notificar que el plato está listo o ha sido entregado."""


def show_menu():
    print('---- Menu ----')
    print('1. Beef and blue cheese burger')
    print('2. Roast chicken')
    print('3. Fish fingers')
    print('4. Boiled eggs')


def get_order() -> str:
    try:
        print('Enter the number of your order: ', end='')
        selected_order = int(input())
        if selected_order == 1:
            return 'Beef and blue cheese burger'
        elif selected_order == 2:
            return 'Roast chicken'
        elif selected_order == 3:
            return 'Fish fingers'
        elif selected_order == 4:
            return 'Boiled eggs'
        else:
            print('Select a valid order')
            get_order()
    except ValueError:
        print('Enter a valid number')
        get_order()


def callback_accept_order(selected_order: str):
    print(f'Order accepted, processing order "{selected_order}"...')


def callback_confirm_order(selected_order: str):
    print(f'Order confirmed: "{selected_order}"...')


def callback_order_completed(selected_order: str):
    print(f'Order complete: "{selected_order}"...')


def callback_order_delivered(selected_order: str):
    print(f'Order delivered: "{selected_order}"')


async def async_order_processing(selected_order: str, accept_order, confirm_order, order_completed, order_delivered):
    accept_order(selected_order)
    await asyncio.sleep(random.randint(1, 10))
    confirm_order(selected_order)
    await asyncio.sleep(random.randint(1, 10))
    order_completed(selected_order)
    await asyncio.sleep(random.randint(1, 10))
    order_delivered(selected_order)


async def main_order_processing():
    await async_order_processing(order, callback_accept_order, callback_confirm_order, callback_order_completed, callback_order_delivered)


if __name__ == "__main__":
    asyncio.run(main())
    while True:
        show_menu()
        order = get_order()
        asyncio.run(main_order_processing())
