// The console object is a property of the window object.
// Console severity levels
  /* 
    .- Verbose: console.debug()
    .- Info: console.info(), console.log()
    .- Warnings: console.warn()
    .- Errors: console.error()
  */

/* Filtrar cuales logs aparecen en consola, dependiendo de la severidad, solo puede ser seteado en el devtool del browser */

/* Métodos del objeto console comunmente usados. Los métodos .group, .groupEnd, .table; así como, el uso de especificadores de formato, nos permiten configurar nuestros loggings */

let gretting = 'Hola Javascript'

console.group('Inicio logging')
// Consejo: Darle contexto a las salidas por consola. 
console.debug('Esto es un console.debug():','Message debug process')
console.log('Esto es un console.log():', 'Hola Javascript')
console.log({gretting}) // Mejora el contexto de la salida por consola
console.info('Esto es un console.info():','No Fumar')
console.warn('Esto es un console.warn():','Atención')
console.error('Esto es un console.error():','Syntax error')
console.groupEnd()
console.log('Otro log más, que no pertebnece al grupò anterior')

let users = [
  {
    id: 1,
    name: 'José',
    phone: 12365478
  },
  {
    id: 2,
    name: 'María',
    phone: 85641239
  },
  {
    id: 3,
    name: 'Luisa',
    phone: 12574598
  }
]

console.table(users)

let fecha = new Date().toLocaleDateString('es-es', {day: 'numeric', month: 'numeric', year: 'numeric'})

console.log(
  '%c Un día como hoy %s aprendí a formatear mensajes por consola',
  'color: green; background:black; font-size: 20pt',
  fecha
)

// Extra

class TaskManager {
  constructor() {
    this.tasks = {}
  }

  add_task(name, description) {
    console.time('test1')
    if (!this.tasks.hasOwnProperty(name)) {
      this.tasks[name] = description
      console.info(`Tarea añadida: ${name}`)
      let length = Object.entries(this.tasks).length
      console.debug('DEBUG:', `Número de tareas: ${length}`)
      this.tasks
    } else {
      console.warn(`Se ha intentado ingresar una tarea que ya existe: ${name}`)
    }
    console.timeEnd('test1')
  }

  delete_task(name) {
    console.time('test2')
    if (this.tasks.hasOwnProperty(name)) {
      delete this.tasks[name]
      console.info(`Tarea eliminada: ${name}`)
      let length = Object.entries(this.tasks).length
      console.debug('DEBUG:', `Número de tareas: ${length}`)
    } else {
      console.error(`Se está intentado eliminar una tarea que no existe: ${name}`)
    }
    console.timeEnd('test2')
  }

  get list_task() {
    console.time('time3')
    Object.entries(this.tasks).forEach(([key, value]) => {
      console.log(`${key}: ${value}`)
    })
    console.timeEnd('time3')
  }
}
let taskList = new TaskManager()
taskList.add_task('Comprar Pan', 'Compra 5 panes')
taskList.add_task('Comprar sixpack', 'Compra 2 sixpack')
taskList.list_task
taskList.delete_task('Comprar sixpack')
taskList.list_task