#Pilas o stacks
mi_lista = []

#Los elementos se van añadiendo
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
print(mi_lista)
#Se debe extraer 1º el último LIFO
print(mi_lista.pop())
print(mi_lista)
mi_lista.pop()
print(mi_lista)

#Colas o queues
mi_lista = []
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
mi_lista.append(4)
#Se debe extraer por el principio FIFO
print(mi_lista)
print(mi_lista.pop(0))
print(mi_lista)

#Navegador web 

lista = []

while True:
    print("1.- Ir a:")
    print("2.- Atrás")
    print("3.- Avanzar")
    print("4.- Salir")
    opcion = input("Seleccione una opción: ")
    match(opcion):
        case "1":
            pagina = input("Introduce la url: ")
            print(f"Esta es la {pagina}")
            lista.append(pagina)
            print(lista)
        case "2":
            print(lista.pop())
            print(lista)
        case "3":
            pass
        case "4":
            print("Saliendo del navegador")
            break    
        case _:
            print("Seleccione una opción válida")


#Cola de impresión
Cola = []
while True:
    Docu = input("Documento o imprimir/salir: ")
    if Docu == "imprimir":
        if len(Cola) > 0:
            print(f"Imprimiendo {Cola.pop(0)}")
        else:
            print("Añade un documento")    
    elif Docu == "salir":
        break
    else:
        Cola.append(Docu)


            
