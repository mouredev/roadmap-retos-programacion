### 03 ESTRUCTURAS DE DATOS ###

##  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.

# Listas
# ------

prelist = list([1,2,2,3,4,5,6,666,7]) # Se construye una lista con el método list
print(prelist)

lista = ['mercurio','venus','tierra','marte','jupiter','saturno','urano','neptuno','plutón'] # La lista
print(lista)

lista.extend(['planeta x','planeta y','planeta z']) # Extiende la lista según la cantidad de iterables
print(lista)

lista.insert(0, 'sol') # inserta un ítem en una posición determinada
print(lista)

lista.remove('planeta z') # Remueve un ítem que coincida con el valor dado
print(lista)

lista.pop(-1) # Remueve un ítem según el índice colocado
print(lista)

del lista[9:] # Borra elementos de la lista pasando un entero o un slice
print(lista)

lista[0] = 'Sol' # Actualización de un valor
print(lista)

lista.sort() # Ordena la lista
print(lista)

lista.reverse() #Invierte el orden de la lista
print(lista)

# Comprehensión de lista

squared = [x**2 for x in range(1,7)]
print(squared)

# Comprehensión de lista anidada
multsquared = [[s*i for s in squared] for i in range(2,5)]
print(multsquared)


# Tuplas
# ------

tup = tuple(multsquared) # Construir tupla
print(tup)

tupla = 1,2,2,3 # Construir tupla
print(tupla)

tupla_1 = (1,1,1,"uno",2,'alpha',4,True)  # Construir tupla
print(tupla_1)

print(tupla_1[5]) # Acceder a un valor indexado

# tupla_1[0] = 0 # no acepta asignación de nuevos valores, inmutable

print(tupla_1.count('uno')) # Cuenta un valor

# Diccionario
# -----------

dicc = dict([                   ## Creación de diccinoario con método dic()
    ('mar', 'Mediterráneo'),
    ('oceano', 'Atlántico'),
    ('longitud', 3700),
    ('ancho', 1600),
    ('profundidad', 1430),
    ('salinidad', 36.2)
])
print(dicc)

egeo = {
    'nombre':'Mar Egeo',
    'oceano':'Mar Mediterráneo',
    'cuenca':'cuenca del mar Egeo',
    'longitud':600,
    'ancho':400,
    'profundidad':2639
    }

print(egeo) ## Creación de diccionario con llaves

egeo['tipo'] = 'Mar' ## Inserción de datos
print(egeo)

egeo.pop('tipo') ## Eliminación de datos
print(egeo)

egeo['profundidad'] = 3544 ## Actualización de datos
print(egeo)

mar_egeo = egeo.copy() # Devuelve una copia del diccionario
print(mar_egeo)

print(mar_egeo.get('nombre')) # Devuelve el valor de la key

print(mar_egeo.items())  # Devuelve los pares de key value del diccionario

print(mar_egeo.keys())  # Devuelve las keys del diccionario

print(mar_egeo.values())  # Devuelve los values del diccionario












## Comprehension de diccionarios

poten3 = {x: x**3 for x in (1,2,3,4,5,6,7,8,9,10)}
print(poten3)


# Sets (conjuntos)
# ----------------

conj = set([1,1,1,1,2,31,23,12,312])
print(conj)

conj2 = {"alpha","beta","gamma"}
print(conj2)

conj2.add("theta")  # Añade un elemento al conjunto
print(conj2)

conj2.remove("theta") # Remueve un elemento del conjunto
print(conj2)

conj2.update(conj) # Actualiza el conjunto con otro conjunto, el resultado no está ordenando
print(conj2)


### Desafío extra

"""
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
"""

#def agenda():
agenda = dict()

def mostrar_menu():
    print("""
    ---------AGENDA---------
    Qué desea hacer:
    1. Agregar contacto
    2. Buscar contacto          
    3. Actualizar contacto
    4. Eliminar contacto
    5. Listar contactos
    6. Salir de la agenda
        """)

def añadir_contacto():
    nombre = input("Ingrese su nombre: ")
    
    telefono = input("Ingrese su número, debe ser menor a 11 dígitos")

    if telefono.isdigit() and len(telefono) <= 11:
        agenda[nombre] = telefono
        print (f"El contacto: {nombre} - {telefono}, se ha registrado exitosamente")        
    else:
        print("Número inválido. Asegúrese de que el número tiene menos de 11 dígitos y solo contiene números.")


def buscar_contacto():      
    busqueda = int(input("Ingrese 1 si desea buscar por nombre y 2 si desea buscar por número: "))
    if busqueda == 1:
        nom = input("Ingrese el nombre que desea buscar: ")
        if nom in agenda:
            print(f"El número del contacto es: {nom} - {agenda[nom]}")
        else:
            print("Ingrese el nombre nuevamente, verifique mayúsculas y minúsculas")
    
    elif busqueda == 2:
        num = input("Ingrese el número que desea buscar: ")
        encontrado = False

        for nombre, fono in agenda.items():
            if fono == num:
                print(f"Contacto encontrado: {nombre} - {fono}")
                encontrado = True
                break
        if not encontrado:
            print("Número inválido o inexistente")
    
    else:
        print("Opción de búsqueda inválida")            

def actualizar_contacto():
    nom_nue = input("Ingrese el nombre de contacto que desea actualizar: ")

    if nom_nue in agenda:
        while True:
            nuenum = input("Ingrese el nuevo número: ")
            if nuenum.isdigit() and len(nuenum) <= 11:
                agenda[nom_nue] = nuenum
                print(f"Contacto encontrado {nom_nue} - {agenda[nom_nue]}")
                break
            else: 
                print("Número inválida, asegúrese que el número tiene 11 o menos dígitos")

    else:
        print("Contacto no encontrado, compruebe mayúsculas y minúsculas")


def borrar_contacto():
    delnom = input("Ingrese el nombre que desea eliminar")

    if delnom in agenda:
        agenda.pop(delnom)
        print(f"El contacto {delnom} se ha elimiado correctamente")
    else:
        print("Nombre inválido o no existente. Compruebe mayúsculas, minúsculas y vuelva a ingresarlo")


def listar_contactos():
    if agenda:
        for nom in agenda:
            print(f"{nom} - {agenda[nom]}")    
    else:
        print("La agenda está vacía")        



while True:
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        añadir_contacto()   
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        actualizar_contacto()
    elif opcion == 4:
        borrar_contacto()
    elif opcion == 5:
        listar_contactos()
    elif opcion == 6:
        print("Adios, gracias por utilizar la agenda!")
        break
    else:
        print("Ingrese nuevamente el número, escoga un número del 1 al 6")
