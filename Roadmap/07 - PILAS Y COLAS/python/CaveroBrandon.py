"""EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las pilas (stacks - LIFO)
y las colas (queue - FIFO) utilizando una estructura de array o lista (dependiendo de las posibilidades de tu lenguaje).
"""


def enter_value():
    i = 0
    while i < 3:
        value = input(f'Enter value # {i + 1} to the list:')
        original_list.append(value)
        print(f'The list is: {original_list}')
        i += 1


def lifo_recover():
    copy_list = original_list.copy()
    print('**** Recovering the information LIFO ****')
    print(f'The list is: {original_list}')
    while len(copy_list) != 0:
        removed_value = copy_list.pop()
        print(f'The value removed was \'{removed_value}\', the list is now: {copy_list}')


def fifo_recover():
    copy_list = original_list.copy()
    print('**** Recovering the information FIFO ****')
    print(f'The list is: {original_list}')
    while len(copy_list) != 0:
        removed_value = copy_list.pop(0)
        print(f'The value removed was \'{removed_value}\', the list is now: {copy_list}')


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""


def web_navigator(web_address, total_address):
    print()
    user_input = input('Enter a web address, or "Adelante" to go forward, "Atras" to go back, or "Salir" to exit: ')
    option = str(user_input).lower()

    if option == 'adelante':
        if len(total_address) != len(web_address):
            web_address.append(total_address[len(web_address)])
            print_website(web_address)
            web_navigator(web_address, total_address)
        else:
            print(f'There is not action to go forward')
            web_navigator(web_address, total_address)
    elif option == 'atras':
        if len(web_address) == 1 or len(web_address) == 0:
            print(f'There is not action to go back')
            web_navigator(web_address, total_address)
        else:
            web_address.pop()
            print_website(web_address)
            web_navigator(web_address, total_address)
    elif option == 'salir':
        pass
    else:
        web_address.append(user_input)
        total_address.append(user_input)
        if web_address != total_address:
            total_address = web_address.copy()
        print_website(web_address)
        web_navigator(web_address, total_address)


def print_website(website_list):
    for element in website_list:
        print(element + '/', end='')


""" Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que 
recibe documentos y los imprime cuando así se le indica.La palabra "imprimir" imprime un elemento de la cola,
el resto de palabras se interpretan como nombres de documentos
"""


def print_spooler(printer_spooler_list):
    user_input = input('Enter the document you want to print, or "imprimir" to print, or "Salir" to exit: ')
    option = str(user_input).lower()

    if option == 'imprimir':
        if len(printer_spooler_list) == 0:
            print('There are no more documents to print')
            print_spooler(printer_spooler_list)
        else:
            printed_element = printer_spooler_list.pop(0)
            print(f'The element printed was "{printed_element}", elements in the printer spooler are:')
            for element in printer_spooler_list:
                print(element)
            print_spooler(printer_spooler_list)
    elif option == 'salir':
        pass
    else:
        printer_spooler_list.append(user_input)
        print(f'The element added is {user_input}, the documents in the printer spooler are:')
        for element in printer_spooler_list:
            print(element)
        print_spooler(printer_spooler_list)


# Exercise
original_list = list()
enter_value()
lifo_recover()
fifo_recover()

# Extra 1
web_address = list()
total_address = list()
web_navigator(web_address, total_address)

# Extra 2
printer_spooler_list = list()
print_spooler(printer_spooler_list)
