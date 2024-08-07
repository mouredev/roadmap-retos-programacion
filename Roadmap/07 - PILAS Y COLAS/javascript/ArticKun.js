

/*

⚡⚡ PILAS Y COLAS

En JavaScript, puedes utilizar un array 
para simular una pila. 


 PILAS / STACK
LAST IN FIRST OUT (LIFO)

Las operaciones principales en una pila 
son push (añadir un elemento en la cima) 
y pop (eliminar el elemento en la cima).


*/

//⚡ LIFO ============================== 
let pila = [];
// Añadir elementos a la pila
pila.push(1);
pila.push(2);
pila.push(3);
// Eliminar el elemento en la cima
//Y lo recuperamos en una variable
let elementoEliminado = pila.pop();
console.log(pila); // Resultado: [1, 2]
console.log(elementoEliminado); // Resultado: 3

/*

QUEUES / COLA 
FIRST IN FIRST OUT (FIFO)

Para implementar una cola en JavaScript, también 
puedes usar un array. Las operaciones principales 
en una cola son push (añadir un elemento al final) 
y shift (eliminar el primer elemento).

*/


//⚡ FIFO ============================== 

let cola = [];

// Añadir elementos a la cola
cola.push(1);
cola.push(2);
cola.push(3);

// Eliminar el primer elemento
//Y lo recuperamos en una variable
let primerElemento = cola.shift();

console.log(cola); // Resultado: [2, 3]
console.log(primerElemento); // Resultado: 1


/* DIFICULTAD EXTRA (opcional):

  - 1. Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
    Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
    el nombre de una nueva web.

  - 2. Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
    impresora compartida que recibe documentos y los imprime cuando así se le indica.
    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
    interpretan como nombres de documentos.

 */

    //1. PILA =========================================

    function simuladorNavegadorWeb() {
      const paginasVisitadas = [];
      let paginaActual = "";
  
      while (true) {
      const comando = prompt("Ingrese 'adelante', 'atrás' o el nombre de una nueva página (o 'salir' para terminar): ");
  
          if (comando.toLowerCase() === 'salir') {
              console.log("Saliendo del simulador del navegador.");
              break;
          } else if (comando.toLowerCase() === 'adelante') {
              if (paginaActual) {
                  console.log(`Avanzar a la página actual: ${paginaActual}`);
              } else {
                  console.log("No hay página actual");
              }
          } else if (comando.toLowerCase() === 'atrás') {
              if (paginasVisitadas.length > 0) {
                  const paginaAnterior = paginasVisitadas.pop();
                  console.log(`Retroceder a la página: ${paginaAnterior}`);
                  paginaActual = paginaAnterior;
              } else {
                  console.log("No hay páginas anteriores");
              }
          } else {
              paginasVisitadas.push(paginaActual);
              paginaActual = comando;
              console.log(`Ir a la página: ${paginaActual}`);
          }
      }
  };
  

// Ejecutar el simulador del navegador
  simuladorNavegadorWeb();
  
    
// 2. COLA ===================================================

const colaDocumentos = [];

const agregarDocumento = (documento) => {
    colaDocumentos.push(documento);
    console.log(`Documento '${documento}' agregado a la cola.`);
};

const imprimirDocumento = () => {
    if (colaDocumentos.length > 0) {
        const documentoAImprimir = colaDocumentos.shift();
        console.log(`Imprimiendo documento: '${documentoAImprimir}'`);
    } else {
        console.log("La cola de documentos está vacía. No hay documentos para imprimir.");
    }
};


while (true) {
    const comando = prompt("Ingrese 'imprimir' o el nombre de un nuevo documento (o 'salir' para terminar): ");

    if (comando.toLowerCase() === 'salir') {
        console.log("Saliendo del simulador de impresora compartida.");
        break;
    } else if (comando.toLowerCase() === 'imprimir') {
        imprimirDocumento();
    } else {
        agregarDocumento(comando);
    }
};


