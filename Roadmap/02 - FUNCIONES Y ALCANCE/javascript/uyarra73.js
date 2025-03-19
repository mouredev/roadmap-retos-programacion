// Función sin parámetros ni retorno
function saludo() {
    console.log("Hola, JavaScript!");
}

// Función con un parámetro
function saludoNombre(name) {
    console.log("Hola, " + name + "!");
}

// Función con varios parámetros
function suma(a, b) {
    console.log(a + b);
}

// Función con retorno
function producto(a, b) {
    return a * b;
}

console.log(producto(2,3));

// Funciones dentro de funciones
function funcionExterior(x) {
    function funcionInterior(y) {
        return x + y;
    }

    return funcionInterior;
}

let addSix = funcionExterior(6);
console.log(addFive(3)); // 8

// Uso de funciones nativas
let numeros = [1, 2, 3, 4, 5];
let numerosCuadrado = numeros.map(function(number) {
    return number * number;
});

console.log(numerosCuadrado); // [1, 4, 9, 16, 25]

// Variables locales y globales
let variableGlobal = 'Soy global';
console.log(variableGlobal);
function imprimirVariable() {
    let variableLocal = "Soy local";
    return variableGlobal + ". " + variableLocal; // "Soy global. Soy Local"
}
console.log(imprimirVariable());
console.log(variableLocal);


// Ejercicio extra

/* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. */


function exercise(str1, str2) {
    let contador = 0;
    let arr = []
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            arr.push(`${str1} y ${str2}`);
        } else if (i % 3 === 0) {
            arr.push(str1);
        } else if (i % 5 === 0) {
            arr.push(str2);
        } else {
            arr.push(i);
            contador++;
        }
    }
    return `${arr} Se han imprimido un total de ${contador} numeros.`;
}

console.log(exercise("Multiplo de 3", "Multiplo de 5"));
