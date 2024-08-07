### Operaciones aritmeticas en Python ###

print("Operaciones aritmeticas en Python")
print()
operando_1 = 24 #Asignación del valor 24 a la variable operando_1
operando_2 = 2
print(f"""Dados dos valores {operando_1} y {operando_2}, siendo estos bool, int, float o complex.
Tener en cuenta al realizar operaciones aritmeticas True equivale al valor 1 y False al 0. 
Recordar tambien que al igual de cuando se trabaja con el conjunto de los números reales o complejos
la division por 0 no esta definida""")
print("En python podemos sumarlos:" , operando_1 + operando_2)
print("Restarlos: ", operando_1 - operando_2)
print("Multiplicarlos: ", operando_1 * operando_2)
print("Dividirlos: ", operando_1 / operando_2)
print("Dividirlos y truncar los todos decimales del resultado: ", operando_1 // operando_2)
print("Calcular el módulo (si ninguno de los operandos es de tipo complex): ", operando_1 % operando_2)
print(f"Tambien se puede elevar un número a otro. Para por ejemplo calcular {operando_1} elevado a {operando_2}, obteniendo {operando_1**operando_2}")
print()
operando_1 = "Monty "
operando_2 = "Python"
print(f"En el caso de que ambos valores sean del tipo string, siendo estos: '{operando_1}',  '{operando_2}'")
print(f"La operación '+' los concatena y crea con el resultado un nuevo string: '{operando_1 + operando_2}'")
print("""De forma similar si ambos operandos son de tipo list o de tipo tuple, 
se obtendrá como resultado una nueva lista/tupla con los elementos del primer operando y del segundo, en ese orden.""")
operando_1 = [1, 2, 3]
operando_2 = [30, 20, 10]
print(f"Por ejemplo, para los operandos {operando_1} y {operando_2} se obtiene:", operando_1 + operando_2)
print()
print(f"""En el caso de que tengamos un objeto int multiplicando un operador de tipo lista, tupla o string.
El resultado es otro iterable del mismo tipo pero que contiene tantas copias del contanido como valor tenga el
objeto int. Examplos: """)
operando_1 = 2
operando_2 = "Hola"
print(f"Para los operandos {operando_1} y '{operando_2}', resultado: '{operando_1*operando_2}'")
operando_1 = 4
operando_2 = [2,3]
print(f"Para los operandos {operando_1} y {operando_2}, resultado: {operando_1*operando_2}")
operando_1 = 3
operando_2 = (2,"cereza")
print(f"Para los operandos {operando_1} y {operando_2}, resultado: {operando_1*operando_2}")
"Se puede observar que si el objeto de tipo int es negativo o igual a cero, el resultado es una lista, tupla o string vacío"
operando_1 = 0
print(f"Para los operandos {operando_1} y {operando_2}, resultado: {operando_1*operando_2}")
operando_1 = -6
print(f"Para los operandos {operando_1} y {operando_2}, resultado: {operando_1*operando_2}")
print("Estas operaciones no se pueden realizar con objetos del tipo set o dict, porque dichos tipos no admiten copias de sus elementos")
print()

### Operadores lógicos ###

print("""Recordar que en Python dado un iterable si este no esta vacío se evalua como verdadero (True) y si esta vacío como falso (False).
Si se trata de un número, se evalua como verdadero (True) si es diferente a cero, en caso contrario se evalua como falso (False)""")
operando_1 = True
operando_2 = False
print(f"""Negación lógica, ejemplo: para el operando_1 = {operando_1} su negación se escribe 'not operando_1'
y es igual a  {not operando_1}""")
print(f"""Or, ejemplo: Para operando_1 = {operando_1} y operando_2 = {operando_2} la operación or se escribe
'operando_1 or operando_2' y da como resultado {operando_1 or operando_2}""")
print(f"""And, ejemplo: Para operando_1 = {operando_1} y operando_2 = {operando_2} la operación and se escribe
'operando_1 and operando_2' y da como resultado {operando_1 and operando_2}""")

### Operadores de comparación ###
print("""Si se los operandos son int o float, se puede realizar las siguientes comparaciones: """)
operando_1 = 4
operando_2 = 4.5
print(f"es igual? Ejemplo: '{operando_1} == {operando_2}', da como resultado {operando_1 == operando_2}")
print(f"es diferente? Ejemplo: '{operando_1} != {operando_2}', da como resultado {operando_1 != operando_2}")
print(f"es menor o igual? Ejemplo: '{operando_1} <= {operando_2}', da como resultado {operando_1 <= operando_2}")
print(f"es mayor o igual? Ejemplo: '{operando_1} >= {operando_2}', da como resultado {operando_1 >= operando_2}")
print(f"es menor? Ejemplo: '{operando_1} < {operando_2}', da como resultado {operando_1 < operando_2}")
print(f"es mayor? Ejemplo: '{operando_1} > {operando_2}', da como resultado {operando_1 > operando_2}")
print("Si los operandos son ambos del tipo complex o dicts solo las operaciones de comparación == o != estan definidas")
print("""Si los operandos son strings, lists, tuples, sets. Todas las operaciones de comparación estan definidas. 
El criterio de comparación varía dependiendo de que contengan.
En el caso de los strings, que contienen carácteres, se realiza una comparación de los códigos ascii cada carácter uno a uno de ambos string
para determinar el resultado.
De forma similar cuando se comparan listas o tuplas, se compara el primer elemento de ambas listas/tuplas, luego el segundo de ambas
y se continua así hasta que terminar una de las listas/tuplas, determinando finalmente el resultado de la comparación""")
print("""En el caso de que los operandos sean sets: 
< : es subconjunto de
> : contiene
>= : contiene o es igual a
<= : es subconjunto de o es igual a
Algunos ejemplos en este caso:""")

operando_1 = {2, 4}
operando_2 = {1, 2, 3, 4}
print(f"son iguales? Ejemplo: {operando_1} == {operando_2}, da como resultado {operando_1 == operando_2}")
print(f"son diferentes? Ejemplo: {operando_1} != {operando_2}, da como resultado {operando_1 != operando_2}")
print(f"es subconjunto o es igual? Ejemplo: {operando_1} <= {operando_2}, da como resultado {operando_1 <= operando_2}")
print(f"contiene o es igual? Ejemplo: {operando_1} >= {operando_2}, da como resultado {operando_1 >= operando_2}")
print(f"es subconjunto y es diferente? Ejemplo: {operando_1} < {operando_2}, da como resultado {operando_1 < operando_2}")
print(f"contiene y es diferente? Ejemplo: {operando_1} > {operando_2}, da como resultado {operando_1 > operando_2}")
print()
### Asignaciones ###
operando_1 = {2, 4, 6, 8, 10}
operando_2 = 4
print("Existen diferentes formas de asignar valores a variables en Python")
# =
print(f"Utilizando =, se asigna un objeto a una variable. Ejemplo: 'even_numbers_to_10 = {operando_1}'")
# +=
operando_1 = 10
print(f"""Utilizando '<variable> += <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> + <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 += operando_2
print(f"'operando_1 += operando_2' da como resultado operando_1 = {operando_1}")
# -=
print(f"""Utilizando '<variable> -= <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> - <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 -= operando_2
print(f"'operando_1 -= operando_2' da como resultado operando_1 = {operando_1}")
# *=
print(f"""Utilizando '<variable> *= <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> * <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 *= operando_2
print(f"'operando_1 *= operando_2' da como resultado operando_1 = {operando_1}")
# /=
print(f"""Utilizando '<variable> /= <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> / <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 /= operando_2
print(f"'operando_1 /= operando_2' da como resultado operando_1 = {operando_1}")
# //=
print(f"""Utilizando '<variable> //= <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> // <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 //= operando_2
print(f"'operando_1 //= operando_2' da como resultado operando_1 = {operando_1}")
# %=
print(f"""Utilizando '<variable> %= <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> % <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 %= operando_2
print(f"'operando_1 %= operando_2' da como resultado operando_1 = {operando_1}")
# **=
print(f"""Utilizando '<variable> **= <objeto>', se obtiene un resultado equivalente a '<variable> = <variable> ** <objeto>'. 
Ejemplo: Si operando_1 = {operando_1} y operando_2 = {operando_2}""")
operando_1 **= operando_2
print(f"'operando_1 **= operando_2' da como resultado operando_1 = {operando_1}")
print("""Notar que para utilizar un tipo de asignación que incluya una operación aritmetica, esta tiene que estar definida
para el objeto guardado en la variable y el objeto que se asigna""")
print("""Tambien se puede realizar una asignación doble, triple, etc en una sola línea (aunque seguramente no siempre
sea recomendable de cara a facilitar la lectura). Utilizando la sintaxis que se muestra en el siguiente ejemplo: 
Dados dos objetos y dos variables de la siguiente forma: 
'smallest_ramanujan_n, fav_dinosaur = 1729, "Triceratops"' de forma que después de la
asignación la variable smallest_ramanujan_n = 1729 y fav_dinosaur = "Triceratops" """)
print()

### Identidad y Pertenencia ###
print("En Python existe una operación que nos permite saber si dos objetos son el mismo (estan guardados en la misma posición de memoria):")
print("Se trata de la operación 'is' y de su contraria 'is not'")
operando_1 = [1,2,3]
operando_2 = [1,2,3]
print(f"Ejemplo: Siendo operando_1 = {operando_1} y operando_2 = {operando_2}, 'operando_1 is operando_2' da como resultado {operando_1 is operando_2}")
print(f"Ejemplo: Siendo operando_1 = {operando_1} y operando_2 = {operando_2}, 'operando_1 is not operando_2' da como resultado {operando_1 is not operando_2}")
print(f"""Notar que el hecho de que ambos valores coincidan (que el resultado de la operación == sea True), 
no significa que se trate del mismo objeto""")
operando_1 = "Hello"
operando_2 = "Hello"
print(f"""También se puede observar que por cuestiones de implementación del lenguaje, 
en el caso de los string que los valores coincidan significa que se trata del mismo objeto en algunos casos. 
Ejemplo: Siendo operando_1 = "{operando_1}" y operando_2 = "{operando_2}", 
'operando_1 is operando_2' da como resultado {operando_1 is operando_2}""")
operando_2 = "He"
operando_3 = "llo"
print(f"""Esto parece que sucede siempre y cuando el string no sea el resultado de una operación
y se haya inicializado como tal por ejemplo: 'operador_1 = "Hello"' 'operador_2 = "He"' y 'operador_3 = "llo"'
'operador_1 is (operador_2 + operador_3)' da como resultado {operando_1 is (operando_2 + operando_3)}""")
print("""Existe además los operadores de pertenencia, 'in' y 'not in', que sirven para saber
si un objeto pertenece a un iterable (objeto que se puede iterar, ejemplo: lists, tuples, dictionaries, sets, strings) """)
operando_1 = "Girona"
operando_2 = ["Barcelona", "LLeida", "Girona", "Tarragona"]
print(f"""Ejemplo: Siendo operando_1 = "{operando_1}" y operando_2 = {operando_2}, 'operando_1 in operando_2' da como resultado {operando_1 in operando_2}
Ejemplo: Siendo operando_1 = "{operando_1}" y operando_2 = {operando_2}, 'operando_1 not in operando_2' da como resultado {operando_1 not in operando_2}""")
print()

### Operaciones con bits ###

print("Hay ciertas operaciones que se realizan bit a bit. Estas se pueden realizar siempre y cuando los operandos sean ambos de tipo int")
operando_1 = 4
operando_2 = 3
# &
print(f"""Conjunción (and) bit a bit, con el operador &: 
Siendo el operando_1 = {operando_1} y operando_2 = {operando_2}, el resultado
de 'operando_1 & operando_2' es {operando_1 & operando_2}""")
# |
print(f"""Disyunción (or) bit a bit, con el operador |: 
Siendo el operando_1 = {operando_1} y operando_2 = {operando_2}, el resultado
de 'operando_1 | operando_2' es {operando_1 | operando_2}""")
# ~
print(f"""Negación bit a bit, en el operador ~:
Siendo el operando_1 = {operando_1}, el resultado
de la operación '~operando_1' es {~operando_1}""")
# ^
print(f"""Disyunción exclusiva (xor) bit a bit, con el operador ^: 
Siendo el operando_1 = {operando_1} y operando_2 = {operando_2}, el resultado
de 'operando_1 ^ operando_2' es {operando_1 ^ operando_2}""")
# >>
print(f"""Desplazamiento bit a bit a la derecha, con el operador >>: 
Siendo el operando_1 = {operando_1} y operando_2 = {operando_2}, el resultado
de 'operando_1 >> operando_2' es {operando_1 >> operando_2}""")
# <<
print(f"""Desplazamiento bit a bit a la izquierda, con el operador <<: 
Siendo el operando_1 = {operando_1} y operando_2 = {operando_2}, el resultado
de 'operando_1 << operando_2' es {operando_1 << operando_2}""")
print()

### Control de flujo: Condicionales ###
print("Ejemplo de control de flujo: estructura condicional if/elif/else")
n = 50
if(not n % 2): # Si el resultado de evaluar la condición es cierto, se ejecutará el código con una tabulación extra respecto del if se encuentra inmediatamente abajo
    print("El número es par")
elif(not n % 3): # Opcional, si la condición es verdadera y las anteriores no lo han sido se imprimirá "El número es múltiplo de tres"
    print("El número es múltiplo de tres")
else: # Opcional, si todas las condiciones anteriores son incorrectas se ejecutará el código dentro del scope de else
    print("El número es impar y no es múltiplo de tres")

print()

### Control de flujo: Bucles ###

print("Ejemplo de control de flujo: bucle for")
# En cada iteración i tomará uno de los objetos del iterable
# hasta que se hayan recorrido todos los elementos del iterable (range(1, 101))
for i in range(1, 101): 
    print(i)
else: #Si el bucle se completa sin excepciones o un break se ejecuta el código en el scope del else
    print("Los números se imprimieron sin percances")

print("Ejemplo de control de flujo: bucle while")
import random
resultado_lanzamiento = random.randint(1, 6) #Genera un número entero dentro del intervalo de 1 a 6 incluyendo ambos
while(resultado_lanzamiento != 6): #El código se repite hasta que la condición se cumpla
    print("No has sacado un 6")
    resultado_lanzamiento = random.randint(1, 6)
else: #Si el bucle se completa sin excepciones o un break se ejecuta el código en el scope del else
    print("Has sacado un 6")

print()

### Control de excepciones ###

print("Ejemplo 1 de control de excepciones")
n = 10
try:
    # Se intenta ejecutar este código y en caso de que se produzca una excepción,
    # se pasará a ejecutar el código dentro del scope the except
    if(n != 9):
        raise ValueError("El número tiene que ser igual a 9") # Se lanza un error del tipo ValueError con el mensaje pasado como argumento
    print("El número es igual a 9")
except ValueError as e: #Si dentro del código en el scope de try, se ha producido una excepción esta se captura
    print(e) #Se imprime la excepción capturada
    #raise ValueError("Valor incorrecto!")
else: #Este código se ejecuta si ninguna excepción se produjo (opcional)
    print("No se ha producido ninguna excepción")
finally: #Esta código se ejecuta en cualquier caso incluso si dentro del except se lanza una excepción (opcional)
    print("Se continua ejecutando el código")

print()

print("Ejemplo 2 de control de excepciones")
n_input = "7"
try:
    n_input = n_input + 5
    print(n_input)
except Exception: #forma más general posible de capturar una excepcion
    #Pero en este caso no se guarda el valor de la excepción
    #Lo cúal dificulta saber porque el programa ha fallado
    print("El programa ha fallado")

### DIFICULTAD EXTRA: EJERCICIO ###
def ejercicio_extra():
    min_n = 11
    max_n = 55
    for n in range(min_n, max_n + 1):
        if( (n % 2 == 0) and (n % 3 != 0) and (n != 16)):
            print(n)

print("Resultado ejercicio extra: ")
ejercicio_extra()
