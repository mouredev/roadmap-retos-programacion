"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 
 """

# listas

# myList = [1,2,3,4,5,6,7,8,9,0]
# myList.append(0) # agregar al final
# myList.insert(2,555) # agregar en posicion indicada
# print(myList)
# myList.remove(0) # eliminar  el elemento indicado
# print(myList)
# myList[0] = 222 # cambiar valor de una posicion
# print(myList)
# myList.sort()

# #tuplas

# myTupla = (8,10,7,100,3,4,5)
# print(type(myTupla))
# o = tuple(sorted(myTupla))
# print(type(o), o)

# #set
# mySet = set(myList )
# print(type(mySet))
# mySet.add(0)
# mySet.remove(555)
# print(mySet)


# # #dic
# myDic = {1:"a",2:"b",3:"c"}
# print(myDic)
# v= myDic.get(1)
# print(v)
# i = myDic.items( )
# print(i)
# k = myDic.keys()
# print(k)
# vv = myDic.values()
# print(vv)
# myDic[101] = "z"
# myDic[1] = "A"
# print(myDic)
# del myDic[1]
# print(myDic)
# orded = dict(sorted(myDic.items()))
# print(orded)

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.

"""
agenda = dict()
def Agenda():
     
    while True:
        print( "*-*- M E N U -*-*")
        print("MOSTRAR TODOS (MT)")
        print("INSERTAR (I)")
        print("ACTUALIZAR(A)")
        print("ELIMINAR (E)")
        print("BUSCAR (B)")
        print("SALIR (S)")

        operacion = input("\nSeleccione opcion : ")
        match operacion:
            case "I":
                Insertar()

            case   "A":
                Actualizar()

            case  "MT":
                Mostrar_Todos()
            
            case "E":
                Eliminar()

            case   "B":
                Buscar()

            case "S":
                break
            case _:
                print("OPCION no VALida, de nuevo")

def agenda_empty():
    if  not agenda :
        print("AGENDA VACIA")
        return 1

def Mostrar_Todos():
    print("\tMOSTrar AGENDA")
    
    if agenda_empty():
        return
    
    print("NOMBRE", "TELEFONO")
    for k,v in agenda.items():
        print(k,v)

def Insertar():
    print("INSERTAR")

    nombre = input("NOMBRE :")
    if busqueda(nombre) != 0:
        print(nombre, "Usuario ya existe")
        return
    tel = input("Telefono :")
    tel = validar_telefono(tel)
    if tel  != 0:
        agenda[nombre] = tel
    else:
        return
    print(agenda)

def Actualizar():
    print("ACTUALIZAR")
    if agenda_empty():
        return
    nombre = input("Usuario a Actualizar :")
    if busqueda(nombre) != 0:
        print(nombre, " : " , agenda[nombre])
        new_telefono = input("Nuevo telefono ")
        new_telefono = validar_telefono(new_telefono)
        if new_telefono > 0 :
            agenda[nombre] = new_telefono
            print(nombre, " : " , agenda[nombre])
    else:
        print("Usuario no encontrado")
        

    

def Eliminar():
    print("ELIMINAR")
    if agenda_empty():
        return
    nombre = input("Usuario a eliminar:")
    if busqueda(nombre) != 0:
        print(nombre, " : " , agenda[nombre])
        del agenda[nombre]
        print(nombre, " : ELIMINADO"  )
    else:
        print("Usuario no encontrado")

def busqueda(nombre):
    if not agenda.get(nombre):
        return 0

def Buscar():
    print("BUSCAR")
    
    if agenda_empty():
        return
    
    nombre = input("Nombre a localizar :")
   
    if busqueda(nombre) != 0:
        print(nombre, " : " , agenda[nombre])
    else:
        print("Usuario no encontrado")
        


def validar_telefono(movil) -> int:  

    print("VALIDANDO DATOS... ")
    try:
        new_movil = int(movil)
    except ValueError:
        print("Error en datos, SOLO NUMEROS")
        return 0
    
    # mas de 5 cifras no permitido
    if new_movil > len(str(new_movil)) >6:
        print("Error en datos, telefonos mayores que 5, NO PERMITIDOS")
        return 0

    print("DATOS CORRECTOS")
    return new_movil
    

Agenda()




