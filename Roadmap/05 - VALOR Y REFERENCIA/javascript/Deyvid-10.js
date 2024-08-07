//  Ejemplos de asignación de variables "por valor" y "por referencia"

// Por valor
let numero = 1
let numero2 = numero
let cadena = "texto"
let cadena2 = cadena

numero2 = 2
cadena2 = "palabra"

console.log(numero);
console.log(numero2);
console.log(cadena);
console.log(cadena2);

// Por referencia
let array = [1, 2, 3]
let array2 = array
let objeto = {a: 1, b:2, c:3}
let objeto2 = objeto

array2.push(4)
objeto2["d"] = 4

console.log(array);
console.log(array2);
console.log(objeto);
console.log(objeto2);

// Funcion por valor 
let numero3 = 3

function porValor()
{
    let numero4 = numero3
    numero4 = 4
    console.log(numero4);
}

porValor()
console.log(numero3);

// Funcion por referencia
let array3 = [1, 2, 3]
function porReferencia()
{
    let array4 = array3
    array4.push(4)
    console.log(array4);
}

porReferencia()
console.log(array3);
