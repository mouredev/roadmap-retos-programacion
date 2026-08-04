/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
*/


// Pilas (stacks - LIFO)
let ropa = ["prenda1", "prenda2"]

function armario(accion, prenda) {
    if( accion == "sacarPrenda") {
        const prendaSacada = ropa.pop()
        return `La prenda sacada es: ${prendaSacada}`
    }
    if(accion == "guardarPrenda") {
        ropa.push(prenda)
        return `El prenda guadada es: ${prenda} `
    }
    return ropa
}
/* console.log(ropa)
console.log(armario("sacarPrenda"))
console.log(ropa)
console.log(armario("guardarPrenda", "prenda3"))
console.log(ropa) */

// Colas (queue - FIFO)
let solicitudes = ["solicitud1", "solicitud2"]

function salidaSolicitudes(accion, solicitud) {
    if(accion === "mandarSolicitud") {
        const inSolicitud = solicitudes.push(solicitud)
        return `Solicitud recibida: ${solicitud}`
    }
    if(accion === "responderSolicitud") {
        const resSolicitud = solicitudes.shift()
        return `Devolver solicitud con respuesta: ${resSolicitud}`
    }
    return solicitudes
}
/* console.log(solicitudes)
console.log(salidaSolicitudes("responderSolicitud"))
console.log(solicitudes)
console.log(salidaSolicitudes("mandarSolicitud", "solicitud3"))
console.log(solicitudes)
console.log(salidaSolicitudes("responderSolicitud"))
console.log(solicitudes)
console.log(salidaSolicitudes("mandarSolicitud", "solicitud4"))
console.log(solicitudes) */



/* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
*/


/* const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

const rl = readline.createInterface({
    input: stdin,
    output: stdout
}); */

async function navegador() {
    let adelante = []
    let atras = []
    let posicionActual = null;
    let activo = true
    
    while(activo) {
        console.log(`
            //////////////////////////////////
            HISTORIAL:
            Atrás:, ${atras}
            Página actual:${posicionActual}
            Adelante: ${adelante};
        `) ;

        if(posicionActual) {
            console.log(`Página actual: ${posicionActual}
            ////////////////////////////////////////////\n`)
        }else {
            console.log("No hay páginas abiertas.")
        }

        const opcion = await rl.question(`
            Introduce el número para elegir una opción:
            
            1. Añadir una URL
            2. Ir hacia atras
            3. Ir hace adelante
            4. Salir de la aplicación
            Opción:
        `)
        
        switch(opcion) {
            case "1": // Introducir URL
                const url = await rl.question("Introduce una URL: ")
                console.log(`Has introducido esta URL: ${url}`)

                if(posicionActual !== null) {
                    atras.push(posicionActual)
                }
                posicionActual = url
                adelante = []
                break;
            case "2": // Ir hacia atras
                if(atras.length > 0) {
                    adelante.push(posicionActual)
                    posicionActual = atras.pop()
                    console.log(`Has vuelto a la página: ${posicionActual}`)
                }else {
                    console.log("No hay paginas anteriores.")
                }
                break;
            case "3": // Ir hacia adelante
                if(adelante.length > 0) {
                    atras.push(posicionActual)
                    posicionActual = adelante.pop()
                }else {
                    console.log("Adelante no hay páginas.")
                }
                break;
            case "4": // Salir de la aplicación
                activo = false;
                console.log("¡Has salido del programa, hasta pronto!\n")
                break;
            default:
                consolet.log("¡Elección incorrecta!\nIntentalo de nuevo.")
                break;

        }
    }
    //rl.close()
}
//navegador()

/* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
*/


const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

const rl = readline.createInterface({
    input: stdin,
    output: stdout
});

async function impresora() {
    let cola = []
    let activo = true
    let documento

    while(activo) {
        const action = await rl.question(`Añade un documento o elige imprimir o salir: `)

        switch(action) {
            case "imprimir":
                if(cola.length > 0) { // Imprimir
                    console.log(`Imprimiendo: ${cola.shift()}`)
                }else {
                    console.log("No hay documentos para imprimir.")
                }
                break;
            case "añadir":
                documento = await rl.question("Nombre del documento: ")
                cola.push(documento) //  Añadir documento
                break;
            case "salir":
                activo = false // Salir
                console.log("\nProgama finalizado!")
                break;
            default:
                console.log("Los datos introducidos no son válidos")
                break;
        }
        if(cola.length === 0) {
            console.log("¡La cola de impresión está vacia!")
        }else {
            console.log(`\nCola de impresión: ${cola}`)
        }
    }
    rl.close()
}
impresora()