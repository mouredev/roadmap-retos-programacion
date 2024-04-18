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
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

//**FUNCION DECLARATIVA**
//-Sin parametros-
const levelPoints = 2000;
let playerPoints = 1800;

function levelUp() {
    if (playerPoints >= levelPoints) {
        console.log('Level Up! GG!');
    } else {
        console.log('Keep playing. Need more points');
    }
}

levelUp();

playerPoints = 2300;
levelUp();

//-Return-
let precio = 830;
let pagoDelCliente = 830;

function compruebaElPago() {
    return pagoDelCliente >= precio;
};

console.log(compruebaElPago());

pagoDelCliente = 0;
console.log(compruebaElPago());

//-Con un parametro-
function duplicador(n) {
    return n * 2;
};

console.log(duplicador(45));
console.log(duplicador(12));

//-Con dos parametros-
function sumaEstosDos(a, b) {
    let result = a + b;
    console.log(`${a} y ${b} suman ${result}`);
};

sumaEstosDos(12, 25);

//-Con multiples parametros-

function sumaEsteArray(arr) {
    sum = 0;
    for (i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    };
    return sum;
};

const numbers = [12, 32, 78, 7, 23, 34, 56, 78, 90];

console.log(sumaEsteArray(numbers));

//-Con infinitos parametros-
function cuentaLosNombres() {
    console.log(`En total son ${arguments.length} nombres`);
};

cuentaLosNombres('Juan', 'Maria', 'Kevin', 'Eduardo', 'Fabian');

//-Anonimas-
const funcionAnonima = function() {
    console.log('Hola. Soy una funcion anonima');
};

funcionAnonima()

const numCuadrado = function(n) {
    return n * n;
}; //de expresion

console.log(numCuadrado(2));

const unNumCuadrado = (function(n){
    return n * n;
})(10); //de autoinvocacion

console.log(unNumCuadrado);

//***FUNCION FLECHA***
const triplicador = (n) => {
    return n * 3;
};

console.log(triplicador(20));

const cuadriplicador = (n) => n * 4;

console.log(cuadriplicador(10));

const restaEstosDos = (a, b) => {
    let result = a - b;
    console.log(`${a} y ${b} restan ${result}`);
};

restaEstosDos(10, 4);

//***PARAMETROS POR DEFECTO***
function laMitadEs(n = 20) {
    return n / 2;
};

console.log(laMitadEs());
console.log(laMitadEs(14));

function saludo(a = 'Ricardo') {
    console.log(`Hola, ${a}`);
};

saludo();
saludo('Josue');

const areaRectangulo = (a = 10, b = 2) => 2 * (a + b);

console.log(areaRectangulo());
console.log(areaRectangulo(12, 10));

//***FUNCION DENTRO DE UNA FUNCION***

function autorizaElEnvio() {
    if (compruebaElPago() === true) {
        console.log('El pago ha sido procesado con exito. Enviando articulo...');
    } else {
        console.log('No se ha procesado el pago');
    };
};

precio = 200;
pagoDelCliente = 200;

autorizaElEnvio();

precio = 120;
pagoDelCliente = 0;

autorizaElEnvio();

const aplicaTodas = (n) => {
    console.log(n);
    console.log(duplicador(n));
    console.log(triplicador(n));
    console.log(cuadriplicador(n));
;}

aplicaTodas(10);

//***FUNCIONES INTEGRADAS***
let myNum = '23';
console.log(parseInt(myNum) + 2);

let misAppsFavoritas = 'Twitch, Discord, VSCode, YouTube';
misAppsFavoritas = misAppsFavoritas.split(', ');
console.log(misAppsFavoritas[2]);

let miNombre = 'Ricardo Marin';
console.log(miNombre.substring(0,3));
console.log(miNombre.slice(8, -2));

const things = ['dish', 'computer', 'dog'];
const count = things.push('bed');
console.log(things);
console.log(things.pop());

let numeroAleatorio = parseInt(100 * Math.random());
console.log(numeroAleatorio);
console.log(typeof(numeroAleatorio));

//***ALCANCE***
let n = 'Soy una variable con alcance global'; //aqui n tiene alcance global
console.log(n);

function local() {
    let m = 'Soy una variable con alcance local';
    console.log(m);
};

//si escribieramos console.log(m); daria error, debido a que m solo es accesible dentro de la funcion
local();

/* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */

function muestraNumeros(a = 'Fizz', b = 'Buzz') {
    for (let i = 1;i <= 100; i++ ) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(a + ' ' + b);
        } else if (i % 3 === 0) {
            console.log(a);
        } else if (i % 5 == 0){
            console.log(b);
        } else {
            console.log(i);
        };
    };
};

muestraNumeros('Papa', 'Frita');