'''
STACK - LISTA
'''

lista = [] 

# introducir en la lista
lista.append("a")
lista.append("b")
lista.append("c")
lista.append("d")

# mostramos el contenido
print(lista)

# recuperar con .pop()
print("sacamos:", lista.pop())
lista.append("e")

print(lista)


'''
QUEUE - COLA 
'''

from collections import deque

cola = deque()

for i in range(5):
    puesto = 'puesto ' + str(i+1)
    print('Llega', puesto)
    cola.append(puesto)
    print('Cola:', cola)


# salen todos los puestos de la cola 
while len(cola) > 0:
    print('Sale', cola.popleft())
    print('Qedan:', cola)


'''
EXTRA
'''

def buscador():
    
    paginas = []

    ultima_pagina = ""

    def link():
       link = input("Ingrese una pagina web: ")
       paginas.append(link)
       print(f"Redirigiendo a {link}") 
    

    def forward():
       if ultima_pagina == "":
           print("Estás en la ultima pagina") 
       else:
           paginas.append(ultima_pagina)
           print("Redirigiendo a ", paginas[-1])


    def backwards():
        backwards = paginas.pop()
        print(f"Ultima pagina: {backwards}")

        return backwards


    while True:

        print()
        print("1. Buscar")
        print("2. Adelante")
        print("3. Atras")
        print("4. Historial")
        print("5. Salir")

        choice = input("Elija una opción: ")

        match choice:

            case "1":
                link()
            case "2":
                forward()
            case "3": 
                ultima_pagina = backwards()
            case "4": 
                print(paginas)
            case "5":
                print("Cerrar el navegador.")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")


buscador()    


def printer():

   queue = deque() 

   def send():
        doc = input("Documento a enviar :")
        queue.append(doc)
        print(f"Cola: {queue}")


   def imprimiendo():
       print('Imprimiendo', queue.popleft())
       print('Qedan:', queue, 'documentos.')

   while True:
       
       print()
       print("1. Enviar")
       print("2. Imprimir")
       print("3. Salir")
       
       choice = input("Elija una opción: ")
       
       match choice:

        case "1":
            send()
        case "2":
            if len(queue ) == 0:
                print("No hay documentos que imprimir.")
            else:
                imprimiendo()
        case "3":
            print("Impresora cerrada.")
            break
        case _:
            print("Opcion no valida. Elige una opcion del 1 al 3")

printer()
