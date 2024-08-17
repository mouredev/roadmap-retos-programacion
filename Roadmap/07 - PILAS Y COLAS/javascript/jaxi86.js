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
console.log('pilas');
let array = [4, 6, 1, 8, 2, 9];
console.log(array);

array.push(10);//aqui uso la introduccion a la pila
console.log(array);

console.log(array.pop());//aqui accedo para recuperar el TOS
console.log(array);

console.log(' ');

console.log('colas');
let arreglo = [1, 7, 4, 2];
console.log(arreglo);

arreglo.push(3);//aqui introdusco un elemento segun las espesificaciones de una cola
console.log(arreglo);

console.log(arreglo.shift());// aqui accedo al elementos de indice cero (el primero en entrar) tal como las espesificaciones de una cola me lo indica
console.log(arreglo);

console.log(' ');

console.log('DIFICULTAD EXTRA');
/* 
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web. */


function web() {
    let pila = [];

    while (true) {
        let opcion = prompt("agrega una pagina o escribe adelante/atras para navegar en las distintas paginas o salir para salir del panel");

        if (opcion === "salir") {
            break;
        } else if (opcion === "adelante") {
            // No se puede volver a delante, pero podríamos mostrar un mensaje
            console.log("No se puede ir hacia adelante");
        } else if (opcion === "atras" && pila.length > 0) {
            pila.pop();
        } else {
            pila.push(opcion);
        }

        // Mostrar la página actual solo si la pila no está vacía
        if (pila.length > 0) {
            console.log(`Página actual: ${pila[pila.length - 1]}`);
        }
    }
}

//web();  comento la llamada a la funcion para poder hacer la siguinete

/* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
*/ 

function impresora () {
    let cola =[];
    while (true) {
        let opcion = prompt("escribe el nombre del ducumento o la palabra 'imprimir', imprime el primer documento", "imprimir");

        if (opcion === "salir") {
            console.log("salio del programa");
            break;
        } else if (opcion === "imprimir" && cola.length > 0) {
            console.log(`documento que se esta imprimiendo: ${cola.shift()}`);
        } else {
            cola.push(opcion);
        }
    }
}

impresora();
