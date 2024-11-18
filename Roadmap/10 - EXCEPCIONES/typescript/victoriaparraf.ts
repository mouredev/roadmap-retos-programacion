//MANEJO DE EXCEPCIONES
function manejarErrores(): void {
    try {
        // Forzando una división por cero
        let resultado = dividir(10, 0);
        console.log(`Resultado de la división: ${resultado}`);
    } catch (error) {
        console.error(`Error capturado: ${error.message}`);
    } finally {
        console.log("Bloque finally ejecutado después de intentar dividir.");
    }

    try {
        // Acceso a un índice no existente en un array
        let lista = [1, 2, 3];
        let elemento = accederIndice(lista, 5);
        console.log(`Elemento en el índice 5: ${elemento}`);
    } catch (error) {
        console.error(`Error capturado: ${error.message}`);
    } finally {
        console.log("Bloque finally ejecutado después de intentar acceder a un índice.");
    }
}

function dividir(a: number, b: number): number {
    if (b === 0) {
        throw new Error("División por cero no permitida.");
    }
    return a / b;
}

function accederIndice(array: number[], index: number): number {
    if (index < 0 || index >= array.length) {
        throw new Error("Índice fuera de los límites del array.");
    }
    return array[index];
}

// Ejecutar el manejo de errores
manejarErrores();


