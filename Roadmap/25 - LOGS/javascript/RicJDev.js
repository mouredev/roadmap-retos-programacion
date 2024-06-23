//EJERCICIO
//Se ejecuta en Node.js
const { error } = require('node:console');
const fs = require('node:fs');
const { Interface } = require('node:readline');

const logFile = 'RicJDev_log.txt';
let counter = 0;

fs.appendFile(logFile, `\n\n\tREGISTRO DEL ${new Date().toLocaleString()}\n`, (error) => {
	if (error) {
		console.error(error);
	}
});

fs.readFile(logFile, 'utf-8', (error, data) => {
	if (error) {
		console.error(error);
	}

	let dataArr = data.split('\n');

	if (dataArr.length > 200) {
		fs.writeFile(logFile, '', (error) => {
			if (error) {
				console.error(error);
			}
		});
	}
});

function addToLog(fun, severity, message) {
	return function (...arg) {
		counter++;
		const messages = new Map([
			['INFO', `se ha ejecutado`],
			['DEBUG', `ha arrojado un valor inesperado`],
			['WARN', `no se ejecutó correctamente`],
			['ERROR', `ha ocurrido un error al ejecutarse`],
			['FATAL', `esto ha petado`],
		]);

		class Log {
			constructor(fun, severity, message) {
				this.date = new Date().toLocaleDateString();
				this[severity] = message || messages.get(severity);
				this.name = fun.name;
			}
		}

		let logContent = new Log(fun, severity, message);

		logContent = `\n${counter}. ${logContent.date} - [${severity}]: ${logContent.name} ${logContent[severity]}`;

		fs.appendFile(logFile, logContent, (error) => {
			if (error) {
				console.error(error);
			}
		});

		return fun(...arg);
	};
}

function infoFunction() {
	console.log('Hola. Soy una función y solo me estoy ejecutando');
}

function errorFunction() {
	console.log('Soy una función que da error. Jejeje');
}

function fatalFunction() {
	console.log('Algo salió terriblemente mal');
}

function debugFunction() {
	console.log('Nothing');
}

infoFunction = addToLog(infoFunction, 'INFO');
errorFunction = addToLog(errorFunction, 'ERROR');
fatalFunction = addToLog(fatalFunction, 'FATAL');
debugFunction = addToLog(debugFunction, 'DEBUG');

infoFunction();
errorFunction();
debugFunction();

//EXTRA
const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const taskList = new Map();

function addTask() {
	rl.question('\nIndique el nombre de la tarea: ', (task) => {
		rl.question('Agregue una descripción para dicha tarea: ', (description) => {
			taskList.set(task, description);
			console.log('Se ha agregado la tarea a la lista!');
			console.time(`${task} ha sido eliminada de la lista!`);
			optionsMenu();
		});
	});
}

addTask = addToLog(addTask, 'INFO', 'ha agregado una tarea a la lista');

function deleteTask() {
	rl.question('\nIndique el nombre de la tarea a eliminar: ', (task) => {
		if (taskList.has(task)) {
			taskList.delete(task);
			console.timeEnd(`${task} ha sido eliminada de la lista!`);
		} else {
			console.log('Tarea no registrada');
		}

		optionsMenu();
	});
}

deleteTask = addToLog(deleteTask, 'INFO', 'ha eliminado una tarea de la lista');

function getList() {
	if (taskList.size > 0) {
		console.log(`\nLISTA DE TAREAS: ${taskList.size}`);
		taskList.forEach((value, key) => {
			console.log(`- ${key}: ${value}`);
		});
	} else {
		console.log('\nNo hay tareas registradas');
	}

	optionsMenu();
}

getList = addToLog(getList, 'INFO', 'ha mostrado la lista de tareas registradas');

function closeApp() {
	console.log('Saliendo de la aplicación');
	rl.close();
}

closeApp = addToLog(closeApp, 'INFO', 'ha cerrado la app');

function optionsMenu() {
	console.log('\nADMINISTRADOR DE TAREAS');

	console.log('\n1. Agregar tarea\n2. Eliminar tarea\n3. Listar tareas\n4. Salir');

	rl.question('\nElige una opción: ', (answer) => {
		if (answer === '1') {
			addTask();
		} else if (answer === '2') {
			deleteTask();
		} else if (answer === '3') {
			getList();
		} else if (answer === '4') {
			closeApp();
		} else {
			console.log('Opción inválida. Elija un número del 1 al 4');
			optionsMenu();
		}
	});
}

optionsMenu = addToLog(optionsMenu, 'INFO', 'ha abierto el menú de opciones');

optionsMenu();
