// 👾 SCOPE
// Variable global
let variableGlobal = 'Soy global';

function ejemploVariables() {
    // Variable local dentro de la función
    let variableLocal = 'Soy local';

    console.log('Dentro de la función:');
    console.log('Variable local:', variableLocal);  // Accesible dentro de la función
    console.log('Variable global:', variableGlobal);  // Accesible dentro de la función

    // Modificando la variable local
    variableLocal = 'Modificada localmente';

    console.log('Después de modificar la variable local:');
    console.log('Variable local:', variableLocal);  // Accesible dentro de la función
    console.log('Variable global:', variableGlobal);  // Accesible dentro de la función
}
ejemploVariables();

console.log('Fuera de la función:');
// console.log('Variable local:', variableLocal); // Esto dará un error, ya que la variable local no es accesible fuera de la función
console.log('Variable global:', variableGlobal); // Accesible fuera de la función

// 👽 FUNCTIONS
// Las funciones en JavaScript pueden clasificarse de varias maneras según su comportamiento y uso.
// Funciones Declarativas
function declarativeSum(a, b) {
    return a + b;
}
console.log(`Función Declarativa: ${declarativeSum(5, 7)}`)

// Funciones de Expresión (anónimas)
const sum = function(a, b) {
    return a + b;
}
console.log(`Función Anonima/Expresión: ${sum(3, 4)}`)

// Funciones Flecha
const sumArrowFunction = (a, b) => {
    return a + b;
}
console.log(`Función Flecha(Arrow function): ${sumArrowFunction(2, 10)}`)

// Funciones Constructoras
function Persona(nombreCompleto, edad, trabajo, pais) {
    this.nombreCompleto = nombreCompleto;
    this.edad = edad;
    this.trabajo = trabajo;
    this.pais = pais;
}

const primeraPersona = new Persona('Julian Enrique Buitrago Charry', 17, 'Futuro Desarrollador de Software', 'Colombia');
console.log(`Función Constructora: ${primeraPersona}`);

// Funciones de Orden Superior: Aceptan funciones como argumentos o devuelven funciones. Ejemplos incluyen map, filter, reduce.

// Funciones Recursivas
function factorial(n) {
    // Caso base
    if (n === 0 || n === 1) {
        return 1;
    } else {
        // Llamada recursiva
        return n * factorial(n - 1);
    }
}
console.log(`Función Recursiva Factorial: ${factorial(6)}`);

// Funciones Anidadas
function exterior() { 
    let variableExterior = 'Exterior'; 
    function interior() {
        console.log(`Función Anidada Variable Exterior: ${variableExterior}`); 
    } 
    interior(); 
} 
exterior();

// Métodos de Objeto
const objeto = {
    metodo: () => {
        return 'Hola, este es un método';
    }
}
console.log(`Metodo de un Objeto: ${objeto.metodo()}`);

/* 👀 DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
- Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
- Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/

const retoSemanal = (primerParametro, segundoParametro) => {
    let contador = 0;
    for (let number = 1; number <= 100; number++) {
        if (number % 3 == 0 && number % 5 == 0) {
            console.log(`${primerParametro} en ${segundoParametro}.`)
            continue;
        } else if (number % 3 == 0) {
            console.log(`${primerParametro} Developer.`);
            continue;
        } else if (number % 5 == 0){
            console.log(`${segundoParametro}.`);
            continue;
        } else {
            contador++;
            console.log(number);
        }
    } 
    return contador;  
}

const primerTexto = 'Es divertido programar';
const segundoTexto = 'JavaScript';

cantidadNumeros = retoSemanal(primerTexto, segundoTexto);
console.log(`Cantidad de veces que se ha impreso un número en vez de los textos: ${cantidadNumeros}`);