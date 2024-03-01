
"""
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
"""


print("\n\n=====================================PILAS=====================================\n\n")


'''
Una pila es una colección ordenada de elementos donde la adición de un nuevo elemento y 
la eliminación de los existentes siempre ocurren desde el mismo extremo.
'''

stack = []

def push():
   
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

push()

def pop():

    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())

pop()
    
print("\n\n=====================================COLAS=====================================\n\n")

"""
Una  cola  es una colección ordenada de elementos donde la adición de nuevos elementos ocurre en un extremo 
y la eliminación de elementos existentes ocurre en el otro extremo. Se denominan delante y detrás respectivamente.

"""
queue = []

def push():

    queue.append("Miguel")
    print(queue)
    
    queue.append("Jose")
    print(queue)
    
    queue.append("Maria")
    print(queue)

    queue.append("Mar")
    print(queue)

    queue.append("Helena")
    print(queue)

push()

def pop():
    
    return queue.pop(0)
    
pop()
print(queue)

pop()
print(queue)

pop()
print(queue)

pop()
print(queue)

pop()
print(queue)


print("\n\n=====================================DIFICULTAD EXTRA=====================================\n\n")

'''
Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
'''

stack = ["program_languages"]

def python():
    print(f"\n{stack}\n")
    print("Bienvenido a la pagina de python")
    new_page = input("¿Que pagina quieres visitar ahora?: \n siguiente / anterior: ")
    if new_page.lower() == "anterior":
        stack.pop()
        program_languages()
    elif new_page.lower() == "siguiente":
        stack.append("javascript")
        javascript()
    else:
        print("Has elegido una opción no disponible \n [+] Saliendo del programa .....")
        exit
        
def javascript():
    print(f"\n{stack}\n")
    print("Bienvenido a la pagina de javascript")
    new_page = input("¿Que pagina quieres visitar ahora?: \n siguiente / anterior: ")
    if new_page.lower() == "anterior":
        stack.pop()
        python()
    elif new_page.lower() == "siguiente":
        stack.append("java")
        java()
    else:
        print("Has elegido una opción no disponible \n [+] Saliendo del programa .....")
        exit
        
def java():
    print(f"\n{stack}\n")
    print("Bienvenido a la pagina de java")
    new_page = input("¿Que pagina quieres visitar ahora?: \n siguiente / anterior: ")
    if new_page.lower() == "anterior":
        stack.pop()
        javascript()
    elif new_page.lower() == "siguiente":
        stack.append("typescript")
        typescript()
    else:
        print("Has elegido una opción no disponible \n [+] Saliendo del programa .....")
        exit

def typescript():
    print(f"\n{stack}\n")
    print("Bienvenido a la pagina de typescript")
    back = input("¿Quieres volver a visitar la página anterior? si / no: ")
    if back.lower() == "si":
        stack.pop()
        java()
    else:
        print("[+] Saliendo del programa .....")
        exit

    

def program_languages():
    print(f"\n{stack}\n")
    print("Bienvenido a la pagina principal\n Los 4 lenguajes mas usados en el roadmap del gran Mouredev son: \n 1º python\n 2º javascript\n 3º java\n 4º typescript")
    languages = input("¿Quieres visitar la página de python?: \nsi / no: ")
    
    if languages.lower() == "si":
        stack.append("python")
        python() 
    elif languages.lower() == "no":
        print("[+] Saliendo del programa .....")
    else:
        print("Has elegido una opción no disponible \n [+] Saliendo del programa .....")
        exit
    
program_languages()


print("\n\n=====================================DIFICULTAD EXTRA=====================================\n\n")
    
'''    
Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
'''

queue = []  

def new_doc(doc):
    queue.append(doc)
    print(queue)
    
new_doc("doc1.txt")
new_doc("doc2.txt")
new_doc("doc3.txt")
new_doc("doc4.txt")
new_doc("doc5.txt")

def impresion():
    print(f"Imprimiéndose el documento {queue.pop(0)}")
    
    

def imprimir():
    result = input("Quieres imprimir el primer documento de la cola de impresión: \nimprimir / no imprimir: ")
    while result == "imprimir":
        impresion()
        print(f"\n{queue}\n")
        if queue != []:
            result = input("Quieres imprimir el siguiente documento de la cola de impresión: \nimprimir / no imprimir: ")
        else:
            print("No hay documentos en la cola de impresión")
            break
        
imprimir()
