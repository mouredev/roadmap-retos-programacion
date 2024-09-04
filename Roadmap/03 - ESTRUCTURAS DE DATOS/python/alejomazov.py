



##sets 

my_set = {"Alejandro", "Kevin", "Carmenza", 36} # no se puede ordenar y no se repiten
my_set.add (24)
my_set.add (24)
print (my_set)
my_set.remove ("Alejandro")
print(my_set)

#diccionarios

diccionario = {
    "nombre": "alejandro",
    "edad":24, 
    "apellido":"Mazo"
    }
print (diccionario)

diccionario["sexo"] = "Masculino"
print (diccionario)
del diccionario["edad"]
print (diccionario)
print(list(diccionario))
print (sorted(diccionario))


#Tuplas
tuplas:tuple = ("hola", "Kevin", "Carmenza", 36) # pueden ser de distintos tipos, pero son inmutables
print (tuplas[1])

#Listas 

lista = [1,2,3,4,5,6,6] #Es mutable, se pueden repetir elementos 
lista.append (5)
print(lista)
lista.sort()
print(lista)
lista.pop(2)
print(lista)
lista[2] = "Fabian"
print(lista)


##extra


contactos = {
    "Nombre":[],
    "Apellido":[],
    "Numero":[]
}
def menu():
    print("\n      Contactos\n\n¿Que operacion desea realizar?\n\n     ----Menu----")
    print("\n1. Agregar contacto.\n2. Buscar contacto\n3. Eliminar contacto.\n4. Actualizar contacto.\n5. Salir.\n ")

def agregar():
    print("Ingresa el nombre: ")
    nombre = str(input())
    contactos["Nombre"].append(nombre)
    print("Ingresa el apellido: ")
    apellido = str(input())
    contactos["Apellido"].append(apellido)
    while True:
        print("Ingresa el numero de telefono: ")
        try:
            numero = int(input())
            numero_str = str(numero)
            count = len(numero_str)
            if count <= 11:
                contactos["Numero"].append(numero)
                print ("contacto agregado")
                break
            else:
                print ("Ingrese un numero de 11 digitos")
        except ValueError as e:
            print(f"Ingrese un numero correcto.... error {e}")


def buscar():
    nombre = str(input("Ingrese el nombre de contacto que desea buscar:\n"))
    apellido = str(input("ingrese el apellido del contato que desea buscar:\n"))

    for nombres, apellidos, numeros in zip(contactos["Nombre"],contactos["Apellido"],contactos["Numero"]):
        if nombre == nombres and apellido == apellidos:
            print (nombres,apellidos, numeros)


def eliminar():
    nombre = str(input("Ingrese el nombre del contacto que desea eliminar:\n"))
    apellido = str(input("ingrese el apellido del contato que desea eliminar:\n"))

    for nombres, apellidos, numeros in zip(contactos["Nombre"],contactos["Apellido"],contactos["Numero"]):
        if nombre == nombres and apellido == apellidos:
            contactos["Nombre"].remove(nombre)
            contactos["Apellido"].remove(apellido)
            contactos["Numero"].remove(numeros)


            print("Usuario eliminado")

def actualizar():
    nombre = str(input("Ingrese el nombre del contacto que desea actualizar:\n"))
    apellido = str(input("ingrese el apellido del contato que desea actualizar:\n"))

    for i in range(len(contactos["Nombre"])):
     if nombre == contactos["Nombre"][i] and apellido == contactos["Apellido"][i]:
         update_tel = int(input("Ingrese el numero nuevo: "))
         contactos["Numero"][i] = update_tel
         print("Contacto actualizado")
         return



def salir():
    print("Saliendo...")



while True:
    menu()
    opcion= int(input())
    if opcion > 5 or opcion < 1:
        print("Seleccione una opcion del menu")
    else:
        if opcion == 1:
            agregar()    
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            eliminar()
        elif opcion == 4:
            actualizar()
        elif opcion == 5:
            salir()
            break    
        else:
            print("Selecione una opcion correcta")

        



