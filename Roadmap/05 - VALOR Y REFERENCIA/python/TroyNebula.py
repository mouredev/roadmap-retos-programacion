'''
 EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)'''

# Las asignaciones dependen de los tipos de datos:
# Los tipos simples e inmutables como tuplas, enteros, flotantes y cadenas se asignan "por valor"
# Los tipos compuestos y mutables como listas, conjuntos/sets y diccionarios se asignan "por referencia".


# Asignación por Valor -----------------------------------------------------------------------
# Se crea una copia local de la variable independiente del valor original. Cambios en la variable original no afectan.

# Asignación por valor con tipos simples (entero)
x = 5
y = x  # Se asigna el valor de x a y

y = 10 # Modificamos y, pero no afectará a x

print(x)  # Salida: 5
print(y)  # Salida: 10

# Asignación con ej de función con variables que se les pasan "por valor" -----------------------------------------------------------------------

x = 10
def funcion(entrada):
    entrada = 0   # entrada almacena una copia local de x
    print(entrada)  #Salida: 0
    print(x)        #Salida: 10 dentro de la función sigue siendo 10 lo que cambió fue la variable anterior
funcion(x)

print(x)    #Salida: 10

# Asignación por valor con tuplas -----------------------------------------------------------------------
# Las tuplas al ser inmutables se comportarn como si fueran por valor:
tupla_original = (1, 2, 3)
tupla_copia = tupla_original  # Asignación por valor

tupla_copia += (4,) # Modificar la tupla_copia no afectará a tupla_original ya que las tuplas son inmutables
# La coma después del 4 es necesaria para diferenciarla de simplemente un paréntesis que rodea un valor, 
# ya que (4) sin la coma se interpretaría como un valor sin formar una tupla.
print(tupla_original)  # Salida: (1, 2, 3)
print(tupla_copia)     # Salida: (1, 2, 3, 4)

# Asignación con ej de función con variables que se les pasan "por valor" -----------------------------------------------------------------------

tupla_original = (1, 2, 3)  # Asignación por valor con tuplas

def modificar_tupla(tupla):
    tupla = tupla + (4,)  # Se crea una nueva tupla y se asigna a la variable local 'tupla'
    print("Dentro de la función:", tupla) # la nueva tupla creada dentro de la función no afecta la tupla original fuera de la función.
    #Salida: Dentro de la función: (1, 2, 3, 4)

modificar_tupla(tupla_original)
print("Fuera de la función:", tupla_original)  #Salida: Fuera de la función: (1, 2, 3)

# Asignación por Referencia -----------------------------------------------------------------------
# La variable apunta al mismo objeto en la memoria. Cambios en una variable afectan tanto dentro como fuera de la función
# Se actúa directamente sobre la variable pasada, por lo que las modificaciones afectarán a la variable original

lista1 = [1, 2, 3]
lista2 = lista1     # Se asigna la referencia de lista1 a lista2

lista2.append(4)    # Modificamos lista2, y esto afectará a lista1

print("lista1:", lista1)  # Salida: [1, 2, 3, 4]
print("lista2:", lista2)  # Salida: [1, 2, 3, 4]

# otro ejemplo con una lista -----------------------------------------------------------------------

original = [1, 2, 3]        # a original le asigno [1,2,3]  ---Se le asigna, no es que valga, son objetos---
copy = original             # original y copy son [1,2,3]
	
original[0] = 99            # modifico original [99,2,3]

original = [4, 5, 6]        # asigno un nuevo objeto a original, es [4,5,6]
print( original)            # [4,5,6]
print (copy)                # [99,2,3]

# Asignación con ej de función con variables que se les pasan "por referencia" -----------------------------------------------------------------------

x = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)

funcion(x)
print(x)    # Salida: [10, 20, 30, 40]


# Ojo, es distinto reasignar que modificar -----------------------------------------------------------------------
# Son distintos objetos, y no cambia la original porque no estoy modificando la variable, sino reasignándola, lo que crea una nueva temporal
x = [10, 20, 30]
def funcion(entrada):
    entrada = []

funcion(x)
print(x)    # Salida: [10, 20, 30]


# Función id() -----------------------------------------------------------------------
# Esta función nos devuelve un identificador único para cada objeto. 
# Volviendo al primer ejemplo podemos ver como los objetos a los que “apuntan” x y entrada son distintos

# id con ejemplo de variable por valor -----------------------------------------------------------------------
x = 10
print("id variable valor: ", id(x)) # 140724755286744
def funcion(entrada):
    entrada = 0
    print(id(entrada)) # 140724755286744

funcion(x)  #Salida: 10

# id con ejemplo de variable por referencia -----------------------------------------------------------------------
x = [10, 20, 30]
print("id variable ref: ", id(x)) # 1737715235264
def funcion(entrada):
    entrada.append(40)
    print(id(entrada)) # 1737715235264

funcion(x)  # Salida: [10, 20, 30, 40]

# id con el último ejemplo -----------------------------------------------------------------------
# Se crea una nueva lista en memoria y asigna la variable entrada a esa nueva lista
# el id de entrada dentro de la función será diferente al id de x fuera de la función.

x = [10, 20, 30]
print (id(x))   #1737715235200
def funcion(entrada):
    entrada = []
    print (id(entrada)) #1737715235264

funcion(x)
print(x)    # Salida: [10, 20, 30]

'''
 DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.'''

print()
variable_valor1 = 1             # entero
variable_valor2 = "Moure"       # cadena/string

variable_referencia1 = [30, 60, 90]             # lista
variable_referencia2 = {True, "conjunto", 0}    # set

def intercambiar_variables_valor(valor1, valor2):
    valor1, valor2 = valor2, valor1
    print(f"Valor1 que era 1, dentro la función: {valor1}")
    print(f"Valor2 que era 'Moure', dentro  la función: {valor2}")
    return valor1, valor2

def intercambiar_variables_referencia(referencia1, referencia2):
    referencia1, referencia2 = referencia2, referencia1
    return referencia1, referencia2

# llamo a las funciones
resultado_valor1, resultado_valor2 = intercambiar_variables_valor(variable_valor1, variable_valor2)
resultado_referencia1, resultado_referencia2 = intercambiar_variables_referencia(variable_referencia1, variable_referencia2)

# imprimo resultados
print()
print("Ya sea valor o referencia invierte los valores")
print(f"Originales Valor: {variable_valor1}, {variable_valor2}")
print(f"Después de pasar por la funcion: {resultado_valor1}, {resultado_valor2}")
print(f"Originales Ref: {variable_referencia1}, {variable_referencia2}")
print(f"Después de pasar por la funcion: {resultado_referencia1}, {resultado_referencia2}")


# pruebo otra función, asigno fuera de función -----------------------------------------------------------------------
print()
print("Es una lista, es mutable, y sería por referencia, modifica las dos")
lista1 = [1, 2, 3]
print ("Lista1 original:", lista1)
lista2 = lista1     
print("Se asigna la referencia de lista1 a lista2 fuera de función")
print("Lista2 original:", lista2)
num=4

def añadir_número(lista_temp):
    lista_temp.append(num) 
    print("Lista temporal dentro de la función:", lista_temp)

añadir_número(lista2)
print("Añado el número 4 a la lista2 con la función añadir_numero...")
print("Lista1:", lista1)
print("Lista2:", lista2)
print("Se han mofificado las dos y sólo pasé la 2 por la función de añadir")

# rescato la lista anterior que invertí: variable_referencia1 = [30, 60, 90]  
# otra prueba, asigno dentro de la función -----------------------------------------------------------------------
print()
print("Pruebo a asignar dentro de la función la ref de la1 como ref de la 2")
print("Variable original ref1:", variable_referencia1)
print("Variable original ref2:", variable_referencia2)
def asignar_mismas_variables_ref(vr1, vr2):
    vr2= vr1
    return vr1, vr2

nueva_vr1, nueva_vr2= asignar_mismas_variables_ref(variable_referencia1, variable_referencia2)
print("Nueva Variable ref1:", nueva_vr1)
print("Nueva Variable ref2:", nueva_vr2)


# Otra prueba de Modificando por referencia -----------------------------------------------------------------------
print()
numeros = [1,2,3]
letras = ["a","b","c"]
print("originales antes función:",numeros, letras)

def modifica_numyletras(valor1, valor2):
    numeros.append(valor1)
    letras.append(valor2)
    return(numeros, letras)

numeros2 , letras2 = modifica_numyletras(valor1=4, valor2="d")

print("Con añaddido:", numeros2, letras2)
