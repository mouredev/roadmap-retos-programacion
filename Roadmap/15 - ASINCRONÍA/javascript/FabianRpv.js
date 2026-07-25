// Asincronia



/**
 * Función asíncrona que simula una tarea que tarda un tiempo en completarse.
 * @param {string} nombre - El nombre de la tarea.
 * @param {number} segundos - El número de segundos que durará la tarea.
 */
async function ejecutarTarea(nombre, segundos) {
    const inicio = new Date();
    console.log(`[${inicio.toLocaleTimeString()}] Tarea "${nombre}" iniciada. Duración: ${segundos} segundos.`);

    // Simulamos la tarea asíncrona con un setTimeout dentro de una promesa
    await new Promise((resolve) => {
        setTimeout(resolve, segundos * 1000);
    });

    const fin = new Date();
    console.log(`[${fin.toLocaleTimeString()}] Tarea "${nombre}" finalizada.`);
}

/**
 * Función principal para ejecutar tareas asíncronas.
 */
async function main() {
    // Ejecutamos varias tareas asíncronas
    await ejecutarTarea("Tarea 1", 3); // Tarea 1 dura 3 segundos
    await ejecutarTarea("Tarea 2", 5); // Tarea 2 dura 5 segundos
    await ejecutarTarea("Tarea 3", 2); // Tarea 3 dura 2 segundos

    console.log("Todas las tareas han finalizado.");
}

// Llamamos a la función principal
main();