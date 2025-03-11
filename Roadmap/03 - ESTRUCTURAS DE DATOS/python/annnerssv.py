#----LISTAS----

mi_lista_nombres = ["Jhan", "Awasa", "Bryan", "PanaMiguel"] #Lista de cadena
mi_lista_numeros = [21, 20, 19, 22] #Lista de numeros 

#--Listas anidadas--
mi_lista_de_listas = [[1,2,3], [4,5,6],[7,8,9]] #Lista de listas de numeros
mi_lista_mixta = ["Jhan", 19, [2,0,0,3]] #Lista mixta de cadenas, numero y lista
mi_lista_de_diccionarios = [{"nombre" : "jhan", "edad": "21"}] #Lista de diccionarios
mi_lista_de_tuplas = [(1,2,3), (3,4,5)] #Lista de Tuplas


#-Metodos de Listas-
print(mi_lista_nombres) #Imprimimos la lista antes de usar los metodos
mi_lista_nombres.append("Gabriel") #Insertar elementos a una lista
print(mi_lista_nombres)
mi_lista_nombres.remove("Jhan") #Remover elementos de una lista
print(mi_lista_nombres)
mi_lista_nombres[0] = "Antonio" #Acceder a la posición del elemento de una lista y modificarlo
print(mi_lista_nombres)
mi_lista_nombres.sort() #Ordenar de menor a mayor o en orden alfabetico
print(mi_lista_nombres)


print("-------------------------------------------------------------------------------------------")

#----TUPLAS---- 

mi_tupla = ("Hola", "soy","una","tupla")
mi_tupla_anidada = ("Hola", [1,2,3], 4, {'clave': 'valor'}) 
print(type(mi_tupla))
print(mi_tupla)
print(mi_tupla_anidada)
print(mi_tupla[2]) #Acceso al elemento de una tupla

#--Convertir lista a tupla--

mi_lista_a_tupla = ["Lista", "convertida", "a", "tupla"]
print(mi_lista_a_tupla)
print(tuple(mi_lista_a_tupla))



#----SETS----

mi_set = {"Hola", "soy", "un", "set"}
print(mi_set)
mi_set.add("nuevo") #Insertar un nuevo elemento a un set
print(mi_set)
mi_set.remove("Hola") #Eliminar un elemento de un set
print(type(mi_set))
mi_primer_set = {1,2,3}
mi_segundo_set = {4,5,6}

print(mi_primer_set|mi_segundo_set) #Union de 2 sets


#----DICCIONARIOS----

mi_diccionario = {'nombre':'Jhan', 'edad': 22, 'correo':'jhan.aries.jp@gmail.com'}
print(mi_diccionario)
print(type(mi_diccionario))

print(mi_diccionario["nombre"]) #Acceso al valor nombre del diccionario 

mi_diccionario['usuario'] = 'Pier' #Añadir un nuevo elemento de clave - valor al diccionario
print(mi_diccionario)

mi_diccionario['nombre'] = 'Aries' #Modifición de un valor del diccionario
print(mi_diccionario)

del mi_diccionario['usuario'] #Eliminación de un elemento de clave - valor del diccionario 
print(mi_diccionario)




#----EJERCICIO EXTRA----

contactos = {}


def añadirContacto(): 
    telefono = input('Ingrese el numero de telefono del contacto: ')
    if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
        contactos[nombre] = telefono
        print(contactos)
    else:
        print('Ingresa un numero de telefono valido')


def buscarContacto():
    nombre = input('Ingresa el nombre del contacto a buscar: ')
    if nombre in contactos:
        print(f'Contacto encontrado  \n Nombre:{nombre}\n Telefono: {contactos[nombre]}')
    else:
        print(f'El contacto {nombre} no se encuentra en la lista')

def actualizarContacto():
    nombre = input('Ingrese el nombre del contacto a atualizar')
    if nombre in contactos:
        añadirContacto()
    else:
        print('Ingresa un contacto valido')

def eliminarContacto():
    nombre = input('Ingresa el nombre del contacto a eliminar')

    if nombre in contactos:
        del contactos[nombre]
        print('Contacto eliminado correctamente...')
    else:
        print('El contacto a eliminar no existe')
    


salir = False

while not salir:
    
    print('''---Bienvenido a la agenda de contactos,¿Qué actividad deseas realizas?---
          1. Añadir un contacto
          2. Buscar un contacto
          3. Actualizar un contacto
          4. Eliminar un contacto
          5. Listar contactos
          6. Salir
''')
    
    opcion = int(input("Elige una opcion: "))

    if __name__ == '__main__':
        if opcion == 1:
            nombre = input('Ingresa el nombre del contacto')
            añadirContacto()
        elif opcion == 2:
            buscarContacto()
        elif opcion == 3:
            actualizarContacto()
        elif opcion == 4:
            eliminarContacto()
        elif opcion == 5:
            print(contactos)
        elif opcion == 6:
            print('Saliendo del Sistema...')
            salir = True
        else:
            print('Ingrese una opción valida')
