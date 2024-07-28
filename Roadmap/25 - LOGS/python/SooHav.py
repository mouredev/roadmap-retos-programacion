# 25 LOGS

# Ejercicio

import logging
import requests
import time


# Niveles de log
# -----------------------------------------------------------------------------
# DEBUG = 10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

# Definición del logger root
# -----------------------------------------------------------------------time.sleep------
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
)

# ========================== SCRIPT ============================================


def info_pokemon(id=None, name=None):
    logging.debug(
        "Comienza el proceso de recopilación de información con la función info_pokemon con un ID o nombre")
    if id is not None:
        url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    elif name is not None:
        url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    else:
        logging.warning("Debes proporcionar un ID o un nombre.")
        return

    response = requests.get(url)

    if response.status_code == 200:
        logging.info("La respuesta fue exitosa")
        pokemon = response.json()
        try:
            print(f"Nombre: {pokemon['name']}")
            print(f"ID: {pokemon['id']}")
            print(f"Peso: {pokemon['weight']} hectogramos")
            print(f"Altura: {pokemon['height']} decímetros")
            print("Tipos:")
            for tipo in pokemon['types']:
                print(f"  - {tipo['type']['name']}")
            logging.debug("Información básica del Pokémon mostrada con éxito.")
        except KeyError as e:
            logging.error(f'Error al extraer información del Pokémon: {e}')

    elif response.status_code == 404:
        logging.critical(
            "El Pokémon no fue encontrado. Revisa el ID o el nombre proporcionado.")
    else:
        logging.error(f'Error: {response.status_code}')


# Ejemplo de uso
info_pokemon(25)
info_pokemon(name="pikachu")
info_pokemon(name="pokefalso")
logging.debug("Fin del script")

# Extra

# Definición del logger root
# -----------------------------------------------------------------------------

# Create a logger object
logger = logging.getLogger(__name__)

# Setear el nivel DEBUG
logger.setLevel(logging.DEBUG)

# Formatter
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Asignar formatter a 'formatter'
logger.formatter = f_format

# Handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
logger.addHandler(c_handler)

# ========================== SCRIPT ============================================


def medir_tiempo(func):
    """
    Función para medir el tiempo de ejecución de las funciones.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion = func(*args, **kwargs)
        fin = time.time()
        logging.debug(f"Tiempo de ejecución de '{func.__name__}': {
                      fin - inicio:.6f} segundos")
        return funcion
    return wrapper


class Tarea:
    """
    Clase que representa una tarea con nombre y descripción.
    """

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class GestorTareas:
    """
    Clase que gestiona una lista de tareas.
    """

    def __init__(self):
        self.tareas = []

    @medir_tiempo
    def agregar_tarea(self, nombre, descripcion):
        """
        Agrega una nueva tarea a la lista.
        """
        nueva_tarea = Tarea(nombre, descripcion)
        self.tareas.append(nueva_tarea)
        time.sleep(5)
        logging.info(f"Tarea '{nombre}' agregada con éxito.")

    @medir_tiempo
    def eliminar_tarea(self, nombre):
        """
        Elimina una tarea de la lista por su nombre.
        """
        tarea_eliminada = None
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea_eliminada = tarea
                break
        if tarea_eliminada:
            self.tareas.remove(tarea_eliminada)
            time.sleep(3)
            logging.info(f"Tarea '{nombre}' eliminada con éxito.")
        else:
            logging.warning(f"Tarea '{nombre}' no encontrada.")

    @medir_tiempo
    def listar_tareas(self):
        """
        Muestra una lista de todas las tareas.
        """
        if self.tareas:
            logging.debug("Lista de tareas:")
            for tarea in self.tareas:
                logging.info(f"- {tarea.nombre}: {tarea.descripcion}")
        else:
            logging.warning("No hay tareas pendientes.")


# Ejemplo de uso
gestor = GestorTareas()

# Agregar tareas
gestor.agregar_tarea("Comprar", "Hacer la compra semanal en el super.")
gestor.agregar_tarea(
    "Limpiar", "Limpiar todos los ambientes de la casa y ordenar el placard.")
gestor.agregar_tarea("Ejercitar", "Hacer los ejercicios de Roadmap.")

# Listar tareas
gestor.listar_tareas()

# Eliminar tarea
gestor.eliminar_tarea("Limpiar")

# Listar tareas nuevamente
gestor.listar_tareas()
