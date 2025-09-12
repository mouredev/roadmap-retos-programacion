// stacks - LIFO last out, pila

let stack = [];
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack);
stack.pop();
console.log(stack);

function peek(stack) {
  return stack[stack.length - 1];
}
console.log(peek(stack));

// stack fifo first out cola queue
let cola = [];
cola.push(11);
cola.push(12);
cola.push(13);
console.log(cola);
cola.shift();
console.log(cola);

//Extra

// - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
//  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
//  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
//  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
//  *   el nombre de una nueva web.

//pila - last in first out 
//la pila de estack siempre elimina al ultimo , no guarda el elemento eliminado, solo puedes agregar y eliminar en un sentido

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});


//sigue bajando amigo ==================================>>>>>>>>>>>

// function web() { //primer intento
//     let stack = []; // no me guardaba el push :(

//   rl.question(
//     "añade una url , o interactua con las palabras adelante/atras/historial/salir : ",
//     (palabra) => {
      
    //   if (palabra == "salir") {
    //     console.log("estas saliendo de el programa");
    //     return rl.close();
    //   } else if (palabra == "adelante") {
    //     console.log("adelante");
    //     web();
    //   } else if (palabra == "atras") {
    //     console.log(" pagina de  atras");
    //     web();
    //   } else if (palabra == "historial") {
    //     console.log(stack);
    //     web();
    //   } else {
    //     stack.push(palabra);
    //     console.log(` bienvenido a la pagina web :  ${palabra} ${stack}`);
    //     web();
    //   }
//     }
//   );
// }

// web();


function webNavigation() {
    const stack = [];
  
    function processInput(action) {
      if (action === 'salir') {
        console.log('Saliendo del navegador web.');
        rl.close();
        return;
      } else if (action === 'adelante') {
        console.log('La función adelante no está implementada no se puede por que el pop elimina el ultimo elemeto .');
      } else if (action === 'atrás') {
        if (stack.length > 0) {
          const poppedUrl = stack.pop();
          console.log(`Has regresado a la web: ${poppedUrl}`);
        } else {
          console.log('No hay páginas anteriores en el historial.');
        }
      } else {
        stack.push(action);
        console.log(`Has navegado a la web: ${action}`);
      }
    }
  
    function promptUser() {
      rl.question('Añade una url o interactúa con palabras adelante/atrás/salir: ', (action) => {
        processInput(action);
        if (action !== 'salir') {
          promptUser(); // Llamada recursiva
        }
      });
    }
  
    promptUser();
  }
  
  // webNavigation();



//   - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
//  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
//  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
//  *   interpretan como nombres de documentos.

function impresora () {

  let archivos = []

  

    function imprimir (respuesta) {
      if(respuesta === 'salir'){
        console.log('saliendo de la impresora')
        rl.close()
        return;
      }else if(respuesta === 'imprimir') {
        if(archivos.length <=0 ){
          console.log('esta vacio la impresora introduce un archivo')
        }else{
          const archivoAImprimir = archivos.shift()
          console.log(archivoAImprimir + 'se esta imprimiendo')
        }
        
      }else {
        console.log(`${respuesta} fue añadiada a la cola de la impresora`)
        archivos.push(respuesta)
        console.log(archivos)
      }
    }

    function archivosEnCola () {
    rl.question('añade un documento  o selecciona  imprimir/salir  : ', (respuesta) => {

      imprimir(respuesta)
      if(respuesta !== 'salir'){
        archivosEnCola()
      }

    })

  }

  archivosEnCola()

}

impresora()