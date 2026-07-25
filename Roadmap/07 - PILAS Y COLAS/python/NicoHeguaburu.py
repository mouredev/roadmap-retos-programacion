# #Pila/Stack (LIFO) Last In First Out

# stack = []
# stack.append("1")
# stack.append("2")
# stack.append("3")


# print(stack)

# stack_last = stack[len(stack) - 1]
# del stack[len(stack) - 1]


# print(stack.pop())

# print(stack_last)
# print(stack)



# #Cola/Queue   (FIFO) Firs In First Out

# queue = []
# queue.append("1")
# queue.append("2")
# queue.append("3")


# queue_first = queue[0]
# del queue[0]


# print(queue.pop(0))

# print(queue)



#Dificultad Extra

#Web
# stack = []



# def navegar(url):
#     print(f"Usted esta visualizando la pagina {url}")
#     stack.append(url)
#     menu()


# def ir_atras():
#     stack.pop()
#     print(f"Usted esta visualizando la pagina {stack[len(stack) - 1]}")
#     menu()

# # def ir_adelante(): No es posible deberia usar listas XD

# def menu():
#     print("NAVEGADOR DE NICOLAS HEGUABURU")
#     print("1----------Navegar en la web")
#     print("2----------Ir hacia atras")
#     print("3----------Ir hacia adelante")
#     print("4----------Salir")
#     i = input("Selecciona una opccion...")

#     if i == "1":
#         pag = input("a que pagina quieres ir...")
#         navegar(pag)
#     elif i == "2":
#         ir_atras()
#     elif i == "3":
#         print("No es posible ir adelante con pilas XD")
#     elif i == "4":
#         exit()
#     else:
#         print("seleccione una opcion valida")
#         menu()

# menu()







#Impresora compartida
cola = []
def menu_impresora():
    print ("1------------Ingresar Documento")
    print ("2------------Imprimir un documento de la cola")
    print ("3------------Salir")
    i = input("ingrese una opcion...")

    if i == "1":
        agregar_documento()
    elif i == "2":
        imprimir_documento()
    elif i == "3":
        exit()
    else:
        print("ingrese una opcion valida!!!")
    

def agregar_documento():
    doc = input("Ingrese el nombre del documento...")
    cola.append(doc)
    print(f"El documento {doc} se a ingresado con exito.")
    menu_impresora()


def imprimir_documento():
    if len(cola) > 0:
        print(f"el documento {cola[0]} se imprimio correctamente")
        cola.pop(0)
        menu_impresora()
    else:
        print("La cola de impresion esta vacia. Porfavor ingrese un documento")
        menu_impresora()


menu_impresora()