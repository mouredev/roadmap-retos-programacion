'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 '''

#Ejemplos de creacion de Listas, Sets, Diccionario, Tuplas

list_hobits = ["Frodo", "Bilbo", "Sam", "Pippin", "Frodo"] #La diferencia con set o conjuntos es que pueden tener elementos duplicados

tupla_posicion_monte_destino = (24, 36) #inmutalbe

diccionario_magia = {
    "nombre_mago" : "Gandalf",
    "poderes" : ["fuego_destino", "luz_poder"]
}

set_armas = {"espada", "lanza", "pistola", "escopeta"}
print(list_hobits)
print(tupla_posicion_monte_destino)
print(diccionario_magia)
print(set_armas)

#Inserción en cada lista
list_hobits.append("Elrond")
#Las tuplas no se pueden añadir
diccionario_magia["Edad"] = 5600000
set_armas.add("lanzallamas") 
print(list_hobits)
print(tupla_posicion_monte_destino)
print(diccionario_magia)
print(set_armas)

#Borrado
'''
list_hobits.pop(5)
diccionario_magia.pop("Edad")
del diccionario_magia["nombre_mago"]
diccionario_magia.popitem()

set_armas.remove("lanzallamas")
print(list_hobits)
print(tupla_posicion_monte_destino)
print(diccionario_magia)
print(set_armas)
'''

#Actualización
list_hobits[0] = "Sam"
diccionario_magia["Edad"] = 10 #Ojo las claves no se pueden modificar
set_armas #Los sets tampoco pueden modificarse
print(list_hobits)
print(tupla_posicion_monte_destino)
print(diccionario_magia)
print(set_armas)

#Ordenación
list_hobits.sort()

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
 */
'''
#Creamos diccionario ejemplo
contacto_agenda = {"nombre": "Paco",
                   "Telefono": "664770496"}
contactos = [
    {"nombre": "Paco",
     "Telefono": "664770496"},
     {"nombre": "Lidia",
      "Telefono":"626899639"}
]
print(contactos)

# Definimos funciones.
def es_telefono_valido(telefono):#para verificar que son números y menos de 11 dígitos
    return telefono.isdigit() and len(telefono)<=11

def añadir():
    nombre = input("Dime el nombre de la persona que quieres añadir:")
    telefono = input("Teléfono: ")
    if es_telefono_valido(telefono):
        print("Telefono valido")
    else:
        input("Número de teléfono inválido. Sólo números y máximo 11 dígitos: ")
    

    contactos.append(
        {"nombre": nombre,
         "Teléfono": telefono}
    )

def buscar():
    nombre_buscado = input("Dime el nombre de la persona que quieres buscar: ")
    for contacto in contactos:
        if contacto["nombre"] == nombre_buscado:
            print(f"El teléfono de {contacto["nombre"]} es {contacto["Telefono"]}")

def actualizar():
    nombre_buscado = input("Dime el nombre de la persona que quieres actualizar: ")
    for contacto in contactos:
        if contacto["nombre"] == nombre_buscado:
            campo_actualizar = input(f"Escribe 1 si quieres actualizar el nombre: {contacto["nombre"]}\nEscribe 2 si quieres actualizar el teléfono: {contacto["Telefono"]}\n? ")
            if campo_actualizar == "1":
                nombre_nuevo = input("Introduce el nuevo nombre: ")
                contacto["nombre"] = nombre_nuevo
            elif campo_actualizar == "2":
                telefono_nuevo = input("Introduce el nuevo número de teléfono: ")
                contacto["Telefono"] = telefono_nuevo
    menu_principal()

def eliminar():
    nombre_buscado = input("Dime el nombre de la persona que quieres eliminar: ")
    for contacto in contactos:
        if contacto["nombre"] == nombre_buscado:
            confirmar_eliminacion = input(f"Estas seguro quer quieres eliminar los datos de:  {contacto["nombre"]} Telefono:  {contacto["Telefono"]}(S/N)?: ")
            if confirmar_eliminacion == "S":
                contactos.remove(contacto)
            else:
                print("Ok no lo eliminamos")
                menu_principal()







# Menú de seleccionar acción:
def menu_principal():
    print("Escoge la acción que quieres hacer en tu agenda?")
    print("1 búsqueda contacto")
    print("2 añadir contacto")
    print("3 actualizar contacto")
    print("4 eliminar contacto")
    accion_menu = input()
    if accion_menu == "1":
        buscar()
    elif accion_menu == "2":
        añadir()
    elif accion_menu == "3":
        actualizar()
    elif accion_menu == "4":
        eliminar()
    
    print(contactos)

menu_principal()
print(contactos)