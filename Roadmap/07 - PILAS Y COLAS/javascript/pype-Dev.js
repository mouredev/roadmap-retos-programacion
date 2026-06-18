/**
 * EJERCICIO
 */

/* Pila | STACK (LIFO) */
const miPila = [];
// Agregar un elemento a la parte superior de la Pila
miPila.push(1);
miPila.push(2);
miPila.push(3);
miPila.push(4);

// Last In
miPila.push(5);
console.log(miPila);

// Fisrt Out
miPila.pop();
console.log(miPila);

/* Pila | QUEUE (FIFO) */
const miCola = [];
// Agregar un elemento al final de la Cola
// First In
miCola.push('A');
miCola.push('B');
miCola.push('C');
miCola.push('D');
miCola.push('E');
console.log(miCola);

// Fisrt Out
miCola.shift();
console.log(miCola);

/**
 * EXTRA
 */

// Navegador
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,       // Recibe y alamcena la entreda de datos del usuario
    output: process.stdout,     // Imprime la información recibida
});

const historialNavegacion = [];
const historialAvanzar = [];

let paginaActual = ""; // Variable que almacena la ubicación actual en la ruta de navegación

console.log(`
        BIENVENIDO AL NAVEGADOR WEB
        Escriba una URL o navegue entre páginas utilizando "Atras"/"Adelante"
        Puede borrar el historial de navegación con "Borrar"
        Cierre el navegador con "Salir"
    `);

const menuNavegacion = () =>{

    rl.question('¿Qué deseas hacer? ', (respuesta) => {
        switch(respuesta.toLowerCase().trim()){
            case 'atras':
                if(historialNavegacion.length <= 1){
                    console.log("\nNo hay sitios web para mostrar. Busca una URL.")
                } else{
                    const ultimaBusqueda = historialNavegacion.pop();
                    historialAvanzar.push(ultimaBusqueda);

                    paginaActual = historialNavegacion[historialNavegacion.length - 1];

                    console.log(`\nPágina Actual:\n${paginaActual}`);
                }
                
                break;

            case 'adelante':
                if(historialAvanzar.length === 0){
                    console.log("\nNo hay sitios web para mostrar.")
                } else{
                    const paginaRecuperada = historialAvanzar.pop();
                    historialNavegacion.push(paginaRecuperada);

                    paginaActual = historialNavegacion[historialNavegacion.length - 1];

                    console.log(`\nPágina Actual:\n${paginaActual}`);
                }
                
                break;

            case 'borrar':
                historialNavegacion.length = 0;
                historialAvanzar.length = 0;
                console.log('Historial de navegación borrado.');
                
                historialAvanzar.length = 0;

                break;

            case 'salir':
                console.log('\nCerrando navegador... ¡Adiós!\n')
                rl.close();
                return;

            default:
                if(historialAvanzar.length >= 1){
                    historialAvanzar.length = 0;
                }

                historialNavegacion.push(respuesta);
                paginaActual = historialNavegacion[historialNavegacion.length - 1]; //último elemento agregado al stack

                console.log(`\nPágina Actual:\n${paginaActual}`);

                break;
        }
        
        menuNavegacion();
    });
}

menuNavegacion();

// Impresora
const colaImpresion = [];

console.log(`
    BIENVENIDO A LA IMPRESORA
        Aquí puede ingresar el nombre del documento que quiere imprimir.
        Escriba "Imprimir" para ver el documento en cola.
        Escriba "Terminar" para apagar la impresora.
    `);

const imprimirDocumentos = () =>{
    rl.question('\n¿Que desea hacer? ', (accion) => {
        switch(accion.toLowerCase().trim()){
            case 'imprimir':
                if(colaImpresion.length === 0){
                    console.log('¡Error! No hay documentos en cola para imprimir');
                } else{
                    let documentoImpreso = colaImpresion.shift();

                    console.log(`\nDocumento impreso: ${documentoImpreso}`);
                    console.log(`Cola actual de impresión: ${colaImpresion}`);
                }

                break;

            case 'terminar':
                console.log('\nCiclo de impresión terminado. Apagando...\n')
                rl.close();
                return;

            default:
                colaImpresion.push(accion);
                console.log(`\nCola actual de impresión: ${colaImpresion}`);

                break;
        }

        imprimirDocumentos();
    });
}

imprimirDocumentos();