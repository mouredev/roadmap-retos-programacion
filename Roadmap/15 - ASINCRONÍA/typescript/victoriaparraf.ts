//FUNCION ASINCRONA
function esperar(segundos: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, segundos * 1000));
}

async function ejecutarFuncion(nombre: string, duracionSegundos: number) {
    console.log(`La función ${nombre} comienza a ejecutarse.`);
    console.log(`Duración esperada: ${duracionSegundos} segundos.`);

    await esperar(duracionSegundos);

    console.log(`La función ${nombre} ha finalizado su ejecución.`);
}

// Ejecutar una función de ejemplo
ejecutarFuncion('Ejemplo', 5);

//EXTRA
//ejecucion de varias funciones asincronas

async function main() {
    // Crear las funciones A, B, y C que se ejecutarán en paralelo
    const funcionC = ejecutarFuncion('C', 3);
    const funcionB = ejecutarFuncion('B', 2);
    const funcionA = ejecutarFuncion('A', 1);

    // Esperar a que todas las funciones C, B, y A terminen
    await Promise.all([funcionC, funcionB, funcionA]);

    // Ejecutar la función D después de que C, B, y A hayan terminado
    await ejecutarFuncion('D', 1);
}

// Llamar a la función principal
main();

