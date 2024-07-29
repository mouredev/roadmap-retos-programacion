// The console object is a property of the window object.
// Console severity levels
  /* 
    .- Verbose: console.debug()
    .- Info: console.info(), console.log()
    .- Warnings: console.warn()
    .- Errors: console.error()
  */

/* Métodos del objeto console comunmente usados. Consejo: Darle contexto a las salidas por consola  */
/* Los métodos .group, .groupEnd, .table; así como, el uso de especificadores de formato, nos permiten configurar nuestros loggings */

let gretting = 'Hola Javascript'

console.group('Inicio logging')
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
    this.task = {},
    this.frontIndex = 0,
    this.backIndex = 0
  }
  /* enqueue */
  add_task(name) {
    this.task[this.backIndex] = name
    this.backIndex++
    return name
  }
  /* dequeue */ 
  delete_task() {
    const task = this.task[this.frontIndex]
    delete this.task[this.frontIndex]
    this.frontIndex++
    return task
  }

  get list_task() {
    return this.task
  } 
}

let newTask = new TaskManager()
newTask.add_task('Comprar Pan')
newTask.add_task('Comprar Té')
let str = newTask.list_task
console.log(str)
newTask.delete_task()
console.log(newTask.list_task);