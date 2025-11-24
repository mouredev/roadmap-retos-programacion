const niveles = {
  DEBUG: 'DEBUG',
  INFO: 'INFO',
  WARNING: 'WARNING',
  ERROR: 'ERROR'
};

function log(nivel, mensaje) {
  const fecha = new Date().toISOString()
  const formato = `${fecha} - ${nivel} - ${mensaje}`

  switch (nivel) {
    case niveles.DEBUG:
      console.debug(formato)
      break
    case niveles.INFO:
      console.info(formato)
      break
    case niveles.WARNING:
      console.warn(formato)
      break
    case niveles.ERROR:
      console.error(formato)
      break
    default:
      console.log(formato)
  }
}

log(niveles.DEBUG, "Esto es un mensaje de DEBUG")
log(niveles.INFO, "Esto es un mensaje de INFO")
log(niveles.WARNING, "Esto es un mensaje de WARNING")
log(niveles.ERROR, "Esto es un mensaje de ERROR")

// ---------------------------------------- DIFICULTAD EXTRA ----------------------------------------
class TaskManager {
  constructor() {
    this.tasks = {}
  }

  addTask(nameTask, description) {
    const startTime = performance.now()
    if (Object.hasOwn(this.tasks, nameTask)) console.warn('Ya existe una tarea con ese nombre')
    else {
      Object.assign(this.tasks, {[nameTask]: description})
      console.info('La tarea se ha agregado correctamente')
    }
    console.debug(`tenes ${Object.keys(this.tasks).length} tarea/s pendiente/s`)
    const endTime = performance.now()
    console.log(`Tiempo de ejecución: ${(endTime - startTime).toFixed(2)}s`)
  }

  deleteTask(nameTask) {
    const startTime = performance.now()
    if (Object.hasOwn(this.tasks, nameTask)) {
      delete this.tasks[nameTask]
      console.info('La tarea se ha borrado correctamente')
    }
    else console.error('La tarea que desea eliminar no existe')
    const endTime = performance.now()
    console.log(`Tiempo de ejecución: ${(endTime - startTime).toFixed(2)}s`)
  }

  viewTaks() {
    const startTime = performance.now()
    console.info(this.tasks)
    const endTime = performance.now()
    console.log(`Tiempo de ejecución: ${(endTime - startTime).toFixed(2)}s`)
  }
}

const taskManager = new TaskManager
taskManager.addTask('javascript', 'terminar el ejercicio 25 de javascript')
taskManager.addTask('papel', 'comprar todo el papel higienico por si se viene el apocalipsis')
taskManager.viewTaks()
taskManager.deleteTask('noExisto')
taskManager.deleteTask('papel')
taskManager.viewTaks()