//PILAS (STACK)
var pila = [1, 2, 3, 4, 5];
console.log('pila original', pila);

pila.push(6);
console.log('agregar elemento a la pila en la ultima posicion', pila);

pila.pop();
console.log('eliminar el ultimo elemento agregado a la pila', pila);


// *COLAS (QUEUE)
var cola = ['b', 'c', 'd', 'e', 'f'];
console.log('cola original', cola);

cola.unshift('a');
console.log('agregar elemento a la cola en la ultima posicion (izquierda)', cola);

cola.pop();
console.log('eliminar el ultimo elemento de la cola (elementos que fue agregado primero)', cola);


//  *   DIFICULTAD EXTRA
//  *   Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
//  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
//  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
//  *   interpretan como nombres de documentos.

var documentos = ['cv.txt', 'examen.txt', 'test.txt', 'comandos.txt'];
var impresora = [];

console.log('agregando a impresora');
for (var i = 0; i < documentos.length; i++) {
    impresora.unshift(documentos[i]);
    console.log('Cola de impresion: ', impresora);
}

console.log('imprimiendo');
do {
    impresora.pop();
    console.log('impresiones pendientes: ', impresora);
} while (impresora.length > 0);


//  *   Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
//  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
//  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
//  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
//  *   el nombre de una nueva web.
var historial = [];
var paginaActual = 0;

var agregarPagina = function (web) {
    if (historial.length > 0) {
        paginaActual++;
    }
    historial.push(web);
};

var atras = function () {
    console.log(historial[paginaActual - 1]);
};

var adelante = function () {
    console.log(historial[paginaActual + 1]);
};

agregarPagina('test.com');
console.log(historial);

agregarPagina('new.com');
console.log(historial);

atras();
console.log(historial);
