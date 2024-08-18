"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""

def proceso_principal(callback):
    print("Proceso principal en ejecución...")
    # Simulamos una tarea con una pausa
    import time
    time.sleep(2)
    print("Proceso principal completado.")
    # Llamamos al callback
    callback()

def mi_callback():
    print("Callback ejecutado después del proceso principal.")

# Llamamos a la función principal y le pasamos el callback
proceso_principal(mi_callback)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
"""

import time
import random

def procesar_pedido(plato, confirmacion_callback, listo_callback, entrega_callback):
    print(f"Procesando pedido para {plato}...")
    confirmacion_callback(plato)
    
    # Simulamos el tiempo de preparación
    tiempo_preparacion = random.randint(1, 10)
    time.sleep(tiempo_preparacion)
    listo_callback(plato)
    
    # Simulamos el tiempo de entrega
    tiempo_entrega = random.randint(1, 10)
    time.sleep(tiempo_entrega)
    entrega_callback(plato)

def confirmar_pedido(plato):
    print(f"Pedido confirmado para {plato}.")

def plato_listo(plato):
    print(f"{plato} está listo para ser entregado.")

def entregar_pedido(plato):
    print(f"{plato} ha sido entregado al cliente.")

def menu():
    while True:
        print("\n--- Menú del Restaurante ---")
        print("1. Hacer un pedido")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            plato = input("Introduce el nombre del plato: ")
            procesar_pedido(plato, confirmar_pedido, plato_listo, entregar_pedido)
        elif opcion == "2":
            print("Saliendo del sistema de pedidos. ¡Gracias!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutamos el menú
menu()
