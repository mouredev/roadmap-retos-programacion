import os, platform,logging

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
"""


#Valores representativos en número de cada nivel de severidad
#NONSET = 0
#DEBUG = 10
#INFO = 20
#WARNING = 30
#ERROR = 40
#CRITICAL = 50

LEVELS = {
	'notset': logging.NOTSET,
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

level = LEVELS.get('debug')#Podemos establecer el nivel mínimo de severidad desde una variable
    

logging.basicConfig(
	#filename="#25.log", #Podemos creal un fichero con extensión .log para almacenar los mensajes de logging
	#filemode= "a", # Con el modo "a" añadimos siempre al final del fichero los nuevos mensajes, con "w" solo se guradan los últimos mensajes
	encoding="utf-8",
	level=level,#Tambien podemos asignar a la clave level del diccionario de configuración básico el propio nivel
	# así: level=logging.DEBUG o con su valor numérico así: level=10
	format="%(asctime)s,%(msecs)1d - %(levelname)s %(message)s",#En format determinamos el formato del mensaje de logging
	datefmt='%d-%B-%Y,%H:%M:%S'#En datefmt le damos formato concreto a la fecha y hora igual que haríamos con datetime.datetime.strftime()
)


def division(a:int, b:int)->int:
	try:
		result = round((a / b),2)
		logging.info(f"División de {a} entre {b}. Resultado: {result} , operación correcta")
		#Mensaje de logging formateado para mostrar si el resultado de la función es correcto
	except ZeroDivisionError as zero:
		result = None
		logging.error(zero)
	except TypeError as type:
		result = None
		logging.error(type)

	return result

def to_upper(text:str)->str: #Podemos prevenir los posibles errores dentro de las funciones con generación de mensajes de logging
	try:
		text = text*2
		text = text.upper()
		
		logging.info(text)
	except ValueError as val:
		text = None
		logging.warning(val) #Dentro de una excepción específica..
	except Exception as ex:
		text = None
		logging.warning(ex) # o dentro de una excepción genérica
	
	return text

def show_element(my_list:list,index:int)->int:
	try:
		num = my_list[index]
		logging.info(f"El índice {index} de la lista {my_list} es {num}")
		#Mensaje de logging formateado para mostrar si el resultado de la función es correcto
	except IndexError as indexerr:
		num = None
		logging.critical(indexerr)
	
    

try:
	division(8, 3)#Función con valores válidos para una división
	division(2, 0)#Aquí provocamos un error de division entre cero
	division(9, "3")#Aquí provocamos un error de tipo de dato
	print()
	show_element([1,2,3],2)#Función con valores correctos para mostrar un elemento de una lista
	show_element([1,2,3],3)#Aquí provocamos un error de fuera de índice
	print()
	to_upper(45)#Provocamos un error porque aunque un int admite multiplicación no admite el método .upper()
	to_upper("Hola Python ")#Aquí le pasamos un string que admite multiplicación y método .upper()
	to_upper("Hola", "Python")#Aquí provocamos que no se pueda ejecutar la función y el programa salta al except,
	# si pusiéramos esta llamada al principio de esta lista no se ejecutaría ninguna llamada
	
except Exception as ex:
	logging.warning(ex)
	print("excepción general antes de la función")
	#Tambien podemos prevenir los errores que no permiten ejecutar la función como en el caso de
	# to_upper() al que le estamos pasando 2 argumentos cuando requiere solo uno


	#Tambien podemos generar mensajes de logging no relacionados con la propia ejecución como este que
	# nos da información del sistema operativo , su versión y la versión en este caso de python que estamos usando
logging.info(f"Runnig at: {platform.platform()} with Python {platform.python_version()}")


""" * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea."""


tasks = {}

def add_task(task:str,description:str):
	tasks[task]= description
	logging.info(f"La tarea {task} se ha añadido correctamente\n")

def show_tasks():
	[print("Tarea: ", t ,"- Descripción: ", d , end = '\n') for t,d in tasks.items()]
print()
	
def delete_task(task:str):
	if task in tasks:
		tasks.pop(task)
		logging.info(f"La tarea {task} ha sido eliminada correctamente\n")
	else:
		logging.warning(f"Tarea {task} no encontrada\n")


while True:
	option = input("-1 Mostrar tareas \n-2 Añadir tarea \n-3 Borrar tarea \n-4 Salir\nSeleccione una opción: ")
	if not option.isdigit():
		logging.error(": Sólo se pueden introducir caracteres numéricos, intente de nuevo\n")
	elif int(option)<1 or int(option)>4:
		logging.warning(": El número no debe ser diferente a las opciones mostradas, intente de nuevo\n")
	else:	
		option = int(option)

		if option == 1:
			logging.debug("listado de tareas:")
			show_tasks()
			continue
		elif option == 2:
			task_name = input("Escriba el nombre de la tarea: ")
			task_desc = input("Describa la tarea: ")
			add_task(task_name,task_desc)
			continue
		elif option == 3:
			task_name = input("Escriba el nombre de la tarea a borrar: ")
			delete_task(task_name)
			continue
		elif option == 4:
			logging.warning(": Está saliendo del programa")
			break
		
		