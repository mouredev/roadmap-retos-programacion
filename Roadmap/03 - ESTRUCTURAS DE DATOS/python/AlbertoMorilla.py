# #03 ESTRUCTURAS DE DATOS


## Ejercicio
 #- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 #- Utiliza operaciones de inserción, borrado, actualización y ordenación.
 
### LISTAS

nombres = ['Alberto', 'Ana', 'Laura', 'Teresa', 'Carmen', 'Daniel']
print(type(nombres))

varios = ['Hola', 150, True]
print(type(varios))

print (nombres[2])
print (nombres[-1])
print (type(varios[1]))

nombres[3:4] = ['Maria Teresa', 'MariCarmen']
print (nombres)

nombres.append('Leo')
print (nombres)

nombres.extend(["Angel", "Pablo"])
print (nombres)

nombres.remove('Ana')
print (nombres)

nombres.insert(1, 'Maria')
print (nombres)

nombres.pop(5)
print (nombres)

nombres.sort()
print (nombres)

clasificacion = [10,7,5,3,1,3]
print (clasificacion.count(3))

print (clasificacion.index(3))

print ('8' in clasificacion)

nombres.clear()
print (nombres)

## TUPLAS

colores = ("azul", "verde", "rojo", "negro")
numero = (2,)

print(type(numero))
print(type(colores))
print (colores[0])
print (colores[-1])
print(colores.index('verde'))
print(colores.count('azul'))
print('rojo' in colores)

## SETS

pesos1 = {22, 66, 25}
pesos2 = set([85,55,96,47,122])
print(pesos2)
print(type(pesos1))
print(pesos1.intersection(pesos2))

pesos2.add(77)
print(pesos2)

pesos2.remove(122)
print(pesos2)

pesos2.discard(51)
print(pesos2)

pesos2.pop()
print(pesos2)

pesos2.clear()
print(pesos2)

## DICCIONARIO

usuario = dict([
    ('nombre', 'Juan'),
    ('edad', 25),
    ('ciudad', 'Bogota')
])
ciudades = {'Alberto':'Sevilla', 'Laura':'Granada', 'Toni':'Madrid'}
print(usuario)

ciudades.popitem()
print (ciudades)
print (ciudades['Alberto'])

usuario2 = {'telefono':658987412}
usuario.update(usuario2)
print (usuario)

usuario.pop('edad')
print (usuario)

ciudades = sorted(ciudades.items())
print(ciudades)

ciudades.clear()
print (ciudades)

# DIFICULTAD EXTRA (opcional):
 # Crea una agenda de contactos por terminal.
 # - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 # - Cada contacto debe tener un nombre y un número de teléfono.
 # - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 #   los datos necesarios para llevarla a cabo.
 # - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 #   (o el número de dígitos que quieras)
 # - También se debe proponer una operación de finalización del programa.
 # - El programa debe mostrar la agenda de contactos al finalizar.

def mi_agenda ():

    def insert_contact():
        phone = input("\nIntroduce el telefono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("El telefono no es correcto, puede que tenga mas de 11 digitos")

    agenda = {}
    while True:

        print('1. Buscar contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Salir')

        option = input("\nSelecciona una opcion: ")

        match option:
            case '1':
                name = input('\nIntroduce el nombre del contacto que desea buscar: ')

                if name in agenda:
                    print(f"El número de telefono de {name} es {agenda[name]}.")
                else:
                    print('\nNo hay contactos con ese nombre')
                
            case '2':
                name = input("\nIntroduce el nombre del contacto: ")
                insert_contact()
        
            case '3':
                name = input("\nIntroduce el nombre del contacto que desea actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print('\nNo hay contactos con ese nombre')
                
            case '4':
                name = input("\nIntroduce el nombre del contacto que desea eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print('\nNo hay contactos con ese nombre')
                
            case '5':
                print('Saliendo de la agenda.')
                break
            case _:
                print("Opción no válida. Por favor, selecciona una opción válida.")

mi_agenda()