/**
pueden pasarse a otras funciones, ser devueltas por ellas y asignarse a variables y propiedades.
pueden tener propiedades y métodos
/**
 * 
 * funciones => objetos de primera clase, caleables por código externo (o interno en caso de recursión)
 * se pueden manipular y transmitir al igual que cualquier otro objeto.
 * Concretamente son objetos Function.
 * 
    *Contiene:
    *declaración de una función 
    *nombre de la función
    *parámetros en caso de necesitarse hasta 255
    *instrucciones
**/

//1.- sin parámetro ni retorno
function saludo() {
    console.log('Hola extraño');
} //no necesita un ; aquí.

saludo();


//2.- con parámetro y sin retorno
function saludarPersona(nombre) {
    console.log(`Hola, ${nombre}`);
}
saludarPersona("Cristian");

//3.- con más de 1 parámetro y retorno
function suma(num1, num2) {
    return num1 + num2  //si el return no tiene expresión después, el valor de retorno es undefined.
}
console.log(suma(14, 62));

//4.- La función es anónima pero asignada a una variable.
const multiplicar = function (num1, num2) {
    return num1 * num2
};
console.log(multiplicar(7, 7));


//5.- la función tiene su propio nombre
//el nombre de la función no se puede cambiar pero sí la variable
const division = function div(x, y) {
    return x / y;
};
console.log(division(6, 2));

//6.- función con valor por defecto
function potencia(base, exponente = 2) {
    return base ** exponente;
}
console.log(potencia(7)); //ocupa el exponente 2 por defecto
console.log(potencia(5, 3)); //reemplaza el exponente por defecto al ingresado en los argumentos


//7.- FUNCIÓN FLECHA - ARROW FUNCTION
/**
 * No tiene sus propios enlaces a this o super y no se debe usar como métodos.
*No tiene argumentos o palabras clave new.target.
*No apta para los métodos call, apply y bind, que generalmente se basan en establecer un ámbito o alcance
*No se puede utilizar como constructor.
*No se puede utilizar yield dentro de su cuerpo.
 * 
 */


//en caso de no tener parámetros, se deja en blanco
let a = 4;
let b = 3;
const sinParametros = () => a + b + 100;
console.log(sinParametros());


//1 parámetro
//no son necesarios los paréntesis
const saludarFlecha = nombre => {
    return `Hola , ${nombre}`;
};

//la misma pero si no llega return, hay que sacar las llaves.

const saludarFlecha2 = nombre => `Hola, ${nombre}`;

console.log('Saludar con flecha normal:', saludarFlecha('cristian'));
console.log('Saludo con flecha 2 : ', saludarFlecha2('cristian2'));

//otra
const conParametros = (a, b) => a + b + 100;
console.log(conParametros(4, 3));

//otra con return, para procesamientos adicionales

const sumarRandom = (a, b) => {
    let random = 42;
    return a + b + random;
}

console.log(sumarRandom(5, 2));

//con array

const materials = ["Hydrogen", "Helium", "Lithium", "Beryllium"];

console.log(materials.map((material) => material.length));

//con nombre de variable
const resta = (x, y) => x - y;
console.log(resta(8, 14));

//8.- método
const obj = {
    resto(x, y) {
        return x % y;
    },
};

console.log(obj.resto(19, 5));


// 9.- funciones recursivas
function recorrerArbol(nodo) {
    if (nodo == null)
        //
        return;
    // haz algo con el nodo
    for (var i = 0; i < nodo.nodosHijos.length; i++) {
        recorrerArbol(nodo.nodosHijos[i]);
    }
}

//10.- funciones anidadas

function calcularAreaCirculo(radio) {
    //función interna - solo visible aquí
    function cuadrado(x) {
        return x * x;
    }
    const area = Math.PI * cuadrado(radio);
    return area.toFixed(4);
}

console.log('Área del círculo r=5:', calcularAreaCirculo(5));


//11.- variables locales y globales
let variableGlobal = "Soy global";

function demostrarScope() {
    let variableLocal = "Soy local";
    console.log(`Dentro - global: accesible ${variableGlobal}`);
    console.log(`Dentro  - Local: accesible ${variableLocal}`);
}

demostrarScope();

console.log(`Fuera - global: accesible ${variableGlobal}`);

try {
    console.log(`Fuera - local: inaccesible ${variableLocal}`);
} catch (error) {
    console.log(`Variable local inaccesible fuera de la función: ${error.message}`);
};



//________________________________________________________________
//______________________DIFICULTAD EXTRA__________________________
//________________________________________________________________

/**
 *   - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 *   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */



function desafio(cadena1, cadena2) {

    let contadorNumeros = 0;

    for (let i = 1; i <= 100; i++) {

        if (i % 3 === 0 && i % 5 === 0) {
            console.log(cadena1 + cadena2);
        } else if (i % 3 === 0) {
            console.log(cadena1);
        } else if (i % 5 === 0) {
            console.log(cadena2);
        } else {
            console.log(i);
            contadorNumeros++;
        }
    }

    return contadorNumeros;
}

console.log(desafio("Uva", "Sandía"));
