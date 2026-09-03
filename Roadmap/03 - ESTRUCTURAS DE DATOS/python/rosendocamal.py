"""
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """

# https://docs.python.org/es/3/tutorial/datastructures.html

# Estructuras de datos por defectos

my_list_1: list[int] = [1, 2, 3, 5, 4]
my_list_2: list[int] = list()

my_tuple1: tuple[int, int] = (1, 2)
my_tuple2: tuple[int, int] = tuple()
my_tuple3: tuple[int, int, str] = 1, 2, "Hello"

from collections import deque
my_queue1: deque[str] = deque(["Eric", "John", "Michael"])
my_queue2: deque[int] = deque([1, 2, 3])

my_set_1: set[str] = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"}
my_set_2: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

my_dict1: dict[str, str] = {"Nombre": "Ernesto",
                           "Apellido": "De la Cruz"}
my_dict2: dict[int, str] = {1: "Uno",
                            2: "Dos",
                            3: "Tres",
                            4: "Cuatro",
                            5: "Cinco",
                            6: "Seis",
                            7: "Siete",
                            8: "Ocho",
                            9: "Nueve",
                            0: "Cero"}

my_stack_1: list[int] = [1, 2, 3]

my_list_1.append(6)
print(my_list_1)
my_list_1.pop(4)
print(my_list_1)
my_list_2.insert(0, 1)
my_list_1.insert(0, 1)
print(my_list_1, my_list_2)
my_list_2[0] = 123
sorted(my_list_1)
print(my_list_1)

for i in range(99, 0, -1):
    my_list_2.append(i)
else:
    my_list_2.sort()
    print(my_list_2)

my_queue1.append("Terence")
my_queue2.append("Graham")
print(my_queue1.popleft())
print(my_queue2.popleft())
print(my_queue1, my_queue2)

print(my_tuple1, my_tuple2, my_tuple3)

my_set_1.add("123")
my_set_2.add(42)
print(my_set_1, my_set_2)
my_set_1.pop()
my_set_2.pop()
print(my_set_1, my_set_2)
my_set_1.discard("Enero")
my_set_2.discard(4)
print(my_set_1, my_set_2)

my_dict1["Nombre"] = "Juan"
my_dict1["Edad"] = 90
print(my_dict1)
del my_dict1 ["Nombre"]
print(my_dict1)

for i in range(-9, 999999999, 7):
    my_stack_1.append(i)
    print(my_stack_1)
else:
    for j in range(len(my_stack_1)):
        if j % 3 == 0:
            continue
        my_stack_1.pop()
    print(my_stack_1)

class Contacto():
    def __init__(self, name: str, lastname: str, number: str):
        self.name = name
        self.lastname = lastname
        self.number = number

    def __str__(self):
        print("="*10)
        print(f"NOMBRE: {self.name.rjust(10, " ")}\nAPELLIDO: {self.lastname.rjust(10, " ")}\nNÚMERO: {self.number.rjust(20, " ")}")
        print("="*10)

class AgendaContactos():
    def __init__(self):
        self.storage: list[Contacto] = []

    def buscar_contacto(self, name: str) -> Contacto:
        for contacto in self.storage:
            if contacto.name == name:
                return contacto

    def agregar_contacto(self, name: str, lastname: str, number: str) -> Contacto:
        if len(number) > 11 and number.isdigit():
            nuevo_contacto: Contacto = Contacto(name, lastname, number)
            self.storage.append(nuevo_contacto)
            return nuevo_contacto

    def actualizar_contacto(self, name: str, contacto_update: Contacto) -> Contacto:
        contacto: Contacto = self.buscar_contacto(name)
        self.storage[self.storage.index(contacto)] = contacto_update
        return contacto

    def eliminar_contacto(self, name: str):
        contacto: Contacto = self.buscar_contacto(name)
        self.storage.pop(contacto)

def AppContactos():
    contactos = AgendaContactos()
    while True:
        try:
            print("CONTACTOS")
            print("[1]. BUSCAR\n[2]. AGREGAR\n[3]. ACTUALIZAR\n[4]. ELIMINAR\n[5]. SALIR")

            opcion: int = int(input("INGRESE UNA OPCION: >>> "))

            match opcion:
                case 1:
                    result = contactos.buscar_contacto(input("Nombre: "))
                    print("Buscando...")
                    print(contactos.__str__())
                case 2:
                    result = contactos.agregar_contacto(input("Nombre: "), input("Apellido: "), input("Número: "))
                    print("Agregado...")
                    print(result)
                case 3:
                    nuevo_contacto = Contacto(input("Nombre: "), input("Apellido: "), input("Número: "))
                    result = contactos.actualizar_contacto(name=nuevo_contacto.name, nuevo_contacto=nuevo_contacto)
                    print("Actualizando...")
                    print(result)
                case 4:
                    contactos.eliminar_contacto()
                    print("Contacto eliminado.")
                case 5:
                    print("Cerrando aplicación...")
                    break
                case _:
                    continue

        except ValueError:
            print("Datos inválidos")
        except KeyboardInterrupt:
            print("Cerrando aplicación...")
            break

AppContactos()