/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

console.log("===> Funciones básicas <===");

// Sin parámetros ni retorno
function greet() {
    console.log("Hola, JavaScript!");
}
greet();

// Con un parámetro
function greetPerson(name) {
    console.log(`Hola, ${name}!`);
}
greetPerson("Wilmer");

// Con varios parámetros
function add(a, b) {
    console.log(`La suma de ${a} y ${b} es ${a + b}`);
}
add(5, 3);

// Con retorno
function multiply(a, b) {
    return a * b;
}
const result = multiply(5, 3);
console.log(`El resultado de la multiplicación es ${result}`);

// Con varios parámetros y un valor por defecto
function greetDefault(name, greeting = "Hola") {
    console.log(`${greeting}, ${name}!`);
}
greetDefault("MoureDev");
greetDefault("Wilmer", "Hello");

// Con parámetros de longitud variable (rest parameters)
function printArgs(...args) {
    console.log("Argumentos variables (...args):");
    args.forEach(arg => {
        console.log(`- ${arg}`);
    });
}
printArgs(1, "texto", true, { framework: "JavaScript", anio: 2024 });


console.log("\n===> Funciones dentro de funciones <===");
function outerFunction() {
    console.log("Esta es la función externa.");
    function innerFunction() {
        console.log("Esta es la función interna.");
    }
    innerFunction();
}
outerFunction();


console.log("\n===> Funciones del lenguaje (built-in) <===");
console.log("Usando la propiedad 'length' de un array:");
const myList = [1, 2, 3, 4, 5];
console.log(`El array ${myList} tiene ${myList.length} elementos.`);

console.log("Usando Math.max() para obtener el valor máximo:");
console.log(`El valor máximo del array es ${Math.max(...myList)}`);


console.log("\n===> Variable LOCAL y GLOBAL <===");
let globalVar = "Soy una variable global";

function myFunctionScope() {
    const localVar = "Soy una variable local";
    console.log(globalVar); // Podemos acceder a la variable global
    console.log(localVar);
}
myFunctionScope();

// Intentar acceder a la variable local desde fuera dará un error
// console.log(localVar); // ReferenceError: localVar is not defined

// Modificar una variable global
function modifyGlobal() {
    globalVar = "He modificado la variable global";
}
console.log(`Antes de modificar: ${globalVar}`);
modifyGlobal();
console.log(`Después de modificar: ${globalVar}`);


/*
 * DIFICULTAD EXTRA (opcional):
 */
console.log("\n====> DIFICULTAD EXTRA <====");
function fizzBuzzExtra(text1, text2) {
    let count = 0;
    for (let i = 1; i <= 100; i++) {
        const isMultipleOf3 = (i % 3 === 0);
        const isMultipleOf5 = (i % 5 === 0);

        if (isMultipleOf3 && isMultipleOf5) {
            console.log(`${text1}${text2}`);
        } else if (isMultipleOf3) {
            console.log(text1);
        } else if (isMultipleOf5) {
            console.log(text2);
        } else {
            console.log(i);
            count++;
        }
    }
    return count;
}

// Llamada a la función de dificultad extra
const timesPrintedNumber = fizzBuzzExtra("Fizz", "Buzz");
console.log(`\nEl número se imprimió un total de ${timesPrintedNumber} veces.`);
