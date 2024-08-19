'''
Estructuras de datos

'''
""" LISTAS """ 
my_list = ['hola' , 'hi', 'hello']
print(type(my_list))
# esta es la sintaxis de una lista comun y corriente
my_list.append('hola')
print(my_list)
#con .append podemos agregar un dato extra la lista 
my_list.extend('bye')
print(my_list)
#con .extend extiendes la lista agregando letra por letra a la lista ejem: bye = 'b', 'y', 'e'
my_list.remove("hi")
print(my_list)
#con .remove podemos borrar un dato de nuestra lista 
print(my_list[2])
#de esta forma llamamos al dato que esta en la posición que indiquemos con el numero (siempre se cuenta desde cero)
my_list.insert(3,"hasta luego")
print(my_list)
#con .insert podemos agregar a la lista y decidir la ubicacion señalando primero el numero de posicióny luego lo que agregaremos
#en este caso indica que 'hasta luego' va despues de la posición 3
my_list[3] = "hi"
print(my_list)
# de esta forma actualizamos un dato, indicando la posición que queremos cambiar en la variable y escibimos el nuevo dato
print(my_list.count('hola')) #aparece dos veces
print(my_list.count('vaca')) #aparece cero veces
#con .count contamos la cantidad de veces que aparece lo que escribamos en nuestra lista
print(my_list.sort())
# sort es una funcion de ordenado en este caso ordenara de forma alfabetica 
#si fueran numeros lo haria de forma ascendente aunque tambien le podemos ordenar la forma que quisieramos 
print(my_list)
my_list.reverse()
print(my_list)
#Con .reverse podemos invertir el orden de la lista, podemos ver por consola como esta invertido a la ordenacion que hizo el .sort
print(my_list.pop(2))
#con .pop borramos un elemento de la lista reprersentado por el numero de posicion que tenga en la lista y nos da por terminal el elemento borrado en este caso 'hola'
print(my_list)
#imprimimos para ver que despues de usar .pop en nuestra lista solo se imprime un 'hola' ya que el otro fue removido

'''Tuplas'''
#Una tupla es similar a una lista pero unas cuantas diferencias
#Estan formadas por valores separadas por comas y siempre se encierran en paréntesis
#son inmutables, no se puden alterar (no se pueden agregar ni eliminar datos de la tupla)
my_tuple = ('manzana')
print(type(my_tuple))
#Podemos ver que la clase de la variable es STR
my_tuple = ('manzana',)
print(type(my_tuple))
#pero en el momento en que ponemos la coma la clase paso a ser una Tupla 

'''Conjuntos / set'''
#Un conjunto es una estructura de dato que sirve para verificar pertenencias y eliminar entradas duplicadas

print(type({'pera'})) 
print(type(set('pera')))
#Los conjuntos se representan usando las llaves '{}' o usando 'set()'

print(type({}))
#si escribimos solo '{}' crearemos un diccionario y no un conjunto vacio
print(type(set()))
#para el conjunto vacio se escribe 'set()'
my_set = {'mesa', 'silla', 'cama', 'mesa', 'puerta', 'cama'}
print(my_set)
#Las entradas no son ordenadas y los elementos no se repiten y en terminal solo aparecera {'mesa','silla','puerta','cama'}

a = set('adios')
b = set('arroz')
#en los conjuntos podemos usar operaciones matematicas
print(f"letras que hay en 'a' y no en 'b' {a - b}")
print(f"letras que hay en 'b' y no en 'a' {b - a}")
print(f"letras que hay en 'a' o 'b' o ambas {a | b}")
print(f"letras que hay en ambas {a & b}")
print(f"letras que hay en 'a' o 'b' pero no en ambas {a ^ b}")

'''diccionarios'''
#Los diccionarios funcionan teniendo una palabra clave y un valor a esa palabra clave:
edades = {'michael':23, 'roger':35, 'dayara':17}
print(type(edades))
#este tipo de datos es un 'dict'
edades['santos'] = 45
print(edades)
# de esta forma podemos agregar un nuevo dato clave:valor a nuestro diccionario

del edades['dayara']
print(edades)
#usando 'del' podemos eliminar la clave del diccionario 

edades['roger']= 27 
print(edades)
# de esta forma podemos actualizar datos de una lista 

print(list(edades))
#de esta forma podemos imprimir las claves que tengas en nuestro diccionario

my_dict = dict ([('mesas', 10), ('vasos', 12), ('cucharas', 33)])
print(my_dict)
print(type(my_dict))
#De esta forma podemos crear tambien una lista siguiendo el orden clave y valor y segura siendo un "dict"
  
"""
extra 
"""

def my_agenda():

   agenda = {}

   def act_save():
     celular = input(f"Ingresa el numero de {nombre} ")
     if celular.isdigit() and len(celular) >0 and len(celular) <=9:
       agenda[nombre] = celular
     else:
       print("Porfavor ingresa un numero de celular valido. ")

   while True:
    
    print("")
    print("1. busqueda de contacto")
    print("2. guardar nuevo contacto")
    print("3. actualizar contacto")
    print("4. eliminar contacto")
    print("5. salir")

    opciones = input("\nPor favor selecciona cual operacion deseas realizar: ")

    match opciones:
      case "1":
        nombre = input(f"Ingresa el nombre del contacto. ")
        if nombre in agenda:
          print(f"El numero de {nombre} es {agenda[nombre]}. ")
        else:
          print(f"el contacto {nombre} no esta en la agenda. ")
      case "2":
        nombre = input(f"Ingresa el nombre del contacto. ")
        act_save() 
      case "3":
        nombre = input(f"Ingresa el nombre del contacto que quieres actualizar. ")
        if nombre in agenda:
          act_save()
        else:
          print(f"El nombre {nombre} no esta en la agenda. ")
      case "4":
        nombre = input(f"Ingresa el nombre del contacto que quieras eliminar. ")
        if nombre in agenda:
          print(f"El contacto {nombre} a sido eliminado")
          del agenda[nombre]
        else:
          print("El contacto no existe en la agenda. ")
      case "5":
        print("Estamos saliendo del sistema, muchas gracias. ")
        break
      case _:
        print("Porfavor selecciona el numero de una de las opciones. ")

my_agenda()
