/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web. Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

// Pila/Stacks )LIFO=

let stack: number[] = []
stack.push(1)
stack.push(2)
stack.push(3)
console.log("Este es el stack completo: ", stack)

let stackItem = stack.pop()
console.log("El tulitmo elemento desapilado es: ", stackItem)
console.log("Este es el stack actualizado: ", stack)

// Cola/Queve (FIFO)

let  queve: number[] = []

queve.push(1)
queve.push(2)
queve.push(3)

console.log("Esta es el queve: ", queve)

 let queveItem = queve.shift()

console.log("Este es el primer elementro desapilado: ", queveItem)
console.log("Este es el queve actualizado", queve)


// Extra

let paginaWeb: number[] = []

let accionMovimiento = (accion: string) =>{
    if (accion === "adelante") {
        let lastNumber = paginaWeb.length
        let newNumber = lastNumber + 1
        paginaWeb.push(newNumber)
        return paginaWeb
    } else if (accion === "atras"){
        paginaWeb.pop()
        return paginaWeb
    }
}

console.log(accionMovimiento("adelante"))
console.log(accionMovimiento("adelante"))
console.log(accionMovimiento("adelante"))
console.log(accionMovimiento("atras"))
console.log(accionMovimiento("atras"))

//! EXTRA

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web. Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica. La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos.
 */

import * as readline from "readline";

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const webNavigation = () =>{
    let stack: string[] = []
    let memoria: (string | undefined)[] = []

    const preguntar = () =>{
        rl.question(`Añade una url o navega con las pabaras "adelante/atras/salir": `, (action)=>{
            console.log("")
            if (action === "adelante") {
                if (memoria.length <= 0) {
                    console.log("")
                    console.log("no tienes registro de memoria")
                    console.log("")
                    preguntar()
                } else {
                    console.log("")
                    console.log("esto es lo que tiene memoria ⬇️:")
                    console.log(memoria)
                    console.log("esto es lo que tiene memoria en la ultima posicion ⬇️:")
                    console.log(memoria[memoria.length -1])
                    stack.push(`${memoria[memoria.length -1]}`)
                    console.log("")
                    console.log("Esta es la pagina en la que estas ahora: ⬇️")
                    console.log(stack[stack.length -1])
                    console.log("")
                    memoria.pop()
                    console.log("asi quedo memoria ⬇️:")
                    console.log(memoria)
                    console.log("")
                    console.log("Asi quedo stack ⬇️:")
                    console.log(stack)
                    console.log("")
                }
            } else if (action === "atras"){

                if (stack.length <= 0) {
                    console.log("")
                    console.error("estas en la pagina de inicio, no puedes ir mas para atras")
                    console.log("")
                    preguntar()
                }else{
                    console.log("")
                    let lastPage = stack.pop()
                    console.log("esta es la ultima pagina eliminada y guardada en la variable lastPage ⬇️:")
                    console.log(lastPage)
                    console.log("")
                    console.log("lastPage ⬇️:")
                    console.log(lastPage)
                    console.log("")
                    memoria.push(lastPage)
                    console.log("Memoria ⬇️:")
                    console.log(memoria)
                    console.log("")
                    console.log("Volviste a la pagina ⬇️:")
                    console.log(stack[stack.length -1])
                    console.log("")
                    console.log("Asi esta el stack ⬇️:")
                    console.log(stack)
                    console.log("")
                }
            } else if (action === "salir"){
                console.log("Saliendo del navegador web")
                console.log()
                rl.close()
            } else{
                stack.push(action)
                console.log("Has navegado a la web ⬇️:")
                console.log(stack[stack.length -1])
                console.log(stack)
                console.log("")
            }
            preguntar()
        })
    }
    preguntar()
}

// webNavigation()

const sharedPrinter = () =>{
    let quece: string[] = [] 

    const preguntar = () =>{
        rl.question("Añade un documento o selecciona imprimir/salir: ", (action)=>{
            if (action === "salir") {
                console.log("")
                console.log("Saliste del programa")
                console.log("")
                rl.close()
            } else if (action === "imprimir") {
                console.log("")
                console.log(`Hay ${quece.length} elemento imprimiendose`)
                console.log("")
                while (quece.length > 0) { //ejecuta un bucle siempre que la condicion sea verdadera y se vuelve a evaluar la condicion hasta que esta sea falsa
                    const documento = quece.shift(); // Elimina el primer elemento
                    console.log("Imprimiendo: ", documento); // en cada bucle imprime el valor de document
                }
                console.log("\nLa cola está vacía.\n");
                preguntar()
            } else {
                console.log("")
                quece.push(action)
                console.log("Esto es loque tiene la variable quece ⬇️")
                console.log(quece)
                console.log("")
                preguntar()
            }
        })
    }
    preguntar()
}

// sharedPrinter()