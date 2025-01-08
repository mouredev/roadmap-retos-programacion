'''
# #07 PILAS Y COLAS
> #### Dificultad: Media | Publicación: 12/02/24 | Corrección: 19/02/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 
'''

class Stack(list):
    '''
    Stack class with the basics methods of a stack
    '''
    def __init__(self)->None:
        self.__stack = []

    # Adding the new element at the end of the list (Last In First Out)
    def push_element(self,element:any)->None:
        self.__stack.append(element)


    # Deleting the last element of the list (Last In First Out)
    def pop_element(self)->any:
        if len(self.__stack)<1:
            return 'error stack is empty add more elements'
        return self.__stack.pop()

    # To show the __stack in a better way
    def __str__(self):
        return str( self.__stack )

class Queve(list):
    '''
    Queve class with the basics methods of a queve
    '''
    def __init__(self)->None: # Create a new list 
        self.__queve = []

    # Adding the new element at the end of the list (First In First Out)
    def enqueve(self,element:any)->None: 
        self.__queve.append(element)

    # Deleting the element of the begins of the list (First In First Out)
    def dequeve(self)-> any:
        if len(self.__queve)<1:
            return 'error queve is empty add more elements'
        return self.__queve.pop(0)

    # To show the __queve in a better way
    def __str__(self):
        return str( self.__queve )


'''
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.

 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.
'''

class Browser():
    def __init__(self) -> None:
        self.__back:Stack =Stack()
        self.__foward:Stack =Stack()
        self.__current:str = ''

    def go_to(self,text:str) -> None:

        if text.lower() == 'adelante':
            self.__back.push_element(self.__current)
            self.__current = self.__foward.pop_element()
            print(f'Going foward to... {self.__current}')

        elif text.lower() == 'atras':
            self.__foward.push_element(self.__current)
            self.__current = self.__back.pop_element()
            print(f'Going back to... {self.__current}')

        else:
            self.__back.push_element(self.__current)
            self.__current = text
            print(f'Going to... {self.__current}')

# chrome = Browser()
# chrome.go_to('retosdeprogramacion.com')
# chrome.go_to('bsky.social')
# chrome.go_to('github.com')
# chrome.go_to('atras')
# chrome.go_to('atras')
# chrome.go_to('adelante')
# chrome.go_to('adelante')
# chrome.go_to('adelante')


class Printer():
    def __init__(self)->None:
        self.__queve:Queve = Queve()
    def to_print_document(self,document:any)->None:
        if document == 'imprimir':
            print(self.__queve.dequeve()) 
        else:
            print('Adding element...')
            self.__queve.enqueve(document)

# my_printer = Printer()
# my_printer.to_print_document(5)
# my_printer.to_print_document('tall')
# my_printer.to_print_document('imprimir')
# my_printer.to_print_document('imprimir')
# my_printer.to_print_document('imprimir')
# my_printer.to_print_document('4')
# my_printer.to_print_document('imprimir')
