"""
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
"""
# Listas - Se pueden modificar
print("Listas \n")
listaMeses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print(listaMeses)
print(type(listaMeses))
# Nota: Si hacemos un return desde una función, los valores han de ir entre corchetes

# Tuplas - No se pueden modificar
print("Tuplas \n")
tuplaDiasSemana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(tuplaDiasSemana)
print(type(tuplaDiasSemana))
# Nota: Si hacemos un return desde una función, los valores han de ir entre comas, sin paréntesis

# Diccionario - Clave valor
print("Diccionario \n")
dicMesesDias = {
    "Enero":31,
    "Febrero":28,
    "Marzo":31,
    "Abril":30,
    "Mayo":31,
    "Junio":30,
    "Julio":31,
    "Agosto":31,
    "Septiembre":30,
    "Octubre":31,
    "Noviembre":30,
    "Diciembre":31
}
for clave,valor in dicMesesDias.items():
    print(f"El mes {clave} tiene {valor} dias")
print(type(dicMesesDias))

# Conjuntos - No ordeandos y sin valores duplicados
print("Conjunto \n")
conjuntoFruta = set()
conjuntoFruta = {"Manzana","Platano","Naranja","Pera","Platano","Mandarina"}
# No se imprime en el orden en el que se introdujeron los datos y los datos repetidos solo muestra uno
print(conjuntoFruta)
print(type(conjuntoFruta))

"""
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# Usaremos los ejemplos estructuras usados en la primera parte del ejercicio

# Operaciones de inserción
print("\n Operaciones de inserción \n")
# Listas
listaMeses.append("Decimotercermes")  # Se agrega al final de la lista
listaMeses.insert(5,"sextomes") # Se agrega en la posición que indiquemos de la lista (Empieza en 0)
print(f"{listaMeses} \n")
# Diccionario
dicMesesDias["Decimotercermes"] = 45
for clave,valor in dicMesesDias.items():
    print(f"El mes {clave} tiene {valor} dias")
# Conjunto
conjuntoFruta.add("Pomelo")
print(conjuntoFruta)

# Operaciones de borrado
print("\n Operaciones de borrado \n")
# Listas
listaMeses.remove("Decimotercermes")
listaMeses.pop(5)
print(f"{listaMeses} \n")
listaABorrar = [1,2,3,4,5]
listaABorrar.clear() # Limpia la lista y la deja vacía
print(f"{listaABorrar} \n")
# Diccionario
dicMesesDias.pop("Decimotercermes")
for clave,valor in dicMesesDias.items():
    print(f"El mes {clave} tiene {valor} dias")
# Conjuntos
conjuntoFruta.discard("Pomelo")
print(conjuntoFruta)
conjuntoFruta.remove("Pera")
print(conjuntoFruta)

# Operaciones de actualización
print("\n Operaciones de actualización \n")
# Listas
listaMeses[5] = "julio"
print(f"{listaMeses} \n")
# Diccionario
dicMesesDias.update({"Diciembre":45})
for clave,valor in dicMesesDias.items():
    print(f"El mes {clave} tiene {valor} dias")
# Conjuntos
conjuntoFruta2 = {"Melon","Sandia"}
conjuntoFruta.update(conjuntoFruta2)
print(conjuntoFruta)

# Operaciones de ordenación
print("\n Operaciones de ordenacion \n")
# Listas
# No modifica la lista original y ordena sin diferenciar mayúsculas y minúsculas, aparte de se más eficiente
sorted(listaMeses)
print(f"{listaMeses} \n")
# Modifica la lista original y ordena diferenciando mayúsculas y minúsculas, aparte de se menos eficiente
listaMeses.sort() 
print(f"{listaMeses} \n")
# Diccionario
for clave,valor in sorted(dicMesesDias.items()):
    print(f"El mes {clave} tiene {valor} dias")
# Conjuntos
print(sorted(conjuntoFruta))

"""
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación 
los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos. 
(o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""

""" Necesitamos un menú inicial, usaremos un bucle While para que no se salga hasta que no se decida
y se muestre si la opción seleccionada no es la correcta"""

import os
import time

"""
* BBDD TEMPORAL
- Lista que actúa como una BBDD para a la aplicación
"""
# Inicial, sin datos
contactosAgenda = []

# Pruebas, con Datos
# contactosAgenda = [
#     ["Pepe",645875932],
#     ["Juan",645875931],
#     ["Juan Pablo",645875934],
#     ["Pepe Viña",645875938]
# ] 

"""
# VARIABLES
- Las usaremos en diferentes partes de la aplicación
"""
timeoutMenuPrincipal = 2
timeoutMenuSeccion = 1
numeroIntentosMax = 3

"""
* CÓDIGO GENÉRICO REUTILIZABLE
- Pequeñas porciones de código a usar en diferentes lugares de la aplicación
"""
# Mensaje de Salida
def mensajeSalidaAPP():
    # Limpiar pantalla
    os.system('cls')
    # Mostrar mensaje
    print("¡Hasta pronto!")

# Cuando acabamos en una sección damos un tiempo para mostrar el resultado y re-direccionar al inicio de la aplicación
def volverInicioApp():
    print(f"Será redireccionado al menú principal ...")
    time.sleep(timeoutMenuPrincipal)
    menuAgenda()

# Cuando acabamos en una sección damos un tiempo para mostrar el resultado y re-direccionar al inicio de la aplicación
def volverSeccionApp(seccion:str):
    print(f"Será redireccionado al menú {seccion} ...")
    time.sleep(timeoutMenuSeccion)
    # Según la elección re-dirigimos a una sección u otra
    if seccion in "buscar":
        buscarContacto()
    elif seccion in "nuevo":
        nuevoContacto()
    elif seccion in "actualizar":
        actualizarContacto()
    elif seccion in "eliminar":
        eliminarContacto()
    elif seccion in "principal":
        menuAgenda()

"""
* COMPROBACIONES
- Pequeñas funciones reutilizables cuyo objetivo es comprobar datos en la BBDD principalmente
"""
# Comprobar si existen contactos en la BBDD
# Objetivo: Devolver el número de contactos si existe alguno en la BBDD
def existenContactos():
    if len(contactosAgenda) > 0:
        return True
    else:
        return False

# Comprobar y no Mostrar si se ha encontrado un contacto almacenado en la agenda
# Objetivo: Comprboar y no Mostrar los datos de un contacto en BBDD (ID, NOMBRE o TELEFONO)
def existeElContacto(id=-1,nombre="",telefono=0):
    # Por los Test unitarios
    if isinstance(telefono,str):
        telefono = int(telefono)
    # Recorremos la BBDD en busca del contacto en base a los datos que nos facilitan
    for i in range(0,len(contactosAgenda)):
        pacienteEncontrado = False
        # Si encontramos una coincidencia asignamos los valores antes de devolverlos
        if id <= len(contactosAgenda) and id >= 0 and nombre == "" and telefono == 0:
            if id == i:
                nombre = contactosAgenda[i][0]
                telefono = contactosAgenda[i][1]
                pacienteEncontrado = True
                break
        elif nombre != "":
            if nombre in contactosAgenda[i][0]:
                nombre = contactosAgenda[i][0]
                telefono = contactosAgenda[i][1]
                pacienteEncontrado = True
                break
        elif telefono != 0:
            if telefono == contactosAgenda[i][1]:
                nombre = contactosAgenda[i][0]
                telefono = contactosAgenda[i][1]
                pacienteEncontrado = True
                break
    # Depende de la resolución, devolvemos una u otra cosa
    if pacienteEncontrado:
        return True,i,nombre,telefono
    else:
        print("No existe el contacto.")
        return False,i,nombre,telefono

# Mostrar UN solo contacto almacenado o no en la agenda
# Objetivo: Mostrar los datos de un contacto en BBDD (ID) o Eliminado (pasando todos los datos)
def mostrarUnContacto(id=-1,nombre="",telefono=0):
    # Por los Test unitarios
    if isinstance(telefono,str):
        telefono = int(telefono)
    # Si nos facilitan el ID
    if id <= len(contactosAgenda) and id >= 0 and nombre == "" and telefono == 0:
        print("-----")
        print(f"Nº {id+1}:")
        print(f"Nombre: {contactosAgenda[id][0]}")
        print(f"Telefono: {contactosAgenda[id][1]}")
        print("-----")
        # Comprobar respuesta
        return True
    # Si nos facilitan el Nombre o Teléfono
    elif nombre != "" and telefono != 0:
        print("-----")
        print(f"Nº {id+1}:")
        print(f"Nombre: {nombre}")
        print(f"Telefono: {telefono}")
        print("-----")
        # Comprobar respuesta
        return True
    else:
        # No se encuentra ningún contacto con los datos proporcionados
        #print("No existe el contacto.")
        return False
    
# Mostrar UNO O VARIOS contactos en la BBDD
# Objetivo: Mostrar los diferentes contactos en BBDD según el filtro pasado, pensado para las búsquedas de contactos
# antes de proceder a seleccionar y proceder a modificar o eliminar
def mostrarContactosFiltrados(tipo,valor):
    try:
        # Si hemos encontrado algún contacto o no
        contactoEncontrado = False
        # Por los Test unitarios
        # if tipo == "telefono":
        #     if isinstance(valor,str):
        #         valor = int(valor)
        # Recorremos la lista sin agregar un +1 porque si no se pasa
        for i in range(0,len(contactosAgenda)):
            if tipo == "nombre" and valor in contactosAgenda[i][0]:
                print("-----")
                print(f"Nº {i+1}:")
                print(f"Nombre: {contactosAgenda[i][0]}")
                print(f"Teléfono: {contactosAgenda[i][1]}")
                contactoEncontrado = True
            if tipo == "telefono" and valor == contactosAgenda[i][1]:
                print("-----")
                print(f"Nº {i+1}:")
                print(f"Nombre: {contactosAgenda[i][0]}")
                print(f"Teléfono: {contactosAgenda[i][1]}")
                contactoEncontrado = True
        # Comprobamos si ha encontrado algún paciente
        if contactoEncontrado:
            return True
        else:
            print(f"No se ha encontrado un contacto por el {tipo}: {valor} \n")
            return False
    except Exception as e:
        print(f"Ha ocurrido algún tipo de error inexperado: {valor} \n Detalles del error: {str(e)}")
        
# Mostrar TODOS los contactos almacenados en la agenda
# Objetivo: Mostrar al usuario TODOS los contactos, bien para consultarlos o para
# que pueda elegir el código (ID) y posteriormente actualizar o eliminar el contacto
def listarTodosLosContactos():
    for i in range(0,len(contactosAgenda)):
        print("-----")
        print(f"Nº {i+1}:")
        print(f"Nombre: {contactosAgenda[i][0]}")
        print(f"Telefono: {contactosAgenda[i][1]}")
    # Devolvemos por defecto True
    return True

"""
* PREGUNTAS
- Funciones de preguntas a realizar al usuario
"""
# Identificación de contacto
# Objetivo: Identificamos al contacto que deseamos actualizar o eliminar
def identificarContacto():
    # Intentos
    intentos = 1
    # Pregunta
    identificadorContacto = input("Ingrese el número de contacto en la agenda: ")
    # Procedemos con las preguntas
    while intentos < numeroIntentosMax:
        
        if len(identificadorContacto) > 0:
            # Convertimos a Numérico
            identificadorContacto = int(identificadorContacto)
            # Comprobamos que sea un número válido
            if identificadorContacto > 0 and identificadorContacto <=len(contactosAgenda):
                # Comprobamos que el identificador existe antes de proseguir
                resultado = existeElContacto(identificadorContacto-1)
                # Si el resultado es correcto devolvemos los datos
                if resultado[0]:
                    return resultado
                break
            else:
                print(f"Debe introducir un idencitificador válido entre el 1 al {len(contactosAgenda)} \n")
                intentos += 1
                identificadorContacto = input("Ingrese el número de contacto en la agenda: ")

        else:
            print(f"Debe introducir un idencitificador válido entre el 1 al {len(contactosAgenda)} \n")
            intentos += 1
            identificadorContacto = input("Ingrese el número de contacto en la agenda: ")

# Preguntar el dato a usar para la búsqueda del contacto
# Objetivo: dar la posibilidad de buscar un contacto en base a los criterios de búsqueda seleccionado y datos facilitados
def preguntarDatosContactoAgenda(tipo):
    try:
        print(f"Busqueda de contacto por {tipo}")
        valorBusqueda = input("Introduzca el valor a buscar: ")
        if len(valorBusqueda) > 0:
            # Si es nombre no tenemos que transformar los caracteres a numérico
            if tipo =="nombre":
                resultado = mostrarContactosFiltrados(tipo=tipo,valor=valorBusqueda)
                if resultado:
                    return True
                else:
                    return False
            # El teléfono ha de ser numérico, en caso de no ser así, asignamos un valor que nunca encontrará un contacto
            elif tipo == "telefono":
                # Convertimos a Numérico
                # if isinstance(valorBusqueda,str):
                #     valorBusqueda = int(valorBusqueda)
                # Si todo va bien
                resultado = mostrarContactosFiltrados(tipo=tipo,valor=valorBusqueda)
                if resultado:
                    return True
                else:
                    return False
        else:
            print("Debe introducir un valor válido para buscar un contacto")
            preguntarDatosContactoAgenda(tipo)
    except:
        print("\n 2 Ha ocurrido algún tipo de error inexperado. \n")
        

# Volver a la sección donde estemos o a la pantalla principal
# Objetivo: dar la posibilidad de volver a la sección anterior o volver al menú principal
def preguntarDondeVolver(seccion:str):
    # Intentos
    intentos = 1
    # Controlamos la selección del usuario
    seleccionVolver = False
    secciónSeleccionada = seccion
    # Pregunta
    respuesta = input(f"¿Desea volver a {seccion.capitalize()} o salir al menú principal? (v/s): ")
    # Donde volveremos tras la acción que hayamos realizado
    while intentos < numeroIntentosMax:
        if respuesta != "v" and respuesta != "V" and respuesta != "s" and respuesta != "S":
            print("Debe responder 'v' o 's' \n")
            intentos += 1
            # Pregunta
            respuesta = input(f"¿Desea volver a {seccion.capitalize()} o salir al menú principal? (v/s): ")
        elif respuesta == "v" or respuesta == "V":
            seleccionVolver = True
            break
        elif respuesta == "s" or respuesta == "S":
            secciónSeleccionada="principal"
            seleccionVolver = True
            break
    
    # Si todo ha ido bien, pasamos los datos
    if seleccionVolver:
        volverSeccionApp(seccion=secciónSeleccionada)
        #return True
    else:
        volverSeccionApp(seccion=secciónSeleccionada)
        #return False
            
# No existen contactos para buscar, actualizar o eliminar
# Objetivo: dar la posibilidad de agregar un nuevo contacto desde otra sección diferente a Nuevo Contacto
def preguntarAgregarNuevoContacto():
    # Intentos
    intentos = 1
    # Controlamos la selección del usuario
    seleccionNuevoContacto = False
    # Existen contactos anteriores
    existenContactosAnteriores = False
    if existenContactos():
        existenContactosAnteriores = True
    # Mostramos un mensaje si no existen contactos en BBDD
    if not existenContactosAnteriores:
        print("Actualmente no hay contactos en la agenda. \n")
    # Pregunta
    respuesta = input(f"¿Desea agregar un contacto? (s/n): ")
    # Añadimos un nuevo contacto sí o no
    while intentos < numeroIntentosMax:
        if respuesta != "s" and respuesta != "S" and respuesta != "n" and respuesta != "N":
            print("Debe responder 's' o 'n' para proceder a agregar o no un nuevo contacto \n")
            intentos += 1
            # Pregunta
            respuesta = input(f"¿Desea agregar un contacto? (s/n): ")
        elif respuesta == "n" or respuesta == "N":
            print("No se ha agregar un nuevo contacto \n")
            break
        elif respuesta == "s" or respuesta == "S":
            print("A continuación deberá agregar los datos del nuevo contacto. \n")
            seleccionNuevoContacto = True
            break
    
    # Si todo ha ido bien, pasamos los datos
    if seleccionNuevoContacto:
        return True
    else:
        return False

# Datos del nuevo contacto
# Objetivo: Preguntas datos sobre del Nuevo Contacto a ingresar en BBDD
def preguntasNuevoContacto():
    # Intentos
    intentos = 1
    # ¿Se han resuelto todas las preguntas?
    resultaPreguntaNombre = False
    resultaPreguntaTelefono = False
    # Pregunta 
    nombreNuevoContacto = input("Ingrese el Nombre del nuevo contacto: ")
    # Comprobaciones
    while intentos < numeroIntentosMax:
        if len(nombreNuevoContacto) >= 1 and nombreNuevoContacto.replace(' ','').isalpha():
            intentos = 1
            resultaPreguntaNombre = True
            break
        else: 
            print("\n El nombre ha de contener exclusivamente caracteres \n")
            intentos += 1
            # Pregunta 
            nombreNuevoContacto = input("Ingrese el Nombre del nuevo contacto: ")
    # Telefono  
    if resultaPreguntaNombre:
        # Pregunta
        telefonoNuevoContacto = input("Ingrese el teléfono del contacto Máximo 12 números): ")
        # Comprobaciones
        while intentos < numeroIntentosMax:
            if len(telefonoNuevoContacto) >= 1 and len(telefonoNuevoContacto) <= 12:
                if not telefonoNuevoContacto.isnumeric:
                    telefonoNuevoContacto = int(telefonoNuevoContacto)
                resultaPreguntaTelefono = True
                break
            else:
                print("\n El telefono ha de contener exclusivamente números y con un máximo de 12 números. \n")
                intentos += 1
                # Pregunta
                telefonoNuevoContacto = input("Ingrese el teléfono del contacto Máximo 12 números): ")
    # Si todo ha ido bien, pasamos los datos
    if resultaPreguntaNombre and resultaPreguntaTelefono:
        return nombreNuevoContacto,telefonoNuevoContacto
    else: 
        print("\n Datos proporcionados no son válidos. \n")
        #volverSeccionApp(seccion="principal")

# Actualizar un contacto existente
# Objetivo: Preguntas datos para actualizar un contacto existente en BBDD
def preguntasActualizadoContacto(id,nombre,telefono):
    # Intentos
    intentos = 1
    # Para controlar si actualizamos alguno de los valores
    resultaPreguntaNombre = False
    resultaPreguntaTelefono = False
    # Mensaje al usuario
    print("*** Si no desea modificar el nombre presione Enter.\n")
    # Pregunta
    nombreNuevoContacto = input(f"Modifique el nombre del contacto ({nombre}): ")
    # Nombre
    while intentos < numeroIntentosMax:
        if nombreNuevoContacto == "":
            print("No se ha modificado el nombre del contacto \n")
            nombreNuevoContacto = nombre
            break
        elif len(nombreNuevoContacto) > 1 and nombreNuevoContacto.replace(' ','').isalpha():
            intentos = 1
            resultaPreguntaNombre = True
            break
        else: 
            print("\n El nombre ha de contener exclusivamente caracteres \n")
            intentos += 1
            # Pregunta
            nombreNuevoContacto = input(f"Modifique el nombre del contacto ({nombre}): ")
    # Telefono    
    telefonoNuevoContacto = input(f"Modifique el teléfono del contacto ({telefono}): ")
    while intentos < numeroIntentosMax:
        if telefonoNuevoContacto == "":
            print("No se ha modificad el teléfono del contacto \n")
            telefonoNuevoContacto = telefono
            break
        elif len(telefonoNuevoContacto) > 1 and len(telefonoNuevoContacto) <= 12:
            # if not telefonoNuevoContacto.isnumeric:
            #     telefonoNuevoContacto = int(telefonoNuevoContacto)
            telefonoNuevoContacto = int(telefonoNuevoContacto)
            resultaPreguntaTelefono = True
            break
        else:
            print("\n El telefono ha de contener exclusivamente números y con un máximo de 12 números. \n")
            intentos += 1
            # Pregunta
            telefonoNuevoContacto = input(f"Modifique el teléfono del contacto ({telefono}): ")
    
    # Si todo ha ido bien, pasamos los datos
    if resultaPreguntaNombre or resultaPreguntaTelefono:
        print("Procedemos a actualizar todos los datos del contacto ... \n")
        return True, id, nombreNuevoContacto, telefonoNuevoContacto
    elif resultaPreguntaNombre and not resultaPreguntaTelefono: 
        print("Procedemos a actualizar el nombre del contacto ... \n")
        return True, id, nombreNuevoContacto, False
    elif not resultaPreguntaNombre and resultaPreguntaTelefono: 
        print("Procedemos a actualizar el teléfono del contacto ... \n")
        return True, id, False, telefonoNuevoContacto
    else:
        return False, id, nombreNuevoContacto, telefonoNuevoContacto
            
# Eliminar un contacto existente
# Objetivo: Preguntas que contacto se desea elimianr de la BBDD
def preguntasEliminadoContacto(id,nombre,telefono):
    # Intentos
    intentos = 1
    # Controlamos la selección del usuario
    seleccionEliminacion = False
    # Pregunta
    respuesta = input(f"¿Desea eliminar al contacto con Nombre ({nombre}) con el Teléfono ({telefono})? (s/n): ")
    # Eliminamos sí o no
    while intentos < numeroIntentosMax:
        if respuesta != "s" and respuesta != "S" and respuesta != "n" and respuesta != "N":
            print("Debe responder 's' o 'n' para proceder con la eliminación o no del contacto\n")
            intentos += 1
            # Pregunta
            respuesta = input(f"¿Desea eliminar al contacto con Nombre ({nombre}) con el Teléfono ({telefono})? (s/n): ")
        elif respuesta == "n" or respuesta == "N":
            break
        elif respuesta == "s" or respuesta == "S":
            seleccionEliminacion = True
            break
        else: 
            print("Debe responder 's' o 'n' para proceder con la eliminación o no del contacto\n")
            intentos += 1
    
    # Si todo ha ido bien, pasamos los datos
    if seleccionEliminacion:
        return True, id
    else:
        return False, id

"""
* MODIFICACIÓN DE BBDD
"""

# BBDD - Agregado de los datos de un nuevo contacto facilitado por el usuario a la agenda
def agregarNuevoContacto(nombre,telefono):
    # Agregamos la lista en la BBDD
    contactosAgenda.append([nombre,telefono])
    # Comprobamos que los datos están en la BBDD
    resultado = existeElContacto(nombre=nombre,telefono=telefono)
    # retornamos si se agregó o no, es decir,que existe en BBDD tras el agregado
    return resultado
        
# BBDD - Actualizar los datos de un contacto por otros datos de la agenda
def actualizarContactoExistente(id,nombre,telefono):
    # Actualizamos los datos, según los datos que nos pasen a actualizar
    if len(nombre) > 0:
        contactosAgenda[id][0]=nombre
    if telefono > 1:
        contactosAgenda[id][1]=telefono
    # Comprobamos que los datos están en la BBDD, cualquierea de los dos
    if  nombre in contactosAgenda[id][0] or telefono == contactosAgenda[id][1]:
        return True
    else:
        return False
         
# BBDD - Agregado de los datos del contacto proporcionado de la Agenda
def eliminarContactoExistente(id):
    # Agregamos la lista en la BBDD
    returnValue = contactosAgenda.pop(id)
    # Comprobamos que los datos ya no están en la BBDD
    if returnValue:
        return True
    else:
        return False
        
"""
* SECCIONES / OPERACIONES
- Se trata de las diferentes secciones / operaciones disponibles desde el menú principal
"""
# SECCIÓN BUSCAR CONTACTOS
def buscarContacto():
    # Limpiar pantalla
    os.system('cls')
    # Inicio del Menú
    print("\n BÚSQUEDA DE CONTACTOS \n")
    # Comprobamos su hay contactos, en aso de no existir, preguntamos si quieren agregar uno nuevo
    if not existenContactos():
        resultado = preguntarAgregarNuevoContacto()
        if resultado:
            nuevoContacto()
        else:
            # Re-enviamos al menú principal
            volverInicioApp()
    else:
        # Menú de opciones de búsqueda de contacto
        menuOpcionesBusquedaContacto()

# SECCIÓN NUEVO CONTACTO
def nuevoContacto():
    # Limpiar pantalla
    os.system('cls')
    # Inicio del Menú
    print("\n NUEVO CONTACTO \n")
    # Comprobamos si hay contactos existentes
    if not existenContactos():
        print("Actualmente no hay contactos disponibles en la agenda.")
    else:
        # Nos guardamos el número de contactos habidos en la agenda
        print(f"Nº de contactos existentes : {len(contactosAgenda)} \n")
    # Preguntamos al usuario
    nombreNuevoContacto, telefonoNuevoContacto = preguntasNuevoContacto()
    # Agregamos los datos en la agenda
    resultado = agregarNuevoContacto(nombre=nombreNuevoContacto,telefono=telefonoNuevoContacto)
    if resultado[0]:
        print("Nuevo contacto agregado a la Agenda")
        # Mostramos datos del contacto recién agregado
        mostrarUnContacto(id=resultado[1])
    else:
        print("Nuevo contacto No fue agregado a la Agenda")
    # Re-enviamos al menú principal
    volverInicioApp()

# SECCIÓN ACTUALIZAR UN CONTACTO EXISTENTE
def actualizarContacto():
    # Limpiar pantalla
    os.system('cls')
    # Inicio del Menú
    print("\n ACTUALIZAR CONTACTO \n")
    
    # Comprobamos su hay contactos, en aso de no existir, preguntamos si quieren agregar uno nuevo
    if not existenContactos():
        resultado = preguntarAgregarNuevoContacto()
        if resultado:
            nuevoContacto()
        else:
            # Re-enviamos al menú principal
            volverInicioApp()
    else:
        # Nos guardamos el número de contactos habidos en la agenda
        print(f"Nº de contactos existentes : {len(contactosAgenda)} \n")
        
    # Preguntamos al usuario
    datosContactoAModificar = identificarContacto()
    # Actualizamos los datos del contacto
    resultado = preguntasActualizadoContacto(id=datosContactoAModificar[1],nombre=datosContactoAModificar[2],telefono=datosContactoAModificar[3])
    # Verificamos que podemos proceder con la actualización del contacto
    if resultado[0]:
        if actualizarContactoExistente(id=resultado[1],nombre=resultado[2],telefono=resultado[3]):
            print("Modificación realizada")
            # Contacto anterior
            print("Contacto anterior")
            mostrarUnContacto(id=resultado[1],nombre=datosContactoAModificar[2],telefono=datosContactoAModificar[3])
            print("Contacto actualizado")
            # Contacto actualizado
            mostrarUnContacto(id=resultado[1])
            # Re-enviamos al menú principal
            volverInicioApp()
    else:
        print("Modificación no realizada, no había nada que actualizar")
        # Re-enviamos al menú principal
        volverInicioApp()

# SECCIÓN ELIMINACIÓN DE CONTACTOS
def eliminarContacto():
    # Limpiar pantalla
    os.system('cls')
    # Inicio del Menú
    print("\n ELIMINAR CONTACTO \n") 
    
    # Comprobamos su hay contactos, en aso de no existir, preguntamos si quieren agregar uno nuevo
    if not existenContactos():
        resultado = preguntarAgregarNuevoContacto()
        if resultado:
            nuevoContacto()
        else:
            # Re-enviamos al menú principal
            volverInicioApp()
    else:
        # Nos guardamos el número de contactos habidos en la agenda
        print(f"Nº de contactos existentes : {len(contactosAgenda)} \n")
        
    # Preguntamos al usuario
    datosContactoAEliminar = identificarContacto()
    # Actualizamos los datos del contacto
    resultado = preguntasEliminadoContacto(id=datosContactoAEliminar[1],nombre=datosContactoAEliminar[2],telefono=datosContactoAEliminar[3])
    # Verificamos que podemos proceder con la actualización del contacto
    if resultado[0]:
        if eliminarContactoExistente(id=resultado[1]):
            print("Eliminación realizada del contacto:")
            # Contacto eliminado
            mostrarUnContacto(id=resultado[1],nombre=datosContactoAEliminar[2],telefono=datosContactoAEliminar[3])
            # Re-enviamos al menú principal
            volverInicioApp()
    else:
        print("Modificación no realizada, no había nada que eliminar")
        # Re-enviamos al menú principal
        volverInicioApp()

"""
* OPCIONES DE MENÚS
- Opciones que corresponden a los diferentes menús
"""
# Menú de opciones de la agenda
opcionesMenuPrincipal = {
    1:"Buscar contacto",
    2:"Nuevo contacto",
    3:"Actualizar contacto",
    4:"Eliminar contacto",
    0:"Salir"
}

# Selección de búsqueda
opcionesBusquedaContacto = {
    1:"Buscar por Nombre",
    2:"Buscar por Teléfono",
    3:"Mostrar todos los contactos",
    0:"Volver"
}

"""
* MENUS
- Diferentes menús a mostrar en las diferentes secciones u operaciones
"""

# Función con el menú de la agenda
def menuAgenda():
    # Limpiar pantalla
    os.system('cls')
    # Inicio del menú
    print("\n MENU AGENDA DE CONTACTOS \n")
    for clave,valor in opcionesMenuPrincipal.items():
        print(f"{clave} - {valor}.")
    try:
        seleccionaOpcionMenu = input("\n Seleccione una opción: ")
        # Podriamos usar un While que ejecute en bucle la app mientras no sea 0 por ejemplo, pero no lo haremos en esta ocasión
        # Verificamos que es un número lo que han introducido 
        if seleccionaOpcionMenu.isnumeric():    
            # pasamos a int el valor pasado
            seleccionaOpcionMenu = int(seleccionaOpcionMenu)
            # Verificamos si el número pasado está dentro de la lista del menú
            if seleccionaOpcionMenu in list(opcionesMenuPrincipal.keys()):
                # Depende de la opcón hacemos una cosa u otra
                if seleccionaOpcionMenu == 0:
                    mensajeSalidaAPP()
                # Buscar contacto
                if seleccionaOpcionMenu == 1:
                    buscarContacto()
                # Nuevo contacto
                if seleccionaOpcionMenu == 2:
                    nuevoContacto()
                # Actualizar contacto
                if seleccionaOpcionMenu == 3:
                    actualizarContacto()
                # Eliminar contacto
                if seleccionaOpcionMenu == 4:
                    eliminarContacto()
            else:
                menuAgenda()
        else:
            menuAgenda()   
    except:
        print("\n Ha ocurrido algún tipo de error inexperado. \n")

# Función del menún de opciones de búsqueda
def menuOpcionesBusquedaContacto():
    # Limpiar pantalla
    os.system('cls')
    # Inicio del Menú
    print("\n MENU BUSQUEDA DE CONTACTOS \n")
    for clave,valor in opcionesBusquedaContacto.items():
        print(f"{clave} - {valor}.")
    try:
        seleccionaOpcionMenuBusqueda = input("\n Seleccione una opción: ")
        # Verificamos que es un número lo que han introducido 
        if seleccionaOpcionMenuBusqueda.isnumeric():    
            # pasamos a int el valor pasado
            seleccionaOpcionMenuBusqueda = int(seleccionaOpcionMenuBusqueda)
            # Verificamos si el número pasado está dentro de la lista del menú
            if seleccionaOpcionMenuBusqueda in list(opcionesBusquedaContacto.keys()):
                # Buscar contacto por nombre
                if seleccionaOpcionMenuBusqueda == 1:
                    preguntarDatosContactoAgenda(tipo="nombre")
                    # Dar opción de volver al menú
                    preguntarDondeVolver(seccion="buscar")
                # Buscar contacto por teléfono
                if seleccionaOpcionMenuBusqueda == 2:
                    preguntarDatosContactoAgenda(tipo="telefono")
                    # Dar opción de volver al menú
                    preguntarDondeVolver(seccion="buscar")
                # Mostrar todos los contactos
                if seleccionaOpcionMenuBusqueda == 3:
                    listarTodosLosContactos()
                    # Dar opción de volver al menú
                    preguntarDondeVolver(seccion="buscar")
                # Salir al menú principal
                if seleccionaOpcionMenuBusqueda == 0:
                    # Dar opción de volver al menú
                    menuAgenda()
            else:
                menuOpcionesBusquedaContacto()
        else:
            menuOpcionesBusquedaContacto()   
    except:
        print("\n Ha ocurrido algún tipo de error inexperado. \n")

"""
# Inicio del programa
"""
menuAgenda()