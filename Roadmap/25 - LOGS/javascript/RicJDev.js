//EJERCICIO
const { error } = require('node:console');
const fs = require('node:fs');

const logFile = 'RicJDev_log.txt';

function addToLog(fun, severity) {
	const message = Object.freeze({
		INFO: `${fun.name} se ha ejecutado`,
		TRACE: `Revise los parámetros de ${fun.name}`,
		DEBUG: `${fun.name} ha arrojado un valor inesperado. ${fun}`,
		WARN: `${fun.name} no se ejecutó correctamente`,
		ERROR: `ha ocurrido un error al ejecutar ${fun.name}`,
		FATAL: `esto ha petado al ejecutar ${fun.name}`,
	});

	return function (...arg) {
		let logContent = `${new Date().toLocaleString()} [${severity}]: ${message[severity]}. Parámetros: ${JSON.stringify(
			arg
		)}\n`;

		fs.appendFile(logFile, logContent, (logError) => {
			if (error) {
				fs.appendFile(
					logFile,
					`${new Date().toLocaleString()}: Error al escribir en el archivo de registro: ${logError}\n`,
					(error) => {
						console.log(error);
					}
				);
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

function traceFunction(any, callback) {
	callback(any);
}

infoFunction = addToLog(infoFunction, 'INFO');
errorFunction = addToLog(errorFunction, 'ERROR');
fatalFunction = addToLog(fatalFunction, 'FATAL');
traceFunction = addToLog(traceFunction, 'TRACE');

infoFunction();

errorFunction();

fatalFunction();

traceFunction('Hola', (greeting) => {
	console.log(greeting);
});

//EXTRA
