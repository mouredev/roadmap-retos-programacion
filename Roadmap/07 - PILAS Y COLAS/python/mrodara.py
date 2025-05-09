#################### PILAS Y COLAS #########################

## PILAS
my_stack = [i for i in range(1,11)]

print(my_stack)

# Añadir un elemento a la pila
my_stack.append(11)
print(my_stack)

# Eliminar una elemento de la pila
my_stack.pop()

print(my_stack)

# Obtención del elemento correspondiente a procesar en una pila
print(my_stack[len(my_stack) - 1])

# Simulación de los procesos de una pila
for proccess in my_stack[::-1]:
    print(f"Procesando el proceso {proccess}")

print("La pila de procesos ha finalizado")

## FIN PILAS

## COLAS (FIFO)

my_queue = [i for i in range(1, 11)]
print(my_queue)

# Inserción de un elemento en la cola
my_queue.append(11)

print(my_queue)

# Extracción de un elemento de la cola
my_queue.pop(0)

print(my_queue)

# Procesando todos los elementos de una cola
for proccess in my_queue:
    print(f"Procesando el proceso {proccess}")
print("La pila de procesos ha finalizado")

## FIN COLAS

#################### FIN PILAS Y COLAS #########################


#################### EXTRA #########################

# Implementación navegador web
my_websites = ["blank page", "www.marca.com", "www.as.com", "www.elmundo.es"]
position = 0
end = False
while not end:
    action = input("Indica que quieres realizar (adelante/atras/web): ")
    if action.lower() == "atras":
        print(f'Navegando a {my_websites[position-1] if position > 0 else my_websites[0]}')
        position -= 1 if position > 0  else 0
    elif action.lower() == "adelante":
        print(f'Navegando a {my_websites[position+1] if position < len(my_websites) else my_websites[len(my_websites)]}')
        position += 1 if position < len(my_websites) - 1 else len(my_websites) - 1
    elif action.lower() == 'salir':
        end = True
        print(f'Historial de navegación: {my_websites}')
        print('Cerrando navegador - Fin de programa')
    else: # Añadimos una nueva web (en este caso en la posición + 1 de donde nos encontremos)
        my_websites.insert(position+1, action.lower())


# Implementación cola de impresión

my_printer_jobs = ["Doc1", "Doc2", "Doc3"]
end = False

while not end:
    action = input("Indica la acción a realizar (imprimir/nombre documento/salir): ")

    if action.lower() == "imprimir":
        print(f'Imprimiendo {my_printer_jobs.pop(0)}')
        print(f'Quedan pendientes estos trabajos: {my_printer_jobs}')
    elif action.lower() == "salir":
        end = True
        print(f"Saliendo del spool de impresión, quedan pendientes {len(my_printer_jobs)} documentos por imprimir: {my_printer_jobs}")
    else:
        my_printer_jobs.append(action.lower())
        print(f'El documento {action.lower()} se ha añadido a la cola de impresión quedando así: {my_printer_jobs}')

#################### FIN EXTRA #########################