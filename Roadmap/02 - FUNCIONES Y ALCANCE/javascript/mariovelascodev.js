//Función sin parámetros ni retorno
function funcionSinParametros() {
    console.log(`¡Hola Mundo!`);
}

funcionSinParametros();

//Función con parámetros
/*
Se pueden poner tantos parámetros como uno desee, tambien se le puede asignar un valor por defecto al parámetro
 */
function funcionConParametros(param1) {
    console.log(`¡Hola, ${param1}!`);
}

funcionConParametros("JavaScript");

//Función con parámetros y retorno
function funcionConParametrosRetorno(param1, param2) {
    return `El primet parámetro es ${param1}, y el segundo parámetro es ${param2}`;
}

console.log(funcionConParametrosRetorno("Mario", 33));

//Función con parámetros por defecto
function funcionConParametrosPorDefecto(param1, param2 = "JS") {
    return `El primer parámetro es ${param1}, y el parámetro por defecto es ${param2}`;
}

console.log(funcionConParametrosPorDefecto("JavaScript"));
console.log(funcionConParametrosPorDefecto("JavaScript", "PHP"));

//Función con varios parámetros
function funcionVariosParametros(...param) {
    return param;
}

console.log(funcionVariosParametros(1, "JS", 30.45, "Juan", 87));

//Función flecha sin argumentos
let sumar = () => 4 + 2;

console.log(`El resultado de la suma es: ${sumar()}`);

//Función flecha con argumentos
let restar = (param1, param2) => param1 - param2;

console.log(`El resultado de la resta es: ${restar(4, 2)}`);

//Función dentro de función
function outer(param1) {
    function inner(param2) {
        return param1 + param2;
    }
    return inner;
}

console.log(outer(3)(5));

//Funciones ya creadas en el lenguaje
let cadena = `Esto es una cadena de prueba`;

//La función/método slice() extrae parte de un string
console.log(cadena.slice(4, 12));
//La función/método replace() reemplaza la primera ocurrencia que encuentra en la cadena
console.log(cadena.replace("cadena", "hilo"));

//Variable local y global
let global = "Variable global";

function variableLocal() {
    let local = "Variable local";
    return local;
}

console.log(global);
console.log(variableLocal());

//La variable global cambiará su valor mientras que la local no lo cambiará ya que su ámbito está solo dentro de la función donde es creada
global = 34;
local = 12;
console.log(`El nuevo valor de la variable global es: ${global}`);
console.log(variableLocal());

//EXTRA
function imprimeNumero(param1, param2) {
    let str1 = String(param1);
    let str2 = String(param2);
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(`${str1} ${str2}`);
        } else if (i % 3 == 0) {
            console.log(str1);
        } else if (i % 5 == 0) {
            console.log(str2);
        } else {
            console.log(i);
            contador += 1;
        }
    }

    return `Número de veces que se ha impreso el número en lugar de textos: ${contador} veces`
}

console.log(imprimeNumero("Hola", "mundo"));