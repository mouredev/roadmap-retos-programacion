/* Función saludar */

function saludar(name) {
    console.log(`¡Hola ${name}!`);
}

saludar("Marcos") // Imprime en consola: "Hola Marcos"



/* Función suma */

function sumar(a,b) {
    let resultado = a + b;
    console.log(resultado);
}

sumar(4,5) // Imprime en consola: 9
sumar(35,77) // Imprime en consola: 112
sumar(1,45) // Imprime en consola: 46
sumar(123,100) // Imprime en consola: 223
sumar(4,7) // Imprime en consola: 11
sumar(-8,-9) // Imprime en consola: -17



/* Función para determinar si un número es primo */

function esPrimo(num) {
    if (num % 2 === 0) {
        console.log(`El número ${num} es primo`);
    } else console.log(`El número ${num} no es primo`);
}

esPrimo(45) // Imprime en consola: "El número 45 no es primo"
esPrimo(222) // Imprime en consola: "El número 222 es primo"
esPrimo(1658) // Imprime en consola: "El número 1658 es primo"
esPrimo(11) // Imprime en consola: "El número 11 no es primo"
esPrimo(732) // Imprime en consola: "El número 732 es primo"
esPrimo(12) // Imprime en consola: "El número 12 es primo"



/* Función para convertir la cadena de texto en mayúscula */

function cadenaDeTexto(string) {
    console.log(string.toUpperCase());
}

cadenaDeTexto("¿Hola que tal?") // Imprime en consola: ¿HOLA QUE TAL?
cadenaDeTexto("otorrinolaringología") // Imprime en consola: OTORRINOLARINGOLOGÍA
cadenaDeTexto("aBcDeFg") // Imprime en consola: ABCDEFG



/* Función para encontrar el máximo en un array */

function maximoValor(arr) {

    let max = 0;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    console.log(`El valor máximo es ${max}`);

}

maximoValor([95, 77, 45, 6, 333, 200]) // Imprime en consola "El valor máximo es 333"
maximoValor([100, 99, 88, 45, 54]) // Imprime en consola "El valor máximo es 100"
maximoValor([9, 8, 7, 6, 0, 7, 6]) // Imprime en consola "El valor máximo es 9"
maximoValor([0, 0, 0, 1, 1, 0]) // Imprime en consola "El valor máximo es 1"



/* Función dentro de otra función */

function funcionExterna() {
    function funcionInterna () {
        console.log("Esta es una función dentro de otra función");
    }

    funcionInterna()

}

funcionExterna() // Imprime en consola "Esta es una función dentro de otra función"


/* Dificultad extra */

function texto(string1, string2) {

    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(string1 + string2);
            contador++;
        } else if (i % 3 === 0) {
            console.log(string1);
            contador++;
        } else if (i % 5 === 0) {
            console.log(string2)
            contador++;
        } else console.log(i);
    }

    return `La cantidad de veces que se imprimió un número es: ${contador}`;
}

console.log(texto("Soda","Stereo"));