#03 ESTRUCTURAS DE DATOS
"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""

#listas
def listas ():
    lista : list= [1,2,3,4,5,6,7,8,9,10]
    print("lista original : " , lista)

    #inserción
    lista.append(11) #agrega al final
    lista.insert(0 , 0) #agrega elemento con el indice
    print("inserción : " , lista )

    #borrado
    lista.pop(-1) #elimina segun el indice
    lista.remove(0) #elimina por el valor/elemento
    print("borrado : " , lista )

    #actualización
    lista[0] = 4
    print("actualización : " , lista )

    #ordenación
    lista.sort(reverse=True)#de mayor a menor
    print("de mayor a menor:" , lista)
    lista.sort(reverse=False)#de menor a mayor
    print("de menor a mayor:" , lista)


def tuplas():
    tupla : tuple = 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 # tambien se pueden crear haci (1,2,3,4,5...)
    print("tupla original" , tupla)

    #acceso de elemento
    print("acceso a tupla : " , tupla[2])#igual que las listas

    #concatenacion
    print("tupla concatenada : " , tupla + (11 , 12, 13))

    #ordenación
    print("de mayor a menor:" , sorted(tupla , reverse=True))#con la funcion sorted
    print("de menor a mayor:" , sorted(tupla))


def conjuntos():
    conjunto : set = {1,2,3,4,5,6,7,8,9,10}
    print("conjunto original" , conjunto)

    #inserción
    conjunto.add(11)
    conjunto.add(0)
    print("inserciones : ", conjunto)

    #borrado
    conjunto.remove(11)
    print("borrado remove : " , conjunto)
    conjunto.pop()
    print("borrado pop" , conjunto)

    #actualización
    conjunto.update({11,12,13})
    print("actualización : " , conjunto)


def diccionarios():
    diccionario: dict ={"nombre" : "apellido",
                        "Homero" : "Simpson",
                        "Brais" : "moure"}

    print("diccionario original : " , diccionario)

    #inserción
    diccionario["nombre_nuevo"] = "nuevo apellido"#nueva clave y valor
    print("inserción : " , diccionario)

    #borrado
    diccionario.pop("nombre_nuevo") #con pop se elimina el valor que pide es la clave
    print("borrado : " , diccionario)

    #actualizacion
    diccionario["santiago"] = diccionario.pop("nombre") #para actualizar la clave
    diccionario["santiago"] = "Lopez" #para actualizar el valor
    print("actualizacion : " , diccionario)


print("\n-----------Listas---------------")
listas()
print("\n-----------Tuplas---------------")
tuplas()
print("\n-----------conjuntos---------------")
conjuntos()
print("\n-----------diccionarios---------------")
diccionarios()
print("\n\n")



### Extra
contactos : dict = {
        "fernandez" : "1111 1111",
        "julieta" : "2222 2222",
        "jose" : "3333 3333",
        "juancho" : "4444 4444",
        }


def busqueda():

    key = input("Introduzca el nombre del contacto : ")
    if key in contactos:
        print(f"{key} - {contactos[key]}")
    else :
        print("contacto no existente")


def inserción():

    nombre = input("Ingrese el nombre del nuevo contacto: ")
    numero = input("Ingrese el número de teléfono: ")

    if numero.isdigit() and len(numero) <= 11:

        contactos[nombre] = numero
        print(f"Contacto {nombre} añadido correctamente.")

    else:
        print("Número de teléfono no válido. Asegúrate de ingresar un número numérico máximo de 11 dígitos.")


def actualizacion():

    antiguo_nombre=input("introduzca el nombre a cambiar : ")
    nuevo_nombre=input("introduzca el nuevo nombre : ")

    if antiguo_nombre in contactos:

        contactos[nuevo_nombre] = contactos.pop(antiguo_nombre)
        print("se cambio correctamente")

    else : print("el contacto a cambiar no existe")


def eliminar():

    nombre = input("introduzca el nombre a eliminar : ")

    if nombre in contactos:
        contactos.pop(nombre)
        print("se elimino correctamente")

    else : print("contacto no existente , intente de nuevo")


while True:
    print("""\nLista de contactos
                Acciones :
                1.mirar contactos
                2.buscar contactos
                3.añadir contactos
                4.actualizar contactos
                5.eliminar contactos
                6.cerrar lista de contactos""")
    opcion = int(input("eliga segun el indice : "))

    try :

        if opcion == 1 :
            for contacto , numero in contactos.items():
                print(f"{contacto} -- {numero}")

        elif opcion == 2 :
            busqueda()

        elif opcion == 3 :
            inserción()

        elif opcion == 4 :
            actualizacion()

        elif opcion == 5 :
            eliminar()

        elif opcion == 6 :
            print("progama finalizado")
            break

        else :
            print("no esta en el indice")

    except Exception as error :
        print("a sucedido un error , Error : " , error)


