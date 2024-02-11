'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

#Listas unidimensionales

compra = ['yogures', 'pan', 'tomate']

#listas bidimensionales

matriz = [[1,3],[2,4]]

#diccionario

datos = {
    "nombre": "toral",
    "edad": 25,
    "profesión": "informático"
}
print(datos["nombre"])
#tuplas

numeros = (1,2,3,4)

#inserción

compra.append('naranjas')
print(compra)

#inserción en diccionario

datos["nacionalidad"] = 'español'
print(datos)

#borrado

del compra[2]
print(compra)

#actualización

compra[1] = 'pan de molde'
print(compra)

#ordenación

compra.sort()
print(compra)

'''
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
'''
agenda = {}
controller = False

def verificador(num):
    try:
        return int(num)
    except:
        print("no has introducido un número")
while controller == False:
    action = input("que acción quieres llevar a cabo: \n I para insertar \n E para eliminar \n A para actualizar \n B para buscar \n S para salir \n").upper()
    if action == "I":
        nombre = input("introduzca el nombre del contacto que quiere insertar: ")
        numero = input("introduzca el número de telefono que quiere insertar: ")
        if len(numero) == 9:

            agenda[nombre] = verificador(numero)
        else:
            print("el número introducido no es correcto")
    elif action == "E":
        nombre = input("Introduce el nombre del contacto que quieres borrar: ")
        if nombre in agenda:
            del agenda[nombre]
        else:
            print("el nombre intrudcido no se encuentra en la agenda")
    elif action == "A":
        nombre = input("Introduce el nombre del contacto que quieres actualizar: ")
        if nombre in agenda:
            numero = input("Introduce el número de telefono actualizado: ")
            if agenda[nombre] == numero:
                print("el numero introducido es el mismo que se encuentra en la agenda")
            else:
                agenda[nombre] = numero
        else:
            print("el nombre intrudcido no se encuentra en la agenda")
    elif action == "B":
        nombre = input("Introduce el nombre del contacto que quieres buscar: ")
        if nombre in agenda:
            print(f'El número de {nombre} es {agenda[nombre]}')
        else:
            print("el nombre intrudcido no se encuentra en la agenda")
    elif action == "S":
        controller = True
    print(agenda)
