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
			return `${timestamp} - [${level.toUpperCase()}]: ${message}`;
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
const taskManagerLogger = winston.createLogger({
	level: 'debug',
	format: winston.format.combine(
		winston.format.timestamp({ format: 'DD-MM-YYYY HH:mm:ss' }),
		winston.format.printf(({ timestamp, level, message }) => {
			return `${timestamp} - [${level.toUpperCase()}]: ${message}`;
		})
	),
	transports: [new winston.transports.File({ filename: 'RicJDev.txt' })],
});

function addToTaskManagerLogger(fun, level, message) {
	taskManagerLogger.log(level, message);
	return function (...arg) {
		return fun.apply(this, arg);
	};
}

class TaskManager {
	taskList = new Map();

	addTask(task, description) {
		this.taskList.set(task, description);
	}

	deleteTask(task) {
		if (this.taskList.has(task)) {
			this.taskList.delete(task);
		}
	}

	listTasks() {
		if (this.taskList.size > 0) {
			this.taskList.forEach((description, task) => {
				console.log(`- ${task}: ${description}`);
			});
		} else {
			console.log('No hay tareas registradas');
		}
	}
}

TaskManager.prototype.addTask = addToTaskManagerLogger(
	TaskManager.prototype.addTask,
	'info',
	'se ha añadido una tarea a la lista'
);

let myTaskManager = new TaskManager();

myTaskManager.addTask('Juan', 'felicitar a Juan por su cumpleaños');
myTaskManager.addTask('Pan', 'ir a comprar pan');
myTaskManager.listTasks();
myTaskManager.deleteTask('Juan');
myTaskManager.listTasks();
