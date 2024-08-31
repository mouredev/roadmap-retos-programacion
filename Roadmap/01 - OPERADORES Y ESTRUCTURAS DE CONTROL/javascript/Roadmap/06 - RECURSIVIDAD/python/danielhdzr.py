# #06 RECURSIVIDAD
#### Dificultad: Difícil | Publicación: 05/02/24 | Corrección: 12/02/24

## Ejercicio
'''
* EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición). 
 '''

def main():
    '''
    La recursion es como una muneca Matryoshka rusa, se repite una y otra vez hasta llegar al final (la muneca mas pequena) ese es nuestro base case.
    El base case o base condition es la condicion para finalizar la funcion.
    '''
    # Del 100 al 0
    def recursion1(n):
        # Lo primero que hace la funcion en su ciclo es imprimir n
        print(n)
        # Caso base o base case. Aqui termina la secuencia 
        if n == 0:
            print("Base case")
            return n
        # Caso de recursion o recursion case
        else: 
            '''
            Llama a la funcion de nuevo, 
            se repite el ciclo de la funcion con el nuevo valor de n
            '''
            return recursion1(n - 1)
    
    recursion1(100)
    print()

    # Otra forma de hacerlo
    # Del 100 al 0
    def recursion2(n):
        # Caso base o base case. Aqui termina la secuencia 
        if n == 100:
            print(f"Base case or base condition {n}")
            return n
        # Caso de recursion o recursion case
        else: 
            recursion2(n + 1)
        print(n)
    recursion2(0)

    print()

    # Del 0 al 100
    def recursion3(n):
        # Caso base o base case. Aqui termina la secuencia 
        if n == 0:
            print(f"Base case or base condition {n}")
            return n
        # Caso de recursion o recursion case
        else: 
            recursion3(n - 1)
        print(n)
    recursion3(100)

    print()


    # def evenNumb(n):
    #     print(n)
    #     if n == 2:
    #         return n
    #     else: 
    #         return evenNumb(n - 2)
        
    
    # evenNumb(8)

if __name__=="__main__":
    main()
