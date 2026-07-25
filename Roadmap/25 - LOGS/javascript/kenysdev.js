/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#25 LOGS
---------------------------------------
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
// ________________________________________________________

import { createLogger, transports, format } from 'winston';

const logger = createLogger({
    level: 'debug',
    format: format.combine(
        format.timestamp(),
        format.printf(({ timestamp, level, message }) => {
            return `${timestamp} - ${level} - ${message}`;
        })
    ),
    transports: [
        new transports.Console()
    ]
});

logger.debug('Depuración');

logger.info('Informativo');

logger.warn('Advertencia');

logger.error('Error');
logger.error('Error crítico');

// ________________________________________________________
console.log("\nDIFICULTAD EXTRA");

function showTime(func) {
    return async function (...args) {
        const startTime = Date.now();
        await func.apply(this, args);
        const endTime = Date.now();
        const executionTime = (endTime - startTime) / 1000;
        logger.debug(`Tiempo de ejecución de ${func.name}: ${executionTime.toFixed(21)} segundos.`);
    };
}

class Program {
    constructor() {
        this.tasks = {};
        logger.debug('Se inició instancia de la clase.');
    }

    add = showTime(async function (name, description) {
        this.tasks[name] = description;
        logger.info('Se agregó una tarea.');
    });

    delete = showTime(async function (name) {
        if (name in this.tasks) {
            delete this.tasks[name];
            logger.info(`Tarea '${name}' eliminada.`);
        } else {
            logger.warn(`No se encontró la tarea '${name}'.`);
        }
    });

    showList = showTime(async function () {
        logger.info('Lista de tareas');
        for (const [task, des] of Object.entries(this.tasks)) {
            console.log(`${task} -- ${des}`);
        }
    });
}

const tasks = new Program();

(async () => {
    await tasks.add("a", ".1");
    await tasks.add("b", "2");
    await tasks.add("c", "3");

    await tasks.delete("a");
    await tasks.showList();

    await tasks.delete("a");
})();
