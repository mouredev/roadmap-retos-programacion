"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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

# Ejemplos de estructuras:

my_list = []
my_tuple = ()
my_set = set()
my_dict = {}

# Dificultad extra:

def agenda():

    agenda = {}
    input_operacion = None

    while input_operacion != "salir":

        completed = False
        print("AGENDA:")
        print("----------------------------------------")
        print(agenda)
        print("----------------------------------------")
        input_operacion = input("Seleccione la operación que quiere realizar: \n Buscar \n Insertar \n Actualizar \n Eliminar \n Salir\n").lower()

        if input_operacion == "buscar":

            input_nombre = input("Indique el nombre del contacto: ")

            if input_nombre in agenda:
                print(agenda[input_nombre])
            else:
                print("No existe ningún contacto con ese nombre.")
        
        elif input_operacion == "insertar":

            input_nombre = input("Introduce el nombre del contacto: ")

            if input_nombre in agenda:
                print("El contacto" + input_nombre + " ya existe.")

            else:
                while not completed:
                    input_numero = input("Introduce el número del contacto: ")
                    numero_telefono = tuple(input_numero)

                    if len(numero_telefono) == 9 and input_numero.isnumeric():
                        completed = True
                        agenda [input_nombre] = input_numero
                        print("Se ha añadido el contacto " + input_nombre + " con el número: " + input_numero + " a la agenda.")
                    
                    else:
                        print("Número de teléfono no válido.")

        elif input_operacion == "actualizar":

            print(agenda.keys())
            input_nombre = input("Que contacto quieres actualizar? ")

            if input_nombre in agenda:

                while not completed:

                    input_numero = input("Introduce el nuevo número del contacto: ")
                    numero_telefono = tuple(input_numero)

                    if len(numero_telefono) == 9 and input_numero.isnumeric():
                        completed = True
                        agenda [input_nombre] = input_numero
                        print("El contacto " + input_nombre + " se ha actualizado correctamente.")
                        
                    else:
                        print("Número de teléfono no válido.")
            else: 
                print("Este contacto no existe")

        elif input_operacion == "eliminar":
            
            print(agenda.keys())
            input_nombre = input("Que contacto quieres eliminar? ")

            if input_nombre in agenda:
                del agenda[input_nombre]
                print("El contacto " + input_nombre + " se eliminó correctamente")
            else:
                print("Este contacto no existe")

        else:
            print("Instrucción no válida. Introduce una instrucción válida.")

agenda()