//  *
//  * EJERCICIO:
//  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
//  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
//  * o lista (dependiendo de las posibilidades de tu lenguaje).

// Pila o stack LAST IN FIRST OUT
pila=[]
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.pop()
// console.log(pila);

// // Fila o queue FIRST IN FIRST OUT
pila=[]
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.shift()
// console.log(pila);

// DIFICULTAD EXTRA (opcional):
//  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
//  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
//  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
//  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
//  *   el nombre de una nueva web.  

let readline = require('readline')
let rl = readline.createInterface({ input: process.stdin, output: process.stdout });

atras=[]
adelante=[]

function navegar(){
    rl.question('Ingresa una url o escribe adelante para ir a la siguiente pagina, atras para ir a la anterior y salir para cerrar el programa ',(answer)=>{
        let ans=answer.trim().toLowerCase()
        switch(ans){
            case 'adelante':
                atras.push(adelante.pop())
                currentPage(atras)
                navegar()
                
                break
            case 'atras':
                if(isEmpty(atras)){
                    currentPage(atras)
                    navegar()
                    
                } else {
                    adelante.push(atras.pop())
                    currentPage(adelante)
                    navegar()
                    
                }
                break
            case 'salir':
                rl.close()
                
            default:
                adelante=[]
                atras.push(ans)
                currentPage(atras)
                navegar()
                
                break
        }
    })
    
}


function isEmpty(pila){
    return pila.length===0
}
function currentPage(pila){
    return isEmpty(pila) ? console.log("Estas en la pagina de inicio") : console.log(`Estas en la pagina ${pila[pila.length-1]}`);
    
    
}
// navegar()


// /*
// Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
// impresora compartida que recibe documentos y los imprime cuando así se le indica.
// La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
// interpretan como nombres de documentos.
// */

cola=[]

function imprimir(){

    printQueue()

    rl.question('Ingresa el documento o escribe imprimir para mostrarlos en pantalla: ',(answer)=>{
        let ans=answer.trim().toLocaleLowerCase()
        switch(ans){
            case 'imprimir':
                if(cola.length===0){
                    console.log('No hay elementos');
                    imprimir()
                } else {
                    for(let i=0;i<cola.length;i++){
                        console.log(cola[i]);
                    }
                    for(let i=0;i<=cola.length+1;i++){
                        cola.shift();
                    }
                    imprimir()
                }
                break
            case 'salir':
                console.log('El proceso ha terminado, hasta luego!');
                
                rl.close()
                break
            default:
                cola.push(ans)
                imprimir()
                break
        }


    })
    
}

function printQueue(){
    if (cola.length===0){
        console.log('No hay elementos para mostrar');
    }  else {
        console.log(`\n Cola de impresion`);
        cola.forEach(document =>{
            console.log(document);
        })
        
    }
}

imprimir()