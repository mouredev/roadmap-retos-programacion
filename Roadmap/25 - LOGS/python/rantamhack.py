
print("\n\n=======================================EJERCICIO=======================================\n\n")

"""
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configuralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 
 * CRITICAL: El nivel mas alto de registro, se utiliza para mensajes de error cri­ticos que pueden hacer que el programa se detenga.
 * ERROR:    Se utiliza para mensajes de error que pueden ser recuperables, pero que indican un problema importante en el programa.
 * WARNING:  Se utiliza para mensajes de advertencia que no son cri­ticos, pero que indican un comportamiento inesperado o problemático.
 * INFO:     Se utiliza para mensajes informativos que indican el estado del programa o el progreso de la ejecución.
 * DEBUG:    Se utiliza para mensajes de depuraciÃ³n que proporcionan información detallada sobre el funcionamiento interno del programa.
"""

# Importamos el modulo
import logging

# Indicamos el nivel de severidad a partir del cual queremos que nos muestre el mensaje
# En este caso desde el mas bajo. Si no pusieramos nada mostrarÃ­a solo los de "Error" y "Critical"
# Tambien se le puede configurar como queremos que salga el mensaje. Vamos a poner que salga con la fecha, nivel de severidad y mensaje 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Registro de un mensaje de depuracion
logging.debug("[+] Entramos a la funcion\n")

# Registro de un mensaje de informacion
logging.info("[+] La conexion con el servidor fue exitosa\n")

# Registro de un mensaje de advertencia
logging.warning("[!] Queda poco espacio en disco\n")

# Registro de un mensaje de error
logging.error("[!] Bloque de sangria previsto\n")

# Registro de un mensaje de depuraciÃ³n
logging.critical("[!] Hay un error critico. Saliendo de la aplicacion ....\n")


print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestion de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripcion.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren informacion segun la 
 * tarea ejecutada (a tu eleccion).
 * Utiliza el log para visualizar el tiempo de ejecucion de cada tarea. 
"""
import time

#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s - %(levelname)s - %(message)s')

def time_spent(function):
    def time_used(*args, **kwargs):
        init = time.time()
        result = function(*args, **kwargs)
        elapsed_time = time.time() - init
        logging.info(f"[+] El tiempo empleado en {function.__name__} es {elapsed_time:.4f} segundos")
        return result
    return time_used

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Task_Manager:
    def __init__(self):
        self.tasks = []

    @time_spent
    def add_task(self, task):
        logging.debug("[*] Comienza la funcion para 'añadir tareas'")
        time.sleep(1)
        if any(t['name'] == task.name for t in self.tasks):
            logging.warning("[!] La tarea ya esta en la lista")
        else:
            self.tasks.append({
                'name': task.name,
                'description': task.description
            })
            time.sleep(1)
            logging.info("[+] Se agrega nueva tarea")
            logging.debug("[*] Finaliza la funcion 'añadir tareas'")
    
    
    @time_spent
    def del_task(self, task_name):
        logging.debug("[*] Comienza la funcion para 'borrar tareas'")
        time.sleep(1)
        self.tasks = [task for task in self.tasks if task['name'] != task_name]
        logging.info(f"[-] Se elimino la tarea: {task_name}")
        logging.debug("[*] Finaliza la funcion 'borrar tareas'")
    
    @time_spent            
    def list_tasks(self):
        logging.debug("[*] Comienza la funcion para 'listar tareas'")
        time.sleep(1)
        for task in self.tasks:
            logging.info(f"[+] Tarea: {task['name']} - Descripcion: {task['description']}")
        logging.debug("[*] Finaliza la funcion 'listar tareas'")    
            
            
    
if __name__ == "__main__":
    task_manager = Task_Manager()

    task1 = Task("Tarea 1", "Descripcion de la tarea 1")
    task2 = Task("Tarea 2", "Descripcion de la tarea 2")
    task3 = Task("Tarea 3", "Descripcion de la tarea 3")
    
    
    task_manager.add_task(task1)  
    task_manager.add_task(task2)
    task_manager.add_task(task3)
    task_manager.add_task(task1)


    task_manager.list_tasks()
    task_manager.del_task("Tarea 2")
    task_manager.list_tasks()



    
