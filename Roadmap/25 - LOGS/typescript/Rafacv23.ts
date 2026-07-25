// Hecho por @Rafacv23 | https://github.com/Rafacv23 | https://twitter.com/rafacanosa  | https://www.rafacanosa.dev

// Tipos de logs que hay en JavaScript
console.log("Esto es un console.log() sirve para mostrar mensajes por consola.")
console.warn(
  "Esto es un console.warn(), sirve para mostrar mensajes de aviso ante posibles errores o áreas a las que haya que prestar especial atención."
)
console.error(
  "Esto es un console.error(), sirve para mostrar errores por consola."
)
console.info(
  "Esto es un console.info(), sirve para aportar información adicional a un mensaje."
)
console.debug(
  "Esto es un console.debug(), sirve para mostrar un mensaje por consola pero con el modo debug activado."
)

// Dificultad opcional
console.log("Iniciando programa de gestión de tareas...")

// Clase Task
class Task {
  name: string
  description: string

  constructor(name: string, description: string) {
    this.name = name
    this.description = description
  }
}

// TaskManager: para gestionar las tareas
class TaskManager {
  taskList: Task[] = []

  // Añadir tarea
  addTask(name: string, description: string): void {
    console.time("Tiempo para añadir tarea")
    const newTask = new Task(name, description)
    this.taskList.push(newTask)
    console.log(`Tarea "${name}" añadida correctamente.`)
    console.timeEnd("Tiempo para añadir tarea")
  }

  // Eliminar tarea
  deleteTask(name: string): void {
    console.time("Tiempo para eliminar tarea")

    // Check if name is provided
    if (!name) {
      console.error("No se ha introducido el nombre de la tarea")
      console.timeEnd("Tiempo para eliminar tarea")
      return
    }

    // Check if task exists
    const taskExists = this.taskList.some((task) => task.name === name)
    if (!taskExists) {
      console.error(
        `Error: No se encontró ninguna tarea con el nombre "${name}".`
      )
      console.timeEnd("Tiempo para eliminar tarea")
      return
    }

    this.taskList = this.taskList.filter((task) => task.name !== name)
    console.log(`Tarea con nombre "${name}" eliminada correctamente.`)
    console.timeEnd("Tiempo para eliminar tarea")
  }

  // Listar tareas
  showTasks(): void {
    console.time("Tiempo para listar tareas")
    if (this.taskList.length === 0) {
      console.warn("No hay tareas para mostrar.")
    } else {
      console.log("Tareas actuales:")
      this.taskList.forEach((task, index) => {
        console.log(`${index + 1}. ${task.name} - ${task.description}`)
      })
    }
    console.timeEnd("Tiempo para listar tareas")
  }
}

// Crear una instancia del administrador de tareas
const taskManager = new TaskManager()

// Añadir algunas tareas
taskManager.addTask("Lavar la ropa", "Separar blanco de color")
taskManager.addTask("Hacer la compra", "Comprar pan, leche y huevos")
taskManager.addTask("Estudiar", "Estudiar para el examen de JavaScript")

// Listar todas las tareas
taskManager.showTasks()

// Eliminar una tarea y mostrar el listado actualizado
taskManager.deleteTask("Estudiar")
taskManager.showTasks()
