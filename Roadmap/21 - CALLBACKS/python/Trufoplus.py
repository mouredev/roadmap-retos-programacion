#######################  EJERCICIO  ###########################################

def my_callback(callback):
    print('Haciendo algo....')
    task = 'Tarea terminada.'
    callback(task)

def result(task):
    print(task)

my_callback(result)


###############################################################################
### DIFICULTAD EXTRA
###############################################################################
from time import sleep
from random import randint

def process_order(confirmation):
    print('\n\nConfirmando el pedido...')
    random_time()
    status = 'Plato confirmado'
    confirmation(status)
    
    sleep(1)
    print('Preparando el plato...')
    random_time()
    ready = 'Plato listo para servir'
    confirmation(ready)
    
    sleep(1)
    print('Entregando plato a la mesa...')
    random_time()
    delivery = 'Plato entregado'
    confirmation(delivery)

def confirmation(status):
    print(status)

def random_time():
    random_time = randint(1, 10)
    print(f'Tiempo de espera: {random_time} segundos\n')
    sleep(random_time)    

process_order(confirmation)
