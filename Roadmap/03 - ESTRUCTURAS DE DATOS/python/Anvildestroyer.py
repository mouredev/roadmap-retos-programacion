# Tipo Listas
lista = [1, 2, 3, 4]
lista = list("1234")
lista = [1, "Hola", 3.67, [1, 2, 3]]
# inserción .append
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]
l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]
#Añade .Extend una lista a otra lista
l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]
#  actualizacion
lista1 = [1,2,3,4,5,10]
lista1[5] = 20
print(lista1)
#borrado .remove
l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]
#Ordenación .sort
l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]
# tambien podemos ordenar de mayor a menor si se pasa como parámetro reverse=True
l = [3, 1, 2]
l.sort(reverse=True)
print(l) #[3, 2, 1]

# Tuplas (son inmutables, no se pueden modificar)
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
#se pueden declarar sin parentesis tambien
tupla = 1, 2, 3
print(tupla)       #(1, 2, 3)
# Ordenación
tupla = tuple(sorted(tupla))  
print(tupla)
print(type(tupla))  #<class 'tuple'>

#Set son muy similar a las listas, pero... no puede haber elementos duplicados, Los set son desordenados, Sus elementos deben ser inmutables
s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>
#Remove
s = set([1, 2])
s.remove(2)
print(s) #{1}
#Insertar
l = set([1, 2])
l.add(3)
print(l) #{1, 2, 3}

# Diccionario
d1 = {
  "Nombre": "Anvildestroyer",
  "Edad": 10,
  "Documento": 11111111
}
print(d1)
#{'Nombre': 'Anvildestroyer', 'Edad': 32, 'Documento': 11111111}

# Eliminación
#Remove .Clear 
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

del d1["Edad"]  
print(f"eliminando edad:",d1) 
# Inserción
d1["Nombre"] = "AnvilDevstroyer"  
print(f"insertando nuevo nombre:",d1)
# Acceso
print(d1["Nombre"])  
# get()
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado
# Actualización
d1["age"] = "32"  
print(f"Actualizando edad:",d1)
# Ordenación
d1 = dict(sorted(d1.items()))  
print(f"Ordenando el directorio:",d1)
print(type(d1))


#Extra
contactos =  {}

def menu_usuario():
    while True:
        print("Agenda de Contactos\n"
        "Si quiere buscar un contacto presione 1\n"
        "Si quiere Insentar un contacto presione 2\n"
        "Si quiere Actualizar un contacto presione 3\n"
        "Si quiere eliminar un contacto presione 4\n"
        "Si quiere salir presione 5")
        seleccion = input("escoja una opcion del siguiente listado: ")
        if 1 <= int(seleccion) <= 5:
            if int(seleccion) == 1:
                buscar_datos_lista()
            elif int(seleccion) == 2:
                añadir_datos_lista()
            elif int(seleccion) == 3:
                Actualizar_contacto_lista()
            elif int(seleccion) == 4:
                Remover_contacto_lista()
            elif int(seleccion) == 5:
                print("Gracias por usar mi Agenda!")
                break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

def añadir_datos_lista():
    global contactos
    nombre = input("Escribe tu nombre: ")
    apellido = input("Ingresa tu apellido: ")  
    # Validación del número de teléfono
    while True:
        telefono = input("Ingresa tu telefono: ")
        if telefono.isdigit() and len(telefono) <= 11:
            break
        else:
            print("Por favor, ingresa un número de teléfono válido de hasta 11 dígitos.")
    identificador = input("Ingresa tu identificador: ")    
    if identificador in contactos:
        print(f"el identificador {identificador} ya existe intenta con otro!!!")
    else:
        contactos[identificador] = ["Nombre: " + nombre, "Apellido: "+ apellido, "Telefono: " + telefono]
        print (f"el contacto {identificador} se ha añadido correctamente a la agenda!")

def buscar_datos_lista():
    global contactos
    identificador = input("Ingresa el identificador del contacto que quieres buscar: ")
    if identificador in contactos:
        print(f"el contacto esta en la agenda {contactos[identificador]}")
    else:
        print("El contacto no existe.")

def Actualizar_contacto_lista():
    global contactos
    identificador = input("Ingresa el identificador del contacto que quieres Actualizar: ")
    if identificador in contactos:
        nombre = input("Escribe tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        while True:
            telefono = input("Ingresa tu telefono: ")
            if telefono.isdigit() and len(telefono) <= 11:
                break
        contactos[identificador] = ["Nombre: " + nombre, "Apellido: "+ apellido, "Telefono: " + telefono]
        print (f"El contacto {identificador} se ha actualizado correctamente!")
    else:
        print("El contacto no existe")

def Remover_contacto_lista():
    global contactos
    identificador = input("Ingresa el identificador del contacto que quieres Eliminar: ")
    if identificador in contactos:
        del contactos[identificador]
        print (f"el contacto {identificador} se ha eliminado correctamente")
    else:
        print("El contacto no existe!")

menu_usuario()