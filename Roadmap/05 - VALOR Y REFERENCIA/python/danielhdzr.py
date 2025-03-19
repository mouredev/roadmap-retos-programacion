# #05 VALOR Y REFERENCIA
#### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

"""
* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 """

def main():
    # Variables por valor (inmutables)
    # al inicio "b" vale lo mismo que "a", pero son variables independientes
    a = 5
    b = a 
    b += 5
    print(a)
    print(b)

    # Variables por referencia (mutables)
    # lista "b" se posiciona en el mismo lugar en memoria que lista "a", ambas son referencia a la misma lista
    a = [1, 2, 3]
    print("Lista a", a)
    b = a
    b.append(4)
    print("Lista a", a)
    print("Lista b", b)

    # Para crear una lista independiente que herede los valores de otra, se debe hacer una copia explicita
    x = [1, 2, 3]
    y = x.copy()
    y.append(4)
    print("Lista x", x)
    print("Lista y", y)

    print()


    # funciones con variables "por valor". Sin retorno
    # Las dos variables "numero1" son independientes (inmutables)
    numero1 = 5
    def func_val(valor):
        numero1 = valor * 3
        print(f"Variable numero1 dentro de la funcion: {numero1}")
    
    func_val(numero1)
    print(f"Variable numero1 fuera de la funcion: {numero1}")

    print()

    # Con retorno
    def func_val_return(valor):
        return valor * 2
    
    print(func_val_return(5) * 2)

    print()

    # funciones con variables "por referencia"
    lista_original = [1, 2, 3]
    lista2 = lista_original.copy()
    
    def func_ref(lista2):
        lista3 = lista2
        lista3.append(4)
        return lista3
    
    lista_nueva = func_ref(lista2)

    print(f"La lista original era: {lista_original}")
    print(f"La lista 2 es: {lista2}")
    print(f"La lista 3 es: {lista_nueva}")
    print(f"La lista 2 se vio modificada al actualizar la lista 3 porque ambas ocupan el mismo sitio en la memoria")
    print(f"Sin embargo la lista original se mantuvo intacta gracias a que se copio mediante el metodo copy()")
        

    '''
    DIFICULTAD EXTRA (opcional):
    * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
    * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
    *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
    *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
    *   Comprueba también que se ha conservado el valor original en las primeras.  
    '''

 
    var1 = 1
    var2 = 2
    # Las variables fuera y dentro de la funcion comparten nombre, pero son variables independientes
    def val_function(var1, var2):
        var1 = 3
        var2  = 4
        return var1, var2
    print(f"Variables 1 y 2 fuera de la funcion: {var1}, {var2}")
    print(f"Variables 1 y 2 dentro de la funcion: {val_function(var1, var2)}")

    print()

    """
    La lista 1 se mantiene igual ya que no se le modifica dentro de la funcion.
    La lista 2 si sufre cambios dentro de la funcion, y estos se manifiestan fuera de la funcion 
    debido a que son exportados mediante el return, y la variable externa que los contiene, al ser usada, 
    modifica el codigo origianl
    """
    lista1 = [1,2,3]
    lista2 = [1,2,3,4]
    def ref_function(par1, par2):
        par1 = lista1
        par2 = lista2
        par2.append(5)
        return par1, par2
    
    resultado = ref_function(lista1, lista2)
    print("Resultados encapsulando la funcion en una variable externa")
    print(f"Lista 1 y 2 fuera de la funcion: {lista1}, {lista2}")
    print(f"Lista 1 y 2 dentro de la funcion: {resultado}")

    print()

    """
    Exactamente el mismo codigo, exceptuando la variable externa que encapsula el return de la funcion.
    El resultado es que la variable que cambia dentro de la funcion, se mantiene intacta fuera de la misma
    """
    lista1 = [1,2,3]
    lista2 = [1,2,3,4]
    def ref_function(par1, par2):
        par1 = lista1
        par2 = lista2
        par2.append(5)
        return par1, par2
    
    print("Resultados sin encapsular la funcion en una variable externa")
    print(f"Lista 1 y 2 fuera de la funcion: {lista1}, {lista2}")
    print(f"Lista 1 y 2 dentro de la funcion: {ref_function(lista1, lista2)}")
    
if __name__=="__main__":
    main()
