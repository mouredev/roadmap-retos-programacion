"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 
 */"""
 
 # Para lista 
x = []
x.append(8) #Agregar elemento a lista
x.append(1)
x.append(2)
x.append(3)
x.remove(1) # Eliminar ellemento de la lista
x.sort() #Ordenar lista
x.insert(1, 88) # insertar elemento segun su posicion
x.reverse() #El reverso de la lista
x.pop() #Eliminar el ultimo elemento de la lista 
x.clear() #Vaciar lista
del x #Borrar lista por completo
x="hola"
print(x)

#Para diccionario
x = {}
x["Pais"]= "Venezuela" # Agreando elemento a la lista
x["Ciudad"]= "Maturin" 
y=x.values() #Muestra el valor de la lista 
y=x.keys() #Muesta la clave del diccionario
print(x)
print(y)

#Para set
x = {4,4,4,5,6,7,8,9,10}
x.discard(10) # Elimina elemento del set
x.add(60) #agregar elelmento al set
print(x)

#Par tupla 
x = ()
x= (4,5,6,7,8,9,10) #mutable
y = x.count(4) #conteo del elemento indicado
print(y)

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
 
 
def myAgenda():
    agenda = {}

    def numeroTelefono():
        ingreseNumero = input("Ingrese su numero telefonico: ")
        if ingreseNumero.isdigit() and len(ingreseNumero) == 11:
            agenda[nombre] = numeroTelefono
            return ingreseNumero
        else:
            print("Tienes que ingresar 11 digitos")
        return numeroTelefono()
    
    print("""
          BIENVENIDO A MI AGENDA TELEFONICA
          Ingrese una opcion:
          1) Agregar contacto
          2) Actualizar contacto
          3) Buscar contacto
          4) elimar contacto
          7) Salir de la agenda
          """)
    while True:
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                nombre = input("Ingrese el nombre del contacto: ")
                agenda[nombre] = numeroTelefono()
                print(agenda)
                print(f"El contacto {nombre} a sido agregado exitosamente.")
            case 2:
                nombre = input("Ingrese el nombre del contacto a actualizar: ")
                if nombre in agenda:
                    agenda[nombre]= numeroTelefono()
                    print(agenda)
                    print(f"El contacto {nombre} a sido actualizado exitosamente.")
                else:
                    print("El contacto no existe.")
            case 3:
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                if nombre in agenda:
                    for i,y in agenda.items():
                        print(i,y)
                        print("La Busqueda fue extiosa")
                else:
                    print(f"Usuario {nombre} no existe.")
            case 4:
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print(f"El contacto {nombre} se ha eliminado exitosamente.")
                else:
                    print(f"El usuario {nombre} a eliminar no fue encontado") 
            case 7:
                print("Saliendo de la agenda. Hasta Pronto")
                break       
    return myAgenda
            

myAgenda()
     