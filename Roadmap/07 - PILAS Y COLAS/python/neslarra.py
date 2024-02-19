"""
 EJERCICIO:
 Implementa los mecanismos de introducción y recuperación de elementos propios de las
 pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 o lista (dependiendo de las posibilidades de tu lenguaje).

 DIFICULTAD EXTRA (opcional):
 - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
   el nombre de una nueva web.
 - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
   impresora compartida que recibe documentos y los imprime cuando así se le indica.
   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
   interpretan como nombres de documentos.
"""

pila = []
cola = []


def apilar(elemento):
    global pila
    pila.append(elemento)


def encolar(elemento):
    global cola
    cola.append(elemento)


def tomar_de_la_pila():
    global pila
    if pila:
        return pila.pop()
    else:
        return None


def tomar_de_la_cola():
    global cola
    if cola:
        return cola.pop(0)
    else:
        return None


print(f"""Tanto las pilas (stacks) como las colas (queues) son estructuras lineales con entrada y salida de datos secuencial:
      1- las pilas se 'apilan' => las últimas entradas son las primeras salidas = tipo LIFO = Last Input First Output
      2- las colas se 'encolan' => las primeras entradas son las primeras salidas = tipo FIFO = First Input First Output
""")

print("Probando pila (Last Input First Output)\n")
print("Apilo 'Mundo'")
apilar("Mundo")
print("Apilo 'Hola'")
apilar("Hola")
print("Apilo 'World'")
apilar("World")
print("Apilo 'Hello'")
apilar("Hello")

print(f"Desapilo {tomar_de_la_pila()}")
print(f"Desapilo {tomar_de_la_pila()}")

print("Apilo 'Monde'")
apilar("Monde")
print("Apilo 'Alo'")
apilar("Alo")

print(f"Desapilo {tomar_de_la_pila()}")
print(f"Desapilo {tomar_de_la_pila()}")
print(f"Desapilo {tomar_de_la_pila()}")
print(f"Desapilo {tomar_de_la_pila()}")
print(f"Desapilo {tomar_de_la_pila()}")
print(f"Desapilo {tomar_de_la_pila()}")

print("\n\nProbando cola (First Input First Output)\n")
print("Encolo 'Hola'")
encolar("Hola")
print("Encolo 'Mundo'")
encolar("Mundo")
print("Encolo 'Hello'")
encolar("World")
print("Encolo 'World'")
encolar("Hello")

print(f"Desencolo {tomar_de_la_cola()}")
print(f"Desencolo {tomar_de_la_cola()}")

print("Encolo 'Alo'")
encolar("Alo")
print("Encolo 'Monde'")
encolar("Monde")

print(f"Desencolo {tomar_de_la_cola()}")
print(f"Desencolo {tomar_de_la_cola()}")
print(f"Desencolo {tomar_de_la_cola()}")
print(f"Desencolo {tomar_de_la_cola()}")
print(f"Desencolo {tomar_de_la_cola()}")
print(f"Desencolo {tomar_de_la_cola()}")

print("\n\nDificultad extra Navegador (usando PILA)\n\n")

pila_atras = []
pila_adelante = []
boton_atras = False
boton_adelante = False


def apilo_atras(pagina):
    global pila_atras
    pila_atras.append(pagina)


def apilo_adelante(pagina):
    global pila_adelante
    pila_adelante.append(pagina)


def tomar_de_la_pila_atras():
    global pila_atras
    if pila_atras:
        return pila_atras.pop()
    else:
        return None


def tomar_de_la_pila_adelante():
    global pila_adelante
    if pila_adelante:
        return pila_adelante.pop()
    else:
        return None


def ver_top_de_pila_atras():
    global pila_atras
    if pila_atras:
        return pila_atras[-1]
    else:
        return None


def habilitar_botones():
    global pila_atras
    global pila_adelante
    global boton_atras
    global boton_adelante
    if pila_atras.__len__() > 1:
        boton_atras = True
    else:
        boton_atras = False
    if pila_adelante:
        boton_adelante = True
    else:
        boton_adelante = False


habilitar_botones()
while True:
    salto = "\n"
    menu = f"Elegir opción:\nhttps://<url-destino>{salto + 'atras' if boton_atras else ''}{salto + 'adelante' if boton_adelante else ''}\nsalir\n  ==> "
    opcion = input(menu).lower()
    if opcion == "salir":
        pila_atras.clear()
        pila_adelante.clear()
        print("Navegador cerrado.")
        break
    if opcion == "atras" and boton_atras:
        pagina = tomar_de_la_pila_atras()
        apilo_adelante(pagina)
        pagina = ver_top_de_pila_atras()
        print(f"Vuelvo a {pagina}")
    elif opcion == "adelante" and boton_adelante:
        pagina = tomar_de_la_pila_adelante()
        apilo_atras(pagina)
        print(f"Voy a {pagina}")
    else:
        if opcion not in ("atras", "adelante"):
            pagina = opcion
            pila_adelante.clear()
            apilo_atras(pagina)
        else:
            pagina = ver_top_de_pila_atras()

    print(f"Estoy en página https://{pagina}")
    habilitar_botones()

print("\n\nDificultad extra Navegador (usando COLA)\n\n")

spool_impresion = []


def cargar_documento(documento: str):
    global spool_impresion
    spool_impresion.append(documento)


def imprimir():
    global spool_impresion
    return spool_impresion.pop(0)


salto = "\n"
tab = "\t"
while True:
    menu = f"Menu de impresora:{salto}{tab}Imprimir{salto}{tab}Ingresar Documento{salto}opcion => "
    opcion = input(menu)
    if not opcion:
        spool_impresion.clear()
        print("\n\nSaliendo.")
        break
    if opcion.lower() == "imprimir":
        if spool_impresion.__len__() > 0:
            print(f"Imprimiendo {imprimir()}", end="\n\n")
        else:
            print("Spool de impresión vacío!!!", end="\n\n")
    else:
        print(f"Mando a imprimir {opcion}", end="\n\n")
        cargar_documento(opcion)
