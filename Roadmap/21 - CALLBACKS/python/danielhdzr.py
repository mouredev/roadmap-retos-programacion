# #21 CALLBACKS
# Dificultad: Media | Publicación: 20/04/24 | Corrección: 27/05/24

## Ejercicio


'''/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 */
'''
# Ej. 1 Callback sincrono
# Definicion de una funcion
def saludo(callback): # Parametro callback
    print("Antes del callback")
    callback() # Llamado a funcion
    print("Después del callback")

# Definicion de una funcion
def decir_hola():
    print("¡Hola!")

# Llamado a funcion
saludo(decir_hola) 
''' Toma como arg. a la funcion decir_hola() que sustituye el parametro callback, 
ahora decir_hola() sera llamada dentro de la funcion saludo en lugar de la funcion callback()'''

'''/////////////////////////////////////////////////////////////////////////'''
# Ej. 2 Callback asincrono
import time
import threading

# Definicion de una funcion
def mi_callback(resultado):
    print(f"Resultado procesado: {resultado}")

# Definicion de una funcion
def tarea_larga(callback):
    print("Iniciando tarea...")
    time.sleep(2)  # Simulación de tarea larga
    resultado = "Tarea completada"
    callback(resultado)

# Llamada en un hilo separado
threading.Thread(target=tarea_larga, args=(mi_callback,)).start() # (Objeto, arg.,) inicio

# Ej. 3
def mi_callback(resultado):
    print(f"El resultado es: {resultado}")

def operacion_asincrona(callback):
    resultado = 42  # Simulación de un resultado
    callback(resultado)  # Llama al callback con el resultado

# Usar el callback
operacion_asincrona(mi_callback)
print()

'''
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
'''

# Simulador de pedidos de restaurante
import asyncio
import random

# Lapso aleatorio para cada etapa
def generar_lapso():
    return random.uniform(1, 10)

# Función principal que inicia el proceso
async def funcion_principal(orden):
    print(f"Pedido recibido: {orden}")
    # Iniciar la cadena de callbacks
    await pedido(orden, confirmacion_pedido)

# Pedido
async def pedido(orden, callback):
    lapso = generar_lapso()
    print(f"Procesando pedido: {orden} (espera de {lapso:.2f} segundos)")
    await asyncio.sleep(lapso)
    print(f"Pedido {orden} realizado")
    # Llamar al siguiente callback
    await callback(orden, pedido_listo)

# Confirmación del pedido
async def confirmacion_pedido(orden, callback):
    lapso = generar_lapso()
    print(f"Confirmando pedido: {orden} (espera de {lapso:.2f} segundos)")
    await asyncio.sleep(lapso)
    print(f"Pedido {orden} confirmado")
    # Llamar al siguiente callback
    await callback(orden, pedido_entregado)

# Pedido listo
async def pedido_listo(orden, callback):
    lapso = generar_lapso()
    print(f"Preparando pedido: {orden} (espera de {lapso:.2f} segundos)")
    await asyncio.sleep(lapso)
    print(f"Pedido {orden} listo")
    # Llamar al siguiente callback
    await callback(orden, None)

# Pedido entregado
async def pedido_entregado(orden, callback):
    lapso = generar_lapso()
    print(f"Entregando pedido: {orden} (espera de {lapso:.2f} segundos)")
    await asyncio.sleep(lapso)
    print(f"Pedido {orden} entregado. ¡Gracias por tu compra!")
    # Este es el último paso, no hay más callbacks

# Capturar la orden
orden = input("Platillo a ordenar: ")

# Ejecutar el flujo
asyncio.run(funcion_principal(orden))
