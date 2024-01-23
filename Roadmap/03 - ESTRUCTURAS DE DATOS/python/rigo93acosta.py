'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
'''

## List
list_1 = []
list_2 = list()
print(type(list_1))
list_3  = ["Hola", "mundo"]
print(list_3)
list_3.append("!")
print(list_3)
list_3.remove("Hola")
print(list_3)
print(list_3[0])
list_3[0] = "Rigo"
print(list_3)
list_3.sort()
print(list_3)

## Tuple
# Tipo Inmutable
tuple_1: tuple = ("Rigo", "Acosta", "@rigo93acosta", "30")
print(tuple_1)
print(type(tuple_1))
tuple_1 = tuple(sorted(tuple_1)) # Sort truco
print(tuple_1)
print(type(tuple_1))

## Sets
my_set = {"Rigo", "Acosta", "@rigo93acosta", "30"}
print(my_set)
print(type(my_set))
my_set.add("rigo93acosta@gmail.com") # Insert
print(my_set)
# print(my_set[0]) # Estructura superoptima, no hay posicion directa
my_set.add("rigo93acosta@gmail.com") # Evita datos duplicados (No lo inserta)
print(my_set)
my_set.remove("Rigo")
print(my_set)
# La actualización sería eliminando y luego insertando. No confundir con el update
print(sorted(my_set))
print(set(sorted(my_set))) # La ordenación carece de sentido pues las posiciones no son fijas

## Dictionary
dict_1: dict = {"name": "Rigoberto", "surname": "Acosta", "alias": "@rigo93acosta", "age": "30"}
print(dict_1)
print(type(dict_1))
dict_1["email"] = "rigo93acosta@gmail.com"  # Insert
print(dict_1)
# print(dict_1[0])  # Error 
print(dict_1["name"]) # Correct!
dict_1["name"] = "Rigo" # Update
print(dict_1)
del dict_1["email"] # Delete
print(dict_1)
# Sort
dict_1 = sorted(dict_1.items())
print(dict_1)
dict_1 = dict(dict_1)
print(dict_1)


## Extra
## Puede mejorarse el check del número de teléfono
## y del nombre con funciones.

agenda = {}

def get_number_phone():
    pass

while True:
    print("Agenda Telefónica:")
    print("1- Insertar")
    print("2- Buscar")
    print("3- Actualizar")
    print("4- Eliminar")
    print("5- Ver Agenda")
    print("Escriba 'Exit' para salir\n")
    answer = input("Selecciona una opción: ")
    
    if answer == "Exit":
        break
    
    elif int(answer) == 5:  # View Agenda
        if len(agenda) == 0:
            print("\nAgenda Empty\n")
        else:
            for name, number in agenda.items():
                print(f'Nombre: {name} -> Teléfono: {number}\n')
    
    elif int(answer) == 1: # Insert
        name = input("\nEscriba el nombre: ")
        if name in agenda.keys(): # Check name
            print("\nEste contacto esta agendado.\n")
        else:
            number_phone = input("Escriba el número de teléfono: ") # Check new number
            number_len = len(number_phone)
            while True:
                if number_len > 0 and number_len <= 11 and number_phone.isnumeric(): # Check new number
                    agenda[name] = int(number_phone)
                    break
                else:
                    print("El número es incorrecto, repita de nuevo")
                    number_phone = input("Escriba el número de teléfono: ")
                    number_len = len(number_phone)
                    
    
    elif int(answer) == 2: # Search
        print("\nBuscar por: \n1-Nombre: \n2-Número:")
        answer = input("Inserte opción: ")
       
        if int(answer) == 1: 
            name = input("\nEscriba el nombre: ")
            if name in agenda.keys(): # Check name
                print(f'\nNombre: {name} -> Teléfono: {agenda[name]}\n')
            else:
               print("\nEl nombre no está agendado\n") 
        
        elif int(answer) == 2:
            number_phone = input("Escriba el número de teléfono: ") # Check new number
            number_len = len(number_phone)
            while True:
                if number_len > 0 and number_len <= 11 and number_phone.isnumeric(): # Check new number
                    
                    if int(number_phone) in agenda.values():
                        for name_1, number_1 in agenda.items(): # Search name link number phone
                            if int(number_phone) == number_1:
                                print(f'\nNombre: {name_1} -> Teléfono: {number_1}\n')
                            break
                    else:
                        print("\nEl número de teléfono no está agendado\n")
                    break
                else:
                    print("El número es incorrecto, repita de nuevo")
                    number_phone = input("Escriba el número de teléfono: ")
                    number_len = len(number_phone)

            if int(number_phone) in agenda.values(): # Ch
                for name_1, number_1 in agenda.items(): # Search name link number phone
                    if int(number_phone) == number_1:
                        print(f'\nNombre: {name_1} -> Teléfono: {number_1}\n')
            else:
                print("\nEl número de teléfono no está agendado\n")

    elif int(answer) == 3: # Update
        print("\nActualizar: \n1-Nombre: \n2-Número:")
        answer = input("Inserte opción: ")
        
        if int(answer) == 2:
            name = input("Escriba el nombre: ")
            if name in agenda.keys(): # Check name
                number_phone = input("Escriba el número de teléfono: ") # Check new number
                number_len = len(number_phone)
                while True:
                    if number_len > 0 and number_len <= 11 and number_phone.isnumeric(): # Check new number
                        agenda[name] = int(number_phone) # Change Number
                        break
                    else:
                        print("El número es incorrecto, repita de nuevo")
                        number_phone = input("Escriba el número de teléfono: ")
                        number_len = len(number_phone)
            else:
                print("\nEl nombre no está agendado\n")
        
        elif int(answer) == 1:
            number_phone = input("Escriba el número de teléfono: ") # Check new number
            number_len = len(number_phone)
            while True:
                if number_len > 0 and number_len <= 11 and number_phone.isnumeric(): # Check new number
                    number = number_phone
                    break
                else:
                    print("El número es incorrecto, repita de nuevo")
                    number_phone = input("Escriba el número de teléfono: ")
                    number_len = len(number_phone)    
            
            name = input("Escriba el nombre: ")
            if int(number) in agenda.values(): # Existe el numero
                for name_1, number_1 in agenda.items():
                    if int(number) == number_1:
                        temp_name = name_1 # Nombre Viejo
                        break
                agenda[name] = int(number) # Nombre Nuevo
                del agenda[temp_name] # Eliminando contancto con Nombre Viejo
            else:
                print("\nEl número de teléfono no está agendado\n")
    
    elif int(answer) == 4: # Delete
        print("\nEliminar empleando: \n1-Nombre: \n2-Número:")
        answer = input("Inserte opción: ")

        if int(answer) == 1:
            name = input("\nEscriba el nombre: ")
            if name in agenda.keys(): # Check name
                del agenda[name]
            else:
                print("\nEl nombre no está agendado\n")
        
        elif int(answer) == 2:
            number_phone = input("Escriba el número de teléfono: ") # Check new number
            number_len = len(number_phone)
            while True:
                if number_len > 0 and number_len <= 11 and number_phone.isnumeric(): # Check new number
                    number = number_phone
                    break
                else:
                    print("El número es incorrecto, repita de nuevo")
                    number_phone = input("Escriba el número de teléfono: ")
                    number_len = len(number_phone)

            if int(number) in agenda.values(): # Existe el numero
                for name_1, number_1 in agenda.items():
                    if int(number) == number_1:
                        break
                del agenda[name_1] # Eliminando contancto con Nombre Viejo
            else:
                print("\nEl número de teléfono no está agendado\n")

    else: # No case
        print("\nElige una de las opciones\n")