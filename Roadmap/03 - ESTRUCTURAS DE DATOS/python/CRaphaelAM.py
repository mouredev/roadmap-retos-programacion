"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

#LISTAS
# Creación de una lista
mi_lista = [10, 20, 30, 40]

# Inserción
mi_lista.append(50)           # Agrega al final
mi_lista.insert(2, 25)        # Inserta el valor 25 en el índice 2

# Actualización
mi_lista[0] = 5               # Cambia el primer elemento

# Borrado
mi_lista.remove(40)           # Elimina el valor 40
del mi_lista[1]               # Elimina el elemento en el índice 1

# Ordenación
mi_lista.sort()               # Ordena de menor a mayor

print(mi_lista)  # [5, 25, 30, 50]

#TUPLAS
# Creación de una tupla
mi_tupla = (10, 20, 30, 40)

# Las tuplas no soportan inserciones, eliminaciones ni actualizaciones porque son inmutables
print(mi_tupla)

#SETs
# Creación de un conjunto
mi_conjunto = {10, 20, 30, 40}

# Inserción
mi_conjunto.add(50)  # Agrega un nuevo elemento

# Borrado
mi_conjunto.remove(30)  # Elimina el elemento 30

# Actualización
# No hay actualización directa en un conjunto, pero puedes eliminar y volver a agregar un elemento

# Ordenación (los conjuntos no tienen un orden definido, por lo que primero debemos convertirlo en una lista)
conjunto_ordenado = sorted(mi_conjunto)

print(conjunto_ordenado)  # [10, 20, 40, 50]


#DICCIONARIOS
# Creación de un diccionario
mi_diccionario = {'nombre': 'Un Nombre', 'edad': 26, 'profesion': 'Doctor'}

# Inserción
mi_diccionario['pais'] = 'España'  # Agrega una nueva clave-valor

# Actualización
mi_diccionario['edad'] = 27      # Actualiza el valor de la clave 'edad'

# Borrado
del mi_diccionario['profesion']  # Elimina la clave 'profesion'

# Ordenación (los diccionarios no son ordenados, pero puedes ordenar las claves y luego acceder a sus valores)
diccionario_ordenado = dict(sorted(mi_diccionario.items()))

print(diccionario_ordenado)  # {'edad': 27, 'nombre': 'Carlos', 'pais': 'Cuba'}

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

print("************Dificultad Extra*************")

agenda = {}
continuar = True

while continuar:
    error = True
    while error:
        print(""" *****Agenda de contactos*****
        1 - Agregar un contacto.
        2 - Actualizar un contacto.
        3 - Buscar un contacto.
        4 - Eliminar un contacto.
        5 - Salir.
        """)
        opcion = input("Que operacion desea realizar?: ")

        if int(opcion)>5 or int(opcion) <1:
            print("Debe ingresar una opcion valida.")
        else: error = False

    print("Procesando solicitud...")

    match opcion:
        case '1':
            error_entrada = True
            while error_entrada:
                print("Ingrese los datos del contacto que desea agregar: ")
                nombre = input("Ingrese el nombre: ")
                telefono = input("Ingrese el telefono: ")
                if len(telefono) != 11 or not telefono.isdigit():
                    print("Por favor ingrese un numero con formato correcto.")
                    continue
                error_entrada = False
                    
            if nombre in agenda:
                print("El contacto parece estar registrado en la agenda.")
            else: 
                agenda[nombre] = telefono
                print("Contacto agregado a la agenda con exito.")
        
        case '2': 
            nombre = input("Ingrese el nombre del contacto que desea modificar: ")
            if nombre in agenda:
                telefono = input("Ingrese el nuevo número de teléfono del contacto: ")
                agenda[nombre] = telefono
                print("Contacto actualizado correctamente.")
            else: print("El contacto no esta registrado en la agenda.")
        
        case '3':
            print("Desea buscar el contacto por nombre o numero de telefono?: ")
            criterio = input("1- Nombre\t\t2- Telefono\nOpcion:")

            if criterio == '1':
                nombre = input("Ingrese el nombre que desea buscar: ")
                if not nombre in agenda:
                    print("El nombre ingresado no esta registrado en la agenda.")
                else:
                    print(f"""
                        Informacion de contacto:
                        Nombre: {nombre}
                        Telefono: {agenda[nombre]}
                    """)
            elif criterio == '2':
                telefono = input("Ingrese el telefono que desea buscar: ")
                for nom,telef in agenda.items():
                    if telefono == telef:
                        print(f"""
                        Informacion de contacto:
                        Nombre: {nom}
                        Telefono: {telef}
                        """)
            else: print("La opcion ingrasada no es valida.")

        case '4':
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
            else: print("El nombre ingresado no se encuentra registrado en la agenda.")

    if opcion != 5:
        continuar = input("Desea realizar otra operacion? 1- Si 2- No : ")
        continuar = True if continuar == '1' else False
    else: break

print("Saliendo del programa...")
