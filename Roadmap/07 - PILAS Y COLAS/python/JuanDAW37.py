"""
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
 *   historial compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

#Pila (Last Input First Output, LIFO)
pila = []

pila.append('A')
pila.append('B')
pila.append('C')
print(f'Pila entera: {pila}')

elemento = pila.pop(len(pila) - 1) #Extraigo el último elemento y lo elimino de la lista
print(f'Último elemento: {elemento}')
print(f'Pila una vez extraído el último elemento: {pila}')

#Cola (First Input First Output)
cola = []
cola.append('A')
cola.append('B')
cola.append('C')
print(f'Cola entera: {cola}')

elemento = cola[0] #Extraigo el primer elemento y lo elimino de la lista. El cero siempre será el primer elemento
print(f'Primer elemento: {elemento}')
del cola[0] #Elimino el primer elemento de la cola. Se puede hacer de una sola vez con elemento = cola.pop(0)
print(f'Cola una vez extraído el primer elemento: {cola}')

# Extra
# Simulación de navegador web, pila LIFO
def navegador_web():
    historial = []
    navegacion = []
    while True:
        comando = input('Introduce una acción (adelante, atrás, URL o salir: ')
        if comando == "salir":
            break            
        elif comando == "adelante":
            pass
        elif comando == "atrás":
            if len(historial) > 0:
                try:
                    historial.pop()                                   
                except Exception:
                    print('No hay más páginas para ir atrás')
        else:
            historial.append(comando)            
            navegacion.append(comando)
            print(f'Página actual: {historial[len(historial) - 1]}')
        if len(historial) > 0:
            print(f'Posición {historial[len(historial)-1]}')                                          
        else:
            print('No hay páginas en el historial')
    return navegacion

print(navegador_web())

# Simulación de cola de impresión compartida, cola FIFO
def impresora():
    cola = []
    while True:
        comando = input('Introduce un nombre de documento o una acción (imprimir, salir): ')
        if comando == 'salir':
            break
        elif comando == 'imprimir':
            if len(cola) > 0:
                print(f'Imprimiendo documento {cola.pop(0)}')
        else:
            cola.append(comando)
        print(f'Documentos en cola: {cola}')
        
impresora()