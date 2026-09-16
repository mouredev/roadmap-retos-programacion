/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
*/

// 1)
for( let i = 1; i < 11; i ++) {
    console.log("1)",i)
}

// 2)
let i = 1
while(i < 11) {
    console.log("2)",i)
    i ++
}

// 3)
const numeros = [1,2,3,4,5,6,7,8,9,10]
for(numero of numeros ) {
    console.log("3)",numero)
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/

// 4)
let e = 1
do {
    console.log("4)",e)
    e++
}while(e < 11)

// 5)
for(const indice in numeros) {
    console.log("5)",numeros[indice]) // Cuando no conoces el valor de la propiedad accedemos mediante corchetes [], si la conoces se accede mediante .nombreDeLaPropiedad
}

// 6)
numeros.forEach(numero => console.log("6)", numero))

// 7)
numeros.map(numero => console.log("7)", numero))

// 8)
numeros.filter(numero => {
    console.log("8)",numero)
    return true
})

// 9)
numeros.reduce((acumulador, numero) => {
    console.log("9)",numero)
    return acumulador
}, 0)

// 10)

const iterador = numeros[Symbol.iterator]()
let resultado = iterador.next()

while(!resultado.done) {
    console.log("10)", resultado.value)
    resultado = iterador.next()
}