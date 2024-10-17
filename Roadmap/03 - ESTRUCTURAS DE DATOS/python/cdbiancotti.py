# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# List
lista_vacia = []
lista = [1, 2, 3, 4, 5, 6]  # tambien se puede utilizar list()
print('Lista 1:', lista)
# Insercion
lista.insert(0, 0)
print('Lista 1 post insert:', lista)
lista.append(6)
print('Lista 1 post append:', lista)
lista.extend([34, 55])
print('Lista 1 post extend:', lista)
# Actualización
lista[2:4] = [10]
print('Lista 1 post asignacion por slicing:', lista)
lista[-1] = 55
print('Lista 1 post modificacion de valor en la posicion -1:', lista)
# Borrado
lista2 = lista[:]
print('Lista 2 pre clear:', lista2)
lista2.clear()
print('Lista 2 post clear:', lista2)
lista.pop()
print('Lista 1 post pop:', lista)
lista.remove(1)
print('Lista 1 post remove:', lista)
del lista[3]
print('Lista 1 post del:', lista)
# Ordenamiento
lista.sort()
print('Lista 1 post sort:', lista)
lista.sort(reverse=True)
print('Lista 1 post reverse sort:', lista)
lista.reverse()
print('Lista 1 post reverse:', lista)

# Tuple
tupla_vacia = ()
tupla = (1, 2, 3, 4, 5, 6)
print('Tupla 1:', tupla)
# Las tuplas no admiten insercion, actualización, borrado, ordenamiento ya que son inmutables

# Set
set_vacio = set()
print('Set vacio:', set_vacio)
set_con_datos1 = {11, 2, 3, 4, True, 'test', ('Prueba', 'tupla')}
print('Set 1:', set_con_datos1)
set_con_datos2 = set((11, 2, 3, 4, True, 'test', ('Prueba', 'tupla')))
print('Set 2:', set_con_datos2)
set_con_datos3 = set([11, 2, 3, 4, True, 'test', ('Prueba', 'tupla')])
print('Set 3:', set_con_datos3)
# inserción
set_vacio.add('Dato nuevo')
print('Set vacio con add:', set_con_datos3)
set_vacio.update('Dato nuevo', )
print('Set vacio con update despues del add:', set_con_datos3)
# borrado
set_con_datos3.remove(('Prueba', 'tupla'))
print('Set 3 post remove:', set_con_datos3)
set_con_datos3.discard('EAEA')
print('Set 3 post discard:', set_con_datos3)
set_con_datos3.pop()
print('Set 3 post pop:', set_con_datos3)
set_con_datos3.clear()
print('Set 3 post clear:', set_con_datos3)
# actualización
set_con_datos2.difference_update((2, 3,))
print('Set 2 post difference update:', set_con_datos2)
set_con_datos2.intersection([11, True])
print('Set 2 post intersection update:', set_con_datos2)
# Los sets no pueden ordenarse ya que sus elementos no estan ordenados por un indice como los otros tipos de daots.

# Dictionary
dicc = {
    1: 'test',
    (2, 'si'): 123,
    'llave': [1, 2, 3, 4.5],
    True: {11, 3, 1, 2, 15, 6, 3, 46, 3, 6, 34}
}  # tambien se puede utilizar dict()
# Las llaves pueden ser cualquier valor inmutable, los valores cualquier tipo de dato
dicc_vacio = {}
print('Dicc:', dicc)
# Insercion y Actualización
dicc['nuevo valor'] = 333
print('Dicc con "nuevo valor":', dicc)
dicc2 = {'key1': "value1", 'llave': 'Cambie mi valor'}
dicc.update(dicc2)
print('Dicc post update with dict:', dicc)
tuple_to_dict = ((1, 'nuevo valor de key "1"'), ("key2", ("soy", "una", "tupla")))
dicc.update(tuple_to_dict)
print('Dicc post update with tuple:', dicc)
dicc_vacio.setdefault("lista", []).append(15)
dicc_vacio['lista'].append(20)
print('Dicc vacio post setdefault:', dicc_vacio)
# Borrado
del dicc[True]
print('Dicc post del:', dicc)
value_popped = dicc.pop('key2')
print('Dicc post pop:', dicc, ', value popped:', value_popped)
item_popped = dicc.popitem()
print('Dicc post popitem:', dicc, ', item popped:', item_popped)
dicc.clear()
print('Dicc post clear:', dicc)

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.
#  */

from typing import List, TypedDict, Optional


class Person(TypedDict):
    name: str
    number: str


class Agenda:
    def __init__(self) -> None:
        self.__agenda: List[Person] = []

    def search(self, name: str) -> None:
        search_result = [person for person in self.__agenda if name in person["name"]]
        if not search_result:
            print(f"No se encontraron contactos relacionados con \"{name}\"")
            return

        print(f"Listado de contactos relacionados con {name}:")
        for i, person in enumerate(search_result):
            print(f"{i}. {person["name"]}: {person["number"]}")

    def create(self, name: str) -> None:
        contact = self.__get_contact_data_by_name(name)

        while True:
            number = input("Ingrese el numero de telefono: ")
            if self.__number_validator(number):
                break

        print(f"Se agrego el contacto {name} correctamente a la agenda.")

    def delete(self, name: str) -> None:
        old_agenda_length = len(self.__agenda)
        self.__agenda = [person for person in self.__agenda if person['name'] != name]
        new_agenda_length = len(self.__agenda)
        if old_agenda_length != new_agenda_length:
            print(f"Se elimino correctamente el contacto {name}")
        else:
            print(f"{name} no corresponde a un contacto de la agenda.")

    def update(self, name: str) -> None:
        contact = self.__get_contact_data_by_name(name)
        if contact is None:
            print(f"No existe el contacto con nombre {name}")
            return

        while True:
            number = input("Ingrese el numero de telefono: ")
            if self.__number_validator(number):
                break

        contact["number"] = number
        print("Se actualizo correctamente el numero de telefono.")

    def __get_contact_data_by_name(self, name: str) -> Optional[Person]:
        persons = [person for person in self.__agenda if name in person["name"]]
        if persons:
            return persons[0]

    def __number_validator(self, incoming_number: str):
        if not incoming_number.isnumeric() or len(incoming_number) > 11:
            print("El numero de telefono debe ser un numero de no mas de 11 digitos.")
            return False
        return True


def main():
    agenda = Agenda()
    while True:
        print('''
========================
          Menu
========================
1. Buscar contacto
2. Agregar contacto
3. Actualizar contacto
4. Eliminar contacto
5. Salir
''')
        selected_option = input("Ingrese la opcion a realizar: ")
        contact_name = input("Ingrese el nombre de contacto: ")
        match selected_option:
            case '1':
                agenda.search(contact_name)
            case '2':
                agenda.create(contact_name)
            case '3':
                agenda.update(contact_name)
            case '4':
                agenda.delete(contact_name)
            case '5':
                print("Hasta luego...")
                return
            case _:
                print("Ingreso una opcion incorrecta, vuelva a intentarlo.")


main()
