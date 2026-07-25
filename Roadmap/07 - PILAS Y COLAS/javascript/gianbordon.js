/* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
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

//
// Pilas 
//

console.group('|* PILAS *|')
let pila = []

// Agregar elementos 
pila.push("Elemento 1")
pila.push("Elemento 2")
pila.push("Elemento 3")

console.log("Pila actual:", pila) 
console.log("Tamaño de la pila:", pila.length) 


// Eliminar elemento (se elimina el ultimo en entrar a la pila)
let ultimo = pila.pop()
console.log("Elemento retirado:", ultimo)
console.log("Pila después del pop:", pila) 
console.log("Tamaño actualizado:", pila.length)

// Ver elemento sin Eliminar
let tope = pila[pila.length - 1]
console.log("Elemento en el tope:", tope) 
console.groupEnd()

//
// Colas
//

console.group('|* COLAS *|')
let cola = []

// Agregar elementos (siempre al final, posicionandose ultimo)
cola.push("Persona 1")
cola.push("Persona 2")
cola.push("Persona 3")

console.log("Cola actual:", cola) 
console.log("Tamaño de la cola:", cola.length) 

// Eliminar elemento (siempre el primero que ingreso)
let atendido = cola.shift() 
console.log("Atendido:", atendido)
console.log("Cola después del dequeue:", cola)
console.log("Tamaño actualizado:", cola.length)

// Ver quién es el siguiente en Eliminar
let primero = cola[0]
console.log("Siguiente en la cola:", primero)
console.groupEnd()

//
// EXTRA
//

// * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
// *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
// *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
// *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
// *   el nombre de una nueva web.

const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

function mainMenu() {
    console.clear()
    console.log("╔═══════════════════════════════════════╗")
    console.log("║         MENÚ PRINCIPAL                ║")
    console.log("╠═══════════════════════════════════════╣")
    console.log("║ 1. Navegar en el navegador            ║")
    console.log("║ 2. Usar la impresora                  ║")
    console.log("║ 0. Salir                              ║")
    console.log("╚═══════════════════════════════════════╝")

    rl.question("Selecciona una opción (1 o 2, 0 para salir): ", (opc) => {
        switch (opc) {
            case "1":
                console.log("→ Accediendo al navegador.")
                web()
                break
            case "2":
                console.log("→ Accediendo a la impresora.")
                impresora()
                break
            case "0":
                console.log("→ Programa finalizado.")
                rl.close(); 
                break
            default:
                console.log("❌ Opción inválida.")
                setTimeout(mainMenu, 1500)
                break
        }
    })
}

let pagesBack = []
let pagesForward = []
let actualPage = null

function web(){
    console.clear()
    console.log("╔════════════════════════════════════════════╗")
    console.log("║             GIANSIN BROWSER                ║")
    console.log("╠════════════════════════════════════════════╣")
    console.log("║                                            ║")
if(actualPage !== null){
    console.log(`║             ${actualPage}                  ║`)
}else {
    console.log("║       No hay una página cargada aún        ║")
}
    console.log("║                                            ║")
    console.log("║  <= Atrás                     Adelante =>  ║")
    console.log("║                                            ║")
    console.log("║                Salir                       ║")
    console.log("╚════════════════════════════════════════════╝")
    rl.question('Ingrese "atrás" o "adelante" o "salir" o una nueva pagina para comenzar a navegar: ', (res)=>{
        res = res.toLowerCase().trim()
        if (res === "") {
            console.log("❌ Entrada vacía. Por favor ingrese una opción válida.")
            setTimeout(web, 1000)
        } else if(res === "salir"){
            console.log("Gracias por usar el navegador. ¡Hasta luego!")
            mainMenu()
        } else if (res === "adelante") {
            nextPage()
        } else if (res === "atras") {
            prevPage()
        } else {
            browse(res)
        }
    })
}

function nextPage(){
    if(pagesForward.length === 0){
        console.log("❌ No hay más páginas adelante.")
    } else {
        const nextPage = pagesForward.pop()
        pagesBack.push(actualPage)
        actualPage = nextPage
        console.log(`🔜 Ahora estás en: ${actualPage}`)
    }
    setTimeout(web, 1000)
}

function prevPage(){
    if(pagesBack.length === 0){
        console.log("❌ No hay más páginas atrás.")
    } else {
        const prevPage = pagesBack.pop()
        pagesForward.push(actualPage)
        actualPage = prevPage
        console.log(`🔙 Ahora estás en: ${actualPage}`)
    }
    setTimeout(web, 1000)
}

function browse(res){
    if(res !== null){
        pagesBack.push(res)
    }
    actualPage = res
    console.log(`🔍 Ahora estás navegando en: ${actualPage}`)
    pagesForward = []
    setTimeout(web, 1000)
}

// * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
// *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
// *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
// *   interpretan como nombres de documentos.

let archivos = []

function impresora() {
    console.clear()

    console.log("╔═══════════════════════════════════════╗")
    console.log("║         🖨 IMPRESORA XP_2000          ║")
    console.log("╠═══════════════════════════════════════╣")
    console.log("║ 1. Agregar documento                  ║")
    console.log("║ 2. Imprimir                           ║")
    console.log("║ 3. Lista de documentos                ║")
    console.log("║ 0. Salir                              ║")
    console.log("╚═══════════════════════════════════════╝")

    rl.question("Seleccioná una opción (1 al 3): ", (opc) => {
        switch (opc) {
        case "1":
            console.log("→ Elegiste AGREGAR documento.")
            addDocument()
            break
        case "2":
            console.log("→ Elegiste Imprimir.")
            printDocument()
            break
        case "3":
            console.log("→ Elegiste LISTA de documentos.")
            showDocuments()
            break
        case "0":
            console.log("→ Programa finalizado.")
            mainMenu()
            break
        default:
            console.log("❌ Opción inválida.")
            setTimeout(impresora, 1500)
        }
    })
}

function addDocument(){
    rl.question('Ingrese el nombre del documento PDF que desea ingresar: ', (doc) =>{
        if (doc.endsWith(".pdf")) {
            archivos.push(doc)
            console.log(`✅ El archivo "${doc}" fue agregado a la cola de archivos para imprimir correctamente.`)
            backToMenu()
        } else {
            console.log('🔁 Archivo inválido., el archivo debe ser .pdf, intente nuevamente.')
            addDocument()
        }
    })
}

function printDocument(){
    if (archivos.length !== 0){
        console.log(`Impriminedo el primer archivo de la cola: "${archivos[0]}"`)
        archivos.shift()
        console.log('✅ Archivo impreso.')
        backToMenu()
    } else {
        console.log('❌ No hay archivos pendientes para imprimir.')
        backToMenu()
    }
}

function showDocuments(){
    if (archivos.length === 0) {
        console.log("❌ No hay archivos en la cola.")
    } else {
        console.log("Lista de Archivos pendientes:")
        archivos.forEach((doc, index) => {
            console.log(`${index + 1}. ${doc}`)
        })
    }
    backToMenu()
}

function backToMenu(){
    rl.question('Presiona ENTER para volver al menú...', ()=>{
        impresora()
    })
}

mainMenu()