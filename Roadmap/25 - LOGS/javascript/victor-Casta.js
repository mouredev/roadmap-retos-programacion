/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 */

let x = 5
console.assert(x > 10, "El valor de x no es mayor que 10")

console.clear()

console.log("Este es un mensaje de log")

console.info("Información: el programa ha iniciado correctamente")

console.warn("Advertencia: estás a punto de alcanzar el límite de uso")

console.error("Error: el archivo no pudo ser encontrado")

console.debug("Debug: se está calculando el valor")

function greeting(user) {
  console.count("Llamadas a greeting")
  return `Hi ${user}`
}

greeting('user_1')
greeting('user_1')
greeting('user_1')

console.countReset("Llamadas a greeting")
greeting('user_1')

function addition(a, b) {
  console.debug("Debug: calculando el total de ", a, b)
  return a + b
}

addition(1, 2)

let users = {
  name: "Victor",
  age: 21,
  address: {
    city: "Madrid",
    country: "España",
  },
}

console.dir(users, { depth: 1, colors: true })

if (typeof document !== 'undefined') {
  console.dirxml(document.body)
}

/*
  * DIFICULTAD EXTRA (opcional):
  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
  * y listar dichas tareas.
  * - Añadir: recibe nombre y descripción.
  * - Eliminar: por no mbre de la tarea.
  * Implementa diferentes mensajes de log que muestren información según la
  * tarea ejecutada (a tu elección).
  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
*/

const readline = require('node:readline')
const { stdin: input, stdout: output } = require('node:process')

const rl = readline.createInterface({ input, output })
let tasks = []

function schedule() {
  console.log('- Gestor de tareas -')
  console.log('1 - Añadir')
  console.log('2 - Eliminar')
  console.log('3 - Listar')
  console.log('4 - Salir')

  rl.question('Ingresa una opción: ', (response) => {
    if (response === '1') {
      rl.question('Ingrese el nombre de la Tarea: ', (taskName) => {
        rl.question('Ingresa la descripción de la tarea: ', (taskDescription) => {
          if (taskName && taskDescription) {
            console.time('Tiempo de ejecución')
            console.log(`Tarea añadida: ${taskName} - ${taskDescription}`)
            tasks.push({ name: taskName, description: taskDescription })
            console.timeEnd('Tiempo de ejecución')
          } else {
            console.log('El nombre y la descripción de la tarea son obligatorios.')
          }
          schedule()
        })
      })
    } else if (response === '2') {
      rl.question('Ingresa el nombre de la tarea a eliminar: ', (taskName) => {
        console.time('Tiempo de ejecución')
        const originalLength = tasks.length
        tasks = tasks.filter(item => !item.name.toLowerCase().includes(taskName.toLowerCase()))
        if (tasks.length < originalLength) {
          console.log(`Tarea eliminada: ${taskName}`)
        } else {
          console.log(`No se encontró la tarea: ${taskName}`)
        }
        console.timeEnd('Tiempo de ejecución')
        schedule()
      })
    } else if (response === '3') {
      console.time('Tiempo de ejecución')
      if (tasks.length > 0) {
        console.table(tasks)
      } else {
        console.log('No hay tareas para mostrar.')
      }
      console.timeEnd('Tiempo de ejecución')
      schedule()
    } else if (response === '4') {
      console.log('Saliendo del gestor de tareas...')
      rl.close()
    } else {
      console.log('Opción no válida. Intente de nuevo.')
      schedule()
    }
  })
}

schedule()