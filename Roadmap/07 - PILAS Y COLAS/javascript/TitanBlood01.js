//Pilas y Colas en javascript

//PILA
let stack = []

//Insertar un elemento a la pila
stack.push(1)
stack.push(11)
stack.push(41)
stack.push(4)
//sacar un elemento de la pila
console.log("Elementos en la pila:", stack)
console.log("Imprimiendo y sacando de la pila:", stack.pop())
console.log("Quedan en la pila: ", stack)
console.log("Imprimiendo y sacando siguiente de la pila:", stack.pop())
console.log("Quedan en la pila: ", stack)

//COLA
console.log("====================")
let queue = []

//Insertar un elemento a la cola
queue.push(1)
queue.push(11)
queue.push(41)
queue.push(4)
//Sacar elemento de la cola
console.log("Elementos en la cola:", queue)
console.log("Imprimiendo y sacando de la cola:", queue.shift())
console.log("Quedan en la cola: ", queue)
console.log("Imprimiendo y sacando siguiente de la cola:", queue.shift())
console.log("Quedan en la cola: ", queue)

/* 
EXTRA:
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.

*/

console.log('//////////////////Navegador Web')

let webNavigatorBack = []
let webNavigatorForward = []
let orden = ''

function handleWebNavigator(order) {
    let web;
    switch (order) {
        case 'adelante':
            if (webNavigatorForward.length <= 0){
                console.log(`No hay paginas para ir de nuevo adelante`)
            } else {
                let lastWeb = webNavigatorForward.pop()
                console.log(`Avanzando adelante: ${lastWeb}`)
                webNavigatorBack.push(lastWeb)
            }
            break
        case 'atras':
            if (webNavigatorBack.length < 2){
                console.log('No hay paginas previas para retroceder');
            } else {
                web = webNavigatorBack.pop()
                console.log(`Regresando a atras: ${webNavigatorBack[webNavigatorBack.length-1]}`)
                webNavigatorForward.push(web)

            }
            break
        default :
            web = order
            console.log(`Tu estas en esta pagina: ${web}`)
            webNavigatorBack.push(web)
            webNavigatorForward = []
    }
}

handleWebNavigator('atras')
handleWebNavigator('Google')
handleWebNavigator('atras')
handleWebNavigator('Facebook')
handleWebNavigator('atras')
handleWebNavigator('Twitter')
handleWebNavigator('Instagram')
handleWebNavigator('atras')
handleWebNavigator('adelante')
handleWebNavigator('atras')
handleWebNavigator('atras')
handleWebNavigator('adelante')
handleWebNavigator('Youtube')


////////////////////////////////

// Impresora

let printQueue = []

function print(action){
    let actionFormatter = action.toLowerCase()
    switch (actionFormatter){
        case 'imprimir':
            if (printQueue.length<=0){
                console.log('ATENCION!, La cola de la impresora esta vacia')
                break
            } else {
                console.log(`Imprimiendo: ${printQueue.shift()}`)
                console.log(`Cantidad de documentos en la cola: ${printQueue.length}`)
                break
            }
        default:
            console.log(`Añadiendo ${action} a la cola de impresion`)
            console.log(`Cantidad de documentos en la cola: ${printQueue.push(action)}`)
    }
}

console.log('//////////////////////Impresora')
print('Hola mundo')
print('Yo soy Garu')
print('Imprimir')
print('Nuevo Documento')
print('Antiguo Documento')
print('Imprimir')
print('Imprimir')
print('Imprimir')
print('Imprimir')