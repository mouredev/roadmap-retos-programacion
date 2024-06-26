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
	transports: [
		new winston.transports.File({ filename: 'RicJDev.txt' }),
		new winston.transports.Console(),
	],
});

logger.debug('mensaje de DEBUG');
logger.info('mensaje de INFO');
logger.warn('mensaje de WARN');
logger.error('mensaje de ERROR');

/*
function addToLog(fun, severity, message) {
	return function (...arg) {
		return fun(...arg);
	};
}
*/

//EXTRA
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
		console.log('\nLISTA DE TAREAS');
		this.taskList.forEach((description, task) => {
			console.log(`- ${task}: $${description}`);
		});
	}
}
