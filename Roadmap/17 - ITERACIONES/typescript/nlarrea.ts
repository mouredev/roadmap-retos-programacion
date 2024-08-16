/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */


// OPTION 1

console.log('OPTION 1: for loop')

for (let num = 1; num <= 10; num++) {
    console.log(num)
}

// OPTION 2

console.log('OPTION 2: while loop')

let num: number = 1
while (num <= 10) {
    console.log(num)
    num++
}

// OPTION 3

console.log('OPTION 3: recursive function call')

function count(start: number, stop: number) {
    console.log(start)

    if (start >= stop) {
        return
    }

    count(start + 1, stop)
}

count(1, 10)


/*
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */


// En los ejemplos anteriores hemos mostrado 3 formas diferentes

// 4. Do-While

num = 1
do {
    console.log(num)
    num++
} while (num <= 10)
    
// Para seguir con otros ejemplos, creamos el siguiente array: [0, ..., 9]
const numbers: number[] = [...Array(10).keys()]

// 5. For Each

numbers.forEach(num => {
    console.log(num)
})

// 6. For in

for (const index in numbers) {
    console.log(numbers[index])  // -> index
}

// 7. For of

for (const num of numbers) {
    console.log(num)
}

// 8. Map

numbers.map(num => {
    console.log(num)
})