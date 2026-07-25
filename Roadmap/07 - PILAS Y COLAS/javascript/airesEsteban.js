// Pilas (stacks -LIFO)

let  pila = []

pila.push(1)
pila.push(2)
pila.push(3)

//console.log(pila)

pila.pop()

//console.log(pila)

// Cola (queue - FIFO)
let cola = []

cola.push("a")
cola.push("b")
cola.push("c")

cola.shift()
//console.log(cola)


/*
Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
 */

let historial = []
let paginaActual = 0

function agregarPagina(web) {
    if (historial.length > 0){
        paginaActual ++
    }    
    historial.push(web)
}

function atras(){
    console.log(historial[paginaActual-1])
    paginaActual--
}

function adelante(){
    console.log(historial[paginaActual+1])
    paginaActual++
}

agregarPagina("test.com")
console.log(historial)

agregarPagina("vip.com")
console.log(historial) 


atras()
adelante()


/*
Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
*/
let readline = require('readline')
let rl = readline.createInterface({ input: process.stdin, output: process.stdout })

cola=[]

function printer(){
    printQueue(cola)

    rl.question('Ingresa un documento o elige "imprimir" o "salir": ', (answer) => {
    let inputFormat = answer.trim().toLowerCase()
    switch (inputFormat){
        case "imprimir":
            if (cola.length === 0){
                console.log("No hay documentos para imprimir")
                printer()
            } else {
                let doc = cola.shift()
                console.log(`Imprimiendo ${doc}`)
                printer()
            }
            break
        case "salir":
            rl.close()
            break
        default:
            cola.push(inputFormat)
            printer()
            break  
    }
})
}

function printQueue(cola) {
    if(cola.length === 0) {
        console.log("No hay documentos en cola para imprimir")
    }else {
        console.log("Cola de impresion")
        cola.forEach(document => {
          console.log(document)  
        })
    }
}

printer()