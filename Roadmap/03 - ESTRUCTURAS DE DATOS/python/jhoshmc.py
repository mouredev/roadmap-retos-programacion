
"""
* Estructuras
"""
#!listas, 
#* son estructuras ordenadas donde vamos a guardar elementos, como un array 
# print("----------------listas-------------------------")
# my_list = ["juan","pedro","ana","maria"]
# print(my_list)
# my_list.append("mario") #* agregar un nuevo elemento a la lista
# print(my_list)
# my_list.remove("ana") #* eliminar un elemento de la lista, en esta caso por valor
# print(my_list)
# my_list[1]= "armando" #* actualizar un elemento de la lista, en este caso por posición
# print(my_list)
# my_list.sort() #* mostrar la lista ordenada, con el ordenamiento predeterminado, se puede cambiar 
# print(my_list)
# print(type(my_list))

# #! tupla
# #* es una estructura donde se puede guardar mas de un dato, pero son inmutables, 
# #* (como se crean, se quedan , no cambian), va entre parentesis ()
# print("---------------- tuplas --------------------")
# my_tupla= ( "mauro","acuario","algo@gmail.com",'20')
# print(my_tupla)
# #* solo se puede hacer operaciones de acceso
# print(my_tupla[2])
# print(type(my_tupla))
# #* se puede cambiar la tupla a una lista para ordarla, con sorted()
# my_tupla= sorted(my_tupla) #* sorted(), devulve una lista ordenada
# print(my_tupla)
# print(type(my_tupla))
# #* cambiar la lista otra vez a tupla con el constructor de tupla
# my_tupla= tuple(my_tupla)
# print(my_tupla)
# print(type(my_tupla))

# #! Set
# #* son otro tipo de estructura, van entre corchetes {}, no permiten valores repetidos, 
# #* set es una estructura desordenada(no se puede fiar de la posición de un elemento) 
# #* transforma sus datos en hash 
# print("---------------- set -----------------")
# my_set: set ={"mauro","acuario","algo@gmail.com",'20'}
# print(my_set)
# print(type(my_set))
# my_set.add("maria") #* insertar elemento
# print(my_set)
# my_set.remove("20") #* eliminar un elemento
# my_set=sorted(my_set) #* ordenarlo, combirtiendolo a lista
# print(my_set)
# print(type(my_set))
# my_set= set(my_set)
# print(my_set)
# print(type(my_set))

# #! Diccionario
# #* el formato en que se guardan los datos es clave, valor (key, value)
# #* en python los diccionarios, son ordenados por defecto
# print("------------ dictionario-----------------------")
# my_dic: dict ={
#   "name":"mauro",
#   "signo":"acuario",
#   "gmail":"algo@gmail.com",
#   "age":'20'}
# print(my_dic)
# print(type(my_dic))
# my_dic["fav_food"]="pato guisado" #* se esta insertando una nueva clave y valor
# print(my_dic)
# print(my_dic["name"]) #* se accede mediante la clave, no hay posiciones
# my_dic["age"]="21" #* actualizar un elemento
# print(my_dic)
# del my_dic["signo"] #* eliminar un elemento 
# print(my_dic)
# my_dic= dict(sorted(my_dic.items())) #* ordenar, es importante poner items(), para que devuelva las claves y los valores
# print(my_dic)

"""
*Extra
"""
import re
patron = r"^\d{1,11}$"  # Expresión regular para validar números de 1 a 11 dígitos
agenda_contactos={}
def verificar_numero(nombre,telefono):
  if re.fullmatch(patron,telefono):
    agenda_contactos[nombre]=telefono
    return True
  else:
    print("el numero ingresado no puede ser mayor a 11 dijitos \n")
    return False 


def ingresar_contacto():
  print("\n\t ingresar contacto: \n")
  nombre=input("ingresa el nombre: ")
  telefono= input("ingresa el numero de telefono: ")
  verificado=verificar_numero(nombre,telefono)
  if verificado:
    print("\nnuevo contacto agregado \n")
  

def buscar_contacto(nombre):
  print("\n\t buscar contacto: \n")
  if nombre in agenda_contactos:
    print(f"contacto encontrado: \n${nombre} Movil:${agenda_contactos[nombre]}")
    return True
  else:
    print(f"el contacto: ${nombre} no existe \n")
    return False

def actualizar_contacto():
  print("\n\t actualizar contacto: \n")
  nombre = input("ingrese el nombre del contacto: ")
  existe = buscar_contacto(nombre)
  if existe:
    telefono= input("ingrese el nuevo numero de telefono: ")
    verificado= verificar_numero(nombre,telefono)
    if verificado:
      print("\n contacto actualizado\n")

    

def borrar_contacto():
  print("\n\t borrar contacto: \n")
  nombre= input("ingrese el nombre del contacto: ")
  existe= buscar_contacto(nombre)
  if existe:
    del agenda_contactos[nombre]
    print("\n contacto eliminado")
  

def ordenar_contactos():
  print("\t\n ordenar contactos: \n")
  agenda_ordenada= dict(sorted(agenda_contactos.items()))
  print(agenda_ordenada)
  print("\n")
  
def agenda():
  
  while True:
    print("\t Menu de agenda : \n")
    print("1. ingresar contacto ")
    print("2. buscar contacto")
    print("3. actualizar contacto")
    print("4. borrar contacto")
    print("5. ordenar contactos")
    print("6. salir")
    #* input rejoge lo que selecciona el usuario desde la terminal
    option=input(" \n ingresa la opcion: ")

    match option:
      case '1':
        ingresar_contacto()
      case '2':
        nombre= input("ingrese el nombre del contacto: ")
        buscar_contacto(nombre)
      case '3':
        actualizar_contacto()
      case '4':
        borrar_contacto()
      case '5':
        ordenar_contactos()
      case '6':
        print("\n saliendo del programa adios\n")
        break
      case _: print("opcion no valida")
  


agenda()