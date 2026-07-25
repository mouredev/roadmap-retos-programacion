
// Pila/Stack → LIFO 
let listado = [1, 2, 3, 4, 5, 6];
// LI (Last In)
listado.push(9);
console.log(listado);
// FO (First Out)
listado.pop();
console.log(listado);

// Cola/Queue → FIFO
//FI (First In)
listado.push(7);
console.log (listado);
//FO (First Out)
listado.shift();
console.log(listado);

/* EJERCICIO:
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

/*1 - Pila + cadena de texto*/
/*Simular adelante/atrás navegador web. */

let navegadorWeb = ["Inicio"];
console.log(navegadorWeb.length)

function atras() {
    if(navegadorWeb.length <= 1){
        console.log("Hasta aquí llegaste");
    } else {
        navegadorWeb.pop()
        console.log(navegadorWeb);
    }
}

function adelante(site) {
    navegadorWeb.push(site);
    console.log(navegadorWeb);
}

adelante("Minijuegos");
atras();
adelante("Google Drive");
adelante("Elrellano.com");
atras();
atras();

/*2- Cola + Cadena de texto*/
/*Simular una cola de impresión */

let colaDeImpresion = ["Archivo 1", "Archivo 2", "Archivo 3"];

function imprimir(document) {
    if (colaDeImpresion >= 0){
        "No hay elementos por imprimir"
    } else {
        colaDeImpresion.push(document);
        console.log(`Se está imprimiendo el documento: "${colaDeImpresion[0]}". Se elimina de la cola.`)
        colaDeImpresion.shift();
        console.log(colaDeImpresion);
    }
}

imprimir("Archivo 4");
imprimir("If it bleeds");