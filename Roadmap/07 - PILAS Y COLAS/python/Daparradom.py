### 07 -- PILAS Y COLAS ###  

# PILA : ultimo elemento en ingresar es el primero en salir

# cambios realizados

cambios = ["escribir", "borrar frase", "aumentar tamano de letra", "poner en negrilla"  ]

print(f"Cambios actuales: {cambios}")

ultimo_cambio = cambios.pop()

print(f'Cambio desecho : {ultimo_cambio}')

print (f' Historial de cambios actual luego de deshacer el ultimo {cambios}')

# Cola : primer elemento en ingresar es el primero en salir

banco_cola = ["Turno 1","Turno 2","Turno 3","Turno 4"]

atendiendo = banco_cola.pop(0)

print(f"se atiende turno {atendiendo}, quedan en espera {banco_cola}")
    

def navegacion () :
    pagina_web = []
    while True :
        comando = input("Escriba adelante o atras para navegar entre las paginas o escriba el nombre de la pagina que desea abrir, presione s para salir: ")
        comando_lower = comando.lower()
        if comando_lower == 's' :
            print("saliendo de la navegacion")
            break
        elif comando_lower == "adelante":
            pass
        elif comando_lower == "atras":
            if len(pagina_web)>0 :
               pagina_web.pop()
        else:
            pagina_web.append(comando_lower)
        
        if len(pagina_web) > 0  :
            print(f'Estas en la pagina : {pagina_web[len(pagina_web)-1]}')
        else :
            print("estas en el inicio")

def imprimiendo () :
    cola_impresion = []
    while True :
        documento = input('agregue documento, imprimir o presione s para salir: ')
        documento_lower = documento.lower()
        if documento_lower == "s" :
            print('saliendo de impresora')
            break
        elif documento_lower == "imprimir":
            if len(cola_impresion)>0 :
                print(f"Imprimiendo el documento: {cola_impresion.pop(0)}")
        else:
            cola_impresion.append(documento_lower)
        
        if len(cola_impresion) > 0:
            print(f"Documentos en cola de impresion: {cola_impresion}")
        else:
            print("No hay documentos en la cola de impresion")

#navegacion()
imprimiendo()