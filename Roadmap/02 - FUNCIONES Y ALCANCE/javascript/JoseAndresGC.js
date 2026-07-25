// función sin sin retorno ni parámetros...

function funcion1(){
    console.log('función sin retorno ni parámetros!');
}
funcion1();

// funciones y función con uno o varios parámetros con retorno...

function funcionStandar() { // con o sin parametro/s
    // código...
    console.log('Esto es una función standar');
}
funcionStandar();

arrowFunction = () => {
    // código...
    console.log('Esto es una función de flecha');
}
arrowFunction();

async function funcionAsincrona(params) {
    // código...
    console.log('Esto es una función Asíncrona');
}
funcionAsincrona();

const asyncArrowFunction = async (params) => {
    // código...
    console.log('Esto es una función Asíncrona de flecha');
}
asyncArrowFunction();

let obj = {
    nombreFuncion: function(param) {
        // código...
    }, // esta sintaxis solo funciona dentro de un objeto para javascript

    nombreFuncion2: (arg) => retornarUnValor // ésta arrow function también se usa dentro de objetos
}

function funcion2(suma) {
    let a = 2;
    let b = 2;
    suma = a + b;
    return suma;
}
console.log(funcion2());

// funciones dentro de funciones...

function funcion3(param) {
    var funcionDentroDeOtra = function() {
        // se agrega la logica...
    };
    // se puede llamar aqui la funcion interna... funcionDentroDeOtra();
}

// Usar algún ejemplo de funciones ya creadas en el lenguaje...

function decirHola() {
    console.log('Hola!! Mensaje enviado después de 1 segundo!!');
}

setTimeout(decirHola, 1000); // después de 1 segundo se enviará por consola "Hola

// Varial local y global...

let global = 'Esto es una variable GLOBAL';

function variableLocal() {
    let local = 'Esto es una variable LOCAL';
    console.log(local);
    console.log(global);
}
variableLocal();

// DIFICULTAD EXTRA:


function dif_Extra(str1, str2) {
    let cont = 0;

    for (let i = 1; i <= 100; i++) {

        if (i % 3 === 0 && i % 5 === 0) {
            console.log(str1 + str2);

        } else if (i % 3 === 0) {
            console.log(str1);

        } else if (i % 5 === 0) {
            console.log(str2);
        } else {
            console.log('Número: ' + i);
            cont++;
        }
    }
    console.log('Se imprimió ' + cont + ' veces un número');
    return cont;
}
dif_Extra('cadena1', 'cadena2');
