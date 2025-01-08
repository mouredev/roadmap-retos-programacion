# 07 Pilas y Colas

# Ejercicio

# Ejercicio pilas
pila = [1, 2, 3]

# metodo append
pila.append(4)
pila.append(5)
print(pila[len(pila)-1])
print(
    f'Mi pila tiene los siguientes elementos {pila} y su longitud es de {len(pila)}')

# metodo pop
pila.pop()
del pila[len(pila)-1]
print(
    f'Mi pila tiene los siguientes elementos {pila} y su longitud es de {len(pila)}')

# Ejercicio colas
cola = [1, 2, 3]

# metodo append
cola.append(4)
cola.append(5)
print(cola[0])
print(
    f'Mi cola tiene los siguientes elementos {cola} y su longitud es de {len(cola)}')

# metodo pop
cola.pop(0)
del cola[0]
print(
    f'Mi cola tiene los siguientes elementos {cola} y su longitud es de {len(cola)}')

# DIFICULTAD EXTRA
# Navegador web con implementación de pila

historial = list()


def abrir_web():
    url = input(f'Ingresa una nueva url: ')
    historial.append(url)
    return print(f"Página abierta: {url}")


def atras():
    web_anterior = historial.pop()
    web_actual = historial[-1]
    return print(f"Retrocediendo a: {web_actual}")


def adelante():
    web_adelante = input(f'Ingresa una nueva url:')
    historial.append(web_adelante)
    return print(f"Avanzando a: {web_adelante}")


def ver_historial():
    return print(f"Historial: {historial}")

# Implementaciòn
# abrir_web()
# abrir_web()
# abrir_web()
# abrir_web()
# atras()
# atras()
# adelante()
# ver_historial()

# Impresora


impresion = list()


def nuevo_doc():
    doc = input(f'Agregue un archivo a la impresora: ')
    impresion.append(doc)
    return print(f"Se agregó el siguiente archivo a la cola de impresión: {doc}")


def imprimir():
    if len(impresion) > 0:
        se_imprime = impresion.pop(0)
        return print(f"Imprimiendo: {se_imprime}")
    else:
        print("No hay documentos para imprimir")


def ver_historial_impresion():
    return print(f"Documentos en cola de impresión: {impresion}")


# implementacion
nuevo_doc()
nuevo_doc()
nuevo_doc()
ver_historial_impresion()
imprimir()
ver_historial_impresion()
