import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(filename="cyberdidac.log", encoding='utf-8', level=logging.DEBUG)

tasks = []


class Task:
    name: str
    date: datetime
    description: str

    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description


def add_task(name, date, description):
    new_task = Task(name=name, date=date, description=description)
    tasks.append(new_task)
    logger.info(f"Tarea '{name}' añadida: {datetime.now()}")


def delete_task(name):
    find = False

    for i, task in enumerate(tasks):
        if task.name == name:
            tasks.pop(i)
            print("Tarea eliminada")
            logger.info(f"Tarea '{name}' eliminada: {datetime.now()}")
            find = True
            break

    if not find:
        print(f"La tarea '{name}' no existe")
        logger.warning(f"La tarea '{name}' no existe: {datetime.now()}")


def list_tasks():
    logger.info(f"Tareas listadas: {datetime.now()}")
    for task in tasks:
        print(f"\n> {task.name}")
        print(f"{task.date}")
        print(f"{task.description}")


def main():
    print("\nBienvenido a gestor de tareas")

    quit = False

    while not quit:
        print("\n¿Qué deseas realizar?"
              "\n1 - Añadir tarea"
              "\n2 - Eliminar tarea"
              "\n3 - Mostrar tareas"
              "\n4 - Finalizar")

        choice = input("> ")

        match choice:
            case "1":
                try:
                    name = input("Nombre: ")

                    day = int(input("Day: "))
                    month = int(input("Month: "))
                    year = int(input("Year: "))
                    hour = int(input("Hour: "))
                    minute = int(input("Minute: "))
                    date = datetime(year=year, month=month, day=day, hour=hour, minute=minute)

                    description = input("Description: ")

                    add_task(name, date, description)
                except Exception as e:
                    print("Error: datos incorrectos")
                    logger.error(f"Datos introducidos incorrectos: {datetime.now()}")
            case "2":
                name = input("Nombre: ")
                delete_task(name)
            case "3":
                list_tasks()
            case "4":
                quit = True
                print("Hasta pronto")
                logger.info(f"Sesión finalizada: {datetime.now()}")
            case _:
                print("Acción no válida")
                logger.error(f"Intento de ejecución de acción inválida: {datetime.now()}")


if __name__ == '__main__':
    main()
