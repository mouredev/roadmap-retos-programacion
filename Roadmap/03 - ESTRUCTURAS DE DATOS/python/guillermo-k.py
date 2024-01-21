''' * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

# Listas
print("LISTAS")
lista = [1,'dos',3.14,[15,2]]
print("BUSQUEDA")
print("Busqueda por indice (buscamos el valor ubicado en el indice '2'): ",lista[2])
print("Busqueda de indice por item (buscamos el indice de '3.14'): ",lista.index(3.14))
print("------")
print("INSERCION")
print(lista)
print("Al final (agregamos el string 'Hola mundo' al final de la lista)")
lista.append("Hola mundo")
print(lista)
print("Entre medio (agregamos el número '3' en la segunda posición)")
lista.insert(2,3)
print(lista)
print("Agregamos los elementos de un iterable al final de la lista")
lista.extend({5,3,8})
print(lista)
print("-----")
print("ACTUALIZACIÓN")
print("Actualizamos el item ubicado en la posición '0' dentro de la sub-lista ubicada en la posición '4' de la lista")
lista[4][0] = 1
print(lista)
print("-----")
print("BORRADO")
print("Borramos el elemento de la lista cuyo valor es 'Hola mundo'")
lista.remove("Hola mundo")
print(lista)
print("Borramos el ultimo elemento de la lista")
lista.pop()
print(lista)
print("Borramos el elemento ubicado en la posición 4 de la lista")
lista.pop(4)
print(lista)
print("-----")
print("ORDENAMIENTO")
print("Invertimos el orden de la lista")
lista.reverse()
print(lista)
print("Ordenamos 'alfabeticamente' la lista")
print("Para ello, primero 'unificamos' los tipos de datos")
lista[4]=2
print(lista)
lista.sort()
print(lista)
print("-----")
print("-----")

print("TUPLAS")
tupla = (1,2,3,'cuatro')
print(tupla)
print("BUSQUEDA")
print("Busqueda por indice (buscamos el valor ubicado en el indice '2'): ",tupla[2])
print("Busqueda de indice por item (buscamos el indice de '3'): ",tupla.index(3))
print("-----")
print("Las tuplas, por definición, son objetos inmutables, por lo cual, no se las puede modificar(agregar, asignar o borrar)")
print("-----")
print("-----")

print("DICCIONARIOS")
dicc = {"nombre": "Guillermo",
        "edad": 38,
        "pais": "Argentina",
        "lenguaje":"PYTHON"
        }
print(dicc)
print("-----")
print("BUSQUEDA (buscamos el valor por la clave)")
print(dicc["lenguaje"])
print("-----")
print("INSERCION (agregamos el par [apellido:Köster])")
dicc["apellido"]="Köster"
print(dicc)
print("-----")
print("RE-ASIGNACIÓN (cambiamos el valor asignado a 'edad')")
dicc["edad"] = 39
print(dicc)
print("-----")
print("BORRADO (borramos el par lenguaje:python)")
dicc.pop("lenguaje")
print(dicc)
print("-----")
print("Siendo los diccionarios estructuras no ordenadas, no hay metodos para realizar ordenamientos")
print("-----")
print("-----")

print("CONJUNTOS")
conjunto = {1,4,3,3,"Python","Kotlin",(1,4)} 
'''Notese que en la declaración del conjunto se incluyo 2 veces el número 3,
    pero este estara una sola vez, ya que los conjuntos no admiten repetidos.
    No ocurre lo mismo con los números 1 y 4, ya que en la segunda aparición 
    se encuentran dentro de una tupla, lo que lo convierte en un objeto distinto'''
print(conjunto)
print("-----")
print("INSERCIÓN")
print("SIMPLE agregamos el número 500 al conjunto")
conjunto.add(500)
print(conjunto)
print("-----")
print("BORRADO borramos el string 'Kotlin'")
conjunto.discard('Kotlin')
print(conjunto)
print("-----")
print("Borrado aleatoreo (se borra un elemento cualquiera del conjunto)")
conjunto.pop()
print(conjunto)
print("Siendo los conjuntos estructuras no ordenadas, no hay metodos para realizar ordenamientos")
print("-----")
print("-----")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 '''
agenda = []
def corre_agenda():
    def seleccion_tarea():
        print("Seleccione la operación a ralizar:")
        print("1.- Buscar contacto")
        print("2.- Crear contacto")
        print("3.- Modificar contacto")
        print("4.- Eliminar contacto")
        print("0.- Cerrar agenda") 
        return opcion_numerica(range(5))
    
    def buscar():
        nombre = input().upper()
        resultado = []
        if len(nombre)>0:
            for i in agenda:
                if nombre in i[0]:
                    resultado.append(i)
        else:
            resultado = agenda
        if len(resultado) > 0:
            for contacto in resultado:
                print(f"{resultado.index(contacto)}.- {contacto[0].capitalize()}: {contacto[1]}")
        else:
            print("Contancto no encontrado")
        return resultado


    def crear():
        nombre = pedir_nombre()
        numero = pedir_numero()
        respuesta = ""
        while respuesta != "Y" and respuesta != "N":
            print(f"Se agregara el contacto: {nombre.capitalize()} con el número {numero}. ¿Es correcto? (Y/N)")
            respuesta = input().upper()
        if respuesta == "Y":
            agenda.append([nombre,numero])
            agenda.sort(key=lambda contacto: contacto[0])
        else:
            print("Operación cancelada")

    def modificar():
        opciones = buscar()
        if len(opciones)>1:
            print("Seleccione el contacto a modificar")
            opciones = opciones[opcion_numerica(range(len(opciones)))]
        elif len(opciones)==0:
            print("Intente nuevamente")
        print("seleccione el campo a modificar:")
        print("1._ Nombre")
        print("2._ Número")
        print("3._ Ámbos")
        campo = opcion_numerica((1,2,3))
        match campo:
            case 1:
                agenda[agenda.index(opciones)][0] = pedir_nombre()
            case 2:
                agenda[agenda.index(opciones)][1] = pedir_numero()
            case 3:
                agenda[agenda.index(opciones)][0] = pedir_nombre()
                agenda[agenda.index(opciones)][1] = pedir_numero()
        agenda.sort(key=lambda contacto: contacto[0])


    def eliminar(contacto=None):
        if not contacto:
            print("Ingrese el nombre (o parte del mismo) del conacto a eliminar")
            contacto = buscar()
            if len(contacto)>1:
                print("Seleccione el contacto a eliminar")
                contacto = contacto[opcion_numerica(range(len(contacto)))]
            elif len(contacto)==0:
                print("Intente nuevamente")
                return False
        print(f"Se borrara permanentemente el contacto: {contacto[0].capitalize()} con el número {contacto[1]}. ¿Es correcto? (Y/N)")
        respuesta = input().upper()
        if respuesta == "Y":
            agenda.remove(contacto)
            return True
        return False

    def pedir_nombre():
        nombre = ""
        while True:
            print("Ingrese el nombre del contacto")
            nombre = input().upper()
            if len(nombre) == 0:
                print("El campo 'nombre' no puede estar vacio")
            else:
                return nombre
    
    def pedir_numero():
        while True:
            print("Ingrese el número")
            numero = opcion_numerica()
            if numero < 100000000000:
                numero = int(numero)
                if not existe_numero(numero):
                    return numero
                else:
                    print("El numero ya se encuentra registrado")
            else:
                print("El número puede tener maximo 11 digitos")
            
    
    def opcion_numerica(rango = None):
        while True:
            opcion = input()
            if opcion.isdigit():
                if not rango or int(opcion) in rango:
                    return int(opcion)
                else:
                    print("Opcion no valida")
            else:
                print("Se debe ingresar un numero")

    def existe_numero(numero):
        for i in agenda:
            if i[1] == numero:
                return True
        return False


    abierta = True
    while abierta:
        opcion = seleccion_tarea()
        match opcion:
            case 1:
                print("Ingrese el nombre (o parte del mismo) del contacto a buscar")
                buscar()
            case 2:
                crear()
            case 3:
                print("Ingrese el nombre (o parte del mismo) del conacto a modificar")
                modificar()
            case 4:
                eliminar()
            case 0:
                abierta = False
                print("Gracias por utilizar la agenda. Nos vemos pronto")
corre_agenda()

        
