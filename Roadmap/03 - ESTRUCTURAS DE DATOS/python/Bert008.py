'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''
# Las estructuras en soportadas en Python son las siguientes
lista = [0, 1, 2, 3, 3]
tupla = (0, 1, 2, 3, 3)
conjunto = {1, 2, 3, 3}
diccionario = {0: 1, 1: 2, 2: 3, 3: 4}
print(lista)
print(tupla)
print(conjunto)
print(diccionario)

print(type(lista))
print(type(tupla))
print(type(conjunto))
print(type(diccionario))

def insercion(obj1, obj2):
    if isinstance(obj1, list):
        obj1.append(obj2)
        print("insercion: ", obj1)
    elif isinstance(obj1, tuple):
        tupla2 = obj1 + (obj2,)  # Corregido el nombre de variable 'tupla' a 'obj1'
        print("insercion: ", tupla2)
    elif isinstance(obj1, set):
        obj1.add(obj2)  # Corregido 'conjunto' a 'obj1'
        print("insercion: ", obj1)
    elif isinstance(obj1, dict):
        if isinstance(obj2, tuple) and len(obj2) == 2:
            obj1[obj2[0]] = obj2[1]  # Mejorado para aceptar pares clave-valor
        else:
            obj1[len(obj1)] = obj2
        print("insercion: ", obj1)

def borrar(obj1, obj2):
    if isinstance(obj1, list):
        try:
            obj1.pop(obj2)
            print("borrar: ", obj1)
        except IndexError:
            print(f"Índice {obj2} fuera de rango para la lista")
    elif isinstance(obj1, tuple):
        try:
            lista_temp = list(obj1)
            lista_temp.pop(obj2)
            obj1 = tuple(lista_temp)
            print("borrar: ", obj1)
        except IndexError:
            print(f"Índice {obj2} fuera de rango para la tupla")
    elif isinstance(obj1, set):
        try:
            obj1.remove(obj2)
            print("borrar: ", obj1)
        except KeyError:
            print(f"Elemento {obj2} no encontrado en el conjunto")
    elif isinstance(obj1, dict):
        try:
            del obj1[obj2]
            print("borrar: ", obj1)
        except KeyError:
            print(f"Clave {obj2} no encontrada en el diccionario")

def actualizar(obj1, obj2):
    if isinstance(obj1, list):
        if isinstance(obj2, list):
            obj1.extend(obj2)
        else:
            obj1.append(obj2)
        print("update: ", obj1)
    elif isinstance(obj1, tuple):
        if isinstance(obj2, (list, tuple, set)):
            obj1 += tuple(obj2)
        else:
            obj1 += (obj2,)
        print("update: ", obj1)
    elif isinstance(obj1, set):
        if isinstance(obj2, (list, tuple, set)):
            obj1.update(obj2)
        else:
            obj1.add(obj2)
        print("update: ", obj1)
    elif isinstance(obj1, dict):
        if isinstance(obj2, dict):
            obj1.update(obj2)
        elif isinstance(obj2, tuple) and len(obj2) == 2:
            obj1[obj2[0]] = obj2[1]
        else:
            obj1[len(obj1)] = obj2
        print("update: ", obj1)

def sorting(obj1):
    if isinstance(obj1, list):
        try:
            obj1.sort()
        except TypeError:
            print("No se puede aplicar sort a una lista con tipos incompatibles")
        print("ordenar: ", obj1)
    elif isinstance(obj1, tuple):
        obj1 = tuple(sorted(obj1, key=lambda x: str(x)))  # Ordena convirtiendo a str para evitar errores
        print("ordenar: ", obj1)
    elif isinstance(obj1, set):
        obj1 = sorted(obj1, key=lambda x: str(x))  # Ordena convirtiendo a str para evitar errores
        print("ordenar: ", obj1)
    elif isinstance(obj1, dict):
        try:
            obj1 = dict(sorted(obj1.items(), key=lambda item: item[1]))
            print("ordenar: ", obj1)
        except TypeError:
            print("No se puede ordenar el diccionario con tipos de valores incompatibles")

estructuras = [lista, tupla, conjunto,diccionario]
for i in estructuras:
    insercion(i, 3)
    borrar(i, 2)
    actualizar(i, 1)
    sorting(i)
    print("=====================================")
'''
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''

# directorio
directorio = {}

# entradas
# ANADIR NUEVO CONTACTO
def add_cto(name, pnum):
    if isinstance(pnum, str) and len(pnum) < 11:
        directorio[name] = pnum

def agenda_telefonica():
    while True:
        print("Agenda telefonica")

        print("1) Agregar contacto nuevo")
        print("2) Actualizar contacto")
        print("3) Eliminar contacto")
        print("4) Mostrar directorio")
        print("5) Salir de la agenda")

        input_match = int(input("Eliga una opcion "))
        match input_match:
            case 1:
                print("Agregar contacto nuevo")
                name = input("Nombre: ")
                pnum = input("Numero de telefono: ")
                add_cto(name, pnum)
            case 2:
                print("Actualizar contacto")
                buscar = input("Contacto: ")
                if buscar in directorio:
                    print("1) Cambiar Nombre")
                    print("2) Cambiar Numero")
                    opcion = int(input("Eliga una opcion"))
                    if opcion == 1:
                        print(f"Cambiar nombre de {buscar} a: ")
                        nuevo_nombre = input()
                        directorio[nuevo_nombre] = directorio.pop(buscar)
                    elif opcion == 2:
                        print(f"Cambiar numero del contacto {buscar} a: ")
                        nuevo_numero = input()
                        directorio[buscar] = nuevo_numero
                else:
                    print("Contacto no existe")

            case 3:
                print("Eliminar contacto")
                drop_cto = input()
                if drop_cto in directorio:
                    del directorio[drop_cto]
                    print("contacto eliminado")
                else:
                    print("contacto no existe")
            
            case 4:
                print("Contactos")
                for nombre, pnum in directorio.items():
                    print(f"{nombre} -- {pnum}")
                    
            
            case 5:
                print("Saliendo de la agenda")
                break

agenda_telefonica()