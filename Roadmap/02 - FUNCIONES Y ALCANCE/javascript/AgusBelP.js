// #02  FUNCIONES Y ALCANCE

/*
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
Debes hacer print por consola del resultado de todos los ejemplos (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/

// <-------------------------> Funciones <------------------------->

// Una función en JavaScript es un bloque de código o un conjunto de instrucciones que realiza una tarea específica y que puede reutilizarse a voluntad. Existen diversas formas de crear una función en JavaScript.

// --->> Funciones por declaración

// Esta forma permite declarar una función que existirá a lo largo de todo el código.

function funcionPorDeclaracion() {
    console.log('Este es el resultado de una función por declaración');
}

funcionPorDeclaracion();

// Es posible ejecutar la función saludar() incluso antes de haberla creado y funcionaría correctamente, ya que Javascript primero busca las declaraciones de funciones y luego procesa el resto del código.

// --->> Variables locales y Globales

// Una variable declarada dentro de una función solo es visible dentro de esa función. A dicha variable se la conoce como local.

function variableLocal() {
    let local = 'Soy una variable local';

    console.log('Muestro el uso de una variable local: ' + local);
}

variableLocal();

// Una función también puede acceder a una variable externa o global. La función tiene acceso completo a la variable externa. Puede modificarlo también. La variable global solo se usa si no hay una local.

let variableGlobal = 'Soy una variable global';

function funcionVariableGlobal() {
    variableGlobal = 'Accediendo a la variable global desde la función'; // Cambio el valor de la variable global

    let message = 'Hola! ' + variableGlobal;
    console.log(message);
}

console.log(variableGlobal); //antes de llamar la función

funcionVariableGlobal();

console.log('Ahora la variable global es: ' + variableGlobal); // el valor fué modificado por la función

// Si una variable con el mismo nombre se declara dentro de la función, le hace sombra a la global. Por ejemplo, en el siguiente código, la función usa la variable userName local. La exterior se ignora:

let userName = 'John';

console.log('La variable global es ' + userName);

function showMessage() {
    let userName = 'Bob'; // declara variable local

    let message = 'Hello, ' + userName; // Bob
    console.log('Accediendo desde la función se lee el mensaje: ' + message);
}

// la función crea y utiliza su propia variable local userName
showMessage();

console.log(
    'La variable global no cambió pues la función utilizó aquella que estaba dentro de su scope, entonces la variable global sigue siendo: ' +
        userName
); // John, se mantiene, la función no accedió a la variable externa

// --->> Funciones con parámetros

// Es posible llamar a una función y pasarle parámetros o argumentos para que los utilice:

function funcionConParametros(from, text) {
    // parámetros: from, text
    console.log(from + ': ' + text);
}

funcionConParametros('Ann', '¡Hola!');
funcionConParametros('Ann', '¿Cómo estás?');

// en el caso de que se llame a una función que requiere de argumentos y no se determinen todos los parámetros aquellos que no estén definidos serán undefined

console.log('Esto es un ejemplo de una función con un parámetro undefined: ');
funcionConParametros('Hola');

// Es posible establecer valores por defecto para los argumentos:

function funcionValorPorDefecto(a, b = 'valor por defecto') {
    console.log(`Ma llamo ${a} y mi valor es: ${b}`);
}
funcionValorPorDefecto('Mabel');

// --->> Funciones con retorno

// Unav función con retorno es una función que devuelve algo al ser llamada. Por ejemplo:

function suma(a, b) {
    return a + b;
}

console.log('El resultado de la suma es: ' + suma(1, 2));

// --->> Funciones anónimas

// Las funciones anónimas o funciones lambda son un tipo de funciones que se declaran sin nombre de función y se alojan en el interior de una variable haciendo referencia a ella cada vez que queramos utilizarla:

const saludo = function () {
    return 'Hola';
};

console.log(saludo); // Imprimo la función
console.log(saludo()); // Imprimo la salida 'Hola'

// --->> Arrow functions

// Las funciones flecha son una forma corta de escribir funciones que aparece en Javascript a partir de ECMAScript 6. Básicamente, se trata de eliminar la palabra function y añadir => antes de abrir las llaves:

const funcionTradicional = function () {
    return 'Función tradicional.';
};

console.log(funcionTradicional());

const funcionFlecha = () => {
    return 'Función flecha.';
};

console.log(funcionFlecha());

// --->> Función dentro de otra función

// Sin determinar un argumento

function funcionExterna() {
    let funcionInterna = (mensaje) => {
        console.log(`¡Función interna ejecutada, con el mensaje ${mensaje}!`);
    };
    funcionInterna('Muy bien');
}

funcionExterna();

// Determinando argumentos

function addCuadrado(a, b) {
    function cuadrado(x) {
        return x * x;
    }
    return cuadrado(a) + cuadrado(b);
}

console.log('El cuadrado de 2 más el cuadrado de 3 es ' + addCuadrado(2, 3));

// --->> Función ya creada en el lenguaje

// En este ejemplo se utiliza Math. Math es un objeto incorporado que tiene propiedades y métodos para constantes y funciones matemáticas. No es un objeto de función. A diferencia de los demás objetos globales, el objeto Math no se puede editar.
//Math funciona con el tipo Number. No funciona con BigInt.

// Utilizando Math para calcular la superficie de un círculo recordando que la fórmula es PI*r2:

const superficie = (radio) => {
    let superficieCirculo = Number((Math.PI * Math.pow(radio, 2)).toFixed(2)); // la función toFixed() devuelve un string
    return superficieCirculo;
};

console.log(superficie(2));

// <-------------------------> EXTRA <------------------------->

const ejercicioExtra = (texto1, texto2) => {
    let contador = 0;

    for (let i = 1; i < 100; i++) {
        if (i % 3 == 0 && i % 5 != 0) {
            console.log(texto1);
        } else if (i % 3 != 0 && i % 5 == 0) {
            console.log(texto2);
        } else if (i % 3 == 0 && i % 5 == 0) {
            console.log(texto1 + '+' + texto2);
        } else {
            console.log(i);
            contador += 1;
        }
    }

    return contador;
};

console.log(
    'La cantidad de veces que se ha impreso un número es: ',
    ejercicioExtra('texto1', 'texto2') // La cantidad de veces que se ha impreso un número es:  53
);
