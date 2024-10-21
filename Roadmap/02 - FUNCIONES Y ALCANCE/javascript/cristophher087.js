/*
¿Qué es una función?

-Es un bloque de codigo que se puede definir una vez y ejecutar en multiples ocaciones.
*/

//sintaxis basica 

function nombreFuncion(parámetro1, parámetro2) {
    // Código a ejecutar
    return resultado; // Opcional
}
/*
Función Declarativa

Se define con la palabra reservada function. Estas funciones se elevan al principio del contexto gracias al hoisting, por lo que pueden ser llamadas antes de ser declaradas.
*/
function suma(a, b) {
    return a + b;
}

console.log(suma(2, 3)); //Salida: 5

/*
Función Anónima

No tiene un nombre asignado y se suele usar como expresión o argumento. Por ejemplo:
*/
const resta = function (a, b) {
    return a - b;
};

console.log(resta(5, 2)); // Salida: 3

/*
Funciones Flecha (Arrow Functions)

Introducidas en ES6, tienen una sintaxis más compacta y no tienen su propio this. Son útiles para funciones cortas.
*/
const multiplicar = (a, b) => a * b;
console.log(multiplicar(3, 4)); // Salida: 12

//Arrow Functions sin parametros
const saludar = () => console.log("¡Hola!");
saludar(); // Salida: ¡Hola!

//Arrow Functions con un solo parámetro (paréntesis opcionales)
const cuadrado = x => x * x;
console.log(cuadrado(5)); // Salida: 25
/**
 * Parametros y argumentos
 * Parametros:Variables que se definen en la declaración de la función.
 * Argumentos: Valores que se pasan al invocar la función.
 */

//Parámetros por defecto
/**
 * Si no se pasa un valor a un parámetro, podemos definir un valor por defecto.
 */
function saludar(nombre = "Visitante") {
    console.log(`Hola, ${nombre}`);
}
saludar(); // Salida: Hola, Visitante
saludar("Ana"); // Salida: Hola, Ana

/**
 * Parámetros Rest (...rest)
 * Permiten capturar un número indefinido de argumentos en un array.
 */
function sumarTodos(...numeros) {
    return numeros.reduce((total, num) => total + num, 0);
}
console.log(sumarTodos(1, 2, 3, 4)); // Salida: 10
/**
 * En este arreglo el argumento "...numeros"
 * nos dice que se capturan ilimitada cantidad 
 * de captura de parametros se puede ver que0
 * se ejecuta la funcion correctamente sumando 
 * todos los números
 */

/**
 * Retorno de valores con return
 * El uso de return permite devolver un valor 
 * al finalizar la ejecución de la función. 
 * Si no se usa, la función devuelve undefined.
 */
function doble(x) {
    return x * 2;
}
console.log(doble(4)); // Salida: 8

/**
 * Funciones de alto orden
 * Son funciones que reciben como argumento 
 * otra función o devuelven una función.
 */
function operar(a, b, operacion) {
    return operacion(a, b);
}
const suma = (x, y) => x + y;
console.log(operar(3, 4, suma)); // Salida: 7

/**
 * Scope y this
 * El scope (ámbito) determina la accesibilidad
 *  de variables en una función. Hay dos tipos
 *  principales de scope:
 * 
    * Global: Variables accesibles desde cualquier parte.
    * Local: Variables definidas dentro de una función.
* Uso de this
    * En las funciones tradicionales, this hace 
    * referencia al objeto que la llama.
    * En arrow functions, this no se enlaza al 
    * contexto de la función, sino al contexto 
    * superior donde se definió.
 */
const objeto = {
    nombre: "VisiónLux",
    mostrarNombre() {
        console.log(this.nombre);
    },
};
objeto.mostrarNombre(); // Salida: VisiónLux

//En cambio:
const objeto2 = {
    nombre: "Óptica Henrris",
    mostrarNombre: () => {
        console.log(this.nombre); // this se refiere al contexto global, no al objeto
    },
};
objeto2.mostrarNombre(); // Salida: undefined

/**
 * Funciones Asíncronas (async/await
 * Permiten manejar operaciones asincrónicas (promesas) de manera más clara.
 */
async function obtenerDatos() {
    const respuesta = await fetch("https://api.ejemplo.com");
    const datos = await respuesta.json();
    console.log(datos);
}
obtenerDatos();

//Uso de Promesas con Funciones
function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
esperar(2000).then(() => console.log("Han pasado 2 segundos"));

/**
 * Closures (Clausuras)
 * Un closure ocurre cuando una función interna recuerda las variables del entorno en el que fue creada, incluso después de que dicho entorno haya terminado.
 */
function crearContador() {
    let contador = 0;
    return function incrementar() {
        contador++;
        console.log(contador);
    };
}
const contador1 = crearContador();
contador1(); // Salida: 1
contador1(); // Salida: 2
/**
 * En este casi, par aeste ejemplo se define "contador = 0;" dentro de la función pero este no toma el valor 0 en el segundo llamado, toma el valor anterior
 */

/**
 * IIFE (Immediately Invoked Function Expression)

Son funciones que se ejecutan inmediatamente después de ser declaradas. Útiles para evitar la contaminación del scope global.
 */
(function () {
    console.log("Función ejecutada inmediatamente");
})();

/**
 * Funciones Recursivas

Una función es recursiva cuando se llama a sí misma. Se usa comúnmente para resolver problemas complejos que pueden descomponerse en subproblemas más pequeños.
 */
function factorial(n) {
    if (n === 0) return 1;
    return n * factorial(n - 1);
}
console.log(factorial(5)); // Salida: 120

/**
 * DIFICULTAD EXTRA
 */

var fizz = "";
var buzz = "";
function convertidorNumeros(fizz, buzz) {

    for (var i = 0; i >= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(`${fizz}${buzz}`);
        }
        if (i % 3 == 0) {
            console.log(`${fizz}`);
        }
        if (i % 5 == 0) {
            console.log(`${buzz}`);
        }
        else {
            console.log(i);
        }
    }
}

convertidorNumeros("Fizz", "Buzz");
