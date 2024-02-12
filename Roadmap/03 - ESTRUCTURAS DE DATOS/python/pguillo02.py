#Python es un lenguaje con una amplia gama de estructuras de datos.

#Listas, son mutables y aceptan datos de cualquier tipo mezclados, están indexados y no poseen un tamañó fijo

lista = [1,  True, "hola"]

print(lista[0])

lista.append(2)

print(lista)

lista.pop(3)

print(lista)

lista.remove("hola")
print(lista)

lista.sort()
print(lista)

#Tuplas, son estructuras inmutables que no se pueden modificar una vez declaradas. Permiten mezclar datos de distinto tipo

tupla = (1,2,"hola")
print(tupla)

print(tupla.count(1))

print(tupla[1])

#Sets, son estructuras mutables y dinámicas que admiten distintos tipos de elemento. Su particularidad es que no están indexadas
#ni permiten duplicados. Lo que los hace útiles para ciertos programas.

sets = {1,2,3,4}

sets.add("hola")
sets.add("hola")

print(sets)

sets.remove(3)

print(sets)

#Diccionarios, estructuras dinámicas y mutables, aceptan todo tipo de datos y trabajan en parejas clave:valor 

diccionario = {1:"fasd", 2: 3, 3:"adfad"}

diccionario.pop(1)

print(diccionario)

diccionario[5]="fsdfaf"

print(diccionario)

#OPCIONAL
agenda = {}

def interaccion_agenda():
    print("Qué desea hacer")
    operacion =int(input("Añadir(1), Eliminar(2), Modificar(3), Buscar(4), Parar(5): "))

    if operacion == 1:
        nombre = input("Nombre del contacto: ")
        try:
            numero = int(input("Número: "))

            if len(str(numero))>9:
                print("El número no puede tener más de 9 dígitos")
                interaccion_agenda()

        except ValueError:
            print("Tiene que ser un número")
            interaccion_agenda()

        agenda[nombre] = numero

        interaccion_agenda()
    
    elif operacion == 2:
        nombre = input("Nombre que desea eliminar: ")
        try:
            agenda.pop(nombre)
        except:
            print("El contacto no está en la agenda")
            interaccion_agenda()
            
        interaccion_agenda()

    elif operacion == 3:
        nombre = input("Nombre del contacto a modificar: ")
        try:
            nuevo_numero = int(input("Nuevo número: "))

            if len(str(nuevo_numero))>9:
                print("El número no puede tener más de 9 dígitos")
                interaccion_agenda()

        except ValueError:
            print("Tiene que ser un número")
            interaccion_agenda()

        agenda[nombre] = nuevo_numero

        interaccion_agenda()
    
    elif operacion == 4:
        nombre = input("Nombre del contacto a buscar: ")

        try:
            print(agenda[nombre])
        except KeyError:
            print("Contacto no existente")
            interaccion_agenda()

        interaccion_agenda()

    elif operacion == 5:
        return 0 

interaccion_agenda()
