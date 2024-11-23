// Ejemplo de funciones básicas en JavaScript

// Función sin parámetros ni retorno
function saludo() {
    console.log("Hola, mundo!");
}
saludo();

// Función con un parámetro
function saludar(nombre) {
    console.log(`Hola, ${nombre}!`);
}
saludar("Juan");

// Función con varios parámetros
function suma(a, b) {
    console.log(`La suma de ${a} y ${b} es ${a + b}`);
}
suma(5, 10);

// Función con retorno
function multiplicar(a, b) {
    return a * b;
}
let resultadoMultiplicacion = multiplicar(3, 4);
console.log(`El resultado de la multiplicación es: ${resultadoMultiplicacion}`);

// Función dentro de otra función
function operacionPrincipal(a, b) {
    function resta(x, y) {
        return x - y;
    }
    console.log(`La resta de ${a} y ${b} es ${resta(a, b)}`);
}
operacionPrincipal(10, 7);

// Uso de una función ya creada en el lenguaje
let numeroAleatorio = Math.random(); // Función para generar un número aleatorio
console.log(`Número aleatorio generado: ${numeroAleatorio}`);

// Variables locales y globales
let globalVariable = "Soy global";

function pruebaVariables() {
    let localVariable = "Soy local";
    console.log(globalVariable); // Acceso a variable global
    console.log(localVariable);  // Acceso a variable local
}
pruebaVariables();
// console.log(localVariable); // Esto dará un error porque localVariable es local a la función

// DIFICULTAD EXTRA
function multiplesDeTexto(cadena1, cadena2) {
    let conteo = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${cadena1}${cadena2}`);
        } else if (i % 3 === 0) {
            console.log(cadena1);
        } else if (i % 5 === 0) {
            console.log(cadena2);
        } else {
            console.log(i);
            conteo++;
        }
    }
    return conteo;
}

let vecesImpreso = multiplesDeTexto("Fizz", "Buzz");
console.log(`El número de veces que se imprimió un número es: ${vecesImpreso}`);
