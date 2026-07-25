//Ejemplos de funciones 
// 1. Sin parámetros ni retorno
function saludar() {
    console.log("¡Hola, JavaScript!");
}

// 2. Con parámetros pero sin retorno
function saludarPersona(nombre) {
    console.log("Hola, " + nombre);
}

// 3. Con parámetros y retorno
function sumar(a, b) {
    return a + b;
}

// 4. Función flecha
const restar = (a, b) => a - b;

// 5. Función flecha con parámetros por defecto
const multiplicar = (a, b = 1) => a * b;

// 6. Función flecha con múltiples líneas
const dividir = (a, b) => {
    if (b === 0) {
        throw new Error("No se puede dividir por cero");
    }
    return a / b;
};

// 7. Función flecha con parámetros rest
const sumarTodos = (...numeros) => {
    return numeros.reduce((acumulador, numero) => acumulador + numero, 0);
};

// 8. Función flecha con parámetros spread
const duplicarTodos = (numeros) => {
    return numeros.map(numero => numero * 2);
};

// 9. Función flecha con parámetros por defecto y spread
const sumarConSpread = (a, b, ...numeros) => {
    return a + b + numeros.reduce((acumulador, numero) => acumulador + numero, 0);
};

// 10. Función flecha con parámetros por defecto y rest
const restarConRest = (a, b = 0, ...numeros) => {
    return a - b - numeros.reduce((acumulador, numero) => acumulador + numero, 0);
};

//funcion dentro de otra funcion
function funcionExterna() {
    console.log("Estoy en la externa");

    function funcionInterna() {
        console.log("Estoy en la interna");
    }

    funcionInterna(); // Se llama dentro
}
funcionExterna(); // Se llama fuera

//variables globales y locales
let variableGlobal = "Soy global";

function pruebaScope() {
    let variableLocal = "Soy local";
    console.log(variableGlobal); // Funciona
    console.log(variableLocal);  // Funciona
}

pruebaScope();
// console.log(variableLocal); // ¡ERROR! No existe fuera de la función 

//retos
function ejercicioExtra(texto1, texto2) {
    let contadorNumeros = 0;

    for (let i = 1; i <= 100; i++) {
        // ¿Es múltiplo de 3 y de 5? (15, 30, 45...)
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(texto1 + texto2);
        }
        // ¿Es múltiplo de 3?
        else if (i % 3 === 0) {
            console.log(texto1);
        }
        // ¿Es múltiplo de 5?
        else if (i % 5 === 0) {
            console.log(texto2);
        }
        // Si no es ninguno de los anteriores
        else {
            console.log(i);
            contadorNumeros++; // Sumamos uno al contador
        }
    }

    return contadorNumeros;
}

// Para probarlo:
let resultado = ejercicioExtra("Fizz", "Buzz");
console.log("Veces que se imprimió un número: " + resultado);