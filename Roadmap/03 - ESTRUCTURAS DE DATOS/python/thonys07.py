"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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
"""Estructuras"""
#listas
lista:list=[1,2,343,4,5,6]
print(lista)
print(type(lista))
lista.pop() #borra segun indice, por defecto -1
print(lista)
lista.append(123)#inserta un valor en la ultima posicion
print(lista)
lista.insert(254,3)#inserta un valor en el indice indicado
print(lista)
lista.remove(4)#elimina el valor indicado
print(lista)
lista.sort()
print(lista)
print(lista[4])#Acceso al valor en la posicion indicada
lista[0]=555 #actualizacion
print(lista)

#tuplas
tupla:tuple=(1,2,3,4,564,645,2323,23)
print(tupla,type(tupla))
print("ordenando de mayor a menor: ", sorted(tupla, reverse=True)) #ordenado de mayor a menor
print("ordenando de menor a mayor: ", sorted(tupla)) #ordenado de menor a mayor

#sets
set1:set={1,2,45,5,33,65,8}
print(set1)
set1.add(7)
print(set1)
set1.remove(5)
print(set1)
set1=set(sorted(set1))
print(set1)

#dictionaries
dicc:dict={1:"a",2:"b",3:"c"}
print(dicc)
dicc[4]="d"
print(dicc)
dicc.pop(2)
print(dicc)
del dicc[1]
print(dicc)
print(dicc[3])
dicc= dict(sorted(dicc.items()))
print(dicc)

"""EXTRAAAA
"""
class Agenda:
    def __init__(self):
        self.contactos = {}

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            return self.contactos[nombre]
        else:
            return None

    def agregar_contacto(self, nombre, telefono):
        if nombre not in self.contactos:
            self.contactos[nombre] = telefono
            print("Contacto agregado correctamente.")
        else:
            print("El contacto ya existe en la agenda.")

    def actualizar_contacto(self, nombre, telefono):
        if nombre in self.contactos:
            self.contactos[nombre] = telefono
            print("Contacto actualizado correctamente.")
        else:
            print("El contacto no existe en la agenda.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print("Contacto eliminado correctamente.")
        else:
            print("El contacto no existe en la agenda.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for nombre, telefono in self.contactos.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda está vacía.")

if __name__ == "__main__":
    agenda = Agenda()

    while True:
        print("\nOperaciones disponibles:")
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print(f"Teléfono de {nombre}: {contacto}")
            else:
                print("El contacto no existe en la agenda.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            if telefono.isdigit() and len(telefono) <= 11:
                agenda.agregar_contacto(nombre, telefono)
            else:
                print("El número de teléfono no es válido.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            telefono = input("Ingrese el nuevo número de teléfono: ")
            if telefono.isdigit() and len(telefono) <= 11:
                agenda.actualizar_contacto(nombre, telefono)
            else:
                print("El número de teléfono no es válido.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "5":
            agenda.mostrar_contactos()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
