from time import sleep
from random import randint

#Ejercicio
def sum_two_values(n1, n2, fun_title_calc):
    fun_title_calc()
    return f"{n1} + {n2} = {n1 + n2}"

def title_calc():
    print("----Calculadora-----")

print(sum_two_values(3, 4, title_calc))

#Extra

def food_order(dish_name, fun_confirm_order, fun_ready_order, fun_delivery_order):
    #Llamar a las callbacks
    fun_confirm_order(dish_name)
    #Tiempo de espera hasta realizar el siguiente proceso
    sleep(randint(1,10))

    fun_ready_order(dish_name)
    sleep(randint(1,10))

    fun_delivery_order(dish_name)

#Función confirmación pedido
def confirm_order(dish_name):
    print(f"{dish_name.capitalize()}, confirmado.")

#Función pedido listo
def ready_order(dish_name):
    print(f"{dish_name.capitalize()}, listo para ser entregado.")

#Función entrega pedido
def delivery_order(dish_name):
    print(f"{dish_name.capitalize()} ha sido entregado.")



food_order("arroz con pollo", confirm_order, ready_order, delivery_order)