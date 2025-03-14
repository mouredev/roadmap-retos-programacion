/*  🔥EJERCICIO:
Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
un ejemplo con cada nivel de "severidad" disponible.

/*Logging con Winston (Node.js) */
// Verificar si estamos en Node.js
if (typeof process !== 'undefined' && process.versions?.node) {
    const winston = require('winston');

    const niveles = {
        error: 0,
        warn: 1,
        info: 2,
        http: 3,
        debug: 4
    };

    const colores = {
        error: 'red',
        warn: 'yellow',
        info: 'green',
        http: 'blue',
        debug: 'white'
    };

    winston.addColors(colores);

    const logger = winston.createLogger({
        levels: niveles,
        format: winston.format.combine(
            winston.format.colorize(),
            winston.format.timestamp(),
            winston.format.printf(({ timestamp, level, message }) => {
                return `${timestamp} [${level}]: ${message}`;
            })
        ),
        transports: [
            new winston.transports.Console(),
            new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
            new winston.transports.File({ filename: 'logs/all.log' })
        ]
    });

    logger.info('Este es un mensaje informativo.');
    logger.warn('Este es un mensaje de advertencia.');
    logger.error('Este es un mensaje de error.');
    logger.http('Este es un mensaje HTTP.');
    logger.debug('Este es un mensaje de depuración.');
}

/* 🔥 DIFICULTAD EXTRA (opcional):
Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
y listar dichas tareas.
- Añadir: recibe nombre y descripción.
- Eliminar: por nombre de la tarea.
Implementa diferentes mensajes de log que muestren información según la 
tarea ejecutada (a tu elección).
Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
 */
// Logger para entornos sin Node.js (navegador)
const loggerBrowser = {
    info: (message) => console.log(`[%cINFO%c] ${message}`, 'color: green', 'color: default'),
    warn: (message) => console.log(`[%cWARN%c] ${message}`, 'color: yellow', 'color: default'),
    error: (message) => console.log(`[%cERROR%c] ${message}`, 'color: red', 'color: default'),
    debug: (message) => console.log(`[%cDEBUG%c] ${message}`, 'color: blue', 'color: default')
};

// Ejemplos en navegador
loggerBrowser.info('Este es un mensaje informativo.');
loggerBrowser.warn('Este es un mensaje de advertencia.');
loggerBrowser.error('Este es un mensaje de error.');

/*  (compatible con ambos entornos) */
class GestorTareas {
    constructor() {
        this.tareas = [];
        // Usar Winston en Node.js o loggerBrowser en navegador
        this.logger = typeof process !== 'undefined' && process.versions?.node
            ? require('winston').loggers.get('default') // Asume que Winston ya está configurado
            : loggerBrowser;
    }

    añadirTarea(nombre, descripcion) {
        const inicio = typeof performance !== 'undefined' ? performance.now() : Date.now();
        this.tareas.push({ nombre, descripcion });
        const duracion = typeof performance !== 'undefined' ? performance.now() - inicio : Date.now() - inicio;
        this.logger.info(`Tarea añadida: ${nombre} (Tiempo: ${duracion.toFixed(2)}ms)`);
    }

    eliminarTarea(nombre) {
        const inicio = typeof performance !== 'undefined' ? performance.now() : Date.now();
        const indice = this.tareas.findIndex(t => t.nombre === nombre);
        if (indice === -1) {
            this.logger.warn(`Tarea no encontrada: ${nombre} (Tiempo: ${Date.now() - inicio}ms)`);
            return;
        }
        this.tareas.splice(indice, 1);
        this.logger.info(`Tarea eliminada: ${nombre} (Tiempo: ${Date.now() - inicio}ms)`);
    }

    listarTareas() {
        const inicio = typeof performance !== 'undefined' ? performance.now() : Date.now();
        if (this.tareas.length === 0) {
            this.logger.warn("No hay tareas para listar. (Tiempo: 0ms)");
            return;
        }
        this.logger.info(`Listando ${this.tareas.length} tareas... (Tiempo: ${Date.now() - inicio}ms)`);
        this.tareas.forEach(tarea => {
            this.logger.http(`- ${tarea.nombre}: ${tarea.descripcion}`);
        });
    }
}

// Ejemplo de uso
const gestor = new GestorTareas();
gestor.añadirTarea("Tarea 1", "Estudiar JavaScript");
gestor.añadirTarea("Tarea 2", "Hacer ejercicio");
gestor.listarTareas();
gestor.eliminarTarea("Tarea 1");
gestor.eliminarTarea("Tarea Inexistente");

/*
dictionary 📗 = {
    if (typeof process !== 'undefined' && process.versions?.node)
    : En el navegador, se usa loggerBrowser para simular niveles de severidad con console.log.,
    npm install winston : Instala Winston,
    node logging.js : Ejecuta el archivo,
}
*/