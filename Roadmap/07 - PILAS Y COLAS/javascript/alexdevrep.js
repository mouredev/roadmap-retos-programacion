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
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

//Pilas

/*
Las pilas son tipos abstactos de datos que se encuentran en un formato de tipo lista
a cuyos elementos se accede de una forma particular (LIFO) Last In First Out que se puede 
traducir como "Lo último en entrar será lo último en salir"
*/

//Creamos un array de objetos
let arrayObjetos = ["Hola","Javascript","Alexdevrep"]
console.log(arrayObjetos)

//Introducimos un elemento en el array
arrayObjetos.push("Mundo") //Añadimos un elemento al final del array
console.log(arrayObjetos)

//Recuperamos el último objeto del array que ha sido añadido
console.log(arrayObjetos.pop()) //Quitamos el último elemento del array
console.log(arrayObjetos)


console.log("---------------------------------------")

//Colas

/*
Las colas son los colecciones de elementos ordenados que únicamente permiten dos acciones 
-Añadir un elemento a la cola
-Sacar un elemento de la cola
La peculiaridad es que el primer elemento en entrar es el primero en salir (FIFO) First In First Out
*/

//Creamos una cola de objetos
let colaObjetos = ["Hola","Mundo","Alexdevrep"]

//Añadimos un elemento a la cola
colaObjetos.push("JavaScript")
console.log(colaObjetos)

//Recuperamos el primer elemento de la cola en ser añadido en este caso "Hola"
console.log(colaObjetos.shift()) //Quita el primer elemento del array y lo devuelve
console.log(colaObjetos)

console.log("---------------------------------------")

//Dificultad EXTRA

//Ejercicio Pilas
const prompt = require('prompt-sync')()
let pila_web = []

console.log("###---NAVEGADOR WEB---###")
console.log("Pestaña Nueva")

while (true) {
    function accion(arg) {
        if (arg == "ADELANTE") {
            const web = prompt("Por favor indique a qué web quiere acceder: ")
            pila_web.push(web)
            console.log(`Ahora estás viendo ${pila_web[pila_web.length - 1]}`)
        } else if (arg == "ATRAS") {
            if (pila_web.length > 1) {
                pila_web.pop()
                console.log(`Ahora estás viendo ${pila_web[pila_web.length - 1]}`)
            } else {
                console.log("No hay historial de navegación para retroceder")
            }
        } else if (arg == "SALIR") {
            console.log("Cerrando el navegador web")
            
        } else {
            console.log("Comando no reconocido")
        }
    }

    const arg = prompt("Por favor escriba ADELANTE si quiere acceder a una URL nueva, ATRAS si quiere cerrar la última URL, o SALIR para salir: ")
    accion(arg)
    if (arg == "SALIR"){
        break
    }
}


//Ejercicio Colas

let documentos = []

while (true){
    function impresora (archivo){
        if (archivo== "IMPRIMIR"){
            if(documentos.length>=1){
                console.log(`Imprimiendo archivo ${documentos.shift()}`)
            }
            else{
                console.log("No hay archivos para imprimir")
            }
        
        }
        else if (archivo == "SALIR"){
            console.log("Apagando la impresora")
            process.exit()
        }
        else {
            documentos.push(archivo)
            console.log("Documento añadido a la cola de impresión")
        }
    }
    archivo=prompt("Por favor escriba el nombre del archivo para añadirlo a la cola de la impresión , IMPRIMIR para imprimirlo y SALIR para apagar la impresora: ")
    impresora(archivo)
    

}

