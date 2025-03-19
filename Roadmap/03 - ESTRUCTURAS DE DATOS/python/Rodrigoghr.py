'''
/*
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
print('\n1. Listas')
print('*********') 
edades = [18, 28, 23, 10]
print(f'Lista: {edades}')

print('\nOperaciones de Listas')
print('*********************')

print('\ta) Inserción:')
edades.append(24)
print(f'\tInsertamos el número 24 a la lista: {edades}')

edades.insert(2,30)
print(f'\tSe inserta el número 30 en el índice 2: {edades}')

print('\n\tb) Eliminar:')
edades.remove(23)
print(f'\tElimina el número 23 de la lista: {edades}')

edades.pop()
print(f'\tElimina el último número de la lista: {edades}')

edades.pop(1)
print(f'\tElimina el elemento de la posición 1: {edades}')

print('\n\tc) Actualizar:')
edades[1] = 45
print(f'\tActualiza el valor en la posición 1: {edades}')

print('\n\td) Ordenar:')
edades.sort()
print(f'\tOrden ascendente: {edades}')

edades.sort(reverse = True)
print(f'\tOrden descendente: {edades}')

print('\n2. Tuplas')
print('*********') 
mi_tupla = (1,2,5,4,7,3,2,1,9)
print(f'\tmi_tupla: {mi_tupla}')

print('\n3. Diccionario')
print('**************') 
mi_alumno = {'nombre' : 'Rodrigo', 'genero': 'M', 'edad':25, 'cursos' : ['python','javascript','github']}
print(f'\tAlumno: {mi_alumno}')

print('\nOperaciones')
print('***********')

print('\ta) Inserción:')
mi_alumno['nota'] = 20
print(f'\tInsertamos la clave "nota" y el valor "20": {mi_alumno}')

print('\n\tb) Eliminar:')
del mi_alumno['genero']
print(f'\tEliminamos la clave "genero" con su valor: {mi_alumno}')

mi_alumno.pop('edad')
print(f'\tEliminamos la clave "edad" con su valor: {mi_alumno}')

print('\n\tc) Actualizar:')
mi_alumno['nombre'] = 'Luis'
print(f'\tActualiza el valor de la clave "nombre": {mi_alumno}')

print('\n\td) Ordenar:')
mi_alumno = dict(sorted(mi_alumno.items()))
print(f'\tOrden ascendente: {mi_alumno}')

print('\n4. Conjuntos')
print('**************') 
frutas = {'manzana', 'platano', 'naranja', 'fresa'}
print(f'\tFrutas: {frutas}')

print('\nOperaciones')
print('***********')

print('\ta) Inserción:')
frutas.add('melon')
print(f'\tInsertamos la fruta "melon" al conjunto: {frutas}')

print('\n\tb) Eliminar:')
frutas.remove('manzana')
print(f'\tEliminamos la fruta "manzana" del conjunto: {frutas}')

frutas.pop()
print(f'\tEliminamos una fruta del conjunto: {frutas}')


print('\n\tc) Actualizar:')
print(f'\tNo se puede actualizar un elemento específico')

print('\n\td) Ordenar:')
print(f'\tOrdenamos el conjunto: {sorted(frutas)}')

'''
/*
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
 # Dificulta Extra
def buscar(agenda):
    nombre = input('Ingrese nombre: ')
    if nombre in agenda:
        print(f'Nombre: {nombre} , Teléfono : {agenda[nombre]}')
    else:
        print('Contacto no encontrado!')

def valida_telefono(telefono):
    return telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11

def insertar(agenda):
    nombre = input('Ingrese nombre: ')
    telefono = input('Ingrese número de teléfono: ')
    
    if valida_telefono(telefono):
        agenda[nombre] = telefono
        print(f'Contacto {nombre} con número de teléfono {agenda[nombre]} ¡Registrado!')
    else:
        print("¡Numero de teléfono inválido! Debe ser numérico y de 11 dígitos como máximo")

def actualizar(agenda):
    nombre = input('Ingrese nombre: ')
    
    if nombre in agenda:
        telefono = input('Ingrese nuevo número de telefono: ')
        if valida_telefono(telefono):
            agenda[nombre] = telefono
            print(f'Contacto {nombre} actualizado con número {agenda[nombre]}')
        else:
            print("¡Numero de teléfono inválido! Debe ser numérico y de 11 dígitos como máximo")
    else:
        print('Contacto no encontrado!')

def eliminar(agenda):
    nombre = input('Ingrese nombre: ')
    if nombre in agenda:
        del agenda[nombre]
        print(f'Contacto {nombre} ¡Eliminado!')
    else:
        print('Contacto no encontrado!')

def main():
    agenda = {}
    
    while True:
        print("\nAgenda de contactos")
        print("\t1. Buscar contacto")   
        print("\t2. Insertar contacto")   
        print("\t3. Actualizar contacto")   
        print("\t4. Eliminar contacto")   
        print("\t5. Salir")    
        
        opcion = input("\nSelecciona una opción: ")
        
        match opcion:
            case '1':
                buscar(agenda)
            case '2':
                insertar(agenda)
            case '3':
                actualizar(agenda)
            case '4':
                eliminar(agenda)
            case "5":
                print("Cerrando agenda...")
                break
            case _:
                print("Opción inválida. Elige del 1 al 5.")
                

if __name__ == '__main__':
    main()