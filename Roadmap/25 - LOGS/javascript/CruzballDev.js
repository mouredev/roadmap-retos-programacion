/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
*/

/*

function log(mensaje, nivel = "info") {

    switch(nivel) {
        case "debug":
            console.debug(`[DEBUG]`)
            break;
        case "info":
            console.log(`[INFO] ${mensaje}`)
            break;
        case "log":
            console.log(`[LOG] ${mensaje}`)
            break;
        case "warn":
            console.log(`[WARN] ${mensaje}`)
            break;
        case "error":
            console.log(`[ERROR] ${mensaje}`)
            break;
        default:
            console.log(`[LOG] ${mensaje}`)
    }
}

log(`Variable usuario creada`, "debug")
log(`Usuario autenticado`, "info")
log(`Procesando pedido`, "log")
log(`El servidor responde lentamente`, "warn")
log(`No se pudo conectar con la base de datos`, "error") */

/*
* DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
*/


class GestionTareas {

    constructor() {
        this.tareas = []
    }


    añadirTarea(nombre, descripcion) {
        const inicio = performance.now();

        const tarea = {
            nombre: nombre,
            descripcion: descripcion
        };

        this.tareas.push(tarea);

        console.info(`¡[INFO] La tarea ${nombre} se ha añadido correctamente!`);

        const final = performance.now();

        console.debug(`[DEBUG] Tiempo de ejecución: ${(final - inicio).toFixed(2)}ms`)

    }

    eliminarTarea(nombre) {
        const inicio = performance.now() //performance.now() te da un valor temporal de alta resolución pensado para medir intervalos de tiempo.

        const indice = this.tareas.findIndex((tarea) => tarea.nombre === nombre)

        if(indice === -1) {
            console.warn(`[WARN] No se encontró la tarea: ${nombre}`)
            return
        }

        this.tareas.splice(indice, 1) // splice(indice, 1) significa : del índice que te pase, cantidad de elementos a eliminar 1.

        console.log(`La tarea ${nombre} se ha eliminado correctamente.`)

        const final = performance.now()


        console.debug(`[DEBUG] Tiempo de ejecución: ${( final - inicio).toFixed(2)}ms`)
    }

    listarTareas() {

        const inicio = performance.now();

        if(this.tareas.length === 0) {
            console.info("[INFO] No hay tareas para mostrar")
            return
        }

        console.info(`[INFO] Lista de tareas: `)

        this.tareas.forEach((tarea, indice) => { // El forEach() reinicia indice en 0 cada vez que vuelves a ejecutarlo. No conserva el número de la ejecución anterior.
            console.log(
                `${indice +1}. ${tarea.nombre} - ${tarea.descripcion} ` // Indice +1 , para que empiece en 1 ya que los arrays por defecto empiezan en 0.
            )
        })

        const final = performance.now();

        console.debug(`[DEBUG] Tiempo de ejecución: ${( final - inicio).toFixed(2)}ms`) // toFixed(2)  Limitamos a 2 los números decimales
    }
}

let gestion1 = new GestionTareas() // Creamos el objeto

gestion1.añadirTarea("Nadar","Nadar durante 20 minutos.")
gestion1.listarTareas()
gestion1.añadirTarea("Pasear", "Caminar por el monte")
gestion1.añadirTarea("Estudiar", "Arquitectura del software y agentes de IA")
gestion1.listarTareas()
gestion1.eliminarTarea("Nadar")
gestion1.listarTareas()