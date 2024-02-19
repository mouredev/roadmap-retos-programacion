/*
 * EJERCICIO:
 * DIFICULTAD EXTRA (opcional):

 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

// <--- Pila --->
let stack = [];

// introducción de datos a la pila
// se puede aplicar directo sin la funcion. stack.push(element);
function push(element) {
  stack.push(element);
}
push(1); // [1]
console.log(stack);
push(2); // [1, 2]
console.log(stack);

// recuperar o eliminar elemento
// elimina el ultimo
function pop() {
  if (stack.length === 0) {
    console.log('El stack esta vació');
    return null;
  }
  return stack.pop();
}
pop(stack)
console.log(stack); // [1]

// <--- Cola --->
let queue  = [];

function enqueue(element) {
    queue.push(element);
}
enqueue(10)
console.log(queue) // [10]
enqueue(20)
console.log(queue)// [10, 20]

function dequeue() {
    if (queue.length === 0) {
        console.log("La cola está vacía");
        return null;
    }
    return queue.shift();
}

dequeue(queue)
console.log(queue)// [20]
dequeue(queue)
console.log(queue)//[]

// * DIFICULTAD EXTRA (opcional):
//<--- historyStack --->

// Creamos una pila vacía para almacenar las páginas web
let historialStack = [];

function navegador(url){
    console.log("Navegando a ",url)
    historialStack.push(url)
}
// function para retrocedes
function goBack(){
    if(historialStack.length > 1){
        historialStack.pop()
        let paginaAnterior = historialStack.pop()
        console.log("Regresando a:", paginaAnterior)
        historialStack.push(paginaAnterior)
    }else{
        console.log("No hay pagina que regresar")
    }
}

function goNext() {
    if (historialStack.length > 1) {
        historialStack.pop
        let nextPage = historialStack.pop();
        console.log("Avanzando a:", nextPage);
        historialStack.push(nextPage);
    } else {
        console.log("No hay página siguiente");
    }
}


function simuladorWeb(secuencias){
    secuencias.forEach(secuencia => {
        if(secuencia === "->"){
            goNext();
        } else if (secuencia === "<-"){
            goBack();
        } else {
            navegador(secuencia)
        }
    })
}
// Ejemplo de uso
let secuencias = ["www.google.com","->","www.Dofus.com", "->", "www.Dofus/foro.com", "->","www.Dofus/foro/1332","<-"];
simuladorWeb(secuencias);

// <---Cola--->

let cola = [];

function enqueueDocument(documento) {
    cola.push(documento);
}

function imprimirDocumento() {
    if (cola.length > 0) {
        let documentoAImprimir = cola.shift();
        console.log("Imprimiendo el documento:", documentoAImprimir);
        console.log("Secuencia de impresión:", JSON.stringify(cola));
    } else {
        console.log("No hay documentos en espera para imprimir");
    }
}

function simuladorImprimir(mandarImprimir) {
    mandarImprimir.forEach(mandar => {
        if (mandar === "imprimir") {
            imprimirDocumento();
        } else {
            enqueueDocument(mandar);
            console.log("Documento añadido:", mandar);
        }
    });
    console.log("// <---Cola--->");
}

let mandarImprimir = ["Documento1", "imprimir", "Documento2", "Documento3", "Documento4", "imprimir"];
console.log("<---------------------->");
simuladorImprimir(mandarImprimir);
