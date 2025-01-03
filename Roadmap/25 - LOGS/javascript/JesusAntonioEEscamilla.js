/** #25 - JavaScript ->Jesus Antonio Escamilla */

/**
 * El concepto de "logging" en JavaScript se refiere al proceso de registrar información
 * sobre la ejecución de un programa. Esto es crucial para el desarrollo y mantenimiento
 * de software, ya que ayuda a los desarrolladores a entender lo que está sucediendo en
 * su código en tiempo real, diagnosticar errores y mejorar el rendimiento.
 */

//---EJERCIÓ---
// Registra un mensaje informativo en la consola
console.log('Esto es un mensaje informativo');

// Es un mensaje error en consola
console.error('Error en la linea xx, corregirla');

// Advertencia del código en la consola
console.warn('Alto aun no has declaro la variable');

// Un mensaje informativo en la consola (similar al `console.log`)
console.info('Te informo que esta quedando super');

// Mensaje depuración en la consola (no siempre esta disponible en todos los navegadores)
console.debug('Mensaje Depurador en tu Proyecto');

// Muestra datos tabulares como tabla en la consola
const usuario = [
    { nombre: 'Jesus', edad: 24},
    { nombre: 'Fatima', edad: 20}
];
console.table(usuario);

// Agrupa los mensajes en la consola
console.group('Detalles del Usuario');
console.log('Nombre: Antonio');
console.log('Edad: 24');
console.groupEnd();

// El Tiempo de ejecución
console.time('Se ejecuto el programa');
//  COGIDO DE LLENO
console.timeEnd('Se ejecuto el programa');



/**-----DIFICULTAD EXTRA-----*/

//Clase de Tareas
class TaskManager{
    constructor(){
        this.tasks = [];
    }

    //  Agregar Tarea
    addTask(nombre, descripción){
        console.time(`Tiempo de Ejecución - Añadir tarea: ${nombre}`);
        const nameTasks = this.tasks.find(tasks => tasks.nombre === nombre);
        if (nameTasks) {
            console.error(`La Tarea "${nombre}" ya existe`);
        } else {
            const task = {nombre, descripción};
            this.tasks.push(task);
            console.log(`Tarea añadida: "${nombre}" - "${descripción}"`);
        }
        console.timeEnd(`Tiempo de Ejecución - Añadir tarea: ${nombre}`);
        return
    }

    //  Borrar Tarea
    removeTask(nombre){
        console.time(`Tiempo de Ejecución - Eliminar tarea: ${nombre}`);
        const initialLength = this.tasks.length;
        this.tasks = this.tasks.filter(task => task.nombre !== nombre);
        if (this.tasks.length === initialLength) {
            console.error(`No se encontró la tarea con el nombre "${nombre}"`);
        } else {
            console.log(`Tarea eliminada: ${nombre}`);
        }
        console.timeEnd(`Tiempo de Ejecución - Eliminar tarea: ${nombre}`);
    }

    //  Listar las Tareas
    listTasks(){
        console.log('Listado de tareas:');
        console.table(this.tasks);
    }
}

//  Ejemplo de las Tareas
const tasksManager = new TaskManager();
tasksManager.addTask('Caminar', 'Caminar todos los días para bajar de peso');
tasksManager.addTask('Leer un libro', 'Leer por 10 minutos un libro');
tasksManager.addTask('Leer un libro', 'Leer por 10 minutos un libro');
tasksManager.listTasks();
tasksManager.removeTask('Caminar');
tasksManager.listTasks();

/**-----DIFICULTAD EXTRA-----*/