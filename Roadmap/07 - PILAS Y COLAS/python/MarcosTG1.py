 
"""
  EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# ----- Pilas -----
 
mi_pila = []

# Introducción
mi_pila.append("duracell")
mi_pila.append("ionos")

last_in = mi_pila[len(mi_pila) - 1]
print(last_in)

del mi_pila[len(mi_pila) - 1]
print(mi_pila)

# Desapilar
mi_pila.pop()


# ----- Colas -----

mi_cola = []

# Encolar
mi_cola.append(1)
mi_cola.append(2)
mi_cola.append(3)

# Desencolar
print(mi_cola[0])
del mi_cola[0]

print(mi_cola)
print(mi_cola[0])


"""
* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""

# Aproveche el hecho de que las secuencias vacías son falsas.

def navegacion_pilas():
    
    traza_webs = []
    navegacion = True
    
    while navegacion:
        print("")
        print("Estás en el navegador waterfox")
        print("¿A qué web quieres navegar?")
        print("En caso de que no quieras navegar di `atrás`")
        print("Para recuperar la web en la que estabas di `adelante`")
        print("")

        peticion_usuario = str(input())
        print("\n")

        if peticion_usuario in ("atrás", "atras") and traza_webs:
            web_eliminada = traza_webs[len(traza_webs) - 1]
            traza_webs.pop()

            if traza_webs:
                last_in = traza_webs[len(traza_webs) - 1]
                print(f"Te encuentras en la web: {last_in}")
            else:
                print("No puedes retroceder más, estás en el home")

        elif peticion_usuario in ("atrás", "atras") and not traza_webs:
            print("No puedes retroceder más, aún no has navegado a ninguna web")
        
        elif peticion_usuario == "adelante" and traza_webs:
            traza_webs.append(web_eliminada)
            print(f"Te encuentras ahora mismo en {web_eliminada}")
        
        elif peticion_usuario == "adelante" and not traza_webs:
            print(f"No hay registros")
        
        elif peticion_usuario == "salir":
            navegacion = False

        else:
            traza_webs.append(peticion_usuario)
            last_in = traza_webs[len(traza_webs) - 1]

            print(f"Te encuentras ahora mismo en {last_in}")
            
navegacion_pilas()

"""
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def imprimir():

    documentos = []
    encendida = True

    while encendida:
        accion = str(input("Introduce un documento o imprímelo con `imprimir`, `salir` para terminar: "))

        if accion == "salir":
            encendida = False
        
        elif accion == "imprimir":
            if not documentos:
                print("No hay documentos listos para imprimir")
            else:
                print(f"Imprimiendo {documentos[0]}")
                documentos.pop(0)
        
        else:
            documentos.append(accion)
            print(documentos)

imprimir()
