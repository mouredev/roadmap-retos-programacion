# Stack / Pilas - LIFO - Last In First Out
# El último elemento en entrar a una estructura de datos tipo LIFO, es el primero en salir cuando es requerido

stack = []
# Añadimos a una lista vacía, un conjunto de números con .append.
stack.append('1')
stack.append('2')
stack.append('3')
stack.append('4')
stack.append('5')
stack.append('6')

print(stack) # Lista.

stack_removed = stack.pop() # El método .pop() remueve el último item de una lista y puede hacer su valor recuperable. 
print(stack)
print(stack_removed) # 6, valor removido mas sí recuperado.

# Cola/Queue - FIFO - First In First Out - El primero que entra en la cola, es el primero que sale.

cola = []

cola.append('Mouse')
cola.append('Tablet')
cola.append('Laptop')
cola.append('Cola')

cola_removed = cola.pop(0) # Eliminamos y obtenemos el valor del elemento 0 dentro de la lista 'cola'.
print(cola_removed)
print(cola)

'''
Ejercicios
'''

def web_browser():
  stack: list = []
  
  while True:
    action = input('Añade una URL o selecciona entre: adelante / atras / salir:\n')

    if action == 'salir':
      print('Saliendo del programa. ¡Hasta luego!')
      break
    elif action == 'adelante':
      # Nos han engañao
      pass
    elif action == 'atras':
      if len(stack) > 0:
        stack.pop()
      else:
        print('Estás en la página de inicio.')
    else: 
      stack.append(action)
    
    if len(stack) > 0:
      print(f'Has navegado hasta: {stack[len(stack) - 1]}')
    else:
      print('Estás en la pagina de inicio.')

# web_browser()

def printer():
  queue = []

  while True:

    action = input('Añade un documento a imprimir, o con la palabra: imprimir/salir selecciona tu acción.\n')

    if action == 'salir':
      print('Cerrando impresora.')
      break
    elif action == 'imprimir':
      if len(queue) > 0:
        first_to_print = queue.pop(0)
        print(f'Imprimiendo: {first_to_print}')
      else:
        print('No hay mas elementos en la cola de impresión.')
    else:
      queue.append(action)

    # print(f'Cola de impresion: {queue}')

printer()