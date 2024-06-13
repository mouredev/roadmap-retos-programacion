// array -----
const arr = [1,2,3,4,5,6,7,8,9,10]
// * - Añade un elemento al final.
arr. push(11)//11
console.log(arr)
// Añade un elemento al principio.
arr.shift()//1 delete
console.log(arr)
// Añade varios elementos en bloque al final.
arr.push(12, 13, 14) //agrego al final
console.log(arr)
// Añade varios elementos en bloque en una posición concreta.
arr.splice(0,0,-2,-1,0) //agrego en la posicion 0
console.log(arr)
// Elimina un elemento en una posición concreta.
arr.splice(8,1) //7 delete
console.log(arr)
// Actualiza el valor de un elemento en una posición concreta.
arr[5] = 10 
console.log(arr) 
arr.splice(0,0,-3)
console.log(arr)
// Comprueba si un elemento está en un conjunto = Comprobar si un elemento existe
console.log(arr.includes(10))
// - Elimina todo el contenido del conjunto.
arr.splice(0, arr.length);
console.log(arr)

// Extra

// * Muestra ejemplos de las siguientes operaciones con conjuntos:
// * - Unión.
const num1 = [1, 2, 3, 4, 5]
const num2 = [1, 2, 3, 4, 6, 7]

function union ( arr, arr2) {
let resultado = [...arr] //[1, 2, 3, 4, 5]
    for (const iterator of arr2) { // iteracion = [1[0], 2[1], 3[2], 4[3], 6[4], 7[5]]
        if(!resultado.includes(iterator) ){ //cuando includes sea false entonces agrega el numero
            resultado.push(iterator)
        }
        
    }
    return resultado
}
console.log(union(num1, num2))

// Intersección.
// La intersección de dos conjuntos (o arreglos) consiste en obtener un nuevo conjunto (o arreglo) que contenga solo los elementos que están presentes en ambos conjuntos (o arreglos) de entrada.
function interseccion (arr, arr2){
let resultado = []
for (const iterator of arr) {
    if(arr2.includes(iterator)){ // cuando includes sea true , agrega al []
        resultado.push(iterator)
    }
}
return resultado
}

console.log(interseccion(num1, num2))

// Diferencia 
// La diferencia de dos conjuntos (o arreglos) consiste en obtener un nuevo conjunto (o arreglo) que contenga los elementos que están presentes en el primer conjunto (o arreglo) pero no en el segundo.

function diferencia(arr, arr2) {
let resultado = []
for (const iterator of arr) {
    if(!arr2.includes(iterator)){ //false 
        resultado.push(iterator)
    }
}
    return resultado
}

console.log(diferencia(num1, num2))
console.log(diferencia(num2, num1))

// Diferencia simétrica.
//recorro el primer arr
function diferenciaSim (arr ,arr2) {
let resultado = []
for (const iterator of arr) {
    if(!arr2.includes(iterator)){ //false
        resultado.push(iterator)
    }
}
//recorre el segundo arr
for (const iterator of arr2) {
    if(!arr.includes(iterator)){//false
        resultado.push(iterator)
    }
}
return resultado
}

console.log(diferenciaSim(num1, num2))