# /*
#  * EJERCICIO:
#  * He presentado mi proyecto más importante del año: mouredev pro.
#  * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
#  * programación de una manera diferente.
#  * Cualquier persona suscrita a la newsletter de https://mouredev.pro
#  * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
#  *
#  * Desarrolla un programa que lea los registros de un fichero .csv y
#  * seleccione de manera aleatoria diferentes ganadores.
#  * Requisitos:
#  * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
#  *    o "inactivo" (y datos ficticios).
#  *    Ejemplo: 1 | test@test.com | activo
#  *             2 | test2@test.com | inactivo
#  *    (El .csv no debe subirse como parte de la corrección)
#  * 2. Recupera los datos desde el programa y selecciona email aleatorios.
#  * Acciones:
#  * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
#  *    ganador de una suscripción, otro ganador de un descuento y un último
#  *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
#  * 2. Muestra los emails ganadores y su id.
#  * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
#  *    no debe tenerse en cuenta.
#  */
import os.path
import csv
import uuid
import random


class Subscriptor():
    """
        Clase que representa a un subscriptor.
    """
    __headers = ['email', 'status','id']

    def __init__(self,email: str, status: bool, id = uuid.uuid1()) -> None:
        self.id = id
        self.email = email
        self.status = status
    
    def __str__(self) -> str:

        estado  = "activo" if self.status  else "inactivo"

        return f"El subscritor {self.id} - {self.email} - {estado} "

    @classmethod
    def get_headers(cls):
        return cls.__headers

class CSVFile():
    """
        Clase que representa a un CSV.
    """

    __path_file = "subscriptores.csv"
    __subscriptores = []

    def __init__(self)-> None:

        if self.check_file():
            self.cargar_datos()
        else:
            self.crear_fichero()

    def check_file(self)-> bool:
        return True if os.path.isfile(self.__path_file) else False
    
    def add_subscriptor(self, subscriptor: Subscriptor)-> bool:
        if any([value for value in self.__subscriptores if value.email == subscriptor.email]):
            print(f'el subscriptor {subscriptor.email} ya existe por lo tanto no se añadirá.')
            return False
        self.__subscriptores.append(subscriptor)
        return True

    def cargar_datos(self)-> bool:
        print(f"Cargando fichero {self.__path_file}....")
        try:
            self.__subscriptores = []
            with open(self.__path_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    status = True if line[Subscriptor.get_headers()[1]] == "True" else False
                    subscriptor = Subscriptor(line[Subscriptor.get_headers()[0]], status , line[Subscriptor.get_headers()[2]])
                    self.__subscriptores.append(subscriptor)

        except Exception as e:
            print(f"No se ha podido cargar los datos {e}")
            print("Creando nuevo fichero....")
            self.crear_fichero()

    def crear_fichero(self)-> bool:
        try:
            with open(self.__path_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=Subscriptor.get_headers())
                writer.writeheader()
        except Exception as e:
            print(f"Ha habido un error al crear el fichero {e}")
            return False
        return True

    def guardar_datos(self)-> bool:

        if len(self.__subscriptores) !=0:
            try:
                with open(self.__path_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=Subscriptor.get_headers())

                    writer.writeheader()

                    for subscriptor in self.__subscriptores:
                        writer.writerow({
                            'email': subscriptor.email,
                            'status': subscriptor.status,
                            'id': subscriptor.id
                        })
            except Exception as e:
                print(f"No se ha podido guardar los datos {e}")
                return False
        else:
            return False
        
        return True

    def leer_datos(self)-> None:
        if len(self.__subscriptores) !=0:

            for subscriptor in self.__subscriptores:

                print(subscriptor)

    def generar_ganador(self) -> Subscriptor:
        
        return random.choice(self.__subscriptores)

    def sorteo(self) -> None:
        ganadores = []
        def backtracking(ganadores_provicionales: list, indice: int):
            if len(ganadores_provicionales) == 3:
                ganadores.extend(ganadores_provicionales)
                return
            if indice >= len(self.__subscriptores):
                return
            
            for i in range(indice, len(self.__subscriptores)):
                subscriptor_random = random.choice(self.__subscriptores)
                if subscriptor_random not in ganadores_provicionales and subscriptor_random.status:
                    ganadores_provicionales.append(subscriptor_random)
                    backtracking(ganadores_provicionales, i+1)
                    if len(ganadores) == 3:
                        return
                    ganadores_provicionales.pop()

        if len([subs for subs in self.__subscriptores if subs.status]) > 3:
            backtracking([],0)

            if len(ganadores) == 3:
                print(f"El ganador de la subscripción es: {ganadores[0]}")
                print(f"El ganador del descuento es: {ganadores[1]}")
                print(f"El ganador del libro es: {ganadores[2]}")
            else:
                print("No se ha podido encontrar una combinación ganadora, intentalo otra vez.")
        else:
            print("No tenemos suficientes subscriptores activos para hacer el sorteo.")


csv_gestion = CSVFile()

subscriptor_1 = Subscriptor('sub10@gmail.com',True)
subscriptor_2 = Subscriptor('sub0@gmail.com',True)
subscriptor_3 = Subscriptor('sub2@gmail.com',False)
subscriptor_4 = Subscriptor('sub1@gmail.com',True)
subscriptor_5 = Subscriptor('sub3@gmail.com',False)



csv_gestion.add_subscriptor(subscriptor_1)
csv_gestion.add_subscriptor(subscriptor_2)
csv_gestion.add_subscriptor(subscriptor_3)
csv_gestion.add_subscriptor(subscriptor_4)
csv_gestion.add_subscriptor(subscriptor_5)



# csv_gestion.guardar_datos()

#csv_gestion.leer_datos()
csv_gestion.sorteo()