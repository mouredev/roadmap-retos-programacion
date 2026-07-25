'''
ESTRUCTURA DE DATOS
python ofrece diferentes estructuras que permiten organizar, almacenar y manipular datos de diferentes maneras
'''

#0-1 listas

my_list = [1,2,3,"hola", 4.2, True] #se puede almacenar elementos de cualquier tipo se pueden modificar
print(my_list) 


#insersion de listas
my_list.append("hola")
my_list.insert(2,"adios")
print(my_list) 

#eliminacion de listas

my_list.remove("hola")
my_list.pop(3)
print(my_list) 

#slicing listas recourre la lista y la guarda

my_second_list = my_list[1::2]
print(my_second_list)

#actualizacion de lista

my_second_list[0] = "actualice lista" 
print(my_second_list)

#ordenar listas

desorder_list = [6,3,7,2,100,6,3,1]

desorder_list.sort()
print(desorder_list)

#tuplas
my_tuple = (1,2,3,"adios", 3.2, False) #listas pero nose peuden modificar
print(my_tuple)


#acceder a los datos
print(my_tuple[0])

#convertir en lista para que sea modificable

list_temporal = list(my_tuple)

list_temporal.append("insersion de datos a la lista")
my_tuple = tuple(list_temporal)

print(my_tuple)

#diccionario
#tipo de almacenamieto en par donde se almacena su clave y su valor y se puede modificar
my_dictionary = {"uno" : 1, "dos" : 2, "hello": "hola", "estado": False, "decimal" : 3.2} 
print(my_dictionary)

#insercion de datos en diccionarios
my_dictionary['nuevo numero'] = 100


#eliminacion de datos

del my_dictionary["estado"]
print(my_dictionary)
print(my_dictionary.pop("hello"))
print(my_dictionary)

#conjuntos
#se puede almacenar cualquier valor y modificar pero con elementos unicos y su orden siempre varia
my_set = { 3, 3, 5, 1, 2, 2, "hola", "hola", False, False}
print(my_set)

my_frozenset = frozenset([1, 2, 3, 3, 4, "hello", False]) #esto es un conjunto pero en este cambia que no se pueda modificar
print(my_frozenset)


#operaciones matematicas con set

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión (elementos en A o B)
union = A | B  # {1, 2, 3, 4, 5, 6}
print(union)

# Intersección (elementos en A y B)
interseccion = A & B  # {3, 4}
print(interseccion)

# Diferencia (elementos en A pero no en B)
diferencia = A - B  # {1, 2}
print(diferencia)

# Diferencia simétrica (elementos en A o B, pero no en ambos)
dif_simetrica = A ^ B  # {1, 2, 5, 6}
print(dif_simetrica)



#cadenas

my_string = "esto tambien es una estructura de datos" #secuencia inmutable de caracteres
print(my_string)


def agenda_contactos():
    list_contact={}
   
    while True:
            accion = input("Bienvenido a la agenda de sus contactos \n"
            "Introduzca alguna de las siguientes opciones: \n"
            "1. Guardar Contacto\n"
            "2. Buscar Contacto\n"
            "3. Eliminar Contacto\n"
            "4. Actualizar Contacto\n"
            "0. Salir de la lista de Contactos\n"
            "Intrduzca el numero de la opcion que desa ----->")
            
    
            match accion:
                case "1":
                    name_contact = input("Como desea que se llame el nuevo contacto\n")
                    if name_contact in list_contact:
                        print("El contacto ya existe")
                    else:
                        number_contact = input("Introduzca el numero\n")
                        if len(number_contact) > 11:
                    
                            print("debe ingresar un numero menor a 11 digitos\n")
                        else:
                            list_contact[name_contact] = number_contact
                            print(f"Su numero a sido agregado asi quedo sus contactos\n {list_contact}\n")
                case "2":
                    name_contact = input("Ingrese el nombre del contacto que desea buscar\n")
                    if name_contact not in list_contact:
                           print("El contacto no existe\n")
                    else:
                         print(f"El numero de {name_contact} es = {list_contact[name_contact]}")
                case "3":
                    name_contact = input("Ingrese el nombre del contacto que desea eliminar\n")
                    if name_contact not in list_contact:
                        print("El contacto no existe")
                    else:
                         del list_contact[name_contact]
                         print(f"El contacto {name_contact} a sido eliminado, su agenda quedo asi\n {list_contact}\n")
                case "4":
                    name_contact = input("Ingrese el nombre del contacto que desea editar\n")
                    if name_contact not in list_contact:
                         print("El contacto no existe")
                    else:
                        number_contact = input("Ingrese el numero nuevo\n")
                        if len(number_contact) > 11:
                            print("el numero no peude ser mayor a 11 digitos")
                        else: 
                            list_contact[name_contact] =  number_contact  
                            print(f"El contacto de {name_contact} a sido actualizaado con el numero {number_contact} asi quedo sus contacto\n {list_contact}")   
                case "0":
                      print("salio del programa. Adios")
                      break
                case _:
                      print("No valido ingrese un dato que sea valido")  

              
                
                           
agenda_contactos()