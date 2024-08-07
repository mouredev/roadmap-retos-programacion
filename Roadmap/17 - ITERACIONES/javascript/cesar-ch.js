/*
    *  #17 ITERACIONES
*/

const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// 1. Bucle for
for (let i = 0; i < numeros.length; i++) {
    console.log(numeros[i]);
}

// 2. Bucle for in
for (const i in numeros) {
    console.log(numeros[i]);
}

// 3. Bucle forEach
numeros.forEach((numero) => {
    console.log(numero);
});

/*
    * DIFICULTAD EXTRA
*/

// 4. Bucle for of 
for (const numero of numeros) {
    console.log(numero);
}

// 5. Bucle while
let i = 0;
while (i < numeros.length) {
    console.log(numeros[i])
    i++
}

// 6. Bucle do while
let j = 0;
do {
    console.log(numeros[j]);
    j++;
} while (j < numeros.length)

// 7. Bucle map 
numeros.map((numero) => {
    console.log(numero);
})

// ...