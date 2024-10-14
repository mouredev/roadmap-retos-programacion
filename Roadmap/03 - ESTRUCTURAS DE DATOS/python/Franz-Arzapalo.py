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

# Sin embargo podemos anidar frozenset que son completamente inmutable sin poder hacer ningun tipo de modificacion.
# Se crea de la siguiente manera.

fs = frozenset((1, 2))
print(type(fs)) # <class 'frozenset'>

# Esta es una sus principales funciones pues no son muy utizadas.

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

# Como vemos podemos usar union para juntar dos a mas sets pero si se repiten algunos datos, estos seran eliminados hasta que quede solo uno.

# Intersection:

print(s1.intersection(s2)) # {4, 5}
print(s1.intersection(s2,s3))  # set()

# Como vemos aqui cuando queremos la interseccion de dos sets nos devuelve los datos que se repiten si ponemos mas solo nos devolvera el dato que
# se repita todos los sets si no hay ninguno nos devuelve simplemente el tipo set por que estara vacio.

# Asi hay varios elementos:
"""
s1.union(s2[, s3 ...])
s1.intersection(s2[, s3 ...])
s1.difference(s2[, s3 ...])
s1.symmetric_difference(s2)
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)
s1.update(s2[, s3 ...])
s1.intersection_update(s2[, s3 ...])
s1.difference_update(s2[, s3 ...])
s1.symmetric_difference_update(s2)
"""
# Asi como elementos hay oprtunidades de trabajar con sets.

# Tuplas:
"""
Las tuplas son parecidas a las listas y a los sets pues almacenan datos y son inmutables osea que no se pueden modificar una vez
creadas como los sets estas se definen con los calsicos parentesis () y con una diferencia en que dependiendo como se usar puede ser
de uso rapido.
"""

# Definir una tupla:

Tupla = (1, 2, 3)
print(type(Tupla)) # <class 'tuple'>
tupla = 1, 2, 3
print(type(tupla)) # <class 'tuple'>
TUpla = tuple(a)
print(TUpla) # ('Franz', 20, 'Python')
print(type(TUpla)) # <class 'tuple'>

# Al poner los datos que queremos almacenar entre parentesis se clasificaran como tupla pero si solo separamos datos con comas tambein funciona.
# y tambien podemos hacer una tupla convirtiendo un grupo de datos iterable con el comando tuple().

# Modificar datos de una tupla:
# Tupla[0] = 2 TypeError: 'tuple' object does not support item assignment
# Como las tuplas son un tipo de dato inmutable cuando intentamos cambiar un dato de este devulve un error igual que los sets.

# Anidar:

TuplA = (Tupla, tupla, TUpla)
print(TuplA) # ((1, 2, 3), (1, 2, 3), ('Franz', 20, 'Python'))

# A diferencia de los sets las tuplas si premiten anidar tuplas dentro de otras tuplas.

# Iterar:

for t in TuplA:
    print(t)
    # (1, 2, 3)
    # (1, 2, 3)
    # ('Franz', 20, 'Python')

# Las iteracion son normales como cualquer otro tipo de dato iterable.

# Asignar:

T, P, A = Tupla
print(T, P, A) # 1 2 3

# Tambien se puede asignar datos a las variables de esta forma con las tuplas.

# Caso poco utilizado:

L = (4,)
print(type(L)) # <class 'tuple'>

# Se puede definir una tupla de un solo dato es util en casos muy selectivos pero es bueno conocerlo lo mas importante es poner la coma.

# Elemento count:

print(TuplA.count((1, 2, 3))) # 3

# El elemento count nos permite contar el numero de datos que se repita un dato que ingresemos en el parentesis.(ojo no ingresa en tuplas anidadas)

# Diccionarios:
"""
Los diccionarios son tipos de datos que almacenan infomacion en forma de llave y valor, estos datos se separan por dos puntos y despues
de ello para separar cada llave y sus valores se usan las comas y estan entre llaves {} igual que los sets, Sus caracteristicas principales
es que son dinamicos, pues se puden añadir y eliminar elementos, son indexados, pues se pueden acceder a sus valores atravez de sus keys y
son anidados, porque se pueden poner diccionarios dentro de otros diccionarios.
"""

# Definir un diccionario:

d1 = {'Nombre':'Franz', 'Edad': 19, 'Lenguaje':'Python'}
print(d1) # {'Nombre': 'Franz', 'Edad': 19, 'Lenguaje': 'Python'}
print(type(d1)) # <class 'dict'>

# Como se habia explicado para separar cada llave o key de su valor o value se usan los dos puntos y para definir otro key y value es la coma.

# Se puede definir un diccionario con un comando como los otros tipos de estructura de datos con dict() pero se tienen que cumplir las siguientes condiciones:
# Deben estar anidados en una lista, deben de estar separados de a dos puede ser en tuplas.
# Si se pueden cumplir esas dos condiciones el comando hara su funcion.
# Pero tambien se puede definir diccionarios igualando una variable a un valor y separarlos por comas para igual otra variable dentro de
# la funcion dict() los convertira en un diccionario.

# Acceder:

print(d1['Nombre']) # Franz
print(d1.get('Edad')) # 19

# Parecido con las listas pero aqui podemos usar las key cambio de la posicion o podemos usar el elemento get() e igualmente poner la key.

# Modificar:

d1['Nombre'] = 'Erick'
print(d1['Nombre']) # Erick

# Al igual que con las listas podemos modificar sus elementos pero otra vez cambio de la posicion se usan las keys.

# Asignar:

d1['Ciudad'] = 'Huancayo'
print(d1) # {'Nombre': 'Erick', 'Edad': 19, 'Lenguaje': 'Python', 'Ciudad': 'Huancayo'}

# Si ingresamos un parametro que no existe en el diccionario sera como asignar una nueva key y tambien un nuevo valor.

# Iteraciones:

for i in d1:
    print(i)
    # Nombre
    # Edad
    # Lenguaje
    # Ciudad

# De esta forma solo podemos interar las keys.

for i in d1:
    print(d1[i])
    # Erick
    # 19
    # Python
    # Huancayo

# Y de esta forma podemos iterar los value.

for i, j in d1.items():
    print(f"{i} es {j}")
    # Nombre es Erick
    # Edad es 19
    # Lenguaje es Python
    # Ciudad es Huancayo

# Para poder iterar las keys y los valores necesitamos poner dos parametros en el bucle y tambien usar el elemento .items() en el diccionario.

# Anidar diccionarios:

anidada1 = {'ejem1':1,'ejem2':2}
anidada2 = {'ejem3':3,'ejem4':4}

Anidada = {'dic1':anidada1,'dic2':anidada2}
print(Anidada) # {'dic1': {'ejem1': 1, 'ejem2': 2}, 'dic2': {'ejem3': 3, 'ejem4': 4}}

print(Anidada['dic2']['ejem3']) # 3

# Como podemos ver podemos ingresar a cualquier valor de el diccionario anidado si usamos las key como posiciones igual que con las listas.

# clear:

Anidada.clear()
print(Anidada) # {}

# El elemento clear elimina todos los valores y key que tenga un diccionario.

# Extencion de get(key, mensaje en caso de no existir value o key):

print(Anidada.get('Nombre', 'No se encontro value.')) # No se encontro value.

# El segundo parametro solo definine un valor o dato que se mostrara si no encuentra el value no sirve para nada mas.

# items:

print(type(anidada1.items())) # <class 'dict_items'>
print(anidada1.items()) # dict_items([('ejem1', 1), ('ejem2', 2)])

# Convierte un diccionario en una clase de lista que puede ser indexada en una lista normal pero nos permite trabajar con las keys y value a la vez.

# keys().

print(d1.keys())
# dict_keys(['Nombre', 'Edad', 'Lenguaje', 'Ciudad'])

# El elemento keys nos devuelve todas las keys del diccionario.

# values().

print(d1.values())
# dict_values(['Erick', 19, 'Python', 'Huancayo'])

# El elemento values nos devuelve todos los valores del diccionario.

# pop().

print(d1.pop('Signo', 'No se encontro la key')) # No se encontro la key

# Al igual que get() con el elemento pop podemos defnir un mensaje en caso de no encotrar la key para que no salte un error.

# popitem().

print(d1) # {'Nombre': 'Erick', 'Edad': 19, 'Lenguaje': 'Python', 'Ciudad': 'Huancayo'}
d1.popitem()
print(d1) # {'Nombre': 'Erick', 'Edad': 19, 'Lenguaje': 'Python'}

# El elemento popitem elimina un dato aleatorio del diccionario.

# update()

anidada1.update(anidada2)
print(anidada1)

# Esta herramineta compara dos diccionarios y si encuentra la misma key en los dos cambia el del primer diccionario por el segundo
# y de no encontrar la key del segundo en el primero lo creara y la asignara el mismo que el del segundo.

"""
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
ag = {}

def búsqueda ():
    x = input("¿Como se llama el contacto? ")
    if x in ag:
        print(f"El numero de {x} es {ag[x]}")
    else:
        print(f"El contacto {x} no existe.")

def inserción ():
    x = input("Ingrese el nombre del contacto que quiere agregar: ")
    if x in ag:
        print("\n Ya existe un contacto con ese nombre \n Por favor:")
        inserción()
    else:
        y = input(f"Ingrese el numero de {x}: ")
        while len(y) > 9:
            print("El numero no puede tener mas de 9 digitos.")
            y = input(f"Ingrese el numero de {x}: ")
        print("  Contacto - Numero")
        for x, y in ag.items():
            print(f"  {x} - {y}")

def actualización ():
    x = input("Ingrese el nombre del contacto que quiere actualizar: ")
    if x in ag:
        y = input(f"Ingrese el nuevo numero de {x} : ")
        while len(y) > 9:
            print("El numero no puede tener mas de 9 digitos.")
            y = input(f"Ingrese el nuevo numero de {x} : ")
        ag[x] = y
    else:
        print("\n El contacto no esta en la agenda \n Por favor:")
        actualización()

def eliminación ():
    x = input("Ingrese el nombre del contacto que quiere elminar: ")
    if x in ag:
        ag.pop(x)
        for x, y in ag.items():
            print(f"  {x} - {y}")
        print("El contacto esta eliminado.")


def agenda ():
    o = 1
    while o != 'no':
        print('Escoja la funcion que quiere hacer: \n 1. Búsqueda \n 2. Inserción \n 3. Actualización \n 4. Eliminación \n 5. Ver_Contactos \n 6. Salir o no.')
        o = input('Ingrese el numero o el nombre de la operación: ')
        if o == '1' or o == 'Búsqueda':
            búsqueda()
            o = input('¿Quiere hacer otra operacion? ')
        elif o == '2' or o == 'Inserción':
            inserción()
            o = input('¿Quiere hacer otra operacion? ')
        elif o == '3' or o == 'Actualización':
            actualización()
            o = input('¿Quiere hacer otra operacion? ')
        elif o == '4' or o == 'Eliminación':
            eliminación()
            o = input('¿Quiere hacer otra operacion? ')
        elif o == '5' or o == 'Ver_Contactos':
            print("  Contacto - Numero")
            for x, y in ag.items():
                print(f"  {x} - {y}")
            o = input('¿Quiere hacer otra operacion? ')
        elif o == '6' or o == 'Salir' or o == 'no':
            o = 'no'    
    else:
        print("La funcion agenda se termino.")

agenda()

# Fin.