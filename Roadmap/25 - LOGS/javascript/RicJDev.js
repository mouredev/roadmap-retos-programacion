/*
- Se ejecuta en Node.js
- Se ha instalado Winston para crear el sitema de logs (https://www.npmjs.com/package/winston)
*/

//EJERCICIO
const winston = require('winston');

const logger = winston.createLogger({
	level: 'debug',
	format: winston.format.combine(
		winston.format.timestamp({ format: 'DD-MM-YYYY HH:mm:ss' }),
		winston.format.printf(({ timestamp, level, message }) => {
			return `[${level.toUpperCase()}] - ${timestamp} : ${message}`;
		})
	),
	transports: [new winston.transports.Console()],
});

logger.log('info', 'mensaje de INFO');
logger.debug('mensaje de DEBUG');
logger.info('mensaje de INFO');
logger.warn('mensaje de WARN');
logger.error('mensaje de ERROR');

const customLevels = {
	levels: {
		'Alerta roja': 0,
		'Alerta amarilla': 1,
		'Alerta verde': 2,
	},
	colors: {
		'Alerta roja': 'red',
		'Alerta amarilla': 'yellow',
		'Alerta verde': 'green',
	},
};

winston.addColors(customLevels.colors);

const customLevelsLogger = winston.createLogger({
	level: 'Alerta verde',
	levels: customLevels.levels,
	format: winston.format.combine(winston.format.colorize(), winston.format.simple()),
	transports: [new winston.transports.Console()],
});

customLevelsLogger.log('Alerta roja', 'se muestra en rojo');
customLevelsLogger.log('Alerta amarilla', 'se muestra en amarillo');
customLevelsLogger.log('Alerta verde', 'se muestra en verde');

//EXTRA
const taskManagerLogs = winston.createLogger({
	level: 'debug',
	format: winston.format.combine(
		winston.format.timestamp({ format: 'DD-MM-YYYY HH:mm:ss' }),
		winston.format.printf(({ timestamp, level, message }) => {
			return `[${level.toUpperCase()}] - ${timestamp} : ${message}`;
		})
	),
	transports: [new winston.transports.Console()],
});

function timeLog(fun, log) {
	return function (...arg) {
		const start = new Date();
		const execute = fun.apply(this, arg);
		const end = new Date();

		log.debug(
			`tiempo de ejecución de ${fun.name}: ${end.getTime() - start.getTime()} milisegundos`
		);

		return execute;
	};
}
class TaskManager {
	#taskList = new Map();

	addTask(task, description) {
		if (this.#taskList.has(task)) {
			taskManagerLogs.warn(`se esta intentando agregar una tarea existente: ${task}`);
			taskManagerLogs.debug(`cantidad de tareas ${this.#taskList.size}`);
		} else {
			this.#taskList.set(task, description);

			taskManagerLogs.info(`se ha agregado una tarea a la lista: ${task}`);
			taskManagerLogs.debug(`cantidad de tareas ${this.#taskList.size}`);
		}
	}

	deleteTask(task) {
		if (this.#taskList.has(task)) {
			this.#taskList.delete(task);

			taskManagerLogs.info(`se ha eliminado una tarea de la lista: ${task}`);
			taskManagerLogs.debug(`cantidad de tareas ${this.#taskList.size}`);
		} else {
			taskManagerLogs.error(`se esta intentando eliminar una tarea que no existe: ${task}`);
			taskManagerLogs.debug(`cantidad de tareas ${this.#taskList.size}`);
		}
	}

	listTasks() {
		if (this.#taskList.size > 0) {
			console.log('\n---- LISTA DE TAREAS ----');
			this.#taskList.forEach((description, task) => {
				console.log(`- ${task}: ${description}`);
			});
			console.log('-------------------------\n');

			taskManagerLogs.info('se ha mostrado la lista de tareas al usuario');
			taskManagerLogs.debug(`cantidad de tareas ${this.#taskList.size}`);
		} else {
			taskManagerLogs.info('no hay tareas para mostrar');
			taskManagerLogs.debug(`cantidad de tareas ${this.#taskList.size}`);
		}
	}
}

TaskManager.prototype.addTask = timeLog(TaskManager.prototype.addTask, taskManagerLogs);
TaskManager.prototype.deleteTask = timeLog(TaskManager.prototype.deleteTask, taskManagerLogs);
TaskManager.prototype.listTasks = timeLog(TaskManager.prototype.listTasks, taskManagerLogs);

const myTaskManager = new TaskManager();

myTaskManager.addTask('Juan', 'felicitar a Juan por su cumpleaños');
myTaskManager.addTask('Pan', 'ir a comprar pan');
myTaskManager.addTask('Pan', 'ir a comprar pan');
myTaskManager.listTasks();
myTaskManager.deleteTask('Juan');
myTaskManager.listTasks();
myTaskManager.deleteTask('Juan');
myTaskManager.deleteTask('Pan');
myTaskManager.listTasks();
