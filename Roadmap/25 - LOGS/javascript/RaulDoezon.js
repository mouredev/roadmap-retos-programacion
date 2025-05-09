/*
  EJERCICIO:
  Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
  un ejemplo con cada nivel de "severidad" disponible.
*/

console.log("+++++++++ NIVELES DE LOGGING +++++++++");

console.log("Soy un console.log()");
console.info("Soy un console.info()");
console.warn("Soy un console.warn()");
console.debug("Soy un console.debug()");
console.error("Soy un console.error()");

/*
  DIFICULTAD EXTRA (opcional):
  Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
  y listar dichas tareas.
  - Añadir: recibe nombre y descripción.
  - Eliminar: por nombre de la tarea.
  Implementa diferentes mensajes de log que muestren información según la 
  tarea ejecutada (a tu elección).
  Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
*/

console.log("\n+++++++++ SISTEMA DE GESTIÓN DE TAREAS +++++++++");

class TaskManagement {
  constructor() {
    this.tasks = [];
    this.taskName;
    this.taskDescription;
  }

  add(taskName, taskDescription) {
    const starTime = Date.now();

    if (taskName !== undefined && taskDescription !== undefined) {
      this.tasks.push({taskName, taskDescription});

      console.info(`La tarea ${taskName} ha sido añadida.`);
    } else {
      console.warn("Debes definir el nombre de la tarea o la descripción");
    }

    const endTime = Date.now();

    console.log(`Tiempo de ejecución para añadir: ${(endTime - starTime) / 1000}s`);
  }

  delete(taskName) {
    const starTime = Date.now();
    const objectIndex = this.tasks.findIndex((task) => {
      return task.taskName === taskName;
    });

    if (objectIndex > -1) {
      this.tasks.splice(objectIndex, 1);

      console.info(`La tarea ${taskName} ha sido eliminada.`);
    } else {
      console.error("La tarea que deseas eliminar no existe");
    }

    const endTime = Date.now();

    console.log(`Tiempo de ejecución para eliminar: ${(endTime - starTime) / 1000}s`);
  }

  show() {
    const starTime = Date.now();

    console.log("Listado de tareas:");

    if (this.tasks.length > 0) {
      for (let index = 0; index < this.tasks.length; index++) {
        const tasks = this.tasks[index];
  
        console.log(`- Tarea: ${tasks.taskName}. Descripción: ${tasks.taskDescription}`);
      }
    } else {
      console.warn("No hay tareas para mostrar.");
    }

    const endTime = Date.now();

    console.log(`Tiempo de ejecución para mostrar: ${(endTime - starTime) / 1000}s`);
  }
}

let myTasks = new TaskManagement();

myTasks.show();
myTasks.add("Roadmap", "Realizar el ejercicio número 25.");
myTasks.add("Tianguis", "Acompañar a mis papás al tianguis.");
myTasks.add("Tianguis");
myTasks.show();
myTasks.delete("Tianjis");
myTasks.delete("Tianguis");
myTasks.show();
