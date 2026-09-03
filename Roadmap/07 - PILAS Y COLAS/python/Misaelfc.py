"""
    Ejercicio
"""
# Pila/Stack (LIFO - Last In, First Out)
pila = []
# Agregar elementos a la pila
pila.append(1)
pila.append(2)
pila.append(3)
print("Pila después de agregar elementos:", pila)

# Eliminar elementos de la pila
elemento_eliminado = pila.pop()
print("Elemento eliminado de la pila:", elemento_eliminado)
print("Pila después de eliminar un elemento:", pila)

# Cola/Queue (FIFO - First In, First Out)
cola = []
# Agregar elementos a la cola
cola.append(1)
cola.append(2)
cola.append(3)
print("Cola después de agregar elementos:", cola)
print("Elemento eliminado de la cola:", cola.pop(0))
print("Cola después de eliminar un elemento:", cola)

"""
Extra
"""
def navegador_web():
    historial_atras = []
    historial_adelante = []
    pagina_actual = None

    while True:
        accion = input("Ingrese una acción (atras, adelante, salir): ").lower()
        
        if accion == "salir":
            print("Saliendo del navegador...")
            break
        elif accion == "atras":
            if historial_atras:
                historial_adelante.append(pagina_actual)
                pagina_actual = historial_atras.pop()
                print(f"Página actual: {pagina_actual}")
            else:
                print("No hay páginas anteriores.")
                
        elif accion == "adelante":
            if historial_adelante:
                historial_atras.append(pagina_actual)
                pagina_actual = historial_adelante.pop()
                print(f"Página actual: {pagina_actual}")
            else:
                print("No hay páginas siguientes.")
                
        else:
            if pagina_actual is not None:
                historial_atras.append(pagina_actual)
                
            pagina_actual = accion
            historial_adelante.clear()
            print(f"Página actual: {pagina_actual}")
            
navegador_web()

# Impresor compartida
def impresora_compartida():
    cola_impresion = []

    while True:
        documento = input(
            "Introduce un documento, 'imprimir' o 'salir': "
        ).strip()

        if documento.lower() == "salir":
            print("Apagando impresora...")
            break

        elif documento.lower() != "imprimir":
            cola_impresion.append(documento)
            print(f"Documento añadido: {documento}")
            print(f"Documentos pendientes: {len(cola_impresion)}")
            
impresora_compartida()

        
        

