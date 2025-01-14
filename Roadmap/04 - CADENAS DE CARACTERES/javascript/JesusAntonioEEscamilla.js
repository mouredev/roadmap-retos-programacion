/** #04 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Este son los ejemplos de cadenas de caracteres
 */

//---STRING---
var cadena = "Hola, mundo";

var primeraCarácter = cadena[0];
var segundoCarácter = cadena[cadena.length - 1];

console.log(primeraCarácter); // H
console.log(segundoCarácter); // o


//---SUB-CADENA---
var subcadena = cadena.substring(2,8);

console.log(subcadena); // la, mu


//---LONGITUD---
var longitud = cadena.length;

console.log(longitud); // 11


//---CONCATENACIÓN---
var cadena1 = "Hola mundo,";
var cadena2 = " Jesus Antonio";

console.log(cadena1 + cadena2); // Hola mundo, Jesus Antonio


//---REPETICIÓN---
var repetido = cadena.repeat(4);

console.log(repetido); // Hola, mundoHola, mundo,Hola mundoHola, mundo


//---MAYÚSCULAS & MINÚSCULAS---
var mayusculas = cadena.toLocaleUpperCase();
var misnusculas = cadena.toLocaleLowerCase();

console.log(mayusculas); //HOLA, MUNDO
console.log(misnusculas); //hola, mundo


//---REMPLAZO---
var nuevaCadena = cadena.replace("mundo", "Mexico");

console.log(nuevaCadena); // Hola, Mexico


//---DIVISION---
var palabra = cadena.split(", ");

console.log(palabra); // ['Hola', 'mundo']


//---UNION---
var listaPalabras = ["Hola", "mundo"];
var nuevaCadena1 = listaPalabras.join(', ');

console.log(nuevaCadena1); // Hola, mundo


//---INTERPOLACIÓN---
var nombre = "Jesus Antonio";
var edad = 24;
var saludos = `Hola, me llamo ${nombre} y tengo ${edad} años.`;

console.log(saludos); // Hola, me llamo Jesus Antonio y tengo 24 años.


//---VERIFICACIÓN---
if (cadena.includes("Hola")) {
    console.log("La cadena contiene 'Hola'"); // La cadena contiene 'Hola'
}



/**-----DIFICULTAD EXTRA-----*/
console.log("----------Palindromo----------");

function palindromo(palabra1) {
    const palabraInvectiva = palabra1.split('').reverse().join('');
    if(palabraInvectiva === palabra1){
        console.log(`La palabra ${palabra1}, si es un palindromo y es ${palabraInvectiva}`);
    }else{
        console.log(`La palabra ${palabra1}, no es un palindromo`);
    }
}
palindromo("reconocer");
palindromo("mundo");


console.log("----------Anagrama----------");

function anagrama(palabra2, palabra3) {;

    const palabraProcesada = palabra2.split('').sort().join('');
    const palabraProcesada1 = palabra3.split('').sort().join('');

    if (palabraProcesada === palabraProcesada1) {
        console.log(`La palabra ${palabra2}, si es un anagrama y su anagrama es ${palabra3}`);
    } else {
        console.log(`La palabra ${palabra2} y la palabra ${palabra3},  no son anagramas`);
    }
}

anagrama("amar", "rama");
anagrama("lápiz", "goma");


console.log("----------Isograma----------");

function isograma(palabra4) {
    const letrasEncontradas = {};
    for (const letra of palabra4) {
        if (letrasEncontradas[letra]) {
            console.log(`La palabra ${palabra4}, no es un isograma`);
            return false;
        }else{
            letrasEncontradas[letra] = true;
        }
    }
    console.log(`La palabra ${palabra4}, si es un isograma`);
    return true;
}

isograma("murciélago");
isograma("programador");
/**-----DIFICULTAD EXTRA-----*/
