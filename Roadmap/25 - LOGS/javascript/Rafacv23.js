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
class Task {
  // Sirve para crear nuevas tareas
  constructor(name, description) {
    this.name = name
    this.description = description
  }

  deleteTask(name, taskList) {
    // check if name is provided
    if (!name) {
      console.error("No se ha introducido el nombre de la tarea")
      return
    }

    //Check if task exists
    const taskExists = taskList.some((task) => task.name === name)

    if (!taskExists) {
      console.error(
        `Error: No se encontró ninguna tarea con el nombre "${name}".`
      )
      return taskList // Retornar el array original si no se encuentra el item
    }

    const updatedTaskList = taskList.filter((task) => task.name !== name)
    console.log(`Tarea con nombre "${name}" eliminada correctamente.`)

    return updatedTaskList // Devolver la lista actualizada
  }

  showTasks(taskList) {
    console.log("Tareas actuales:")
    for (let i = 0; i < taskList.length; i++) {
      console.log(`${i + 1}. ${taskList[i].name} - ${taskList[i].description}`)
    }
  }
}

const taskList = []
