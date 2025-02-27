/* 🔥EJERCICIO:
Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
números del 1 al 10 mediante iteración.
*/
// * 1. Bucle for tradicional 
console.log("Mecanismo 1: Bucle for");
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

// * 2. Bucle while
console.log("\nMecanismo 2: Bucle while");
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

// * 3. Método forEach con un array
console.log("\nMecanismo 3: forEach con un array");
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
numeros.forEach((numero) => {
    console.log(numero);
});

/* 🔥 DIFICULTAD EXTRA (opcional):------------------------------------------------------------------------
Escribe el mayor número de mecanismos que posea tu lenguaje
para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/
// * 4.  Bucle do...while
console.log("\nMecanismo 4: Bucle do...while");
let j = 1;
do {
    console.log(j);
    j++;
} while (j <= 10);

// * 5. Método map con un array
console.log("\nMecanismo 5: map con un array");
const numerosMap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
numerosMap.map((numero) => {
    console.log(numero);
});

// * 6. Recursión
console.log("\nMecanismo 6: Recursión");
function imprimirNumeros(n) {
    if (n > 10) return;
    console.log(n);
    imprimirNumeros(n + 1);
}
imprimirNumeros(1);

// * 7. Generadores (function*)
console.log("\nMecanismo 7: Generadores");
function* generarNumeros() {
    for (let i = 1; i <= 10; i++) {
        yield i;
    }
}
const generador = generarNumeros();
for (const numero of generador) {
    console.log(numero);
}

// * 8. Método reduce con un array
console.log("\nMecanismo 8: reduce con un array");
const numerosReduce = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
numerosReduce.reduce((_, numero) => {
    console.log(numero);
    return null;
}, null);

// * 9. Iterador personalizado (Symbol.iterator)
console.log("\nMecanismo 9: Iterador personalizado");
const iterable = {
    [Symbol.iterator]() {
        let i = 1;
        return {
            next() {
                if (i <= 10) {
                    return { value: i++, done: false };
                } else {
                    return { done: true };
                }
            },
        };
    },
};
for (const numero of iterable) {
    console.log(numero);
}

// * 10. Promesas encadenadas
console.log("\nMecanismo 10: Promesas encadenadas");
let promesa = Promise.resolve(1);
for (let i = 1; i <= 10; i++) {
    promesa = promesa.then((valor) => {
        console.log(valor);
        return valor + 1;
    });
}