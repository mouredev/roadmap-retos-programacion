"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

"""

#ESTRUCTURAS

#Listas
lista = [1, 10, 100, 1000]
print(lista)

#Inserción
lista.append(88)
print(lista)

#Actualizacion
lista[0] = 23

#Borrado
lista.remove(10)

#Ordenación
lista.sort()

#Tupla - Estructura inmutable
tupla = (3, 90, 200, 301, 55)
print(tupla)

#Acceso
print(tupla[3])

#Ordenacion de Tupla
tupla = tuple(sorted(tupla))
print(tupla)
print(type(tupla))

#Set - No ordenada - No admite duplicados - No se puede acceder a una posicion
mi_set = {1 , 5, 9, 22, 4}
print(mi_set)

#Insercion
mi_set.add("KDB")
print(mi_set)

#Actualizacion - Añadir mas datos
#mi_set.update()

#Borrado
mi_set.remove(5)
print(mi_set)

#Ordenacion - los set no tiene orden

#Diccionario
dic = {"name" : "Diego",
        "age" : 35,
        "job" : "Trucker",
        "height (m)" : 1.70,
        "active" : True}

print(dic)

#Insercion
dic["brand"] = "JRR10"
print(dic)

#Eliminacion
del dic["job"]
print(dic)

#Actualizacion
dic["height (m)"] = 1.75
print(dic)

#Ordenacion
dic = dict(sorted(dic.items()))
print(dic)
print(type(dic))


#Extra

agenda = {"james" : 12345678901,
          "karim" : 98765432122,
           "moran": 12345987600}

def acciones_agenda():
    #pedir al usuario que accion desea relaizar
    print("1 Insertar \n 2 Eliminar \n 3 Actualizar \n 4 Buscar \n 5 Salir")
    accion = int(input("Ingrese la accion que desea realizar: "))
    #Insertar
    if accion == 1:
        nombre = input("Ingrese el nombre del contacto que desea insertar: ")
        numero = input("Ingrese el nuevo numero de 11 digitos: ")
        if len(numero) == 11 and numero.isdigit() == True: #Control tamaño del numero 
            agenda[nombre] = numero
            print(agenda)
            acciones_agenda()
        else: #Insertar numero valido
            print("El numero no es valido - debe tener 11 digitos unicamente numeros")
            print(type(numero))
            acciones_agenda()
    #Eliminar
    elif accion == 2:
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        try: #Trata de eliminar el contacto
            del agenda[nombre]
            print(agenda)
            acciones_agenda()
        except: #Si no existe el contacto
            print(f"La accion no se pudo completar, revise los datos ingresados \n No exite el contacto: {nombre}")
            acciones_agenda()
    #Actualizar
    elif accion == 3:
        nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
        if nombre in agenda: #Comprobar si exite el contacto a actualizar
            numero = input("Ingrese el nuevo numero de 11 digitos: ")
            if len(numero) == 11 and numero.isdigit() == True: #Control tamaño del numero
              agenda[nombre] = numero
              print(agenda)
              acciones_agenda()
            else: #Errores de tamaño del numero o str
              print("El numero no es valido - debe tener 11 digitos unicamente numeros")
              acciones_agenda()
        else: #Si no existe el contacto
            print(f"La accion no se pudo completar, revise los datos ingresados \n No exite el contacto: {nombre}")
            acciones_agenda()
    #Buscar
    elif accion == 4:
        nombre = input("Ingrese el nombre del contacto que desea consultar: ")
        try: #Traer el numero del contacto
            print(agenda[nombre])
            acciones_agenda()
        except: #Si no existe el contacto
            print(f"La accion no se pudo completar, revise los datos ingresados. \n No exite el contacto: {nombre}")
            acciones_agenda()
    #Salir
    elif accion == 5:
        print("Gracias por usar la agenda")
    #Error de accion
    else:
        print("La opcion ingresada no es valida")
        acciones_agenda()

acciones_agenda()