/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

let cadena = 'hola a todos los que puedan leer esto';
console.log(cadena);

console.log(' ');


console.log('acceso');
console.log(cadena[10]);//se accede como si fuera un array
console.log(cadena.charAt(3));// conel metodo charAt

console.log(' ');

console.log('subcadenas');
console.log(cadena.substring(13, 16));

console.log(' ');

console.log('longitud');
console.log(cadena.length);

console.log(' ');

console.log('concatenacion');
console.log(cadena + " " + "hoy");
let strn1 = 'hola';
let strn2 = 'mundo';
console.log(strn1.concat(' ',strn2));//con el metodo concat()

console.log(' ');

console.log('repeticion');
let saludo = 'hola';
console.log(saludo.repeat(5));

console.log(' ');

console.log('recorrido');
let reco = 'josue';
for (let i = 0; i < reco.length; i++){
    console.log(reco[i]);
}

console.log(' ');

console.log('conversion a mayusculas');
console.log(cadena.toLocaleUpperCase());

console.log(' ');

console.log('conversion a minusculas');
let cadenaMay = 'JESUS ES TREMENDA PERRA';
console.log(cadenaMay.toLocaleLowerCase());

console.log(' ');

console.log('reemplazo');
console.log(cadena.replace('leer', 'ver'));


console.log(' ');

console.log('division');
let compras = "harina, huevos, salsa";
console.log(compras.split(','));


console.log(' ');

console.log('union');
let compras2 = ["harina, huevos, salsa"];
console.log(compras2.join(','));

console.log(' ');

console.log('interpolacion');
let marcaMoto = 'empire';
let marcaCauchos = 'firestone';
let oracion = `tengo una moto ${marcaMoto} y con los cauchos de ${marcaCauchos}`;
console.log(oracion);

console.log(' '); 

console.log('verificacion');
let veri = cadena.includes("a");
console.log(veri);

console.log(' ');


console.log('dificultad extra');

// function principal () {
//     let plb1 = prompt ('escribe la primera palabra para validar');
//     let plb2 = prompt ('escribe la segunda palabra para validar');
//     if (palindromo(plb1, plb2)===true){
//         console.log(`${plb1} y ${[plb2]} son palindromos`);
//     }
    
//     palindromo()
// }
// principal();

// function palindromo (plbr1, plbr2) {
//     let palabraRever = plbr1.split('').reverse().join('');
//     if (palabraRever === plbr2){
//         return true;
//     }
// }

// function Anagrama (plbr1, plbr2) {
//     let check = plbr1.toLowerCase().split("").sort().join();
//     let check1 = plbr2.toLowerCase().split("").sort().join();
//     if (check === check1) {
//         return true;
//     }
// }

// function isograma (plbr1, plbr2) {
//     let check1 = plbr1.toLowerCase().split("")
//     let check2 = plbr2.toLowerCase().split("")
//     let i = 0;
//     for (letra1 of check1){
//         for (letra2 of check2){
//             if (letra1 == letra2){
//                 return true;
//             }
//         }
//     }
// }

/* aqui tengo que confesar que todo el bloque de codigo anterior llevaba 3 dias intentando hacer que funcionara pero no lo logre 
asi que en el codigo que sigue use gemini para que lo corrigera y este fue el resultado, claro el codigo que me dio gemini tenia
algunos errores de funcionamiento pero le retoque algunas lineas (eso si fue por mi propio merito) y asi quedo*/


function principal() {
    let plb1 = prompt('escribe la primera palabra para validar');
    let plb2 = prompt('escribe la segunda palabra para validar');

    if (palindromo(plb1, plb2)) {
        console.log(`${plb1} y ${plb2} son palíndromos`);
    }else {console.log('no es un palindromo');
    }

    if (anagrama(plb1, plb2)) {
        console.log(`${plb1} y ${plb2} son anagramas`);
    }else {console.log('no es un anagrama');
    }

    if (isograma(plb1, plb2)) {
        console.log(`${plb1} y ${plb2} comparten al menos una letra`);
    } else {
        console.log(`${plb1} y ${plb2} no comparten ninguna letra`);
    }
}

principal();

function palindromo(palabra, palabra2) {
    return palabra.split('').reverse().join('') === palabra2.split('').join('');
}

function anagrama(palabra1, palabra2) {
    return palabra1.toLowerCase().split("").sort().join("") === palabra2.toLowerCase().split("").sort().join("");
    
}

function isograma(palabra1, palabra2) {
    let letras1 = palabra1.toLowerCase().split("");
    let letras2 = palabra2.toLowerCase().split("");

    for (let letra of letras1) {
        if (letras2.includes(letra)) {
        return true;
        }
    }
    return false;
}
