# #03 ESTRUCTURAS DE DATOS

# Listas
my_list = ["Antonio", "Pedro", "Juan", "José"]
print (my_list)
my_list.append ("Axel")
print (my_list)
print (my_list [2]) # Acceso
(my_list [2]) = "Michael" # Actualización
print (my_list)
my_list.sort() # Ordenación
print (my_list)

## Tuplas
my_tuple = ("Antonio", "Mendoza", "@tony", "29")
print (my_tuple)
print (my_tuple [3]) #acceso
my_tuple= tuple (sorted(my_tuple)) # ordenación 
print (my_tuple)
print (type(my_tuple))

# Sets 
my_set = {"Antonio", "Mendoza", "@tony", "29"}
print (my_set)
my_set.add ("antonio@gmail.com") #inserción
print (my_set) 
my_set.remove ("Mendoza") #eliminación
print (my_set)
my_set = set(sorted(my_set)) # no se puede ordenar
print (my_set)

print (type(my_set))

# Diccionario
my_dict: dict = {
    "name": "Antonio", 
    "surname": "Mendoza", 
    "Alias": "@tony", 
    "edad": "29"
}
print (my_dict)
my_dict ["email"] = "antonio@gmail.com" # Inserción
print (my_dict)
del my_dict["surname"] # Eliminación
print (my_dict)
print (my_dict["name"]) #Acceso
my_dict ["edad"] = "30" # Actualización
print (my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print (my_dict)
print (type(my_dict))

# ejercicio extra

def agenda():

    mi_agenda = {}

    def agregar_telf():
        cel = input ("Escribe el teléfono del contacto: ")
        if cel.isdigit() and len(cel) > 0 and len(cel) <= 11:
            mi_agenda [nombre] = cel
        else:
            print ("tu número de telefono tiene más de 11 digitos")
            print ("vuelve a escribir tu número de teléfono")

        

    while True:
        print ("")
        print ("Hola, esto es una agenda de contactos")
        print ("Elije una opción:")
        print ("")
        print ("1. agregar nuevo contacto a la agenda ")
        print ("2. Busqueda de contacto en la agenda ")
        print ("3. Actualización de algún contacto en la agenda")
        print ("4. Eliminar contacto de la agenda")
        print ("5. Salir de la agenda")

        option = input ("\nEscribe tu opción aquí: ")

        match option:
            case "1":
                nombre = input ("Escribe el nombre del contacto: ")
                agregar_telf()
                    
            case "2":
                nombre = input ("Escribe el nombre del contacto que deseas buscar: ")
                if nombre in mi_agenda:
                    print (f"el número de teléfono de {nombre} es: {mi_agenda[nombre]}")
                else:
                    print (f"el contacto {nombre} no existe.")
                
            case "3":
                nombre = input ("Escribe el nombre del contacto que deseas actualizar: ")
                if nombre in mi_agenda:
                    agregar_telf()

            case "4":
                nombre = input ("Escribe el nombre del contacto que quieres eliminar ")
                if nombre in mi_agenda:
                    del mi_agenda [nombre]
                else:
                    print (f"el contacto {nombre} no existe.")
                
            case "5":
                print ("Saliendo de agenda...")
                break
            case _:
                print ("debes elegir del 1 al 5")

agenda()

