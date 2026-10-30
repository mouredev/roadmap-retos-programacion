"""/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
"""

# Crear una pila vacía
pila = []

# Añadir elementos (Push)
pila.append(10)
pila.append(20)
pila.append(30)
print("Pila actual:", pila)  # [10, 20, 30]

# Sacar elementos (Pop - sale el último: 30)
sacado_pila = pila.pop()
print("Elemento sacado:", sacado_pila)
print("Pila después del pop:", pila)  # [10, 20]

# Crear una cola vacía
cola = []

# Añadir elementos (Enqueue)
cola.append(10)
cola.append(20)
cola.append(30)
print("Cola actual:", cola)  # [10, 20, 30]

# Sacar elementos (pop - sale el primero: 10)
sacado_cola = cola.pop(0)
print("Elemento atendido:", sacado_cola)
print("Cola después de atender:", cola)  # [20, 30]

#Pila


def navegador_web():

    Pila_web_atras=[]
    Pila_web_adelante=[]
    
    while True:

        action=input("añade una url o indica una palabra realizar una acción adelante/atras/salir ")

        if action == "salir":
            print("Saliendo del historial de webs")
            break
        elif    action == "adelante":
            if len(Pila_web_adelante)>0:
                web=Pila_web_adelante.pop()
                Pila_web_atras.append(web)
            else:
                  print("no hay mas paginas adelante")
        elif    action == "atras":
            if len(Pila_web_atras)>1:
                web=Pila_web_atras.pop()
                Pila_web_adelante.append(web)
            else:
                print("no hay mas paginas atras")
        else:
            Pila_web_atras.append(action)
            Pila_web_adelante.clear()
        
        if len(Pila_web_atras) >0 : 
            print(f"la web es: {Pila_web_atras[len(Pila_web_atras)-1]}")
        else:
            print("Pagina de inicio")

#navegador_web()

def cola_impresion():

    coladeimpresion=[]

    while True:

        action = input("agrega un documento a imprimir o salir")

        if action == "salir":
            break
        elif action == "imprimir":
            if coladeimpresion :
                print(f"se ha impreso el documeo {coladeimpresion[0]}")
                coladeimpresion.pop(0)
            else:
                print("no hay documentos en la cola por imprimir")
            pass
        else:
            coladeimpresion.append(action)

        print(f"Cola de impresión: {coladeimpresion}")    

cola_impresion()        


