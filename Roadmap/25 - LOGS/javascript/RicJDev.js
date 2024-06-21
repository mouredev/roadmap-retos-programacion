//EJERCICIO
const fs = require('node:fs');
const { Interface } = require('node:readline');

const logFile = 'RicJDev_log.txt';
let counter = 0;

if (counter === 0) {
	fs.appendFile(logFile, `\nREGISTRO DEL ${new Date().toLocaleString()}\n\n`, (error) => {
		if (error) {
			console.log(error);
		}
	});
}

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
				this.date = new Date().toLocaleString();
				this.name = fun.name;
				this.severity = severity;
				this.message = message || messages.get(severity);
			}
		}

		let newLog = new Log(fun, severity, message);
		let logContent = `${counter}. ${newLog.date}: [${newLog.severity}]\n\t${newLog.name}: ${newLog.message}\n`;

		fs.appendFile(logFile, logContent, (error) => {
			if (error) {
				console.log(error);
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

//EXTRA
/*
SISTEMA DE REGISTRO DE TAREAS

Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
y listar dichas tareas.
- Añadir: recibe nombre y descripción.
- Eliminar: por nombre de la tarea.
Implementa diferentes mensajes de log que muestren información según la 
tarea ejecutada (a tu elección).
Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
*/

const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const taskList = new Map();

taskList.set('Primera tarea', 'Esta es la descripcion de la primera tarea');
taskList.set('Segunda tarea', 'Esta es la descripcion de la segunda tarea');

function addTask() {
	rl.question('\nAgregue el nombre de la tarea: ', (task) => {
		rl.question('Agregue una descripción para dicha tarea: ', (description) => {
			taskList.set(task, description);
			console.log('Se ha agregado la tarea a la lista!');
			optionsMenu();
		});
	});
}

addTask = addToLog(addTask, 'INFO', 'ha agregado una tarea a la lista');

function deleteTask() {
	rl.question('\nIndique el nombre de la tarea a eliminar: ', (task) => {
		if (taskList.has(task)) {
			taskList.delete(task);
			console.log('Tarea eliminada con exito');
		} else {
			console.log('Tarea no registrada');
		}

		optionsMenu();
	});
}

deleteTask = addToLog(deleteTask, 'INFO', 'ha eliminado una tarea de la lista');

function getList() {
	console.log('\nLISTA DE TAREAS');
	taskList.forEach((value, key) => {
		console.log(`- ${key}: ${value}`);
	});

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
