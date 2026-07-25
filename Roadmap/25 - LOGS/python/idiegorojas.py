"""
25 - Logs
"""
# Es uan herramienta para rastrear enventos que ocurren cuando se ejecuta un software
# Se puede usar para:
    # Depurar codigo
    # Monitorear el comportamiento de una aplicacion
    # Mantener registros historicos

"""
Estructura
"""
# DEBUG: Informacion detallada cuando ocurre un problema
# INFO: Confirmacion de que este funcionando como se espera
# WARNING: Indicacion que algo inesperado ocurrio o podria ocurrir
# Error: Problemas mas grabe, el software no realiza alguna funcion
# CRITICAL: Un error muy grave, no permite que el programa se ejecute

"""
Usos y Funcionalidad
"""
# Depuración: Ayuda a rastrear y diagnosticar problemas en el código.
# Monitoreo: Permite monitorear la actividad de la aplicación en tiempo real.
# Auditoría: Mantiene un registro histórico de eventos importantes y errores.
# Mantenimiento: Facilita el mantenimiento y la mejora del software al proporcionar un historial de eventos y errores.

"""
Ejemplos:
"""
# Configuracion de un login
import logging

# Configura el logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # fecha, nombre del logger, nivel de severidad, mensaje.
                    handlers=[logging.FileHandler("app.log"),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)

# Ejemplos de logging
logger.debug('Esto es un mensaje de depuración')
logger.info('Esto es un mensaje de información')
logger.warning('Esto es una advertencia')
logger.error('Esto es un mensaje de error')
logger.critical('Esto es un mensaje crítico')


# Procesar pedidos een una tienda en linea
def procesar_pedidos(order_id):
    logger.info(f'Procesando el pedido: {order_id}')
    try:
        if order_id == 0:
            raise ValueError('El ID del pedido no puede ser 0')
        logger.info(f'El pedido: {order_id} procesado exitosamante')
    except ValueError as e:
        logger.error(f'Error al procesar el pedido {order_id}: {e}')
    except Exception as e:
        logger.critical(f'Error critico al procesar el pedido {order_id}: {e}')

print(procesar_pedidos(1))
print(procesar_pedidos(0))


"""
Extra
"""
# Añadir, eliminar, listar tareas


class GestorTareas:

    def __init__(self) -> None:
        self.tareas = {}
        # Puedes usar el logger que ya configuraste
        self.logger = logging.getLogger(__name__)

    def añadir(self, nombre: str, descripcion: str):
        if not nombre or not descripcion:
            print("El nombre y la descripción no pueden estar vacíos")
            self.logger.warning("Intento de añadir tarea con campos vacíos")
            return
            
        if nombre not in self.tareas:
            self.tareas[nombre] = descripcion
            print(f'Se añadió la tarea {nombre}')
            self.logger.info(f'Tarea añadida: {nombre}')
        else:
            print(f'Lo sentimos, ya existe la tarea {nombre}.')
            self.logger.warning(f'Intento de añadir tarea duplicada: {nombre}')

    def listar(self, nombre: str):
        if nombre in self.tareas:
            print(f'La tarea {nombre} tiene la siguiente descripción: {self.tareas[nombre]}')
            self.logger.info(f'Tarea consultada: {nombre}')
        else:
            print(f'No existe la tarea con el nombre: {nombre}')
            self.logger.warning(f'Intento de consultar tarea inexistente: {nombre}')
            
    def listar_todas(self):
        if not self.tareas:
            print("No hay tareas registradas")
            return
            
        print("Lista de todas las tareas:")
        for nombre, descripcion in self.tareas.items():
            print(f"- {nombre}: {descripcion}")
        self.logger.info('Listado completo de tareas solicitado')

    def modificar(self, nombre: str, nueva_descripcion: str):
        if nombre in self.tareas:
            self.tareas[nombre] = nueva_descripcion
            print(f'La tarea {nombre} ha sido modificada')
            self.logger.info(f'Tarea modificada: {nombre}')
        else:
            print(f'No existe la tarea con el nombre: {nombre}')
            self.logger.warning(f'Intento de modificar tarea inexistente: {nombre}')

    def eliminar(self, nombre: str):
        if nombre in self.tareas:
            del self.tareas[nombre]
            print(f'La tarea {nombre} ha sido eliminada')
            self.logger.info(f'Tarea eliminada: {nombre}')
        else:
            print('Lo sentimos, la tarea no ha sido eliminada porque no existe')
            self.logger.warning(f'Intento de eliminar tarea inexistente: {nombre}')


gestor = GestorTareas()
gestor.añadir('Comprar leche', 'Comprar 2 litros de leche en el supermercado')
gestor.añadir('Llamar al médico', 'Concertar cita para el próximo mes')
gestor.listar_todas()
gestor.modificar('Comprar leche', 'Comprar 1 litro de leche deslactosada')
gestor.listar('Comprar leche')
gestor.eliminar('Comprar leche')