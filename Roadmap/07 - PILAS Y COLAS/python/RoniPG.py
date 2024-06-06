# @Roni

"""
EJERCICIO: Implementa los mecanismos de introducción y recuperación de elementos propios de las pilas (stacks - LIFO)
y las colas (queue - FIFO) utilizando una estructura de array o lista (dependiendo de las posibilidades de tu lenguaje).
"""

"""PILA (STACK)"""

"""Creamos una lista y la utilizamos como pila"""

pila= [1,2,3]

"""Insertar datos"""

print(pila)
pila.append(4)
pila.append(5)
print(pila)

"""Borrar datos"""
print(f"Contenido de la pila: {pila}")
pila.remove(1) # --> Borrar dato en la posicion deseada
print(f"Contenido de la pila despues del remove(1): {pila}")
#pila.clear() --> Eliminar(limpiar) todos los datos de la lista
print(f"Contenido de la pila: {pila}")
elementoCima=pila.pop() # ---> Borrar dato en la cima de la pila con un return del dato
print(f"Contenido de la pila despues del pop(): {pila}")
print(f"Elemento en la cima de la pila: {elementoCima}")

"""Actualizar datos"""

print(f"Contenido de la pila: {pila}")
pila.insert(0,1)
print(f"Contenido de la pila despues del insert(0,1): {pila}")

"""Ordenar datos"""

pila.append(8)
pila.append(5)
pila.append(7)
print(f"Contenido de la pila: {pila}")
pila.sort()
print(f"Contenido de la pila despues del sort(): {pila}")

"""COLA(QUEUE)"""

"""Creamos una lista y la utilizamos como cola"""

cola=["Elemento 0","Elemento 1","Elemento 2"]

"""Agregamos elementos a la cola"""

print(f"Contenido de la cola: {cola}")
cola.append("Elemento 3")
print(f"Contenido de la pila despues del append(\"Elemento 3\"): {cola}")

"""Eliminamos y mostramos el primer elemento de la cola"""

print(f"Contenido de la cola: {cola}")
firstElement= cola[0] # --> Obtenemos pero no eliminamos el primer elemento de la cola
print(f"Contenido del primero de la cola: {firstElement}")
cola.remove(cola[0])
print(f"Contenido despues del remove(0): {cola}") # --> Mostramos la cola actualizada

"""
DIFICULTAD EXTRA (opcional):
 - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web.
Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás,
mostrando en cada caso el nombre de la web. Laspalabras "adelante", "atras" desencadenan esta acción,
el resto se interpreta como el nombre de una nueva web.
"""
def Programa1():
    url = ["www.google.com", "www.twitter.com", "www.gmail.com"]
    texto=""
    pos=0

    while(texto.lower()!="salir"):
        print("\n*******Navegación web*******\n")
        print("Escribe la url de la página web para dirigirte a ella.")
        print("Si la url no existe se creara una nueva web")
        print("Escribe 'adelante' para ir a la siguiente web.")
        print("Escribe 'atras' para ir a la web anterior.")
        print("Escribe 'salir' para cerrar el programa.")
        texto=input("Escribe aquí: ")
        if texto.lower()=="adelante":
            if pos +1 >= len(url):
                print("Ya te encuentras en la url del final")
                print(f"La url es:\n{url[pos]}")
            else:
                print("Avanzamos")
                print(f"La siguiente url es:\n{url[pos+1]}")
                pos += 1
        elif texto.lower()=="atras":
            if pos -1 < 0:
                print("Ya te encuentras en la url del principio")
                print(f"La url es:\n{url[pos]}")
            else:
                print("Retrocedemos")
                print(f"La url anterior es:\n{url[pos-1]}")
                pos -= 1 
        elif texto.lower()=="salir":
            print("Vuelva pronto")
        elif texto in url: # --> url.__contains__(texto): Es otra manera de comprobarlo.
            print("Encontramos url")
            pos= url.index(texto)
            print(f"La url es:\n{url[pos]}")
        else:
            print("Creamos url")
            url.append(texto)
            print(f"La url es:\n{url[len(url)-1]}")
            # pos= round(len(url)/2) --> Nos posiciona en la url del medio
Programa1()
"""
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida 
que recibe documentos y los imprime cuando así se le indica. La palabra "imprimir" imprime un elemento de la cola,
el resto de palabras se interpretan como nombres de documentos.
"""
def Programa2():
    doc=["Documento 1","Documento 2","Documento 3"]
    texto=""
    while texto.lower()!="salir":
        print("\n*******Mecanismo de una impresora*******\n")
        print("Escribe 'imprimir' para ir a la imprimir el primer documento de la cola.")
        print("Si no, introduce el nombre del nuevo documento a imprimir y se añadira a la cola")
        print("Escribe 'salir' para cerrar el programa.")
        texto= input("Escribe aquí: ")

        if texto.lower()=="imprimir":
            if len(doc) < 1:
                print("La impresora esta vacía")
            else:
                print(f"Procedemos a imprimir el documento: {doc[0]}")
                doc.remove(doc[0])
        elif texto.lower()=="salir":
            print("Vuelva pronto")
        else:
            print("Introducimos el nuevo documento")
            doc.append(texto)
Programa2()
