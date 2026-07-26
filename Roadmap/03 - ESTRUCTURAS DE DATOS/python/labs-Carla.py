#Listas
## Mutable el orden es de inserción por defecto
zodiac_signs = ["Virgo", "Géminis", "Acuario"] #se crean con corchetes las listas
print(zodiac_signs)
zodiac_signs.append("Libra") #agrega
print(zodiac_signs)
zodiac_signs.remove("Géminis") #elimina elemento de la lista
print(zodiac_signs)
print(zodiac_signs[0]) #acceso al elemento
zodiac_signs[1] = "Capricornio" #cambiamos elemento de la lista por otro con su posicion
print(zodiac_signs)
zodiac_signs.sort() #ordena alfabeticamente
print(zodiac_signs)

#Tupla
## Inmutables 
my_tupla_planetas = "Sol", "Mercurio", "Plutón", "Urano"
print(my_tupla_planetas)
print(my_tupla_planetas[0]) #acceso
my_tuple = tuple(sorted(my_tupla_planetas)) # tuple convierte a tupla lo que se convierta a lista con sorted
print(type(my_tuple))
print(my_tuple)

#Sets
## Estructura desordenada, se genera un hash

my_set = {"Marte", "Neptuno", "Luna", "Jupiter"}
my_set.add("Venus") #inserción
my_set.remove("Luna") #eliminar
my_set = set(sorted(my_set)) #no se puede ordenar
print(type(my_set))
print(my_set)

#Diccionario
##No es una estructura de datos ordenada

my_dict:dict = { #carta natal como diccionario
"Nombre": "Carla", 
"Edad": "25",
"Ascendente": "Capricornio",
"Sol": "Virgo",
"Luna": "Cancer"
}
print(my_dict["Nombre"]) #acceso
my_dict["Medio Cielo"] = "Aries" #agrego
print(my_dict)
my_dict["Edad"] = "26" #actualizo
print(my_dict)
del my_dict["Sol"] #elimino
print(my_dict)
my_dict = dict(sorted(my_dict.items())) #ordena
print(my_dict)
print(type(my_dict))

#Extra

def my_agenda():

    agenda = {}

    def insertar_contacto():
        if phone.isdigit() and len(phone) > 0 and len(phone) <11: 
            agenda[name]=phone
        else:
            print("No es un número válido. Intenta nuevamente.")

    is_on= True

    while is_on:

        print("")
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("Selecciona una opción\n")

        match option:
            case "1":
                name = input("Ingresa el nombre que deseas buscar:")
                if name in agenda:
                    print(f"El teléfono de {name} es: {agenda[name]}.") #name:phone
                else:
                    print(f"El contacto {name} no existe.")
                pass
            case "2":
                name = input("Ingresa el nombre\n")
                phone =input("Ingresa número\n")
                insertar_contacto()
            case "3":
                name = input("Ingresa el nombre")
                if name in agenda:
                    phone = input("Nuevo numero: ")
                insertar_contacto()
                pass
            case "4":
                name = input("Ingresa el nombre")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado exitosamente.")
                else:
                    print(f"El contacto {name} no existe.")

                pass
            case "5":
                print("Saliendo de la agenda...")
                is_on = False
            case _:
                print("Opción no válida, vuelve a elegir")
                
my_agenda()


