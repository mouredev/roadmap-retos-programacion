 # DIFICULTAD EXTRA (opcional):
 # Crea una agenda de contactos por terminal.
 # - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 # - Cada contacto debe tener un nombre y un número de teléfono.
 # - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 #   los datos necesarios para llevarla a cabo.
 # - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 #   (o el número de dígitos que quieras)
 # - También se debe proponer una operación de finalización del programa.






#listas
listas = [1,2,3,4,"bryan",4,5]
# tuplas este tipo de estructura no es mutable
tuple = (1,2,3,"python")
#diccionarios
diccionarios = {"nombre":"bryan",
              "cedula":"1234556"}
#conjuntos-sets elementos unicos
sets = {1,2,3,4}
#strings (textos)
strings= "creando string"

agenda=[]
def agregarContacto():
    nombre = input("Escribe el nombre de tu contacto: ")
    try:
        telefono = int(input("Escribe el telefono: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    agenda.append({nombre: telefono})
    opciones()
def actualizar():
    nombreActualizar = input("Escribe el nombre del contacto a actualizar: ")
    encontrado = False
    for contacto in agenda:
        if nombreActualizar in contacto:
            nuevoTelefono = input("Escribe el nuevo telefono: ")
            contacto[nombreActualizar] = nuevoTelefono
            encontrado = True
            break
    if not encontrado:
        print("Contacto no encontrado.")
    opciones()

def eliminar():
    nombreEliminar = input("Escribe el nombre del contacto a eliminar: ")
    encontrado = False
    for contacto in agenda:
        if nombreEliminar in contacto:
            agenda.remove(contacto)
            encontrado = True
            break
    if not encontrado:
        print("Contacto no encontrado.")
    opciones()
    
def salir():
    print("gracias por usar Agenda.APP")

def vercontactos():
    print(agenda)
    print("gracias por usar Agenda.APP")
def opciones():
    opciones=int(input("Seleciona una opcion 1-Agregar 2-Actualizar 3-Eliminar 4-Ver Contactos 5-Salir "))
    if opciones == 1:
        agregarContacto()

    elif opciones == 2:
        actualizar()
    elif opciones == 4:
        vercontactos()
    elif opciones == 5:
        salir()
    else:
        eliminar()


opciones()




