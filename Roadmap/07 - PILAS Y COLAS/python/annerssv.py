#PILAS Y COLAS

#PILA (LIFO)


mi_pila = []

#APILAR
mi_pila.append("1")
mi_pila.append("2")
mi_pila.append("3")
print(mi_pila)

#DESAPILAR
mi_pila.pop()
print(mi_pila)
mi_pila.pop()
print(mi_pila)
mi_pila.pop()
print(mi_pila) #DEVUELVE LA LISTA VACIA


#COLA (FIFO)

cola = []

#ENCOLAR

cola.append("1")
cola.append("2")
cola.append("3")
print(cola)


#DESENCOLAR

cola.pop(0)
print(cola)
cola.pop(0)
print(cola)
cola.pop(0)
print(cola) #DEVUELVE LA LISTA VACIA



#EJERCICIO EXTRA NAVEGADOR CON PILA
def pila_web():
    
    pila = []
    
    while True:
        
        option = input("Añade una url o navega con los comandos: 'adelante/atras/salir': ")
        
        if option == "adelante":
            pass
        elif option == "atras":
            if len(pila) > 0:
                pila.pop()
        elif option == "salir":
            print("Saliendo del navegador")
            break
        else:
            pila.append(option)
        
        if len(pila) > 0:
            print(f"Estas en la pagina {pila[len(pila) - 1]}.")
        else:
            print("Estas en la pagina de inicio")
        
#pila_web()
            
            
#EJERCICIO EXTRA IMPRESORA

def cola_impresora():
    
    cola_de_docs = [] 
    
    while True:
        
        print('''Bienvenido al sistema de impresora Canon elige una de las siguientes opciones:
                    1. Imprimir
                    2. Añadir documentos
                    3. Salir''')
        
        option = input("Elige una opción: ")
        
        if option == "1":
            if len(cola_de_docs) > 0:
                print(f"Imprimiendo el documento: {cola_de_docs[0]}")
                cola_de_docs.pop(0)
                print(f"Cola de documentos: {cola_de_docs}")
            else:
                print("No tienes documentos en la cola")
        elif option == "2":
            documento = input("Ingresa el nombre del documento a añadir con la terminación .doc: ")
            cola_de_docs.append(documento)
            print("Documento añadido correctamente")
            print(f"Cola de documentos: {cola_de_docs}")
        elif option == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Elige una opcion valida")
        
        
cola_impresora()        
