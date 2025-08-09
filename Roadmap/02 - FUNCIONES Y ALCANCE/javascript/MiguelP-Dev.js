//  Variables globales
let nombre = "Miguel";
let edad = 31;
let ciudad = "Medellín";

console.log(nombre, edad, ciudad)

// Variables locales
{
    let variableLocal = 3223;
    console.log(variableLocal);
}


// Declaración de una función 
function helloWorld() {
    console.log("¡Hello, World!");
}

// Llamada a la función
helloWorld()

// Declaración de una función con parámetros
function suma(a, b) {
    console.log(a + b);
}

// Llamada a la función
suma(2, 3)

// Declaración de una función con parámetros y retorno
function sumaConRetorno(a, b) {
    return a + b;
}

// Llamada a la función cin retorno
console.log(sumaConRetorno(2, 3))

// Declaración de una función anónima sin parámetros y retorno
const saludoAnonimo = function () {
console.log("Hola, Bienvenido a mi función anónima");
}

// Llamada a la función anónima
saludoAnonimo()

// Declaración de una función anónima con parámetros y retorno
const sumaAnonima = function (a, b) {
    return a + b;
}

// Llamada a la función anónima con parámetros y retorno
console.log(sumaAnonima(2, 3))

// Declaración de una función flecha sin parámetros y retorno
const saludoFlecha = () => {
    console.log("Hola, Bienvenido a mi función flecha");
}

// Llamada a la función flecha
saludoFlecha()

// Declaración de una función flecha con parámetros y retorno
const sumaFlecha = (a, b) => {
    return a + b;
}

// Llamada a la función flecha con parámetros y retorno
console.log(sumaFlecha(2, 3))

// Declaración de una función flecha con parámetros y retorno simplificado
const sumaFlechaSimplificado = (a, b) => a + b;

// Llamada a la función flecha con parámetros y retorno simplificado
console.log(sumaFlechaSimplificado(2, 3))

// Declaración de una función flecha con un solo parámetro y retorno
const cuadrado = (x) => x * x;

// Llamada a la función flecha con un solo parámetro y retorno
console.log(cuadrado(2))

// Declaracion de funciones en objetos

let persona = {
    nombre: "Miguel",
    apellido: "Portillo",
    edad: 31,
    saludar: function () {
        console.log(`Hola, mi nombre es ${this.nombre} y mi apellido es ${this.apellido} y tengo ${this.edad} años`)
    }
}

persona.saludar()

// Nota: En JavaScript, las funciones se pueden declarar dentro de otros objetos, como en el ejemplo anterior. Esto se conoce como "funciones anidadas" o "funciones de ámbito local".
// Las funciones anidadas pueden acceder a las variables y funciones del ámbito padre, lo que permite organizar mejor el código y reutilizar partes de código.

// Reglas: 
// 1. Si la función tiene un solo parámetro, se pueden omitir los paréntesis.
// 2. Si la función tiene un solo sentencia de retorno, se pueden omitir las llaves y la palabra clave return.
// 3. Usa funciones declaradas para utilidades generales
// 4. Usa funciones expresión o arrow(flecha) para funciones de callback o funciones de alto nivel
// 5. Usa funciones flecha para funciones de una sola línea
// 6. Usa funciones flecha para funciones de una sola línea que no devuelven un objeto
// 7. Usa funciones flecha para funciones de una sola línea que no devuelven un objeto y que no tienen un solo parámetro
// 8. Usa funciones flecha para funciones de una sola línea que no devuelven un objeto y que no tienen un solo parámetro y que no tienen un solo sentencia de retorno
// 9. Usa funciones flecha cuando no se necesita el this



//  DIFICULTAD EXTRA (opcional):
//  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
// 
//  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
//  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

function EjercicioExtra(text1, text2) {
contador = 0;
for (let i = 1; i <= 100; i++) {
    if (i % 15 === 0 ) {
        console.log(text1 + text2);
    } else if (i % 3 === 0) {
        console.log(text1);
    } else if (i % 5 === 0) {
        console.log(text2);
    } else {
        console.log(i);
        contador++;
    }
}
return contador;
}

// EjercicioExtra("Miguel", "Portillo");
console.log("Cantidad de veces que se ha impreso el número en lugar del texto: " + EjercicioExtra("fizz", "buzz"));