// Variables de asignacion por valor - PRIMITIVOS
// Se crea una copia del valor original
let numero1 = 1;
let letra1 = 'A';
let verdad1 = true;
let indefinido1 = undefined;
let nulo1 = null;

let numero2 = numero1;
let letra2 = letra1;
let verdad2 = verdad1;
let indefinido2 = indefinido1;
let nulo2 = nulo1;

// Variables de asignacion por referencia
// Ambas variables apuntan al mismo espacio en la memoria
let arreglo1 = [1, 2, 3];
let objecto = {nombre: 'Jeronimo'};
let esFuncion = function funcion(){}

let arreglo2 = arreglo1;    // arreglo2 = [1, 2, 3]
arreglo2.pop();             // Se modifica el lugar en la memoria
console.log(arreglo1)       // [1, 2]
console.log(arreglo2)       // [1, 2]

////////////////////////////////////////////////////
//                  EXTRA

function porValor(value1, value2){
    let temp = value1;
    value1 = value2
    value2 = temp;
    return [value1, value2];
}
function porReferencia(ref1, ref2){
    let temp = ref1;
    ref1 = ref2;
    ref2 = temp;
    return [ref1, ref2]
}


let primerV = 'Hola';
let segV = 2;
let primerRef = [1, 2, 3];
let segRef = [4, 5, 6];

let newFirstValor = porValor(primerV, segV)[0];
let newSecondValor = porValor(primerV, segV)[1];
let newFirtsRef = porValor(primerRef, segRef)[0];
let newSecondRef = porValor(primerRef, segRef)[1];

console.log(`
    POR VALOR 
    original = ${primerV}, ahora es ${newFirstValor};
    original = ${segV}, ahora es ${newSecondValor};
    
    POR REFERENCIA
    original = ${primerRef}, ahora es ${newFirtsRef};
    original = ${segRef}, ahora es ${newSecondRef};
    `)
