import time
from random import randrange
#Callbacks

def sum_callback(a,b):
    return a+b

def main(function_callback):
    print("Doing main function")     
    result = function_callback
    print(f'Return of the callback {result}')

main(sum_callback(2,3))    

#Extra 

def confirm_order(order:str):
    print(f'Order {order} has been confirmed')

def orden_ready(order:str):
    print(f'Order {order} is ready')

def order_deliver(order:str):
    print(f'Order {order} has been delivered')

def process_order(order_name,callback_confirmation,callback_ready,callback_deliver):
    callback_confirmation(order_name)
    random = randrange(0,10)
    time.sleep(random)
    callback_ready(order_name)
    random = randrange(0,10)
    time.sleep(random)
    callback_deliver(order_name )




process_order("Pizza",confirm_order,orden_ready,order_deliver)