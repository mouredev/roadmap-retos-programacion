/*
    * #15 ASINCRONÍA
*/

function funcionAsincrona(nombre, tiempo) {
    return new Promise((resolve, reject) => {
        if (isNaN(tiempo) || tiempo <= 0) {
            reject(new Error('El parámetro "tiempo" debe ser un número positivo'));
            return;
        }

        console.log(`Iniciando función "${nombre}"...`);
        console.log(`Duración: ${tiempo} segundos`);

        const tiempoInicio = Date.now();

        setTimeout(() => {
            console.log(`Función "${nombre}" finalizada`);
            console.log(`Tiempo total de ejecución: ${Date.now() - tiempoInicio} milisegundos`);
            resolve();
        }, tiempo * 1000);
    });
}

/*
    *  DIFICULTAD EXTRA
*/

async function ejecutarFunciones() {
    const functionA = () => funcionAsincrona("A", 3)
    const functionB = () => funcionAsincrona("B ", 2)
    const functionC = () => funcionAsincrona("C", 1)
    const functionD = () => funcionAsincrona("D", 1)

    await Promise.all([functionA(), functionB(), functionC()]);
    await functionD();
}

ejecutarFunciones();
