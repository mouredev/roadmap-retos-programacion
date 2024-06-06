/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */



// Stacks

const stack = []
stack.push('Hello')
stack.push('World')
stack.push('from')
stack.push('JavaScript')

console.log('This is the stack:')
console.log(stack)
const lastElement = stack.pop()
console.log('LIFO - Last element is the first out: ',lastElement)
console.log('This is the stack after popping:')
console.log(stack)

// Queue

const queue = []
queue.push('Hello')
queue.push('World')
queue.push('from')
queue.push('JavaScript')

console.log('This is the queue:')
console.log(queue)
const firstElement = queue.shift() 
console.log('FIFO - First element is the first in: ', firstElement)
console.log('This is the queue after shifting:')
console.log(queue)


// EXTRA TASK:

// Web Browser:

const history=[]
let pointer=-1
let actualPage=''

function visit(url){
    history.push(url)
    pointer++
}

function back(){
    pointer--
    console.log(history[pointer])
}
function next(){
    pointer++
    console.log(history[pointer])
}

visit('moure.dev')
visit('othamae.dev')
visit('retosdeprogramacion.com')
visit('github.com')

console.log('This is the history:')
console.log(history)
console.log(`We are now in page: ${history[pointer]}`)
console.log(`We go back: `)
back()
console.log(`We go back again: `)
back()
console.log(`Now we go forward: `)
next()


// Printer:

const printerQueue = []

function sentToPrinter(document){
    printerQueue.push(document)
    console.log(`Document "${document}" sent to printer`)
}

function printDocuments(){
    while(printerQueue.length>0){
        const currentDocument = printerQueue.shift()
        console.log(`Printing "${currentDocument}"`)
    }
    console.log('No documents to print')
}

sentToPrinter('Document 1')
sentToPrinter('Document 2')
sentToPrinter('Document 3')
sentToPrinter('Document 4')

console.log('Pressing IMPRIMIR button:')
printDocuments()