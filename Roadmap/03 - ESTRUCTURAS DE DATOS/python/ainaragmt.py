# Listas
print("\nListas")
my_list = [1,3,7,5,8,2,0]
print(my_list)
print(type(my_list))
my_list.append(10) # insertar
print(my_list)
my_list.remove(5) # eliminar
print(my_list)
my_list[2] = 4 # acceder y actualizar
print(my_list)
my_list.sort() # ordenar
print(my_list)

# Tuplas (no modificables)
print("\nTuplas")
my_tuple = ("Ainara", "ainaragmt", "Python")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[1]) # acceder
my_tuple = tuple(sorted(my_tuple)) # ordenar una tupla
print(my_tuple)

# Sets (estructura desordenada)
print("\nSets")
my_set = {"Ainara", "ainaragmt", "Python"}
print(my_set)
print(type(my_set))
my_set.add("ainaragmt@gmail.com") # insertar
print(my_set)
my_set.add("ainaragmt@gmail.com") # no se vuelve a insertar (no hay datos duplicados)
print(my_set)
my_set.remove("Python") # eliminar
print(my_set)
# my_set.update() sirve para concatenar más datos
# si queremos actualizar algún dato lo mejor es eliminarlo y insertarlo

# Diccionario
print("\nDiccionario")
my_dict = {
    1: {"name": "Ainara", "number": 1},
    3: {"name": "Marta", "number": 2},
    2: {"name": "Lucía", "number": 3}
}
print(my_dict)
print(my_dict[1])
print(type(my_dict))
del my_dict[1] # eliminar
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ordenar
print(my_dict)

'''
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''
print("\nEjercicio de dificultad extra") # idea: crear una función

salir = 0
agenda = {
    "Ainara": 1234
}

while salir == 0:
    print(f"\nAgenda: {agenda}\n")

    # idea: match + case
    x = int(input("Elige la función que desees y pulsa enter: \n1. Buscar contacto\n2. Insertar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n5. Salir\n"))
    while x != 1 and x != 2 and  x != 3 and x != 4 and x != 5:
        print("\nEl número elegido no existe.\n")
        x = int(input("¿Qué quieres hacer? \n1. Buscar contacto\n2. Insertar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n"))
    print(x)

    if x == 5:
        salir = 1

    elif x == 1:
        nombre = str(input("\nEscribe el nombre del contacto que quieres buscar: "))
        if nombre in agenda:
            print(f"El número de {nombre} es {str(agenda[nombre])}")
        else:
            print(f"{nombre} no está en la lista.")

    elif x == 2:
        nombre = input("\nEscribe el nombre del contacto que quieres añadir: ")
        numero_str = input("Escribe el número del contacto que quieres añadir: ")
        # idea: numero.isdigit()
        try:
            numero_int= int(numero_str)
            if len(numero_str) > 11:
                print("Error: Número con más de 11 dígitos.\n")
            else:
                agenda[nombre] = numero_int
                print("\nContacto añadido:")
        except ValueError:
            print("Error: Número no numérico.\n")
    
    elif x == 3:
        # idea: codigo repetido del case 2 -> crear una función común
        nombre = input("\nEscribe el nombre del contacto que quieres actualizar: ")
        if nombre not in agenda:
            print("El contacto no está en la agenda\n")
        else:
            numero_str = input("Escribe el número del contacto que quieres actualizar: ")
            try:
                numero_int= int(numero_str)
                if len(numero_str) > 11:
                    print("Error: Número con más de 11 dígitos.\n")
                else:
                    agenda[nombre] = numero_int
                    print("\nContacto actualizado:")
            except ValueError:
                print("Error: Número no numérico.\n")

    elif x == 4:
        nombre = str(input("\nEscribe el nombre del contacto que quieres eliminar: "))
        if nombre not in agenda:
            print("El contacto no está en la agenda\n")
        else:
            del agenda[nombre]