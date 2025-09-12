import logging

# Configurar logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Crear logger
logger = logging.getLogger(__name__)

# Mensajes de logs
logger.debug('Mensaje de depuración')
logger.info('Mensaje de información')
logger.warning('Mensaje de advertencia')
logger.error('Mensaje de error')
logger.critical('Mensaje crítico')

'''
EXTRA
'''
import random

class TaskManager:
    def __init__(self) -> None:
        self.tasks={}
        logger.info('Gestor de tareas iniciado')

    def add_task(self):
        name = input('Nombre de la tarea a agregar: ')
        description = input('Descripción de la tarea: ')
        if name in self.tasks:
            logger.warning(f'Tarea ya existente: {name}')
            return
        exec_time = random.randint(1, 5)
        self.tasks[name] = {
            'description': description,
            'exec_time': exec_time
        }
        logger.info(f'Tarea{name} añadida')
        logger.debug(f'tiempo de ejecución de la tarea {name}: {exec_time} segundos')
    
    def delete_task(self):
        name = input('Ingrese tarea a eliminar: ')
        if name not in self.tasks:
            logger.warning(f'Tarea inexistente: {name}')
            return
        del self.tasks[name]
        logger.info(f'Tarea {name} eliminada')

    def get_task(self):
        name = input('Buscar tarea: ')
        if name not in self.tasks:
            logger.warning(f'Tarea inexistente: {name}')
            return
        task = self.tasks[name]
        print(f"Tarea: {name}\n\tDescripción: {task['description']}\n\tTiempo de ejecución: {task['exec_time']} segundos")
        logger.info(f'Información de la tarea {name} proporcionada')
        
    
    def list_tasks(self):
        if not self.tasks:
            logger.info('No se encontraron tareas')
            return
        for name, info in self.tasks.items():
            print(f"Tarea: {name}:\n\tDescripción: {info['description']}\n\tTiempo de ejecución: {info['exec_time']} segundos")
            logger.info(f"Tiempo de ejecucion de la tarea '{name}' es {info['exec_time']} segundos.")

managment = TaskManager()

while True:
    print('Gestor de tareas')
    print('1. Añadir tarea')
    print('2. Eliminar tarea')
    print('3. Buscar tera')
    print('4. Listar tareas')
    print('5. Salir')

    choice = input('>>> ')
    if choice == '1':
        managment.add_task()
    elif choice == '2':
        managment.delete_task()
    elif choice == '3':
        managment.get_task()
    elif choice == '4':
        managment.list_tasks()
    elif choice == '5':
        break
    else:
        print('Opción no válida')
