/**
 * Función asíncrona que simula una tarea que tarda un tiempo específico
 * @param {string} nombre - Nombre de la tarea
 * @param {number} segundos - Duración de la tarea en segundos
 * @returns {Promise} Una promesa que se resuelve cuando la tarea termina
 */
function ejecutarTareaAsincrona(nombre, segundos) {
    return new Promise(resolve => {
        console.log(`${nombre} - Iniciando...`);
        console.log(`${nombre} - Durará ${segundos} segundos`);
        
        setTimeout(() => {
            console.log(`${nombre} - Finalizada`);
            resolve();
        }, segundos * 1000);
    });
}

/**
 * Demostración básica de una tarea asíncrona
 */
async function demostracionBasica() {
    console.log("=== Demostración Básica ===");
    await ejecutarTareaAsincrona("TareaEjemplo", 2);
}

/**
 * Implementación de la dificultad extra
 * Ejecuta las tareas C, B y A en paralelo y luego D cuando las anteriores terminan
 */
async function dificultadExtra() {
    console.log("\n=== Dificultad Extra ===");
    
    // Ejecutar tareas C, B y A en paralelo
    const tareaC = ejecutarTareaAsincrona("Tarea C", 3);
    const tareaB = ejecutarTareaAsincrona("Tarea B", 2);
    const tareaA = ejecutarTareaAsincrona("Tarea A", 1);
    
    // Esperar a que todas las tareas terminen
    await Promise.all([tareaC, tareaB, tareaA]);
    
    // Ejecutar tarea D después de que las otras hayan terminado
    await ejecutarTareaAsincrona("Tarea D", 1);
}

/**
 * Función principal que ejecuta todas las demostraciones
 */
async function main() {
    await demostracionBasica();
    await dificultadExtra();
}

// Ejecutar el programa
main().catch(error => console.error('Error:', error));