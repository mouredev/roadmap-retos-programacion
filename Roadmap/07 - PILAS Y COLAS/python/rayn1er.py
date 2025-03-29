# /*
#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#  */

# pilas o stacks (primero en entrar, ultimo en salir) 

stack = []
stack.append('primero')  #primero en entrar (push)
print(stack)
stack.append("segundo")
print(stack)
stack.pop() # utilizamos pop para eliminar el ultimo elemento (pop)
print(stack) #elimina el ultimo funcionando como una pila

# colas or queue (primero en entrar, primero en salir)
print()
queue = []
queue.append('primero')  #primero en entrar (push)
print(queue)
queue.append("segundo")
print(queue)
queue.pop(0) # utilizamos pop con el indice cero para eliminar el priemr elemento en la lista (pop)
print(queue) # elimina el primero funcionando como una cola


#extra 




def surfing_web():
    web_browser = []
    while True:
        element = input("Ingrese la url o si desea ir adelante o hacia atras o salir -> ")

        if element.lower() == 'salir':
                print('Cerrando ')
                break
        elif element.lower() == 'adelante':
                pass
        elif element.lower() == 'atras':
            if len(web_browser) > 0:
                web_browser.pop()
        else:
            web_browser.append(element)

        if len(web_browser) > 0:
              print(f"has navegado hasta {web_browser[len(web_browser) - 1]} ")
        else:
              print("Estas en la pagina de inicio ")

def print_element():
    printer_queue = []

    while True:
         element = input("Escriba si quiere imprimir un elemento de la cola o agregar uno o salir de la impresora-> ")
         element = element.lower()
         if element == 'salir':
              print('Cerrando ')
              break
         if element == "imprimir":
                if printer_queue:
                    print(f"Imprimiendo: {printer_queue.pop(0)}")
                else:
                    print("No hay documentos en cola")
         else:
                printer_queue.append(element)
                print(f"Documento agregado: {element}")


            
while True:
    print(f'''
        Seleccione una opcion
        1 - Navegador web
        2 - Impresora
        3 - Salir
          ''')
    
    option = input('Seleccione opcion -> ')

    if option == '1':
        surfing_web()
    elif option == '2':
        print_element()
    elif option == '3':
        print('Cerrando ')
        break
    else:
        print("Seleccione una opcion correcta -> ") 