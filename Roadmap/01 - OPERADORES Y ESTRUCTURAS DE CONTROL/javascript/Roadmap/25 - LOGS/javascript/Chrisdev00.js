/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
 */


// instalar la biblioteca de logging 'winston'

const winston = require('winston')

const logger1 = winston.createLogger({
    level: 'debug',
    format: winston.format.json(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({filename: 'app.log'}),
    ]
})

logger1.info("An info log")
logger1.error("An error log")



/////////////// --------------------------------- EXTRA ---------------------------------- ///////////////////

const readline = require('readline');
const winston = require('winston');
const { format } = require('path');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// configuracion del logger con winston

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.combine(
        winston.format.timestamp({format: 'YYYY-MM-DD HH:mm:ss' }),
        winston.format.printf(({ timestamp, level, message}) => {
            return `${timestamp} - ${level.toUpperCase()} - ${message}`;
        })
    ),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'test.log' })
    ]
});


class TaskManager {
    constructor() {
        this.tasks = {};
        logger.info("Gestor de Tareas inicializado.");
    }

    addTask() {
        rl.question("Ingrese el nombre de la tarea: ", name => {
            rl.question("Ingrese la descripción de la tarea: ", description => {
                if (this.tasks[name]) {
                    logger.warn(`Intento de añadir una tarea ya existente: ${name}`);
                    return;
                }
                const execution_time = Math.floor(Math.random() * 5) + 1;
                this.tasks[name] = {
                    description,
                    execution_time
                };
                logger.info(`Tarea '${name}' añadida.`);
                logger.debug(`Tiempo de ejecución de la tarea '${name}': ${execution_time} segundos.`);
            });
        });
    }

    deleteTask() {
        rl.question("Ingrese el nombre de la tarea a eliminar: ", name => {
            if (!this.tasks[name]) {
                logger.warn(`Intento de eliminar una tarea inexistente: ${name}`);
                return;
            }
            delete this.tasks[name];
            logger.info(`Tarea '${name}' eliminada.`);
        });
    }

    listTasks() {
        if (Object.keys(this.tasks).length === 0) {
            logger.info("No hay tareas para listar.");
            return;
        }
        for (const [name, info] of Object.entries(this.tasks)) {
            console.log(`Tarea: ${name} - Descripción: ${info.description} - Tiempo de ejecución: ${info.execution_time} segundos`);
            logger.info(`Tiempo de ejecución de la tarea '${name}' es ${info.execution_time} segundos.`);
        }
    }
}


const manager = new TaskManager();

function mainMenu(){
    rl.question("\nGestor de Tareas\n1. Añadir Tarea\n2. Eliminar Tarea\n3. Listar Tareas\n4. Salir\n Seleccione una opcion: ", choice => {
        if (choice === '1'){
            manager.addTask();
        }else if (choice === '2'){
            manager.deleteTask();
        }else if (choice === '3'){
            manager.listTasks();
        }else if (choice === '4'){
            rl.close();
            return;
        }else{
            logger.error("Opción no válida, por favor intente nuevamente.");
        }
        mainMenu();
    });
}

mainMenu();
