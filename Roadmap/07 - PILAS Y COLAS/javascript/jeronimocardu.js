const { read } = require('fs');
const { dot } = require('node:test/reporters');
const { serialize } = require('v8');

////////// PILA stacks (LIFO) Last In, First Out
let pila = [];

pila.push(3);      
// PUSH añade un elemento al final de la pila
pila.push(4);  
console.log(pila)

// POP elimina el utlimo elemento y lo guarda en una variable
let ultimoEliminado = pila.pop();   
console.log(`se eliminó {${ultimoEliminado}} ahora la pila: ${pila}`);


////////// COLA queue (FIFO) First In, First Out
let cola = [];
cola.push(1);
cola.push(2);
cola.push(3);
console.log(cola)

// SHIFT Elimina elementos de la primera posicion
cola.shift()
cola.shift()
console.log(cola)


////////////////////////////////////////////////////////////
//                  Extra
let readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let paginas = ['facebook', 'youtube', 'github', 'instagram', 'X', 'TikTok'];

function espera(){
    readline.question('\nPrecione ENTER para continuar...', tecla =>{
        if(tecla === ''){
            console.clear();
            searching();
        } else{
            espera();
        }
    })
}

function searching(){
    console.log('\n Usted esta en', paginas[0]);
    readline.question(`\nDesea ir 'Adelante' o 'Atras o Salir'?\n`, (respuesta) => {
        if(respuesta.toLowerCase() === 'adelante'){
            paginas.push(paginas.shift());
            searching();
        } else if(respuesta.toLowerCase() === 'atras'){
            paginas.unshift(paginas.pop());
            searching();
        } else if(respuesta.toLowerCase() === 'salir'){
            console.log('\nSaliendo...');
            imprimir();
        }else{
            console.log('\nOpcion no valida');
            espera();
        }
    })
}


let docs = []
function imprimir(){
    readline.question('Añada un documento o seleccione Imprimir/Salir: \n', (accion) => {
        if(accion.toLowerCase() === 'imprimir'){
            if(docs.length > 0){
                console.log('\nImprime: ',docs.shift());
                console.log(docs);
            } else console.log(docs);
            imprimir();
        } else if(accion.toLowerCase() === 'salir'){
            console.log('\nSaliendo...');
            readline.close();
        }
        else{
            docs.push(accion);
            console.log('\n', docs);
            imprimir();
        }
    })
}
searching();
imprimir();




