"""
Estructura de datos
"""

#Lista: Mutable (se puede modificar). Más lenta que la tupla. Se declara con []

lista = ['Jose', 'Daniel', 'Julio', 'Maria']
print(lista)

lista.append('Eddy') #insercion
print(lista)
lista.remove('Daniel') #Eliminacion
print(lista)
print(lista[2]) #imprimir la persona que esta en la posicion 2
lista[2] = 'Ana' #actulizacion, el que estaba en la posicion 2 desaparece
print(lista)
lista.sort() #ordenacion
print(lista)
print(type(lista))


#Tuplas: Inmutable (no se puede modificar). Más rápida que la lista. Se declara con ()
tupla: tuple = ('Jose', 'Feliciano', 'King', '20')
print(tupla[1]) #Feliciano
print(tupla[3]) #20
tupla = tuple(sorted(tupla)) #ordernar la tupla 
print(tupla)
print(type(tupla))



#Sets: Colección desordenada, sin índices. No permite elementos repetidos. Se declara con {} o set().
my_sets: set = {'Jose', 'Feliciano', 'King', '20'}
print(my_sets)
print(type(my_sets))
my_sets.add("Curso de programacion") #Inserccion
print(my_sets)
#print(my_sets[0]) # tendria sentido hacer esto porque es una coleccion sin indice (desordenada)
my_sets.remove('King') #Eliminacion
print(my_sets)
my_sets = set(sorted(my_sets)) #No se puede ordenar
print(my_sets)


#Diccionario: es una colección desordenada de pares clave-valor, donde cada valor se accede mediante su clave (no por posición).
diccionario: dict =  {
    'name': 'Eddy',
    'surname': 'Hernandez',
    'Alias': 'Complex',
    'age': 23
}

print(diccionario)
print(diccionario['name']) #me imprime el valor de la clave name
diccionario['Email'] = 'Complex781gmail.com' #inserccion
print(diccionario)
diccionario['age'] = 24 #Actualizacion
print(diccionario)
del diccionario['surname'] #Eliminacion
print(diccionario)
diccionario = dict(sorted(diccionario.items())) #Ordenacion. Items  se usa pedir todos los pares de datos (clave y valor) junto
print(diccionario)
print(type(diccionario))

"""DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """

def agenda_contaco():


    agenda: dict = {}

    def insertar_contacto():
        telefono = input('Introduzca el nuevo numero telefonico: ')
        if telefono.isdigit and len(telefono) >= 0 and len(telefono) <= 11:
                agenda[nombre] = telefono
        else: 
                    print('------------------------------------')
                    print('Debes introducir un numero de telefono maximo de 11 digitos: ')

    def contancto_no_existe():
         print('------------------------------------')
         print(f'Contacto {nombre} no existe')
            


    while True:

        print('=============================')
        print('1. Buscar contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Salir')
        print('=============================')

        opcion = input('\nElige una opcion: ')

        match opcion:
            case "1":
                nombre = input('Introduzca el nombre del contacto: ')
                if nombre in agenda:
                    print(f'El Telefono de {nombre} es: {agenda[nombre]}')
                else: 
                    contancto_no_existe()


            case "2":
                nombre = input('Introduzca el nombre del contacto: ')
                insertar_contacto()
                print('Los datos se han ingresado correctamente!!')

            
            case "3":
                nombre = input('Introduzca el nombre del contacto: ')
                if nombre in agenda:
                    insertar_contacto()
                    print('Los datos se han actualizado correctamente!!')
                else: 
                    contancto_no_existe()
                        
                
            case "4":
                nombre = input('Introduzca el nombre del contacto: ')
                if nombre in agenda:
                    del agenda[nombre]
                    print('Los datos se han borrado correctamente!!')
                else: 
                    contancto_no_existe()


            case "5":
                print('------------------------------------')
                print('saliendo...')
                break
             

            case _:
                print('------------------------------------')
                print('Opcion no valida. Elige un numero del 1 al 5')
                print('')


agenda_contaco()
  


