/**
 * TEORÍA SOBRE LOGGING EN JAVASCRIPT
 * 
 * JavaScript proporciona varios métodos nativos de logging a través del objeto console:
 * - console.error(): Para errores críticos
 * - console.warn(): Para advertencias
 * - console.info(): Para información general
 * - console.debug(): Para información de depuración
 * - console.trace(): Para stack traces
 * 
 * Ventajas del logging:
 * 1. Facilita la depuración
 * 2. Permite monitorear el estado de la aplicación
 * 3. Ayuda a diagnosticar problemas en producción
 * 4. Proporciona información sobre el rendimiento
 */

// Clase para manejar el logging con niveles de severidad y timestamps
class Logger {
    /**
     * Añade timestamp y formato al mensaje de log
     * @param {string} level - Nivel de severidad
     * @param {string} message - Mensaje a registrar
     * @returns {string} - Mensaje formateado
     */
    static formatMessage(level, message) {
        const timestamp = new Date().toISOString();
        return `[${timestamp}] [${level}] ${message}`;
    }

    static error(message) {
        console.error(this.formatMessage('ERROR', message));
    }

    static warn(message) {
        console.warn(this.formatMessage('WARN', message));
    }

    static info(message) {
        console.info(this.formatMessage('INFO', message));
    }

    static debug(message) {
        console.debug(this.formatMessage('DEBUG', message));
    }

    static trace(message) {
        console.trace(this.formatMessage('TRACE', message));
    }
}

/**
 * Clase que representa una tarea
 */
class Task {
    /**
     * @param {string} name - Nombre de la tarea
     * @param {string} description - Descripción de la tarea
     */
    constructor(name, description) {
        this.name = name;
        this.description = description;
        this.createdAt = new Date();
        this.id = crypto.randomUUID(); // Generamos un ID único para cada tarea
    }
}

/**
 * Clase para la gestión de tareas
 */
class TaskManager {
    constructor() {
        this.tasks = new Map(); // Usamos Map para almacenar las tareas por su nombre
    }

    /**
     * Mide el tiempo de ejecución de una función
     * @param {Function} fn - Función a ejecutar
     * @param {string} operationName - Nombre de la operación
     * @returns {*} - Resultado de la función
     */
    async measureExecutionTime(fn, operationName) {
        const startTime = performance.now();
        try {
            const result = await fn();
            const endTime = performance.now();
            Logger.debug(`Tiempo de ejecución ${operationName}: ${(endTime - startTime).toFixed(2)}ms`);
            return result;
        } catch (error) {
            Logger.error(`Error en ${operationName}: ${error.message}`);
            throw error;
        }
    }

    /**
     * Añade una nueva tarea
     * @param {string} name - Nombre de la tarea
     * @param {string} description - Descripción de la tarea
     */
    async addTask(name, description) {
        await this.measureExecutionTime(async () => {
            if (this.tasks.has(name)) {
                Logger.warn(`La tarea "${name}" ya existe`);
                return;
            }

            const task = new Task(name, description);
            this.tasks.set(name, task);
            Logger.info(`Tarea "${name}" añadida exitosamente`);
        }, 'addTask');
    }

    /**
     * Elimina una tarea por su nombre
     * @param {string} name - Nombre de la tarea a eliminar
     */
    async removeTask(name) {
        await this.measureExecutionTime(async () => {
            if (!this.tasks.has(name)) {
                Logger.warn(`No se encontró la tarea "${name}"`);
                return;
            }

            this.tasks.delete(name);
            Logger.info(`Tarea "${name}" eliminada exitosamente`);
        }, 'removeTask');
    }

    /**
     * Lista todas las tareas existentes
     */
    async listTasks() {
        await this.measureExecutionTime(async () => {
            if (this.tasks.size === 0) {
                Logger.info("No hay tareas registradas");
                return;
            }

            Logger.info("Lista de tareas:");
            for (const task of this.tasks.values()) {
                Logger.info(
                    `- ${task.name}: ${task.description} ` +
                    `(Creada: ${task.createdAt.toISOString()}) ` +
                    `[ID: ${task.id}]`
                );
            }
        }, 'listTasks');
    }
}

/**
 * Función principal para demostrar el uso del sistema
 */
async function main() {
    try {
        Logger.info("Iniciando sistema de gestión de tareas");

        // Demostración de diferentes niveles de logging
        Logger.error("Ejemplo de mensaje de error");
        Logger.warn("Ejemplo de mensaje de advertencia");
        Logger.info("Ejemplo de mensaje informativo");
        Logger.debug("Ejemplo de mensaje de depuración");
        Logger.trace("Ejemplo de mensaje de trace");

        // Crear instancia del gestor de tareas
        const taskManager = new TaskManager();

        // Ejemplos de uso del sistema
        await taskManager.addTask(
            "Aprender JavaScript", 
            "Estudiar conceptos avanzados de JS"
        );
        
        await taskManager.addTask(
            "Hacer ejercicio", 
            "30 minutos de cardio"
        );

        // Intentar añadir una tarea duplicada
        await taskManager.addTask(
            "Aprender JavaScript", 
            "Tarea duplicada"
        );

        // Listar tareas
        await taskManager.listTasks();

        // Eliminar una tarea
        await taskManager.removeTask("Aprender JavaScript");

        // Listar tareas actualizadas
        await taskManager.listTasks();

        // Intentar eliminar una tarea que no existe
        await taskManager.removeTask("Tarea inexistente");

        Logger.info("Finalizando sistema de gestión de tareas");
    } catch (error) {
        Logger.error(`Error en la ejecución principal: ${error.message}`);
    }
}

// Ejecutar el programa
main().catch(error => {
    Logger.error(`Error crítico: ${error.message}`);
});