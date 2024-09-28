"""
EJERCICIO:
    - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
    - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# region Ejercicio simple


def my_print(
    arg, title: str = '', space: int = 20, symbol: str = "-", color: str = None
):
    """
    Imprime el dato recibido anticipando una linea horizontal para su separación.

    Parameters
    ---
    arg: Cualquier dato a imprimir por consola
    title: Titulo para identificar cada separación
    space: Cantidad de espacios o symbol a dibujar
    symbol: Símbolo a agregar para alinear
    """
    all_colors = {
        'blue': "\033[1;34m{}\033[0m",
        'yellow': "\033[1;33m{}\033[0m",
        "cyan": "\033[1;36m{}\033[0m",
        "white": "\033[1;0m{}\033[0m",
        "red": "\033[1;31m{}\033[0m",
    }

    if not color or not color in all_colors.keys():
        color_print = all_colors['blue']
    else:
        color_print = all_colors[color]

    print(color_print.format(symbol * space + title))
    if not arg == None:
        print(arg)


def lists():
    """
    Listas

    Sintaxis
    ---
    nombre_var = [datos]

    Características
    ---
    - Permiten modificar los elementos después de creada la lista.
    - Permite insertar multiples tipos de datos en una sola lista. Ej: [enteros, booleanos, string...]
    - Permite datos repetidos. Ej: [1, 50, 50, 3]
    """

    # Ejemplos
    my_numbers_list = [1, 2, 3, 4]
    my_string_list = ["H", "o", "l", "a"]
    my_mix_list = [1, "Hola", True]

    # Yo utilizare esta para los siguientes puntos inserción, borrado, actualización y ordenación
    my_list = [x for x in range(20)]  # la sentencia crea una lista de 20 elementos
    my_print(my_list, "Creación de lista")

    # region Inserción
    # - Insertion al final de la lista
    my_list.append(180)
    my_print(my_list, "Inserción al final de la lista")

    # - Inserción en posición indicada
    my_list.insert(3, 250)
    my_print(my_list, "Inserción en la posición indicada de la lista")

    # endregion

    # region Borrado
    # - Borrar el elemento al final de la lista
    my_list.pop()
    my_print(my_list, "Borrado del ultimo elemento")

    # - Borrar un elemento en la posición indicada y lo retorna(el elemento eliminado)
    item_eliminated = my_list.pop(4)
    my_print(item_eliminated, "Borrado elemento en posición, retorna elemento borrado")

    # endregion

    # region Actualización
    # - Debes pasar la posición, en este caso (-1) estoy actualizando la ultima posición. Ej: my_list[2] = 450
    my_list[-1] = 450
    my_print(my_list, "Actualización ultima posición")
    # endregion

    # region Ordenamiento
    # - Ordenamiento por defecto (ascendente)
    my_list.sort()
    my_print(my_list, "Ordenamiento por defecto (ascendente)")

    # - Ordenamiento personalizado (creare otra lista)
    new_list = [
        {"name": "Carlos", "age": 30},
        {"name": "Marina", "age": 21},
        {"name": "Raquel", "age": 34},
        {"name": "Juan", "age": 18},
    ]

    new_list.sort(key=lambda x: x['age'])
    my_print(new_list, "Ordenamiento personalizado, orden de edad")

    # - Ordenamiento personalizado descendente
    new_list.sort(key=lambda x: x['age'], reverse=True)
    my_print(new_list, "Ordenamiento personalizado, Descendente")

    # endregion


def tuples():
    """
    Tuples

    Sintaxis
    ---
    nombre_var = (datos)

    Características
    ---
    - No permite modificación después de su creación
    - Son mas ligeras en memoria que las listas
    - Permite insertar multiples tipos de datos en una sola lista. Ej: [enteros, booleanos, string...]
    - Permite datos repetidos. Ej: [1, 50, 50, 3]
    """
    my_tuple = (1, 2, 3, "Hola", 3)
    my_print(my_tuple, "Creación de tupla")


def sets():
    """
    Conjuntos

    Sintaxis
    ---
    - Conjunto con datos:

            nombre_var = {datos}

    - Conjunto de datos vació:

            nombre_var = set()

    Características
    ---
    - Datos desordenados
    - No permite datos duplicados
    - No se pueden actualizar posiciones (pero se puede agregar y eliminar)
    - Su creación vacía debe ser con set() no con {} ya que este ultimo creara otro tipo de dato(diccionario)
    - Permite insertar multiples tipos de datos en una sola lista. Ej: [enteros, booleanos, string...]
    - El orden en que se añaden los elementos puede cambiar
    - Al crear un conjunto con set y pasarle como argumento una lista, la iterara y dejara solamente los elementos que no estén repetidos
    """

    # region Creación
    # Este sera el conjunto que utilizare para los siguientes ejemplos de Inserción...
    my_set = {1, 2, 3, 4, "Hola"}
    my_print(my_set, "Creación de conjunto")

    var_to_add = "leonardohenao.com"

    # Creo un nuevo conjunto con set. Creara el conjunto vació para después agregar elementos
    my_new_set = set()
    my_print(my_new_set, "Creación de conjunto con función set()")

    # Creo un conjunto con set y le paso una variable la cual iterara
    my_new_set_with_var = set(var_to_add)
    my_print(
        my_new_set_with_var,
        "Creación de conjunto pasando una variable con un string (leonardohenao.com)",
    )

    my_other_new_set = set([1, 3, 5, 6, 1, 5])
    my_print(my_other_new_set, "Creación de conjunto con lista y datos repetidos")

    # endregion

    # region Inserción
    my_set.add(56)
    my_set.add("Carro")
    # Nota en la impresión del conjunto que no se agrego este nuevo valor
    my_set.add(56)
    # Este nuevo "carro" lo toma como un nuevo elemento. Distingue de mayúsculas o minúsculas
    my_set.add("carro")
    # Analiza como se agrega esta variable en un set cuando ya esta creado
    my_set.add(var_to_add)

    my_print(my_set, "Inserción elementos en conjunto")

    # endregion

    # region Borrado
    # - En este caso, pop() elimina el primer elemento del conjunto
    my_set.pop()
    my_print(my_set, "Eliminación con pop(). Primer elemento, si, primero")

    # - Eliminar un elemento en especifico
    my_set.remove(var_to_add)
    my_print(my_set, f"Eliminación de un elemento en especifico. {var_to_add}")

    # endregion

    # Actualización(elemento o posición) y ordenamiento no son posibles


def dictionaries():
    """
    Diccionarios

    Sintaxis
    ---
    my_dict = {"key_name": value}

    Características
    ---
    - Permite datos de tipo llave:valor (tipo JSON)
    - Palabras llave únicas
    """

    # region Creación
    my_dict = {
        "name": "Teodoro",
        "age": 23,
        "address": "CO",
        "website": "leonardohenao.com",
    }
    my_print(my_dict, "Creación de diccionario")

    # endregion

    # region Inserción
    my_dict['height'] = 1.78
    my_print(my_dict, "Inserción de elementos")
    # endregion

    # region Borrado
    # - pop requiere la llave a eliminar y regresa el valor eliminado
    data_removed = my_dict.pop('address')
    my_print(my_dict, "Borrado de elemento con pop(). (address)")
    my_print(data_removed, space=0)
    # - del elimina sin mas el dato y la llave seleccionada
    del my_dict["age"]
    my_print(my_dict, "Borrado de elemento con del. (age)")

    # endregion

    # region Actualización
    my_dict["name"] = "Leonardo Henao"
    my_print(my_dict, "Actualización de datos. (name)")

    # endregion

    # region Ordenamiento
    # sorted retorna una lista de las llaves ordenadas alfabéticamente
    keys_from_my_list = sorted(my_dict)
    new_dict = {}
    for k in keys_from_my_list:
        new_dict[k] = my_dict[k]

    my_print(None, "Ordenamiento ascendente")
    my_print(keys_from_my_list, "Llaves del diccionario ordenadas", space=5)
    my_print(new_dict, "Nuevo diccionario ordenado", space=5)

    # endregion


"""
# Pilas
    Las pilas son un concepto de datos de estructura lineal.
    LIFO: Donde el ultimo dato en ingresar es el primero en salir.
    FIFO: Donde el primer dato en ingresar es el primero en salir.

    Para el ejemplo cree una clase llamada MyStack a la cual voy a dotar con las funciones/métodos que yo o mi equipo utilizara,
    también puedes utilizar queue de la librería de python, yo no la utilizare para que se vea el concepto un poco mas claro.

    Al crear nuestra propia clase también controlamos las funciones/métodos a utilizar ya que por lo regular la lista es privada y la modificación de dicha lista debe ser interna de la clase, también optimizamos el uso de la memoria.
"""


class MyStack:
    def __init__(self, data: list):
        self.__my_data = data

    def pop(self):
        pass

    def push(self, new_data):
        self.__my_data.append(new_data)

    def size(self):
        return len(self.__my_data)


# region Pilas (LIFO [Last in - First out])
class MyStackLifo(MyStack):
    def __init__(self, data: list):
        super().__init__(data)

    def pop(self):
        """
        Elimina el ultimo elemento de la lista y lo retorna
        """
        return self._MyStack__my_data.pop()


def stack_lifo():
    """
    Para LIFO se crea adicional una clase que implementa MyStackLifo la cual tiene el método pop con el funcionamiento indicado(eliminar el ultimo elemento de la lista).
    """
    my_stack = MyStackLifo(["Carlos", "Maria", "Juan", "Pedro"])
    my_print(my_stack._MyStack__my_data, "Creación de pila LIFO")

    # region Inserción
    my_stack.push("Leonardo")
    my_print(my_stack._MyStack__my_data, "Insertando datos a pila LIFO")

    # endregion

    # region Borrar
    my_stack.pop()
    my_print(my_stack._MyStack__my_data, "Borrado de elemento de pila LIFO")

    # endregion

    # Actualización y ordenamiento no son aconsejables dentro de las pilas, si utilizas la librería de python por defecto no tendrás estos métodos


# endregion


# region Pilas (FIFO [First in - First out])
class MyStackFifo(MyStack):
    def __init__(self, data: list):
        super().__init__(data)

    def pop(self):
        """
        Elimina el primer elemento de la lista y lo retorna
        """
        assert self.size != 0
        return self._MyStack__my_data.pop(0)


def stack_fifo():
    """
    Para FIFO se crea adicional una clase que implementa MyStackFifo la cual tiene el método pop con el funcionamiento indicado(eliminar el primer elemento de la lista).
    """
    my_stack = MyStackFifo(["request1", "request2", "request3"])
    my_print(my_stack._MyStack__my_data, "Creación de pila FIFO")

    # region Inserción
    stack_length = my_stack.size()
    my_stack.push(f"request{stack_length+1}")
    my_print(my_stack._MyStack__my_data, "Inserción de datos a la pila FIFO")
    # endregion

    # region Eliminación
    try:
        # my_stack.pop()
        # my_stack.pop()
        # my_stack.pop()
        my_stack.pop()
    except:
        pass
    finally:
        my_print(my_stack._MyStack__my_data, "Eliminación de datos de la pila FIFO")

    # endregion

    # Actualización y ordenamiento no son aconsejables dentro de las pilas, si utilizas la librería de python por defecto no tendrás estos métodos


# endregion

# Quitar el comentario a la función del tipo de dato que desea revisar
# lists()
# tuples()
# sets()
# dictionaries()
# stack_lifo()
# stack_fifo()

# endregion

# region Ejercicio dificultad extra

"""
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
    - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
    - Cada contacto debe tener un nombre y un número de teléfono.
    - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
    - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos (o el número de dígitos que quieras).
    - También se debe proponer una operación de finalización del programa.
"""


# Agenda
class PhoneBook:
    def __init__(self):
        self.__phone_book = [
            {"name": "Carlos", "phone_number": 89098},
            {"name": "Marcos", "phone_number": 98780},
            {"name": "Mariela", "phone_number": 23654},
            {"name": "Mouredev", "phone_number": 911},
        ]

    def insert_data(self, name: str, phone_number: int):
        """
        Agrega un nuevo contacto

        Parameters
        ---
        name: Nombre del nuevo contacto
        phone_number: Numero de teléfono del nuevo contacto
        """
        self.__phone_book.append({"name": name, "phone_number": phone_number})

    def remove_data(self, id: int):
        """
        Elimina un contacto

        Parameters
        ---
        id: Posición del contacto en la lista
        """
        self.__phone_book.pop(id)

    def update_data(self, id, name=None, phone=None):
        """
        Selecciona un elemento de la agenda con la posición (id) y actualiza el dato que no sea null en los parámetros

        Parameters
        ---
        id: Posición del contacto
        name: Nuevo nombre del contacto
        phone: Nuevo numero del contacto
        """
        if name:
            self.__phone_book[id]['name'] = name

        if phone:
            self.__phone_book[id]['phone_number'] = phone

    def search(self, name: str):
        """
        Busca un contacto por su nombre, también retorna las coincidencias con el nombre

        Parameters:
        ---
        name: Nombre o fragmento del nombre de un contacto

        Return
        ---
        list : Contactos encontrados o lista vacía
        """
        result = []
        for i, x in enumerate(self.__phone_book):
            if (x['name'].lower()).find(name.lower()) == 0:
                result.append({"id": i, **x})

        return result

    def get_all(self):
        """
        Obtiene una lista de todos los contactos guardados
        """
        return self.__phone_book

    def size(self):
        """
        Obtiene el tamaño de la lista de los contactos
        """
        return len(self.__phone_book)


my_phone_book = PhoneBook()

max_length_phone_number = 5
# Lista de los contactos encontrados
contacts_selected = []


def print_all_phonebook():
    """
    Imprime todos los contactos guardados en la agenda
    """
    my_print(None, title="Contactos", color='yellow', space=4)
    for i, c in enumerate(my_phone_book.get_all()):
        my_print(
            None,
            title=f"{i} | \t Nombre: {c['name']} \t Teléfono: {c['phone_number']}",
            space=2,
            symbol=' ',
            color="white",
        )


def print_a_phonebook(**arg):
    """
    Imprime los datos de un contacto seleccionado

    Parameters
    ---
    **arg : Diccionario con datos del contacto a imprimir
    """
    my_print(
        None,
        title=f"{arg['id']} | \t Nombre: {arg['name']} \t Teléfono: {arg['phone_number']}",
        space=2,
        symbol=' ',
        color="white",
    )


def remove_contact(id_: int):
    """
    Elimina un contacto

    Parameter
    ---
    id_ : ID del contacto
    """
    my_phone_book.remove_data(id_)
    my_print(None, title="Contacto eliminado correctamente 🚩", space=4, color="yellow")


def my_print_error(message: str):
    """
    Muestra en consola un error

    Parameters
    ---
    message: Mensaje del error
    """
    my_print(None, title=message, space=0, color="red")


def show_menu():
    """
    Muestra el menu principal
    """
    my_print(
        None, title=f"Bienvenido(a) a tu agenda telefónica 📱", space=0, color="cyan"
    )
    my_print(
        None,
        title="[1] Ver todos tus contactos \n  [2] Buscar un contacto \n  [3] Agregar un contacto \n  [0] Cerrar",
        space=2,
        color='white',
        symbol=' ',
    )


def show_menu_search_contact():
    """
    Muestra el menu para buscar un contacto por su nombre
    """
    global contacts_selected

    my_print(None, title="Buscar contactos", color='yellow', space=4)
    to_search = input("Ingresa el nombre o parte del nombre del contacto: ")
    contacts_selected = my_phone_book.search(to_search)

    if not contacts_selected:
        my_print(
            None,
            title="No se encontró un contacto con ese nombre",
            space=4,
            color='yellow',
        )
    else:
        my_print(
            None,
            title="Contactos encontrados:",
            space=4,
            color='yellow',
        )

        for x in contacts_selected:
            print_a_phonebook(**x)

        show_submenu_contact()


def show_menu_editar(id_contact: int):
    """
    Muestra el menu para editar un contacto

    Parameters
    ---
    id_contact: ID del contacto previamente seleccionado
    """
    my_print(
        None,
        title="Puedes ingresar [0] para dejar el dato como esta 😇",
        space=4,
        color="yellow",
    )
    new_name = input("Ingresa el nuevo nombre: ")
    new_num = None

    while True:
        try:
            input_num = int(
                input(
                    f"Ingresa el nuevo numero (mínimo y máximo {max_length_phone_number} caracteres): "
                )
            )

            if input_num == 0:
                break
            elif len(str(input_num)) != max_length_phone_number:
                raise ValueError
            else:
                new_num = input_num
                break

        except ValueError:
            my_print_error("Valor ingresado invalido 💀 ")

    my_phone_book.update_data(
        id_contact, new_name if new_name != '0' else None, new_num if new_num else None
    )
    my_print(None, title="Contacto editado correctamente 😎", space=4, color="yellow")


def show_submenu_contact():
    """
    Muestra el submenu con las opciones para editar o eliminar un contacto
    """
    ids_contact_selected = [x['id'] for x in contacts_selected]
    my_print(
        None,
        title="Opciones disponibles: \n [1] Editar [2] Eliminar [3] Regresar al menu principal",
        color="yellow",
        space=0,
    )

    try:
        option_submenu = int(input("Selecciona una opción:"))

        # Editar contacto
        if option_submenu == 1:
            while True:
                contact_selected = int(
                    input("Selecciona el ID del contacto a editar: ")
                )
                if not contact_selected in ids_contact_selected:
                    my_print_error("ID seleccionado invalido 💀 ")
                    continue

                show_menu_editar(contact_selected)
                break

        # Eliminar contacto
        elif option_submenu == 2:
            while True:
                contact_selected = int(
                    input("Selecciona el ID del contacto a eliminar: ")
                )
                if not contact_selected in ids_contact_selected:
                    my_print_error("ID seleccionado invalido 💀 ")
                    continue

                remove_contact(contact_selected)
                break
        elif option_submenu == 3:
            pass
        elif not option_submenu == 1 or not option_submenu == 2:
            raise ValueError()

    except ValueError:
        my_print_error("Opción seleccionada invalida 💀")
        show_submenu_contact()


def show_menu_add_contact():
    """
    Muestra el menu para agregar un contacto
    """
    my_print(None, title="Agregar nuevo contacto", color='yellow', space=4)
    new_name = None
    new_num = None

    while True:
        name = input("Ingresa el nuevo nombre: ")
        if len(name) == 0:
            my_print_error("El nombre no puede estar vació")
            continue
        else:
            new_name = name
            break

    while True:
        input_num = input(
            f"Ingresa el nuevo numero de teléfono (mínimo y máximo {max_length_phone_number} caracteres): "
        )

        if len(input_num) != max_length_phone_number:
            my_print_error(
                f"El numero de teléfono no puede estar vació y debe tener {max_length_phone_number} caracteres"
            )
        else:
            try:
                new_num = int(input_num)
            except:
                my_print_error("Valor ingresado invalido (solo números) 💀 ")
                continue
            else:
                break

    my_phone_book.insert_data(new_name, new_num)
    my_print(None, title="Contacto agregado correctamente 🗽", space=4, color="yellow")


def start_app():
    while True:
        show_menu()

        try:
            option_selected = 0
            try:
                option_selected = int(input("Selecciona una opción: "))
            except ValueError:
                my_print_error("Opción seleccionada invalida 💀")
                continue

            if option_selected == 1:
                print_all_phonebook()

            if option_selected == 2:
                show_menu_search_contact()

            if option_selected == 3:
                show_menu_add_contact()

            if option_selected == 0:
                my_print(
                    None,
                    title="👋 Hasta la proxima!",
                    space=0,
                    color='cyan',
                )
                break
        except KeyboardInterrupt:
            my_print(
                None,
                title="👋 Hasta la proxima!",
                space=0,
                color='cyan',
            )
            exit()


start_app()

# endregion
