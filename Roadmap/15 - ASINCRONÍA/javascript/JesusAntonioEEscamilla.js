/** #15 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Es uno de los pilares de fundamentales de JavaScript,
    ya que es un lenguaje de programación de uns sólo sub-proceso
    o hilo (single thread), lo que significa que solo puede
    ejecutarse una cosa a la vez
*/

//---EJERCIÓ---
// Aquí esta función asíncrona
async function asyncFunction(nombre, segundo) {
    console.log(`Inicia la ejecución de ${nombre}, empieza en ${new Date().toLocaleTimeString()}.`)

    // La forma asíncrona para simular la esperar utilizando SetTimeout
    await new Promise (res => {
        setTimeout(res, segundo * 1000);
    });

    console.log(`Se finaliza la ejecución de ${nombre} en ${segundo / 1000} segundos, finalizo en ${new Date().toLocaleTimeString()}.`);
}

// Una función muestra para ejecutar la función asíncrona
async function muestra() {
    try {
        await Promise.all([
            asyncFunction('Proceso1', 2),
            asyncFunction('Proceso2', 3)
        ]);
    } catch (error) {
        console.error('Se produjo un error:', error);
    }
}

// Se ejecuta el main
muestra()



/**-----DIFICULTAD EXTRA-----*/

//  Ejecución de funciones de A B C D
async function main() {
    //  Se un Try-Catch para evitar errores al ejecutarlos
    try {
        //  La funciones a ejecutar
        await Promise.all([
            asyncFunction('función C', 3),
            asyncFunction('función B', 2),
            asyncFunction('función A', 1),
        ]);

        //  La muestra la ultima función
        await asyncFunction('función D', 1);
    } catch (error) {
        console.error('Se produjo un error:', error)
    }
}

//  La ejecución de la función principal
main()

/**-----DIFICULTAD EXTRA-----*/