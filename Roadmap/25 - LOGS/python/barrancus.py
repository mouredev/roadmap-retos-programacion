#25 - Pyton - Logs 
# EJERCICIO:
# Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
# un ejemplo con cada nivel de "severidad" disponible.
# 
# DIFICULTAD EXTRA (opcional):
# Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
# y listar dichas tareas.
# - Añadir: recibe nombre y descripción.
# - Eliminar: por nombre de la tarea.
# Implementa diferentes mensajes de log que muestren información según la
# tarea ejecutada (a tu elección).
# Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
# 
import logging as log
import os

class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

identifier = iter(Counter())

class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.identifier = f'{next(identifier):03}'

    def __str__(self):
        return f'{self.identifier} - {self.name}: {self.description}'
    
    def show_task(self):
        print(self)

def separacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena * 20}')

contador = iter(Counter())

log.basicConfig(filename=r'.\25_logs.log',
                level=log.DEBUG,
                format='%(asctime)s - %(name)s - %(funcName)-8s - %(levelname)-8s - %(message)s',
                encoding='utf-8')

def mensages_log() -> None:
    separacion('-:-')
    log.debug('Este es un mensaje de DEBUG')
    log.info('Este es un mensaje de INFO')
    log.warning('Este es un mensaje de WARNING')
    log.error('Este es un mensaje de ERROR')
    log.critical('Este es un mensaje de CRITICAL')
    print('Mensajes de log generados. Revisar el archivo 25_logs.log')

def task_manager() -> None:
    separacion('-:-')
    tasks = []
    while True:
        print("\nGestor de Tareas")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("0. Salir")
        option = input("Selecciona una opción: ")
        
        match option:
            case'1':
                name = input("\nNombre de la tarea: ")
                description = input("Descripción de la tarea: ")
                tasks.append(Task(name, description))
                log.info(f'Tarea añadida: {tasks[-1].name} - {tasks[-1].description}')
                print(f'Tarea "{tasks[-1].name}" añadida.')
            case'2':
                name = input("\nNombre de la tarea a eliminar: ")
                for task in tasks:
                    if task.name == name:
                        tasks.remove(task)
                        break
                log.warning(f'Tarea eliminada: {name}')
                print(f'Tarea "{name}" eliminada.')
                print(f'Tareas pendientes: {len(tasks)}')
            case '3':
                log.info('Listado de tareas solicitado')
                for task in tasks:
                    task.show_task()
            case'0':
                log.info('Salida del gestor de tareas')
                print("Saliendo del gestor de tareas.")
                break
            case _:
                log.error('Opción inválida seleccionada')
                print("Opción inválida. Inténtalo de nuevo.")

def main():
    mensages_log()
    task_manager()
    log.shutdown()
    print("\nQuieres borrar el archivo de logs? (s/n): ", end='')
    if input().lower() == 's':
        os.remove(r'.\25_logs.log')

if __name__ == '__main__':
    main()
