"""
ESTRUCTURAS DE DATOS
"""

# Listas -> para guardr varios datos de forma ordenada
my_list = ["Hosi", "Loli", "Paca"]
print(my_list)
my_list.append("Jacobo") #para INSERTAR elementos a la lista
print(my_list)
my_list.remove("Paca") #para ELIMINAR elementos de la lista
print(my_list)
print(my_list[1]) #para ACCEDER a la posición 1 
my_list[1]="Cosini" #para ACTUALIZAR la posición 1
print(my_list)
my_list.sort() #para ORDENAR
print(my_list)

#Tuplas -> estructuras inmutables donde guardar datos
my_tuple = ("Hosi", "Eloso", "20") # el 20 podría ser int pero con el SORTED nos daría problemas
print(my_tuple[1]) #solo puedo hacer operaciones de ACCESO
#si aplicaramos sorted a la tupla, nos devolverá una lista
#para evitar eso haremos:
my_tuple=tuple(sorted(my_tuple))
print (my_tuple)

#Sets -> NO se puede ORDENAR
my_set = {"Hosi", "Eloso", "20"}
print(my_set)
my_set.add("hosi@gmail.com") #no puedo añadir 2 veces lo mismo. los sets evitan DUPLICADOS
print(my_set)
my_set.remove("Eloso") #para eliminar elementos
print(my_set)
#sorted(my_set) #si aplicamos esto nos devolvería una LISTA
print(type(my_set)) 

# Diccionario
my_dict: dict = {
    "Nombre":"Hosi",
    "Apellido":"Eloso",
    "Edad":"20",
    "Email":"hosi@gmail.com"
} #asociamos una clave a cada valor
print(my_dict["Apellido"]) #para ACCEDER a un elemento
my_dict["Email"] = "Hosi@gmail.com" # para AÑADIR un elemento al diccionario
print(my_dict)
my_dict["Edad"] = "21" #para ACTUALIZAR elementos
print(my_dict)
del my_dict["Email"] #para ELIMINAR un elemento del diccionario
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # para ORDENAR
print(my_dict)


'''
Extra
'''
'''
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''

mi_agenda: dict = {
    "Hosi":123456789,
    "Loli":789456123,
    "Paca":456789123,
    "Jacobo":123789456
}

print("Tu agenda actual es:")
print(mi_agenda)
acabar="y"
while acabar=="y":
    print("Tienes las siguientes opciones:")
    print("1: Añadir un número")
    print("2: Editar un número")
    print("3: Eliminar un número")
    opc=input("Elige una opción: ")
    opc=int(opc)

    if opc == 1:
        i=0
        new_name=input("Introduce el nombre del nuevo contacto: ")
        while i < 1:
            new_num=input("Introduce el nuevo número: ") 
            digitos_num=len(new_num)
            new_num=int(new_num)
            if type(new_num)!=int or digitos_num>11:
                print("Introduce un número válido")
            else:
                mi_agenda[new_name] = new_num
                i+=1
    elif opc == 2:
        act_nombre=input("Introduce el nombre del contacto que se quiere actualizar: ")
        new_num=input("Introduce el nuevo número: ")
        new_num=int(new_num)
        mi_agenda[act_nombre]=new_num 
    elif opc == 3:
        bor_nombre=input("Introduce el nombre del contacto a eliminar")
        del mi_agenda[bor_nombre]

    print("Ahora tu agenda es la siguiente:")
    print(mi_agenda)
    acabar=input("Quieres hacer algo más? [y/n]: ")

print("Fin")

'''
SU SOLUCIÓN:
def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()



'''
