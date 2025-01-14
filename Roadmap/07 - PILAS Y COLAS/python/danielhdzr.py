# #07 PILAS Y COLAS
#### Dificultad: Media | Publicación: 12/02/24 | Corrección: 19/02/24

## Ejercicio
''' 
* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 '''
def main():
    """
    Creamos nuestra pila.
    En las pilas o stacks el ultimo elemnto u objeto en entrar es el primero en salir
    """ 
    pila = [1, 2, 3, 4, 5]
    print(f"Pila original: {pila}")
    # Introducimos nuevo objeto a la lista
    pila.append(6)
    print(f"Pila despues de introducirle nuevo objeto: {pila}")
    # Recuperamos un elemento 
    elemento_pila = pila.pop()
    print(f"Elemento recuperado: {elemento_pila}")
    print(f"Pila final: {pila}")

    """
    Creamos nuestra cola.
    En las colas o queues el primer elemnto u objeto en entrar es el primero en salir
    """ 
    cola = [1, 2, 3, 4, 5]
    print(f"Cola original: {cola}")
    cola.append(6)
    print(f"Cola despues de introducirle nuevo objeto: {cola}")
    elemento_cola = cola.pop(0)
    print(f"Elemento recuperado de cola: {elemento_cola}")
    print(f"Cola final: {cola}")

   

    
if __name__=="__main__":
    main()