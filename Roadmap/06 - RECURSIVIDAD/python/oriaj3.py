"""	
06 - RECURSIVIDAD	
Autor de la solución: Oriaj3	
Teoría:	
Las funciones recursivas son aquellas que se llaman a sí mismas. Son útiles para resolver problemas que pueden ser descompuestos en subproblemas más pequeños,	
y que se resuelven de forma similar. La recursividad es una forma de iteración, y puede ser más sencilla de entender y de implementar en algunos casos.	
#El factorial de un número n se define como el producto de todos los números enteros positivos desde 1 hasta n. 	
n! = 1 * 2 * 3 * ... * n	
#La sucesión de Fibonacci es una sucesión infinita de números naturales, que comienza con los números 0 y 1, y a partir de ellos, cada término es la suma de los dos anteriores.	
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...	
Recuerda:	
Nonlocal: Permite modificar variables no locales en una función anidada.	
Global: Permite modificar variables globales en una función.	
Por defecto, las variables en Python son locales, a menos que se especifique lo contrario, por tanto dentro de una función no se puede modificar una variable que esta afuera.	
"""	

"""	
 * EJERCICIO:	
 * Entiende el concepto de recursividad creando una función recursiva que imprima	
 * números del 100 al 0.	
"""	
# ejercicio 1 variable global	
indice = 0	
def recursiva():	
    global indice	
    print(indice)	
    indice += 1 	
    if indice<101:	
        recursiva()	
recursiva()	

# ejercicio 1 con parametro	
def recursiva1(indice):	
    print(indice)	
    indice += 1 	
    if indice<101:	
        recursiva1(indice)	
number = 0 	
recursiva1(number)	

# ejercicio 1 nonlocal	
def recursiva2():	
    indice = 0	
    def interna():	
        nonlocal indice	
        print(indice)	
        indice += 1 	
        if indice<101:	
            interna()	
    interna()	

recursiva2()	

""""	
* DIFICULTAD EXTRA (opcional):	
 * Utiliza el concepto de recursividad para:	
 * - Calcular el factorial de un número concreto (la función recibe ese número).	
 * - Calcular el valor de un elemento concreto (según su posición) en la 	
 *   sucesión de Fibonacci (la función recibe la posición).	
"""	
# Factorial	
# Se usa indice y resultado como variables no locales para guardar el avance de la recursividad	
def factorial(num: int)-> int:	
    indice = 0	
    resultado = 1	
    def interna():	
        nonlocal indice	
        nonlocal resultado	
        indice += 1 	
        if indice<=num:	
            resultado *= indice	
            interna()	
    interna()	
    return resultado	

# Factoriales del 0 al 9:	
for i in range(10):	
    print(f"El factorial de {i} es igual a {factorial(i)}.")	

# Calcula la sucesion de fibonacci hasta n	
# lista es una lista dónde se guardan los valores de la sucesión	
# n_2, n_1 y n son los tres últimos valores de la sucesión, siendo n el actual, n_1 el anterior y n_2 el anterior a n_1	
def fibonacci_hasta(posicion: int)-> list:	
    lista = []	
    n_2 = 0 	
    n_1 = 1	
    n = 0	
    if posicion==0:	
        return None	
    for i in range(0, posicion):	
        lista.append(n)	
        n_2 = n_1	
        n_1 = n 	
        n = n_1 + n_2	
    return lista	
# Calcula el valor de la sucesión de fibonacci en la posición n	
# n_2, n_1 y n son los tres últimos valores de la sucesión, siendo n el actual, n_1 el anterior y n_2 el anterior a n_1	
# index es el índice actual de la sucesión por la que va la recursividad	
# La función interna() se llama a sí misma hasta que index sea igual a la posición deseada 	
# y en cada llamada se actualizan los valores de n_2, n_1 y n para que se cumpla la sucesión	
def fibonnaci_valor(posicion: int)-> int:	
    n_2 = 0	
    n_1 = 1	
    n = 0	
    index = 1	
    if(posicion==0):	
        return 0	
    def interna():	
        nonlocal n_2	
        nonlocal n_1	
        nonlocal n 	
        nonlocal index	
        if index<=posicion:	
            n_2 = n_1	
            n_1 = n 	
            n = n_1 + n_2	
            index+=1	
            interna()	
    interna()	
    return n	



# Fibonnaci del 0 al 9	
print(f"El fibonacci hasta {10} es igual a {fibonacci_hasta(11)}.")	


# Fibonnaci del 0 al 9	
for i in range(11):	
    print(f"El fibonacci de {i} es igual a {fibonnaci_valor(i)}.")

# Corrección Factorial:
def factorial(number: int)-> int:
    if number == 0:
        return 1
    elif number < 0:
        print("No se puede calcular el factorial de un número negativo")
        return 0
    else:
        return number * factorial(number-1)

#Ejemplo 
print(factorial(5)) # 120

# Corrección Fibonacci:
def fibonacci(number: int)-> int:
    if number < 0: 
        print("No se puede calcular la sucesión de Fibonacci de un número negativo")
        return 0
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2) 