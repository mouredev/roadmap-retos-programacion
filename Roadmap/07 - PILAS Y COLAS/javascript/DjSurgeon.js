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

// stack - LIFO: Last In, First Out

const arr = [0,1,2,3,4,5];

const lastIn = (num) => {
    arr.push(num);
    console.log(arr);
}
const firstOut = () => {
    arr.pop();
    console.log(arr);
}
// lastIn(8); output => [0,1,2,3,4,5,8]
// firstOut(); output => [0,1,2,3,4,5]

// queue - FIFO: First In, First Out

const firstIn = (num) => {
    arr.unshift(num);
    console.log(arr);
}

// firstIn(8); output => [8,1,2,3,4,5];
// firstOut(); output => [8,1,2,3,4];

/*
* En la pila (stack) el último en llegar es el primero en salir, su analogia seria una pila de platos.
* En la cola (queue) uno llega por un extremo y el otro sale por el otro extremo, su analogia seria una cola en el supermercado.
*/

const webs = ["inicio"];
let index = 0;
const paginaWeb = (string) => {
    if (string === "adelante") {
        index++;
        console.log(webs[index])
    } else if (string==="atras") {
        index--;
        console.log(webs[index])
    } else if (string) {
        webs.push(string);
        console.log(webs);
    }
}
/* 
paginaWeb("55");
paginaWeb("0");
paginaWeb("adelante");
paginaWeb("adelante");
paginaWeb("atras");
paginaWeb("adelante");
*/

const documentos = ["lista", "dibujo", "redacción"];

const impresora = (string) => {
    if (string === "imprimir") {
        console.log(`Imprimiendo: ${documentos[documentos.length-1]}`)
        documentos.pop();
    } else if (string) {
        documentos.unshift(string);
        console.log(`Lista de documentos: ${documentos}`);
    }
}
/*
impresora("cv");
impresora("imprimir");
impresora("nuevo cv");
*/
