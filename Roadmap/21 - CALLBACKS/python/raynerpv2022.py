# /*
#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.
#  */

def get_last (list1):
     
    
    return list1[len(list1)-1]

def get_first(list1):
    return list1[0]

def print_index(list1, function):
     return function(list1)
    
    


print(f" LAst items is  {print_index([1,2,3,4,5,6,7,8,9], get_last)}")
print(f" First items is  {print_index([1,2,3,4,5,6,7,8,9], get_first)}")

import tkinter as tk

def on_button_click():
    print("¡Botón presionado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Callback")

# Crear un botón y asignar el callback
button = tk.Button(root, text="Presiona aquí", command=on_button_click)
button.pack()

# # Iniciar el bucle de eventos
root.mainloop()


def Confirm(name : str):
    return f"El plato {name} esta confirmado"

def Ready(name :str):
    return f"El plato {name} esta listo"

def Delivered(name :int, price):
    return f"El plato {name} cuesta {price} y ha sido entregado"

import random, time

def Orders(name :str, action_Confirm,action_Ready,action_Delivered):
    stunden = random.randint(1,10)
    time.sleep(stunden)
    print( f" {action_Confirm(name)}, tiempo de demora {stunden} Horas")
    stunden = random.randint(1,10)
    time.sleep(stunden)
    print( f" {action_Ready(name)}, tiempo de demora {stunden} Horas")
    stunden = random.randint(1,10)
    time.sleep(stunden)
    print( f" {action_Delivered(name,12*stunden)}, tiempo de demora {stunden} Horas")


import threading

def Extra():
    print("")
    print("Extra")
    print("")
    orders = ["Brocolicon Queso", "Pizza de Coliflor", "Tortilla de Helado"," Helado de Zanahoria"]
    Threading = []
    for order in orders:
        Hilo = threading.Thread(target=Orders,args=(order,Confirm,Ready,Delivered))
        Threading.append(Hilo)
        Hilo.start()

    # espera que terminen todos los hilos activos
    for h in Threading:
        h.join()
    print("Estamos Cerrados")
    

Extra() 