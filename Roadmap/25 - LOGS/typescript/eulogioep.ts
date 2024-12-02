/**
 * TEORÍA SOBRE LOGGING EN TYPESCRIPT
 * 
 * El logging es una práctica fundamental en el desarrollo de software que permite:
 * - Registrar eventos y estados durante la ejecución del programa
 * - Facilitar la depuración y el diagnóstico de problemas
 * - Monitorear el rendimiento y comportamiento de la aplicación
 * 
 * Niveles de severidad comunes:
 * - ERROR: Errores críticos que impiden el funcionamiento correcto
 * - WARN: Advertencias sobre situaciones potencialmente problemáticas
 * - INFO: Información general sobre el flujo del programa
 * - DEBUG: Información detallada útil para depuración
 * - TRACE: Información muy detallada sobre el flujo de ejecución
 */

// Importamos la biblioteca de logging (en este caso usaremos console por simplicidad)
class Logger {
    static error(message: string) {
        console.error(`[ERROR] ${new Date().toISOString()} - ${message}`);
    }

    static warn(message: string) {
        console.warn(`[WARN] ${new Date().toISOString()} - ${message}`);
    }

    static info(message: string) {
        console.info(`[INFO] ${new Date().toISOString()} - ${message}`);
    }

    static debug(message: string) {
        console.debug(`[DEBUG] ${new Date().toISOString()} - ${message}`);
    }

    static trace(message: string) {
        console.trace(`[TRACE] ${new Date().toISOString()} - ${message}`);
    }
}

// Ejemplo básico de uso de diferentes niveles de logging
function demonstrateLogging() {
    Logger.error("Error crítico en la conexión a la base de datos");
    Logger.warn("El espacio en disco está por debajo del 20%");
    Logger.info("Aplicación iniciada correctamente");
    Logger.debug("Valor de la variable x: 42");
    Logger.trace("Entrando en la función calculateTotal()");
}

// Definición de la interfaz para una tarea
interface Task {
    name: string;
    description: string;
    createdAt: Date;
}

// Clase para la gestión de tareas
class TaskManager {
    private tasks: Task[] = [];

    /**
     * Añade una nueva tarea al sistema
     * @param name Nombre de la tarea
     * @param description Descripción de la tarea
     */
    addTask(name: string, description: string): void {
        const startTime = performance.now();
        
        try {
            // Verificar si ya existe una tarea con el mismo nombre
            if (this.tasks.some(task => task.name === name)) {
                Logger.error(`Tarea "${name}" ya existe`);
                return;
            }

            const newTask: Task = {
                name,
                description,
                createdAt: new Date()
            };

            this.tasks.push(newTask);
            Logger.info(`Tarea "${name}" añadida exitosamente`);
            
            const endTime = performance.now();
            Logger.debug(`Tiempo de ejecución addTask: ${endTime - startTime}ms`);
        } catch (error) {
            Logger.error(`Error al añadir tarea: ${error}`);
        }
    }

    /**
     * Elimina una tarea por su nombre
     * @param name Nombre de la tarea a eliminar
     */
    removeTask(name: string): void {
        const startTime = performance.now();
        
        try {
            const initialLength = this.tasks.length;
            this.tasks = this.tasks.filter(task => task.name !== name);

            if (this.tasks.length === initialLength) {
                Logger.warn(`No se encontró la tarea "${name}"`);
            } else {
                Logger.info(`Tarea "${name}" eliminada exitosamente`);
            }

            const endTime = performance.now();
            Logger.debug(`Tiempo de ejecución removeTask: ${endTime - startTime}ms`);
        } catch (error) {
            Logger.error(`Error al eliminar tarea: ${error}`);
        }
    }

    /**
     * Lista todas las tareas existentes
     */
    listTasks(): void {
        const startTime = performance.now();
        
        try {
            if (this.tasks.length === 0) {
                Logger.info("No hay tareas registradas");
                return;
            }

            Logger.info("Lista de tareas:");
            this.tasks.forEach(task => {
                Logger.info(`- ${task.name}: ${task.description} (Creada: ${task.createdAt})`);
            });

            const endTime = performance.now();
            Logger.debug(`Tiempo de ejecución listTasks: ${endTime - startTime}ms`);
        } catch (error) {
            Logger.error(`Error al listar tareas: ${error}`);
        }
    }
}

// Ejemplo de uso
function main() {
    Logger.info("Iniciando sistema de gestión de tareas");

    const taskManager = new TaskManager();

    // Ejemplo de uso del sistema
    taskManager.addTask("Estudiar TypeScript", "Aprender sobre tipos y interfaces");
    taskManager.addTask("Hacer ejercicio", "30 minutos de cardio");
    taskManager.listTasks();
    taskManager.removeTask("Estudiar TypeScript");
    taskManager.listTasks();
    taskManager.removeTask("Tarea inexistente");

    Logger.info("Finalizando sistema de gestión de tareas");
}

// Ejecutar el programa
main();