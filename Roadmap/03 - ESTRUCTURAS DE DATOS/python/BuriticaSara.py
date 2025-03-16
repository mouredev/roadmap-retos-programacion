03 - Estructuras de datos:

Las estructuras son conjuntos de datos agrupados.
"""

#listas: son conjuntos de datos organizados, que se pueden modificar
#funciones: append(), remove(), [1], sort()

milista = ['Daniel', 'Sara', 'Silvi', 'Corazón']
print(milista)

milista.append('Toulouse') #inserta el nuevo elemento al final de la lista
print(milista)

milista.remove('Toulouse') #borra el elemento mencionado
print(milista)

print(milista[1]) #acceso a un elemento específico, se pone el lugar del elemento, los lugares siempre empiezan desde 0

milista[2]= 'Silvano' #actualización, me remplaza un elemento por otro
print(milista)

milista.sort()
print(milista)

print(type(milista))

#Tuplas: son conjuntos de datos pero inmutables, se realizan con parentesis
#como no lo puedo cambiar no puedo borrar ni cambiar elementos.

mitupla= ('dirección','edad','telefono','1234')

print(type(mitupla))

print(mitupla[0]) #acceso a un elemento específico

#puedo usar las siguientes funciones, pero me convierten la tupla en lista, por eso tendría que volver a convertirla en tupla: tuple()

mitupla = tuple(sorted(mitupla))
print(mitupla)
print(type(mitupla))

#Sets: conjuntos de datos que no mantienen un orden específico. se crean con {} corchetes

miset = {'a','b','c','d'}

print(miset)
print(type(miset))

miset.add('e') #agregar un nuevo elemento, no me agrega elementos que ya existen, porque no guarda duplicados
print(miset)

miset.remove('b') #Eliminar un elemento
print(miset)

#Diccionario: es un conjunto de datos que guarda elementos y una clave para cada uno de ellos, se crea con {}

midiccionario = {'primero': '1', 'segundo': '2', 'tercero': '3', 'cuarto': '4'}
print(type(midiccionario))
print(midiccionario)

print(midiccionario['segundo']) #Asceso a un elemento, se hace por la clave
print(type(midiccionario))

midiccionario['tercero']= '3.0' #Actualizar un dato, se hace a través de la clave
print(midiccionario) 
print(type(midiccionario))

midiccionario['quinto']= '5' #Agregar, se escribe la clave y el elemento
print(midiccionario)

del midiccionario['primero'] #borrar un elemento, se llama por la clave
print(midiccionario)


"""
Ejercicio extra
"""

def mi_agenda():
  agenda = {}

  while True:

    print("Bienvenida a tu agenda, escribe el número de lo que deseas hacer")
    print("1. Buscar un contacto")
    print("2. Agregar un contacto")
    print("3. Modificar un contacto")
    print("4. Eliminar un contacto")
    print("5. Ver tu lista de contatos")
    print("6. Salir")

    decision = input()

 
    match decision:
      case "1":
        name = input("Escribe el nombre del contacto que estas buscando:")
        if name in agenda:
          print(f"El número de {name} es {agenda[name]}")
        else:
          print(f"El contacto {name} no se encuentra en la agenda")
      case "2":
        name = input("Escribe el nombre de la persona:")
        telefono = input("Escribe el número de teléfono:")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
          agenda[name] = telefono
        else: 
          print("teléfono no valido, por favor escribe un teléfono máximo de 11 digitos")
      case "3":
        name = input("Escribe el nombre del contacto que deseas modificar:")
        if name in agenda:
          telefono = (input("Escribe el nuevo número de teléfono:"))
          if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
            agenda[name] = telefono
            print(f"El nuevo numero de {name} es {agenda[name]}")
          else:
            print("telefono no valido, por favor escribe un teléfono máximo de 11 digitos" )
        else:
          print(f"El contacto {name} no existe")
      case "4":
        name = input("Escribe el nombre del contacto que deseas eliminar:")
        if name in agenda:
          del agenda[name]
          print(f"Tu contacto {name} ha sido borrado")
        else:
          print(f"El contacto {name} no existe")
      case "5":
        print(agenda)
        break
      case "6":
        print("Hasta luego")
        break
      case _:
        print(f"Opción no valida, selecciona una de las 5 opciones")

mi_agenda()
