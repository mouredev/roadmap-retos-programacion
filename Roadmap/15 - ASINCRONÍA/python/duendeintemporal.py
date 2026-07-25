#15 { Retos para Programadores } ASINCRONÍA

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 
"""

import time
import threading

# Short for print()
log = print

def run_func(name, seconds):
    log(f"{name} - Start at: {time.strftime('%H:%M:%S')}")
    log(f"{name} - Last: {seconds} seconds")

    time.sleep(seconds)

    log(f"{name} - Ends at: {time.strftime('%H:%M:%S')}")

def run_funces():
    # Create threads for each function to run concurrently
    function_c = threading.Thread(target=run_func, args=('Function C', 3))
    function_b = threading.Thread(target=run_func, args=('Function B', 2))
    function_a = threading.Thread(target=run_func, args=('Function A', 1))

    # Start all threads
    function_c.start()
    function_b.start()
    function_a.start()

    # Wait for all threads to complete
    function_c.join()
    function_b.join()
    function_a.join()

    # Run Function D after A, B, and C have completed
    run_func('Function D', 1)

# Simulate the loading of a web page
time.sleep(2)  # Simulate a delay before showing the alert
log('Retosparaprogramadores #15')

run_funces()

# Output Example:
"""  
Retosparaprogramadores #15
Function C - Start at: 07:27:35
Function C - Last: 3 seconds
Function B - Start at: 07:27:35
Function B - Last: 2 seconds
Function A - Start at: 07:27:35
Function A - Last: 1 seconds
Function A - Ends at: 07:27:36
Function B - Ends at: 07:27:37
Function C - Ends at: 07:27:38
Function D - Start at: 07:27:38
Function D - Last: 1 seconds
Function D - Ends at: 07:27:39

"""
