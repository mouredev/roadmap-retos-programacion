
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 */


// SOLUCION:

console.log(`//////////////////////      Asignacion por valor:     ////////////////////`)

// Copiamos el valor de la variable y si modificamos la copia la original no cambia
// Aplica para tipos primitivos como .... numeros, strings, booleanos, etc

let a = 28
let b = a
b = 30
console.log('a: ', a)
console.log('b: ', b)
//En este caso a y b estan en distintas posiciones de memoria, por eso cambiar b no afecta a la variable a.


console.log(`//////////////////////      Asignacion por Referencia:     ////////////////////`)

// Copiamos la referencia (direccion en memoria). Si modificamos una copia, la original tambien cambia en este caso.
// Esto aplica para tipo no primitivos como objetos, arrays, funciones, etc

let vehiculo1 = { nombre: 'Tesla', año: 2010 }
let vehiculo2 = vehiculo1
vehiculo2.año = 2000
console.log('vehiculo1: ', vehiculo1)
console.log('vehiculo2: ', vehiculo2)
// En este caso ambas variables (persona1 y persona2) apuntan al mismo objeto en memoria, por ende cambiar cualquiera de las 2 tambien afectara a la otra.


console.log(`//////////////////////      Funcion "por Valor":     ////////////////////`)

function cambiarEdad(edad) { // <-- aqui el parametro edad recibe una copia del valor de numero. (Justamente por eso el cambio dentro de la funcion no efecto a la variable original)
    edad = edad + 1
    console.log('Dentro de la funcoin: ', edad)
}

let numero = 28
cambiarEdad(numero)

console.log('Fuera de la funcion: ', numero)


console.log(`//////////////////////      Funcion "por Referencia":     ////////////////////`)

function cambiarEdad(x) { // <--- El parametro x recibe una referencia al mismo objeto que num, por eso al modificar p modificas tambien el objeto original.
    x.edad = 29
    console.log('Dentro de la funcion: ', x)
}

let num = { edad: 50 }
cambiarEdad(num)

console.log('Fuera de la funcion: ', num)


////////////////////////////////////////////////// PARA EVITAR CAMBIAR EL ORIGINAL: podemos copiar un objeto o un array para romper la referencia

let mascotaA = { nombre: 'Sally', edad: 10 }
let mascotaB = { ...mascotaA } // una copia usando spread operator

mascotaB.nombre = 'Camilo'

console.log(mascotaA)
console.log(mascotaB)



/*
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*/

console.log(`//////////////////////      DIFICULTAD EXTRA:     ////////////////////`)


//FUNCION POR VALOR:
function programaValor(val1, val2) {
    let valor = val1
    val1 = val2
    val2 = valor

    return [val2, val1]
}

let arrVal1 = 10
let arrVal2 = 20

let [newArrVal2, newArrVal1] = programaValor(arrVal1, arrVal2)

console.log(arrVal1)
console.log(arrVal2)
console.log(newArrVal1)
console.log(newArrVal2)



//FUNCION POR REFERENCIA:
function programaReferencia(param1, param2) {
    let nuevo = param1.nombre
    param1.nombre = param2.nombre
    param2.nombre = nuevo
    return [param2, param1]
}

let arg1 = { nombre: 'Imanol' }
let arg2 = { nombre: 'Maximiliano' }

let [newArg2, newArg1] = programaReferencia(arg1, arg2)

console.log(arg1)
console.log(arg2)
console.log(newArg1)
console.log(newArg2)




