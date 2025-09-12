# ###############################################################################
# ###Estructuras de datos
# ###############################################################################
# array = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# lista = ["oro", "plata", "cobre", "hierro", "diamante"]

# tupla = (1, 3, 4, 5)

# diccionario = {"dani":34,
#                 "pedro":42,
#                 "ana": 56,
#                 "manolo": 15}

# mi_conjunto = {1, 9, 8, 5, 6, 2}


# #############################LISTA#############################################
# print("\nLista") 
# # insercion
# lista.append("estalacmita")
# lista.insert(1, "roca")
# print(lista)
# #borrado
# borrado = lista.pop(1)
# lista.remove("oro")
# print(lista) 
# #actualizacion
# lista[2] = "arena"
# print(lista)
# #ordenacion
# list_sorted = sorted(lista)
# print(list_sorted)
# lista.reverse()
# print(lista)


# ##############################MATRIZ###########################################
# print("\nMatriz") 
# #insercion
# array.append([10, 11, 12])
# #borrado
# array.remove([1, 2, 3])
# #actualizacion
# array[0][1] = "new"
# #ordenacion
# array.sort(reverse=True)
# print(array)


# ##########################TUPLA################################################
# print("\nTupla") 
# # insercion:
# tupla_a_lista = list(tupla)
# tupla_a_lista.append(22)
# tupla = tuple(tupla_a_lista)
# print(tupla)


# ###############################DICIONARIO######################################
# print("\nDicionario") 
# #insercion/actualizacion
# diccionario["ana"] = 5
# #borrado
# del diccionario["manolo"]
# #ordenacion
# sorted(diccionario.items())
# print(diccionario)


# #########################CONJUNTOS / sets ############################################
# print("\nconjuntos")
# #insercion
# mi_conjunto.add(15)
# #borrado
# mi_conjunto.remove(1)
# #actualizacion
# #inmutables
# #ordenacion:
# mi_lista_ordenada = set(sorted(mi_conjunto))
# print(type(mi_conjunto))
# print(mi_lista_ordenada)


# print()
# print()
# print()
# ##############################################################################
### DIFICULTAD EXTRA
##############################################################################

diary = dict()

def new_contact(name, phone):
    diary[name] = phone
    print(f"contacto {name} agregado")

def update_contact(name, phone):
    diary[name] = phone
    print(f"contacto {name} agregado")

def phone_contact(name):
    if name in diary:
        print()
        print(f"Numero Telefono: {diary[name]}")
        print()
    else:
        print(f"El contanto {name} no existe")
    
def remove_contact(name):
    if name in diary:
        del diary[name]
        print(f"{name} ha sido eliminado de la agenda")
    else:
        print(f"No se encontró el contacto {name}")


def main():
    while True:
        print("MENU:")
        print("1. Nuevo contacto")
        print("2. Buscar telefono de contacto")
        print("3. Eliminar un contacto")
        print("4. Cambiar numero de un contacto")
        print("5. ver agenda completa")
        print("6. salir")
        order = input("\ncuál es la operación que se quiere realizar:")
        if order=="6" or order=="salir":
            print("Adios!")
            break 
        else:
            options(order)

def options(order):    
    if order=="1" or order=="nuevo contacto":
        name = input("Nombre del contacto: ")
        phone = phone_number()
        new_contact(name, phone)
    
    elif order=="2" or order=="Buscar telefono de contacto":
         name = input("Nombre del contacto: ")
         phone_contact(name)

    elif order=="3" or order=="eliminar un contacto":
        name = input("Nombre del contacto: ")
        remove_contact(name)
    
    elif order=="4" or order=="cambiar numero de un contacto":
        name = input("Nombre del contacto: ")
        phone = phone_number()
        update_contact(name, phone)
    
    elif order=="5" or order=="ver agenda completa":
        for key, value in diary.items():
            print(f"{key}: {value}")   
    
    else:
        print("Error opcion no valida")   

def phone_number():
    while True:
        phone = input("Telefono del contacto: ")
        if phone.isdigit() and len(phone) == 9:
            break
        else:
            print("Numero de telefono no valido.")
            print("Por favor, escribe un numero valido.")
    return int(phone)
    
main()
