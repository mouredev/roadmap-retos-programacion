#Listas: estructura que sirve para guardar varios elementos de forma ordenada

my_list: list = ["Yani", "Inés", "Pedro", "Tomás"]

print (my_list)

my_list.append ("Castor") # inserción 
my_list.append ("Castor")
print (my_list)

my_list.remove ("Yani") # eliminación

print (my_list)

"""
para poder actualizar un elemento de la lista primero hay que acceder al elemento 
hay que acceder por la posición que ocupa el elemmento
"""
my_list[1]

print (my_list[1]) #acceso 

my_list[1] = "Patricia" # si quisiera actualizar a Pedro tendría que acceder a la lista y a su posición darle un nuevo valor por ej: Patricia 
 
print (my_list) 

my_list.sort ()  #oredenación  # por defecto sigue un criterio designado por el sistema 

print (my_list)  #sort:  ordena alfabeticamente 

print (type(my_list))

# Tuplas: estructuras donde podemos guardar mas de un dato
#las tuplas son inmutables, como están creadas quedarán, la iliminación, inserción, actualización etc. no existirá en la tupla

my_tuple: tuple = ("Yani", "Barr", "Yanines", "47")

print (my_tuple[1]) #lo único que podría hacer con la tupla son operaciones de acceso

print (my_tuple[3])

my_tuple = tuple (sorted (my_tuple))  # se puede hacer la ordenación con cierto truco 

print (my_tuple)

print (type(my_tuple))

#Sets:sirven para evitar duplicados,  son otro tipo de estructuras, es desordenado, no podemos confiar en la posición que vaya a agregar el elemento, los set son ideales para guardar muchos datos y recorrerlos pero NO para buscar datos 

my_set = {"Yani", "Barr", "Yanines", "47"}

print (my_set)

my_set.add ("yanines2025@gmail.com") #inserción 

my_set.add ("yanines2025@gmail.com") #no se pueden agregar duplicados, esta estructura observa que el elemento está insertado y no agrega el duplicado  

print (my_set)

my_set.remove("Yanines") #eliminación 

print (my_set)

my_set  = set (sorted (my_set)) #el set no se puede ordenar

print (my_set)

print (type(my_set))

#diccionario: hay que agregarle una clave 

my_dict: dict = {
    "name":"Yani", 
    "surname": "Barr", 
    "alias": "Yanines", 
    "age": "47"
}

my_dict ["email"] = "yanines2025@gmail.com"  #inserción 
print (my_dict)

del my_dict ["surname"] #eliminación 

print (my_dict)

print (my_dict["name"]) #acceso 

my_dict ["age"] = "48" #actualización 

my_dict = dict (sorted (my_dict.items ())) # ordenación 

print (my_dict)

print (type(my_dict))

"""
Extra 

"""

def my_agenda ():

    agenda = {}

    def insert_contact(): 
            phone = input ("Introduce el numero del contacto : ")
            if phone.isdigit () and len(phone) >0 and len(phone) <= 8:
                        agenda [name] = phone
            else: 
                print (
                        "Debes introducir un  número de teléfono con menos de 11 dígitos.")

    while True: 


        print ("")
        print ("1. Buscar contacto")
        print ("2. Insertar contacto")
        print ("3. actualizar contacto")
        print ("4. eliminar contacto")
        print ("5. salir")

        option = input ("\nSelecciona una opción: ")


        match option:

            case "1":

                name = input ("Introduce el nombre del contacto a buscar: ") # Buscar
                if name in agenda:
                    print (f"El número de teléfono {name} es {agenda [name]}.")
                else:
                    print (f"El contacto y el nombre {name} no se ha encontrado. ")
            
            case "2":

                name = input ("Introduce el nombre del contacto : ")  # Insertar 
                #phone = input ("Introduce el numero del contacto : ")

                insert_contact()
           
            case "3":

                name = input ("Introduce el nombre del contacto a actualizar: ") # Actualizar 
                if name in agenda:
                    insert_contact()
                else:
                    print (f"el contacto {name} no existe.")    
           
            case "4":

                name = input ("Introduce el nombre del contacto a eliminar: ")   # Eliminar
                if name in agenda:
                    del agenda [name]
                else: 
                    print (f"El contacto {name} no existe.")
          
            case "5":
                    
                    print ("Saliendo de la agenda.")
                    break
           
            case _:

                print ("Opción no válida. Elige una opción del 1 al 5.")

  
  
  
    """

    if option == "1":
        elif option == "2": 
            
    """

my_agenda()