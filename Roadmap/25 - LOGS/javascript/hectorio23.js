// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";
const winston = require('winston'); // npm install winston
const { combine, timestamp, printf } = winston.format;

// Configuración de winston para logging
const myFormat = printf(({ level, message, timestamp }) => {
  return `${timestamp} - ${level.toUpperCase()}: ${message}`;
});

const logger = winston.createLogger({
  level: 'debug',
  format: combine(
    timestamp(),
    myFormat
  ),
  transports: [
    new winston.transports.Console()
  ]
});

// Lista para almacenar las tareas
let tareas = [];

function addTask(nombre, descripcion) {
  const startTime = Date.now();
  logger.info(`Añadiendo tarea: ${nombre}`);
  const tarea = { nombre, descripcion };
  tareas.push(tarea);
  logger.debug(`Tareas actuales: ${JSON.stringify(tareas)}`);
  const endTime = Date.now();
  logger.info(`Tarea añadida en ${(endTime - startTime) / 1000} segundos`);
}

function deleteTask(nombre) {
  const startTime = Date.now();
  logger.info(`Eliminando tarea: ${nombre}`);
  tareas = tareas.filter(tarea => tarea.nombre !== nombre);
  logger.debug(`Tareas actuales: ${JSON.stringify(tareas)}`);
  const endTime = Date.now();
  logger.info(`Tarea eliminada en ${(endTime - startTime) / 1000} segundos`);
}

function showTask() {
  logger.info("Listando todas las tareas");
  if (tareas.length === 0) {
    logger.warning("No hay tareas para listar");
  } else {
    tareas.forEach(tarea => {
      logger.info(`Tarea: ${tarea.nombre}, Descripción: ${tarea.descripcion}`);
    });
  }
}

// Ejemplo de uso del programa de gestión de tareas
addTask("Comprar pan", "Ir a la panadería y comprar una barra de pan");
addTask("Estudiar JavaScript", "Completar el ejercicio de logging en JavaScript");
showTask();
deleteTask("Comprar pan");
showTask();
