"""
EJERCICIO: ESTRUCTURAS DE DATOS
 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 - Utiliza operaciones de inserción, borrado, actualización y ordenación.
   DIFICULTAD EXTRA (opcional):
  Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.
 """

# 1. Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.

"""
Aqui entran los tipos de datos primitivos: Int, Flt, Str y Bool. Pero, no se profundisara en estos porque ya los vimos en un reto anterior.
"""

# Numeros complejos:
"""
Los numeros complejos en python es una operacion de numeros reales y numeros imaginarios su uso puede llegar a ser complejo, 
tiene usos matematicos y fisicos pues son utiles para describir ondas electromagnéticas y la corriente electrica.
"""

print(type(x := 3 + 1j)) # Complex

# Se pueden hacer operaciones con los numeros complejos algunas son igual que trabajar con numeros reales pero en otras se siguen
# otro procedimiento. Pero, estas son solo operaciones simples para hacer uso mas profundo se necesita una libreria (cmath)

# Listas:
"""
Son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinamicas esto quiere decir que sus datos pueden ser
modificados y que se puede añadir o eliminar informacion tambien son anidadas osea que se pueden meter unas dentro de otras y son ordenadas
pues mantienen el orden en el que han sido definidas.
"""

# Las listas se pueden definir usando los corchetes [] o usando el comando list().

a = ["Franz", 19, "Python"]
print(a) # ['Franz', 19, 'Python']

b = list("1234")
print(b) # ['1', '2', '3', '4']

print(type(a)) # List
print(type(b)) # List

# Como se puede ver los datos se separan con comas y la forma de llamarlos es la siguiente.

print(a[1]) # 19

# El orden de una lista empieza desde el 0, en este ejemplo se tienen 3 datos el primero sera la posicion 0 despues 1 y asi.
# Tambien se pueden llamar usandos los datos negativos por ejemplo -1 llamara al ultimo aqui por obvias razones no se empieza de 0
# Pero la logica es la misma haciendo que -2 llame al penultimo y asi.

# Para modificar una de los datos de una lista es tan simple como hacer lo siguiente:

a[1] = 20
print(a) #['Franz', 20, 'Python'] 

# Como se puede observar el valor que era 19 cambio a 20 asi de facil es hacer un cambio.

# Elminar datos de una lista:

c = list("abcdefg") 
print(c) #['a', 'b', 'c', 'd', 'e', 'f', 'g']

# del elimina el dato que se encuentre en la posicion definida.

del c[1]
print(c) #['a', 'c', 'd', 'e', 'f', 'g']

# Listas anidadas osea que podemos definir listas dentro de listas.

d = ['1', '2', '3', a, b]
print(d) #['1', '2', '3', ['Franz', 20, 'Python'], ['1', '2', '3', '4']]

# Esto se puede hacer indefinidamente y para ingresar a esos datos anidados solo tenemos que usar tantos corchetes como los necesitemos.

print(d[3][0]) # Franz

# y asi podemos ingresar a los datos anidados.

# Tambien podemos sacar datos usando un rago en las posiciones y para definir el rango se usan los corchetes y los dos puntos.

print(d[0:4]) # ['1', '2', '3', ['Franz', 20, 'Python']]

# Como ya es constumbre en el leguaje cuando definimos un rango tomar el primero pero no el ultima posicion definida.
# Esto tambien nos sirve para cambiar un rago de datos en las listas usando el = como antes.

# Las listas se pueden combinar con algunois operadores:

print(d) # ['1', '2', '3', ['Franz', 20, 'Python'], ['1', '2', '3', '4']]
d += [7, 8, 9]
print(d) # ['1', '2', '3', ['Franz', 20, 'Python'], ['1', '2', '3', '4'], 7, 8, 9]

# Otro uso muy util que podemos hacer con las listas es definir muchas variables con su ayuda.

e = [1, 2, 3]
x , y , z = e
print(x, y , z) # 1 2 3

# Obviamente respeta el orden para definirlos.

# La iteracion con listas es facil, mas que en la mayoria de lenguajes.

for index, dato in enumerate(e):
    print(index, dato)
    # 0 1
    # 1 2
    # 2 3

# Con enumerate() podemos añadir el valor de la posicion y el dato en estas iteraciones.

# Tambien podemos iterar dos listas a la vez.

for i1, i2 in zip(a, b):
    print(i1, i2)
    # 0 1
    # 1 2
    # 2 3

# La ireacion termina cuando se terminan los datos en una de las listas.

# Longitud de una lista.
# Con el comando len() podemos obener el numero de datos que tiene una lista.

g = ['a', 'b', 'c']
print(len(g)) # 3

# Es una herramienta util.

# Elemento append() nos ayuda a añadir un dato al final de la lista.

h = [1, 2 ,3]
h.append(4)
print(h) # [1, 2, 3, 4]

# Como vemos su uso va llamando a la lista y añadiendo .append() mientras que dentro del parentesis se ingresa el dato.

# Elemento extend() sirve para añadir una lista a otroa lista.

j = [1, 2 ,3]
j.extend([4, 5])
print(j) # [1, 2, 3, 4, 5]

# Una diferencia con append() es que extend() añade los datos de la lista y append() lo añade como lista.

# Elemento insert() añade un dato pero en la posicion que se define.

k = list("1235678") 
print(k) # ['1', '2', '3', '5', '6', '7', '8']
k.insert(3,4)
print(k) # ['1', '2', '3', 4, '5', '6', '7', '8']

# Como vemos primero se ingresa la posicion y despues de la coma el dato que se desea añadir.

# Elemento remove().

print(k) # ['1', '2', '3', 4, '5', '6', '7', '8']
k.remove('8')
print(k) # ['1', '2', '3', 4, '5', '6', '7']

# Elmina el elemento ingresado dentro del parentesis obviamente tiene que estar en el mismo tipo de dato para poder ser identificado.

# Elemento pop()

print(k) # ['1', '2', '3', 4, '5', '6', '7']
k.pop()
print(k) # ['1', '2', '3', 4, '5', '6']

# pop() elmina el dato que este en la posicion indicada por defecto esta en -1 la posicion.

# Elemento reverse().

l = [1, 2, 3, 4, 5]
l.reverse()
print(l) # [5, 4, 3, 2, 1]

# Recordemos que las listas conservan el orden en el que se han definido los datos reverse() invierte el orden en el que se han definido.

# Elemento sort().

m = [1, 2 ,7 ,4, 6, 5, 3]
m.sort()
print(m)

# El elemto sort() ordena la lista siempre que esta se pueda ordenar de menor a mayor.
# Tambien se puede hacer que la ordenen de mayor a menor si ponemos reverse=True en los parametros.

# index().

n = list("ABCDEFGHIJK")
print(n) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
print(n.index('A')) # 0

# El elemento index nos permite buscar un dato dentro de una lista y nos devuelve la posicion en la que se encuentras ese dato.

# Sets:
"""
Los sets tambien almacenan datos, pero poseen diferencias con respecto a las listas como: En los sets no se pueden repetir los datos,
otra diferencia es que no mantienen el orden de cuando son definidas y sus elementos son inmutables lo que significa que sus datos
no pueden ser modificados.
"""

# Para definir los sets podemos usar las llaves {} o el comando set() y pasarle un tipo iterable como con el comando list().

s = set(a) # "a" es una lista que se creo antes. 
print(s) # {'Python', 20, 'Franz'}
s0 = {1, 4, 3, 2, 5}
print(s0) # {1, 2, 3, 4, 5}

print(type(s)) # <class 'set'>
print(type(s0)) # <class 'set'>

# Como podemos ver las llaves definen un set y tambien podemos ver que no conservan el orden con el que son definidos.

# Como dije antes si intentamos modifocar uno de sus datos como con las listas.
# s[0] = 1 TypeError: 'set' object does not support item assignment.
#  Nos dara ese error.

# Tampoco podemos anidar listas o diccionarios en los sets pues estos tipos de datos son mutables a diferencias de los sets.
# s1 = {'ejemplo', 'ejemplo2', a} TypeError: unhashable type: 'list'
# Si lo intetamos nos dara un error en la terminal.

# Los sets tambien se pueden iterar.

for ss in s0:
    print(ss)
# 1
# 2
# 3
# 4
# 5

# Se asemeja bastante a la iteracion a las listas.

# Elemento len().

len(s0) # 5

# El elemento len() retorna la cantidad de datos iterablescen este caso 5.

# Operador de pertenencia in.

if 2 in s0:
    print("EL numero 2 esta en el set s0.")
else:
    print("El numero 2 no esta en el set s0")

# Como vimos en un reto anterior el operador in nos siver para saber si un dato esta dentro de otro.

# Union o | es una forma de unir sets pero recordar que si se repite el mismo valor se eleminara hasta que solo
# quede uno.

print(s | s0) # {1, 2, 3, 4, 5, 'Franz', 20, 'Python'}

# Practicamente solo une los datos y los podemos asiganar a un nuevo set.

# AL igual que append() en las listas en los sets tenemos add().
# Con el que podemos agregar un dato a un set.

s.add(6)
print(s) # {1, 2, 3, 4, 5, 6}

# Agregara al set el dato que se ponga en el parentesis pero recordar que no se pueden anidar listas dentro de los sets.

# Y de la misma forma que con las listas en elemento remove pude eliminar un dato de un set.

s.remove(6)
print(s) # {1, 2, 3, 4, 5}

# Como vimos eliminar el dato que se ponga entre los parentesis y de no encontrarlos devolvera un error key.

# Elemento discard().

s.discard(5)
print(s) # {1, 2, 3, 4}

# Hace la misma funcion que el elemento remove() solo que si no encuentra el dato no devolvera ningun error.

# Elemento pop().

s.pop()
print(s) # {2, 3, 4}

# Como los sets no censervan el orden con el que se definen cuando el pop elimina un dato lo hace de forma pseudoaleatoria.

# Elemento clear().

s.clear()
print(s) # set()

# El elemento clear elimina todos los datos que esten dentro del set().

# Otras operaciones interesantes:
# Como obseravaremos estos funcionan poniendo un punto y el elemneto para por ultimo poner el parametro.
# EJemplos para las operaciones.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {7, 8, 9, 10, 11}

# Union:

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.union(s2,s3)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Intersection:

print(s1.intersection(s2)) # {4, 5}
print(s1.intersection(s2,s3))  # set()

# 