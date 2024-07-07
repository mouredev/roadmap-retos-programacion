import logging


LOGFILE = "isilanes.log"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Fijamos el nivel mínimo de logs a DEBUG:
    logger.setLevel(logging.DEBUG)

    # Console handler (salida a pantalla):
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Formateador para consola:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)

    # Añadir el console handler al logger:
    logger.addHandler(handler)

    # File handler (salida a fichero):
    handler = logging.FileHandler(filename=LOGFILE)
    handler.setLevel(logging.WARNING)

    # Formateador para fichero:
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    handler.setFormatter(formatter)

    # Añadir el console handler al logger:
    logger.addHandler(handler)

    return logger


def get_logger_extra(filename: str) -> logging.Logger:
    logger = logging.getLogger("TaskManager")

    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=filename)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


log = get_logger(__name__)


class TaskManager:
    log_filename = "task_manager.log"
    log = get_logger_extra(log_filename)

    def __init__(self):
        self.tasks = {}

    def contains(self, name: str) -> bool:
        return name in self.tasks

    def add(self, name: str, description: str) -> None:
        if self.contains(name):
            self.log.warning(
                "Pasamos de añadir la tarea '%s', porque ya existe en TaskManager.",
                name,
            )
            return

        self.tasks[name] = description
        self.log.info("La tarea '%s' fue añadida al TaskManager", name)

    def remove(self, name: str) -> None:
        if not self.contains(name):
            self.log.warning("No podemos eliminar la tarea '%s', puesto que no existe.", name)
            return

        del self.tasks[name]
        self.log.info("La tarea '%s' fue eliminada del TaskManager", name)

    def list(self) -> None:
        print("Lista de tareas pendientes:")
        for i, (task, desc) in enumerate(self.tasks.items()):
            print(f" {i+1:2d} - {task}: {desc}")

    def summary(self) -> None:
        """
        Nótese que parsear el log de esta manera es frágil, y podría ser buena
        idea usar algún tipo de log estructurado.
        """
        tasks = {}


def main():
    print("===== MAIN =====")
    who = "Iñaki"
    log.debug(
        "Hemos configurado el logger para usar loguear por pantalla todo, y por fichero todo"
        " lo que sea WARNING o más grave."
    )
    log.debug(
        "Mencionar que los formatos del mensaje en fichero y por pantalla pueden configurarse"
        " por separado (y lo hemos hecho)."
    )
    log.debug("%s, un mensaje de nivel DEBUG sólo saldrá por pantalla", who)
    log.info("%s, un mensaje de nivel INFO sólo saldrá por pantalla", who)
    log.warning(
        "%s, un mensaje de nivel WARNING saldrá por pantalla y también irá a fichero (%s)",
        who,
        LOGFILE,
    )
    log.error(
        "%s, un mensaje de nivel ERORR saldrá por pantalla y también irá a fichero (%s)",
        who,
        LOGFILE,
    )
    log.critical(
        "%s, un mensaje de nivel ERROR saldrá por pantalla y también irá a fichero (%s)",
        who,
        LOGFILE,
    )


def extra():
    print("\n===== EXTRA =====")
    print("Inicializamos el gestor de tareas:")
    print('>>> tm = TaskManager()')
    tm = TaskManager()

    print("\nAñadimos tareas:")
    print('>>> tm.add(name="fregar", description="Fregar los platos")')
    print('>>> tm.add(name="leer", description="Dedicar un rato a leer un libro")')
    tm.add(name="fregar", description="Fregar los platos")
    tm.add(name="leer", description="Dedicar un rato a leer un libro")

    print("\nHemos configurado TaskManager para que esas acciones sólo guarden log a fichero.")
    print("Podemos listar las tareas activas (esto no guarda log, y sólo imprime por pantalla):")
    print('>>> tm.list()')
    tm.list()

    print("\nSi intentamos añadir una tarea repetida, será ignorada (y un aviso añadido al log):")
    print('>>> tm.add(name="fregar", description="Quiero fregar más")')
    tm.add(name="fregar", description="Quiero fregar más")
    print('>>> tm.list()')
    tm.list()

    print("\nPodemos eliminar una tarea:")
    print('>>> tm.remove(name="fregar")')
    tm.remove(name="fregar")
    print('>>> tm.list()')
    tm.list()

    print("\nIntentar eliminar una tarea no existente no hará nada (y guardará aviso en log):")
    print('>>> tm.remove(name="bailar")')
    tm.remove(name="bailar")
    print('>>> tm.list()')
    tm.list()


if __name__ == "__main__":
    main()
    extra()
