//EJERCICIO
const { error } = require('node:console');
const fs = require('node:fs');

function addToLog(fun, severity) {
	const message = Object.freeze({
		INFO: `${fun.name} se ha ejecutado`,
		TRACE: '',
		DEBUG: `${fun.name} ha arrojado un valor inesperado`,
		WARN: `${fun.name} no se ejecutó correctamente`,
		ERROR: `ha ocurrido un error al ejecutar ${fun.name}`,
		FATAL: 'ha petado esto, tío',
	});

	const logContent = `${new Date().toLocaleString()} [${severity}]: ${message[severity]}\n`;

	return function (...arg) {
		fs.appendFile('logs.txt', logContent, (error) => {
			if (error) {
				console.log(error);
			}
		});

		return fun(...arg);
	};
}

function infoFunction() {
	console.log('Hola. Soy una funcion');
}

function errorFunction() {
	console.log('Soy una funcion que da error. Jejeje');
}

function fatalFunction() {
	console.log('Revisa el log');
}

infoFunction = addToLog(infoFunction, 'INFO');

errorFunction = addToLog(errorFunction, 'ERROR');

fatalFunction = addToLog(fatalFunction, 'FATAL');

infoFunction();

errorFunction();

fatalFunction();

//EXTRA
