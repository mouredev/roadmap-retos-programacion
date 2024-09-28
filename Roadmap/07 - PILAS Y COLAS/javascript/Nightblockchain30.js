// <<< STACK >>>
const stack = [1,2,3,4];
// Push new Element
stack.push(5);
console.log(stack);
// Pop LAST Element
stack.pop();
stack.pop();
stack.pop();
console.log(stack);


// <<< QUEUE >>>
const queue = [1,2,3,4,5]
// Push new Element
queue.push(6)
console.log(queue);
// Pop FIRST Element
queue.shift();
queue.shift();
queue.shift();
console.log(queue);

//  *   DIFICULTAD EXTRA
//  *   Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
//  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
//  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
//  *   interpretan como nombres de documentos.

var documentos = ['cv.txt', 'examen.txt', 'test.txt', 'comandos.txt'];
var impresora = [];

console.log("Agregando documentos a la cola de impresión..");
for (let i = 0; i < documentos.length; i++){
    impresora.unshift(documentos[i])
}
console.log(impresora);

console.log("Imprimiendo los documentos..");
do {
    impresora.pop();
    console.log(`Queda por imprimir [${impresora}]`);
} while (
    impresora.length > 0
)


//  *   Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
//  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
//  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
//  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
//  *   el nombre de una nueva web.

historial = [];
pagina_actual = 0;

let agregarWeb = function (web){
    if (historial.length > 0) {
        pagina_actual++;
    }
    historial.push(web)
}



let volverAtras = function(){
    console.log(historial[pagina_actual - 1]);
}

let adelantar = function(){
    console.log(historial[pagina_actual + 1]);
}

agregarWeb("www.google.com");
agregarWeb("www.ikea.com");
agregarWeb("www.marca.com");
console.log(historial);

volverAtras();


