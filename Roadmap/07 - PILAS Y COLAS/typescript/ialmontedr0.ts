/**
 * Introduccion y recuperacion de elementos de pilas y colas, con array 
 */
 
// Arreglo Global
let arreglo: number[] = [1, 2, 3, 4, 5];

// PILAS (STACK)
console.log(`Arreglo de numeros: ${arreglo}`);

// Insercion de elemento a la lista
arreglo.push(6);
console.log(`Arreglo de numeros con nuevo digito: ${arreglo}`);

// Recuperar el ultimo elemento de la lista
let ultimoElemento = arreglo.push;
console.log(`Ultimo elemento: ${ultimoElemento}`);

// Ver el ultimo elemento de la lista sin eliminarlo
let lastItem = arreglo[arreglo.length - 1];
console.log(`Ultimo elemento sin eliminarlo: ${lastItem}`);

// Verificar si la pila esta vacia
function isEmpty(): boolean {
    return arreglo.length === 0;
}
console.log(`Verificando si la pila esta vacia: ${isEmpty()}`);

// Obtener el tamano de la pila
const size = (): number => {
    return arreglo.length;
}
console.log(`Obteniendo el tamano de la pila: ${size()}`);

// Eliminacion de elemento de la pila
// Eliminar el ultimo elemento de la pila
arreglo.pop();
console.log(`Arreglo de numeros sin el ultimo elemento de la lista: ${arreglo}`);

// Eliminar todosl os elementos de la pila
arreglo = [];
console.log(`Arreglo vacio: ${arreglo}`)


// COLAS (QUEUE)
// Insertar un elemento en la Cola
arreglo.push(1);
console.log(arreglo);

// Recuperar el elemento en la Cola
let primerElemento = arreglo.shift();
console.log(`Primer elemento: ${primerElemento}`);

// Verificar si la cola esta vacia
function isEmptyQueue(): boolean {
    return arreglo.length === 0;
}
console.log(`Verificando si la cola esta vacia: ${isEmptyQueue()}`);

// Obtener el tamano de la cola
const sizeQueue = (): number => {
    return arreglo.length;
}
console.log(`Obteniendo el tamano de la cola: ${sizeQueue()}`);

// Eliminar un elemento de la Cola
arreglo.shift();
console.log(`Cola sin el primer elemento: ${arreglo}`);

// Eliminar todos los elementos de la Cola
arreglo = [];
console.log(`Cola vacia: ${arreglo}`);

// Ejercicio Extra: Simulacion de navegador web
let webs: string[] = ["Google", "Yahoo", "Facebook", "Twitter", "Instagram"];

// Simulacion de navegacion a una web
function navegarA(web: string): void {
    console.log(`Navegando a: ${web}`);
    webs.push(web);
    console.log(`Historial de navegacion: ${webs}`);
    console.log();
    imprimeHistorialWeb();
    imprimeWebActual();
    imprimeBotonesAdelanteAtras();
    console.log();
    imprimeDocumentoCola();
    console.log();
    imprimeCola();
    console.log();
    imprimeDocumentoActual();
    imprimeBotonesImprimir();
    console.log();
}

function imprimeHistorialWeb(): void {
 console.log("Historial de navegacion:");
 webs.forEach((web, index) => {
     console.log(`${index + 1}. ${web}`);
 });
 console.log();
}

function imprimeWebActual(): void {
    const currentWebIndex = webs.length - 1;
    console.log(`Pagina actual: ${webs[currentWebIndex]}`);
    console.log();
}

function imprimeBotonesAdelanteAtras(): void {
    const currentWebIndex = webs.length - 1;
    const hasBackButton = currentWebIndex > 0;
    const hasForwardButton = currentWebIndex < webs.length - 2;
    console.log(`Botones de retroceso y avance: ${hasBackButton? "Habilitado" : "Deshabilitado"} - ${hasForwardButton? "Habilitado" : "Deshabilitado"}`);
    console.log();
}

function imprimeDocumentoCola(): void {
    console.log("Documentos en espera:");
    webs.forEach((web, index) => {
        console.log(`${index + 1}. ${web}`);
    });
    console.log();
}

function imprimeCola(): void {
    console.log("Impresiones en espera:");
    webs.forEach((web, index) => {
        console.log(`${index + 1}. ${web}`);
    });
    console.log();
}

function imprimeDocumentoActual(): void {
    const currentWebIndex = webs.length - 1;
    console.log(`Documento actual: ${webs[currentWebIndex]}`);
    console.log();
}

function imprimeBotonesImprimir(): void {
    console.log("Botones de impresion:");
    webs.forEach((web, index) => {
        console.log(`${index + 1}. Imprimir ${web}`);
    });
    console.log();
}