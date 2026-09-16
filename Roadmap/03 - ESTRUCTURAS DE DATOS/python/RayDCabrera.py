#---------------- Listas ---------------------
lista = [1,2,3,4]

#acceder a un elemento  
print(lista[1])

#insertar elemento
lista.append(6)
print(lista)

#borrar ultimo elemento
lista.pop()
print(lista)

#remover un elemento
lista.remove(3)
print(lista)

#ordenar elementos  
lista.sort()
print(lista)

#ordenar con sorted hace que se ordene la lista pero no la modifica 
li = [5,2,1,4]
print(sorted(li))
print(li)


#insertar elemento en la posicion elegida   
lista.insert(1,5) #en la posicion 1 insertame el numero 5.
print(lista)



#---------------- Tuplas ---------------------
tupla = (1.123,2.352,1)

#acceder a un elemento  
print(tupla[1])

#acceder al indice donde se encuentra el elemento
print(tupla.index(1.123))

#contar cuantas veces aparece en la tupla
print(tupla.count(1.123))

#las tuplas no pueden ser modificadas, por ende, no se pueden agregar, mpdificar o eliminar elementos.
print(sorted(tupla)) #sorted ordena la tupla pero la convierte en una lista, para traerlo nuevamente como tupla debemos transformarla con tuple()

#--------------- Sets --------------------
# Un set es una coleccion no ordenada de elementos que no pueden duplicarse, en el caso de que haya un duplicado este se elimina automaticamente
seto = {'manzana','naranja','banana','manzana'}
print(seto)

print ('naranja' in seto) #pregunta si naranja existe en set y trae True

#insertar, eliminar y actualizar    
seto.add('pera')
seto.update(['chorizo','sandia']) #update añade multiples elementos a la vez   
seto.remove('chorizo') #elimina un elemento especifico
seto.pop() #elimina y devuelve un elemento aleatorio del conjunto    
print(seto)
#--------------- Diccionarios -------------------
#los diccionarios permiten usar una palabra clave para encontrar un valor rapidamente, y se definen usando llaves, las claves son unicas, o sea que no pueden repetirse
diccionario = {"nombre": "Raymond", "edad": 28}

#acceder a un valor usando la clave
print(diccionario['nombre'])

#modificar un valor
diccionario["edad"] = 25
print(diccionario["edad"])

print(diccionario)

#ordenación
dicordenado = sorted(diccionario.items())
print(dicordenado) # aqui al ordenar ordena por clave pero lo transofrma en una lista de tuplas, cada clave valor se transforma en una tupla de dos elementos
diccionario_ordenado = dict(dicordenado)
print(diccionario_ordenado)

#eliminar valor
edad = diccionario.pop("edad")
print(diccionario)#elimina la edad pero deja guardado el valor en la variable edad
print(edad)

#----------------EXTRA----------------------
contactos = []
def agregar(nombre, nro):
    nuevo_contacto = {"nombre":nombre, "telefono":nro}
    contactos.append(nuevo_contacto)
    print("El contacto ha sido creado con exito: ", nuevo_contacto)
s = 1

def buscar(contacto):
    for c in contactos:
        if c["nombre"] == contacto:
            print(c)

def modificar(contacto):
    filtro = []
    for i, c in enumerate(contactos):
        if c["nombre"] == contacto:
            filtro.append((i,c))
    if len(filtro) == 0:
        print ("No se encuentra el contacto")
        return    
    for pos, (i,c) in enumerate(filtro):
        print(f"{pos} - {c["nombre"]} / {c["telefono"]}")
    numero = int(input("Seleccione el id del cual desea modificar: "))
    while True:
        if len(filtro) > numero and numero >= 0:
            indice_real, contacto_elegido = filtro[numero]
            nuevonro = input("Ingrese el numero nuevo: ")
            contactos[indice_real]["telefono"] = nuevonro
            print(f"Modificado: {contacto_elegido['nombre']} / {contacto_elegido['telefono']}")
            break
        else:
            print('Debe seleccionar el numero que corresponda: ')
            numero = int(input("Seleccione el id del cual desea modificar: "))


def borrar(contacto):
    filtro = []
    for i, c in enumerate(contactos):
        if c["nombre"] == contacto:
            filtro.append((i,c))
    if not filtro:
        print('No se encuentra el contacto')
        return
    for pos, (i,c) in enumerate(filtro):
        print(f"{pos} - {c["nombre"]} / {c["telefono"]}")
    numero = int(input("Seleccione el id del cual desea borrar: "))
    while True:
        if len(filtro) > numero and numero >= 0:
            indice_real, contacto_elegido = filtro[numero]
            contactos.pop(indice_real)
            print(f"Modificado: {contacto_elegido['nombre']} / {contacto_elegido['telefono']}")
            break
        else:
            print('Debe seleccionar el numero que corresponda: ')
            numero = int(input("Seleccione el id del cual desea borrar: "))





while s:
    print("------------------------------------------")
    print("AGENDA DE CONTACTOS")
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Modificar contacto")
    print("4. Borrar contacto")
    print("0. Salir")
    print("------------------------------------------")
    valor = input("Elige una de las opciones: ")

    if valor == "0":
        s = 0
    elif valor == "1":
        print("------------Buscar Contacto----------")
        contacto = input("Nombre del contacto: ")
        buscar(contacto.upper())
    elif valor == "2":
        print("---------Agregar Contacto----------")
        nombre = input("Nombre del contacto: ")
        nro = input("Numero de telefono: ")
        while True:
            if len(nro) <= 11 and nro.isdigit():
                agregar(nombre.upper(), nro)
                break
            else:
                print("El numero de telefono no puede ser mayor a 11 digitos y debe ser numerico: ")
                nombre = input("Nombre del contacto: ")
                nro = input("Numero de telefono: ")
    elif valor == "3":
        print("----------Modificar Contacto----------")
        contacto = input('Ingrese el nombre del contacto: ')
        modificar(contacto.upper())
    elif valor == "4":
        print("------------Borrar Contacto----------")
        contacto = input("Ingrese el nombre del contacto: ")
        borrar(contacto.upper())
